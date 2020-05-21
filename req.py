import requests
req = requests.post(
    "https://webhook.site/a89b3763-9030-42e7-86f0-d2b525dd1b2d", 
    json={
        "amount": 0.1,
        "metadata": {
            "order_id": "3883c868-9b2c-11ea-8008-acde48001122",
            "product_name": "Service Name",
            "product_description": "Description"
        }
    },
    headers={'Content-Type': 'application/json'}
)
responses = req.text
print(responses)