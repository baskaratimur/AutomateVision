import base64

# Encoded password
encoded_password = "NDMyMUx1cGE="

# Decode Base64-encoded string to bytes
decoded_bytes = base64.b64decode(encoded_password)

# Convert bytes to string using UTF-8 encoding
original_string = decoded_bytes.decode('utf-8')

print("Decoded password:", original_string)
