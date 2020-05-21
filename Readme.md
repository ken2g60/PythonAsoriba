# Asoriba Payment
- Create an account at https://app.mybusinesspay.com.
- Upload your documents for account verification.

Clone 
` git clone https://github.com/ken2g60/PythonAsoriba.git`

Create a virutual environment
`python3 -m venv venv`

Activate the virutualenv
`source venv/bin/activate`

Install the requirements
`pip install -r requirements.txt`

import the file into your project
` from asoriba.pay import Asoriba`

initialize the payment
` pay = Asoriba("pubkey", "webhook url", "Product Name", "Description") `

Create a payment for ussd only
` pay = cbs.initialize("amount", "first_name", "last_name", "phonenumber") `
