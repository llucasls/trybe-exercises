curl https://api.stripe.com/v1/charges \
  -u sk_test_4eC39HqLyjWDarjtT1zdp7dc: \
  -H "Idempotency-Key: yH2VPwTykCnMAXme" \
  -d amount=2000 \
  -d currency=usd \
  -d description="My First Test Charge (created for API docs)" \
  -d source=tok_mastercard

curl https://httpbin.org/anything \
  -u sk_test_4eC39HqLyjWDarjtT1zdp7dc: \
  -H "Idempotency-Key: yH2VPwTykCnMAXme" \
  -d amount=2000 \
  -d currency=usd \
  -d description="My First Test Charge (created for API docs)" \
  -d source=tok_mastercard
