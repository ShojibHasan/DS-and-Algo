import requests

headers = {
            'content-type': 'application/x-www-form-urlencoded',
            'charset': 'utf-8',
            'access-token': 'access_token_6b22f9960875e67e98af0091faac37c2d7bf59ad'
        }



base_url = "http://localhost:8069/"
data = {
            'name': 'Shojib',
        }
req = requests.post('%s/api/hr.department/' %base_url, headers=headers, data=data)

# payload = "{}"
# headers = {
#     'content-type': "application/json"
#     }

# response = requests.request("GET", url, data=payload, headers=headers)

# print(response.text)


journal_items = [    
                 {        "name": "Invoice Line 1",        "account_id": 1,        "debit": 100.00,        "credit": 0.00,        "partner_id": 1,        "analytic_account_id": 1,        "currency_id": 1,        "tax_ids": [(6, 0, [1, 2])],
        "product_id": 1,
    },
    {
        "name": "Invoice Line 2",
        "account_id": 2,
        "debit": 0.00,
        "credit": 200.00,
        "partner_id": 1,
        "analytic_account_id": 1,
        "currency_id": 1,
        "tax_ids": [(6, 0, [1, 2])],
        "product_id": 2,
    },
    {
        "name": "Invoice Line 3",
        "account_id": 3,
        "debit": 50.00,
        "credit": 0.00,
        "partner_id": 1,
        "analytic_account_id": 1,
        "currency_id": 1,
        "tax_ids": [(6, 0, [1, 2])],
        "product_id": 3,
    }
]
