from twilio.rest import Client


# account_sid = "AC14021b41bb9d8412998a8f451de3d94e"
# auth_token  = "828a1fbd41b3c5eb91a0c8aab3c0b7c9"

import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure

account_sid ='AC14021b41bb9d8412998a8f451de3d94e'
auth_token = '828a1fbd41b3c5eb91a0c8aab3c0b7c9'
mobile_number="+919441856390"
client = Client(account_sid, auth_token)
verification = client.verify \
                     .v2 \
                     .services('VA452ba6c31e581e1e3983473a2c4555b7') \
                     .verifications \
                     .create(to=mobile_number, channel='sms')

print(verification)