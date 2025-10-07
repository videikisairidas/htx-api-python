from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import base64

# Generate key
private_key = ed25519.Ed25519PrivateKey.generate()
public_key = private_key.public_key()


# Export private key as PKCS#8, encrypted with a password
pem_priv = private_key.private_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

# Export public key
pem_pub = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.DER,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

# Convert to base64 single-line
private_b64 = base64.b64encode(pem_priv).decode()
public_b64 = base64.b64encode(pem_pub).decode()

# Format as compact PEM
private_pem = f"-----BEGIN PRIVATE KEY-----\n{private_b64}\n-----END PRIVATE KEY-----"
public_pem = f"-----BEGIN PUBLIC KEY-----\n{public_b64}\n-----END PUBLIC KEY-----"

# Save to files
with open("htx_api_python/HTX_Manager/_createED25519/ed25519-private.pem", "w") as f:
    f.write(private_pem)

with open("htx_api_python/HTX_Manager/_createED25519/ed25519-public.pem", "w") as f:
    f.write(public_pem)

# Print results
print(private_pem)
print(public_pem)