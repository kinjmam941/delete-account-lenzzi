from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Shopify store credentials
SHOPIFY_ACCESS_TOKEN = "560f20b590c3808d06ebddb8f0ae9239"
SHOP_NAME = "m0dz2y-3z"

@app.route('/delete-account', methods=['POST'])
def delete_account():
    customer_id = request.json.get("customer_id")
    
    if not customer_id:
        return jsonify({"error": "Customer ID is required"}), 400

    url = f"https://{SHOP_NAME}.myshopify.com/admin/api/2023-07/customers/{customer_id}.json"
    
    headers = {
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN,
        "Content-Type": "application/json"
    }

    response = requests.delete(url, headers=headers)

    if response.status_code == 200:
        return jsonify({"message": "Customer account deleted successfully"}), 200
    else:
        return jsonify({
            "error": "Failed to delete customer account",
            "shopify_response": response.text
        }), response.status_code


if __name__ == '__main__':
    app.run(debug=True)
