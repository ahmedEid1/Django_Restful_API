from rest_framework.test import APITestCase
import os.path
from django.conf import settings

from store.models import Product



class ProductCreateTeatCase(APITestCase):
    def test_create_product(self):
        initial_product_count = Product.objects.count()
        new_product = {
            'name': "new product",
            'description': 'this is a test Product',
            'price': '126.25'
        }
        response = self.client.post('/api/products/new', new_product)
        if response.status_code != 201:
            print(response.data)
        self.assertEqual(
            Product.objects.count(),
            initial_product_count+1
        )

        for attr, expected_val in new_product.items():
            self.assertEqual(response.data[attr], expected_val)
        self.assertEqual(response.data['is_on_sale'], False)
        self.assertEqual(response.data['current_price'], float(new_product['price']))


class ProductDestroyTestCase(APITestCase):
    def test_destroy_product(self):
        initial_product_count = Product.objects.count()
        product_id = Product.objects.first().id
        self.client.delete('/api/products/{}'.format(product_id))

        self.assertEqual(
            Product.objects.count(),
            initial_product_count - 1
        )

        self.assertRaises(
            Product.DoesNotExist,
            Product.objects.get,
            id=product_id
        )


class ProductListTestCase(APITestCase):
    def test_list_products(self):
        products_count = Product.objects.count()
        response = self.client.get('/api/products')

        self.assertIsNone(response.data['next'])
        self.assertIsNone(response.data['previous'])
        self.assertEqual(
            response.data['count'],
            products_count
        )
        self.assertEqual(
            len(response.data['results']),
            products_count
        )


class ProductUpdateTestCase(APITestCase):
    def test_update_product(self):
        product_id = Product.objects.first().id
        response = self.client.put(
            '/api/products/{}'.format(product_id),
            {
                'name': 'new updated product',
                'description': 'nothing newsssssssssssssssssssssssssssssssssssssssssssssssss',
                'price': 256.5
            },
            format='json'
                          )
        print(response)
        updated = Product.objects.get(id=product_id)

        self.assertEqual(updated.name, 'new updated product')

    def test_upload_product_photo(self):
        product = Product.objects.first()
        product_photo = Product.photo
        new_photo_path = os.path.join(settings.MEDIA_ROOT, 'products', 'vitamin-multi.jpg')

        with open(new_photo_path, 'rb') as photo_data:
            response = self.client.patch(
                '/api/products/{}'.format(product.id),
                {
                    'photo': photo_data
                },
                format='multipart'
            )

        self.assertEqual(response.status_code, 200)
        self.assertNotEqual(response.data['photo'], product_photo)

        try:
            updated = Product.objects.get(id=product.id)
            # remove .jpg
            new_photo_path = os.path.join(settings.MEDIA_ROOT, 'products', 'vitamin-multi')
            self.assertTrue(
                updated.photo.path.startswith(new_photo_path)
            )
        finally:
            # remove the newly uploaded photo
            os.remove(updated.photo.path)




