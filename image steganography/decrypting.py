from PIL import Image

def decode_message_column_wise(original_image_path, encrypted_image_path, password):
    # Open the original and encrypted images
    original_image = Image.open(original_image_path, 'r')
    encrypted_image = Image.open(encrypted_image_path, 'r')

    if original_image is None or encrypted_image is None:
        print("Image not found. Check the file path and make sure the images exist.")
        exit()

    # Get the dimensions of the images
    width, height = original_image.size

    # Initialize dictionaries for mapping characters to their ASCII values and vice versa
    d = {chr(i): i for i in range(256)}
    c = {i: chr(i) for i in range(256)}

    # Initialize variables for decoding the actual message
    decrypted_message = []
    k = 0

    # Decode the actual message
    for j in range(width):
        for i in range(height):
            # Get the pixel values from both images
            r_orig, g_orig, b_orig = original_image.getpixel((j, i))
            r_enc, g_enc, b_enc = encrypted_image.getpixel((j, i))
            # Decode the character from the red channel of the pixel
            encoded_value = (r_enc - r_orig - int(password)) % 256
            decrypted_character = c[encoded_value]
            decrypted_message.append(decrypted_character)

            # Stop decoding if the termination character is found
            if decrypted_character == '\x00':
                break

            k += 1

        if decrypted_character == '\x00':
            break

    # Join the decrypted message list into a string, removing the termination character
    decrypted_message = ''.join(decrypted_message).rstrip('\x00')

    print(f"Decrypted message: {decrypted_message}")

# Usage
original_image_path = "C:\Users\NIKHIL\OneDrive\Desktop\image steganography\images\bird img.png"
encrypted_image_path = "C:\Users\NIKHIL\OneDrive\Desktop\image steganography\images\bird encrypted img.jpg"
password = input("Enter the passcode used for encoding: ")
decode_message_column_wise(original_image_path, encrypted_image_path, password)
