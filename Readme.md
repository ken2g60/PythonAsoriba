# Asoriba Payment
# Initialize the payment processor with your public key, webhook and product_name and the description for the payment
# Create Asoriba Business Account and provide your business infomation for Verification 
# Create a merchant account and copy the public key
# Visit https://webhook.site to get webhook for the API 
cbs = Asoriba("pubKey", "webhook url", "Service Name", "Description")
# debit 
cbs.initialize("amount", "firstname", "lastname", "phonenumber")
# credit 
cbs.payout("amount", "phonenumber")
