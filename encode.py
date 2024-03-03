import base64

# Original string
original_string = "4321lupa"

# Encode the original string to bytes using UTF-8 encoding
utf8_bytes = original_string.encode('utf-8')

# Base64-encode the bytes
encoded_password = base64.b64encode(utf8_bytes).decode('ascii')

print("Encoded password:", encoded_password)