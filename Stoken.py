from itsdangerous import URLSafeTimedSerializer
secret_key="Tanuja11"
salt="Otpverify"

# For Encryption

def endata(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.dumps(data,salt=salt)

# For Decryption

def dndata(data):
    serializer=URLSafeTimedSerializer(secret_key)
    return serializer.loads(data,salt=salt) 
   # return serializer.loads(data,salt=salt,max_age=30)   # max_age -> number of sec the otp will work until (it's optional) 
