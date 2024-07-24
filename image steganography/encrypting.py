from PIL import Image

# Paths to the original and encrypted images
original_image_path = "C:\Users\NIKHIL\OneDrive\Desktop\bird img.png"
encrypted_image_path = "C:\Users\NIKHIL\OneDrive\Desktop\bird encrypted img.png"

# Open the original and encrypted images
original_image = Image.open(original_image_path, 'r')
encrypted_image = Image.open(encrypted_image_path, 'r')

if original_image is None or encrypted_image is None:
    print("Image not found. Check the file path and make sure the images exist.")
    exit()

# Get the dimensions of the images
width, height = original_image.size

# Prompt the user to input the password
password = input("Enter the passcode: ")

# Initialize dictionaries for mapping characters to their ASCII values and vice versa
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Initialize variables for decoding the message length
message_length_str = ""
k = 0

# Decode the length of the message (3 characters)
for j in range(width):
    for i in range(height):
        if k < 3:
            # Get the pixel values from both images
            r_orig, g_orig, b_orig = original_image.getpixel((j, i))
            r_enc, g_enc, b_enc = encrypted_image.getpixel((j, i))
            # Decode the character from the blue channel of the pixel
            encoded_value = (b_enc - b_orig - int(password)) % 256
            decrypted_character = c[encoded_value]
            message_length_str += decrypted_character
            k += 1
        else:
            break
    if k >= 3:
        break

# Convert the decoded length to an integer
message_length = int(message_length_str)

# Initialize variables for decoding the actual message
decrypted_message = []
k = 0

# Decode the actual message using the length
for j in range(width):
    for i in range(height):
        if k >= 3 and k < 3 + message_length:  # Skip the first 3 pixels used for message length
            # Get the pixel values from both images
            r_orig, g_orig, b_orig = original_image.getpixel((j, i))
            r_enc, g_enc, b_enc = encrypted_image.getpixel((j, i))
            # Decode the character from the blue channel of the pixel
            encoded_value = (b_enc - b_orig - int(password)) % 256
            decrypted_character = c[encoded_value]
            decrypted_message.append(decrypted_character)
            k += 1
        else:
            k += 1
            if k >= 3 + message_length:
                break
    if k >= 3 + message_length:
        break

# Join the decrypted message list into a string
decrypted_message = ''.join(decrypted_message)

print(f"Decrypted message: {decrypted_message}")
