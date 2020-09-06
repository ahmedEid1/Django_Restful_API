Project Description: 
Rest API to
- show list of products and their data along with 
- - filtering and search options to narrow down the products list
- show details about each product along with 
- - the ability to create, delete, update a product                     

endPoints:
- Show all products: GET /api/products

- show details for a product: GET /api/products/{id}

- create new producr : post /api/products/new

- update a product : put, patch /api/products/{id}

- Delete a product : delete /api/products/{id}

- ## stats for a particular product(compost data): get /api/product/{id}/stats
