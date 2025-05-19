import secrets

# Generate a secure secret key
secret_key = secrets.token_hex(32)
print(f"Generated Flask Secret Key: {secret_key}")