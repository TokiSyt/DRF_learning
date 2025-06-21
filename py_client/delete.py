import requests

product_id = input("What is the product ID you want to delete?\n")


try:
    product_id = int(product_id)
except:
    product_id = None
    print(f"{product_id} is not a valid id")

if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    delete_response = requests.delete(endpoint)
    print(delete_response.status_code, delete_response.status_code==204)