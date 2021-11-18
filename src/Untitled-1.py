import rsa, base64

pubkey, privkey = rsa.newkeys(512)

data = " Victor - AGENDA"

signature = rsa.sign(data.encode('utf-8'), privkey, 'SHA-1')

print(data + '\n' + base64.b64encode(signature).decode('ascii'))

try:
    rsa.verify(data.encode('utf-8'), signature, pubkey)
except rsa.VerificationError:
    print("Rsa Verification Error")
else:
    print("validate") 