const express = require("express");
const bodyParser = require("body-parser");
const fetch = require("node-fetch");
const cors = require("cors");

const app = express();
const port = 3000;

// Shopify Config
const SHOPIFY_STORE_URL = "https://m0dz2y-3z.myshopify.com";
const SHOPIFY_ACCESS_TOKEN = "560f20b590c3808d06ebddb8f0ae9239";

app.use(cors());
app.use(bodyParser.json());

// DELETE Customer Endpoint
app.post("/delete-customer", async (req, res) => {
  const { customer_id } = req.body;

  if (!customer_id) {
    return res.status(400).json({ message: "Customer ID is required." });
  }

  try {
    const endpoint = `${SHOPIFY_STORE_URL}/admin/api/2025-04/customers/${customer_id}.json`;

    const response = await fetch(endpoint, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        "X-Shopify-Access-Token": SHOPIFY_ACCESS_TOKEN,
      }
    });

    if (response.ok) {
      res.status(200).json({ message: "Customer deleted successfully." });
    } else {
      const error = await response.json();
      res.status(500).json({ message: "Failed to delete customer.", error });
    }
  } catch (err) {
    res.status(500).json({ message: "Server error.", error: err.toString() });
  }
});

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
