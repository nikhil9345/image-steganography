import cv2
import os
image_path = "C:\Users\NIKHIL\OneDrive\Desktop\bird img.png"

# Open the image
image = Image.open(image_path, 'r')
newimage = image.copy()

if image is None:
    print("Image not found. Check the file path and make sure the image exists.")
    exit()

# Get the dimensions of the image
width, height = image.size

# Prompt the user to input the secret message
msg = input("Enter secret message: ")  # For example, Enter "Thala for a reason"

# Prompt the user to input the password
password = input("Enter a passcode: ")  # For example, Enter 7

# Convert the length of the message to a string and prepend it to the message
msg = str(len(msg)).zfill(3) + msg

# Initialize dictionaries for mapping characters to their ASCII values and vice versa
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

k = 0
for j in range(width):  # Column-wise
    for i in range(height):  # Iterate over rows within each column
        if k < len(msg):
            # Get the current pixel value
            r, g, b = image.getpixel((j, i))
            # Encode the character into the blue channel of the pixel
            new_b = (b + int(password) + d[msg[k]]) % 256
            # Update the pixel value in the new image
            newimage.putpixel((j, i), (r, g, new_b))
            k += 1
        else:
            break
    if k >= len(msg):
        break

# Save the modified image to a new file
new_image_name = "C:\Users\NIKHIL\OneDrive\Desktop\bird encrypted img.png"
newimage.save(new_image_name, str(new_image_name.split(".")[1].upper()))

print("Image created.")










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
