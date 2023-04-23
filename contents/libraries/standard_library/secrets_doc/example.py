import secrets


# Generate a 32-bit random integer:
print(secrets.randbits(32))
print()

# Generate a random URL-safe text string, in Base64 encoding:
print(secrets.token_urlsafe(16))
print()

# Generate a random text string, in Base64 encoding:
print(secrets.token_bytes(16))
print()

# Generate a random text string, in hexadecimal encoding:
print(secrets.token_hex(16))
print()

# Choose one from the list
print(secrets.choice(['apple', 'banana', 'cherry']))
print()

# Generate random below 100
print(secrets.randbelow(100))
print()

