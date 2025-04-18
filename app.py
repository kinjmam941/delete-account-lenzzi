from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

# Shopify Store Credentials
SHOP_NAME = "m0dz2y-3z"
ACCESS_TOKEN = "560f20b590c3808d06ebddb8f0ae9239"

class DeleteRequest(BaseModel):
    customer_id: int

@app.post("/delete-account")
async def delete_account(request: DeleteRequest):
    customer_id = request.customer_id

    if not customer_id:
        return {"error": "Customer ID is required"}

    url = f"https://{SHOP_NAME}.myshopify.com/admin/api/2023-07/customers/{customer_id}.json"
    headers = {
        "X-Shopify-Access-Token": ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200 or response.status_code == 204:
        return {"message": "Customer account deleted successfully"}
    else:
        return {
            "error": "Failed to delete customer account",
            "shopify_response": response.text
        }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
