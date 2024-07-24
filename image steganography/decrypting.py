import cv2
import os

def encode_message_column_wise(image_path, msg, output_path):
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found. Check the file path and make sure the image exists.")
        exit()

    height, width, channels = img.shape

    # Create dictionaries for ASCII conversion
    d = {chr(i): i for i in range(256)}

    # Initialize variables for encoding
    n = 0  # Row index
    m = 0  # Column index
    z = 0  # Color channel index

    # Encode the message
    for i in range(len(msg)):
        # Calculate the new pixel value
        new_value = (int(img[n, m, z]) + d[msg[i]]) % 256
        img[n, m, z] = new_value

        # Move to the next pixel
        n += 1
        if n >= height:
            n = 0
            m += 1
        if m >= width:
            print("Image too small to hold the entire message.")
            break
        
        z = (z + 1) % 3

    # Save the modified image
    cv2.imwrite(output_path, img)
    print(f"Message has been encoded into '{output_path}'.")

# Usage
image_path = r"C:\Users\NIKHIL\OneDrive\Desktop\bird img.png"
output_path = os.path.join(os.path.dirname(image_path), "encryptedImage_column_wise.jpg")
msg = input("Enter secret message: ")
encode_message_column_wise(image_path, msg, output_path)




import cv2

def decode_message_column_wise(image_path, message_length):
    img = cv2.imread(image_path)
    if img is None:
        print("Image not found. Check the file path and make sure the image exists.")
        return

    height, width, channels = img.shape

    # Initialize variables for decoding
    n = 0  # Row index
    m = 0  # Column index
    z = 0  # Color channel index
    decoded_message = ""

    # Extract the message
    for i in range(message_length):
        pixel_value = int(img[n, m, z])
        decoded_message += chr(pixel_value)

        # Move to the next pixel
        n += 1
        if n >= height:
            n = 0
            m += 1
        if m >= width:
            print("Image too small to contain the entire message.")
            break
        
        z = (z + 1) % 3

    # Print the decoded message
    print("Decoded message:", decoded_message)

# Usage
image_path = r"C:\Users\NIKHIL\OneDrive\Desktop\encryptedImage_column_wise.jpg"
message_length = int(input("Enter the length of the message (in characters): "))
decode_message_column_wise(image_path, message_length)
