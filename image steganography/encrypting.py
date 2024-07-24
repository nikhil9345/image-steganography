from PIL import Image

def encode_message_column_wise(image_path, msg, password, output_path):
    # Open the image
    image = Image.open(image_path, 'r')
    newimage = image.copy()

    if image is None:
        print("Image not found. Check the file path and make sure the image exists.")
        exit()

    # Get the dimensions of the image
    width, height = image.size

    # Initialize dictionaries for mapping characters to their ASCII values and vice versa
    d = {chr(i): i for i in range(256)}
    c = {i: chr(i) for i in range(256)}

    # Append a termination character to the message
    msg += '\x00'

    k = 0
    for j in range(width):  # Column-wise
        for i in range(height):  # Iterate over rows within each column
            if k < len(msg):
                # Get the current pixel value
                r, g, b = image.getpixel((j, i))
                # Encode the character into the red channel of the pixel
                new_r = (r + int(password) + d[msg[k]]) % 256
                # Update the pixel value in the new image
                newimage.putpixel((j, i), (new_r, g, b))
                k += 1
            else:
                break
        if k >= len(msg):
            break

    # Save the modified image to a new file
    newimage.save(output_path, str(output_path.split(".")[1].upper()))

    print(f"Message has been encoded into '{output_path}'.")

# Usage
image_path = "C:\Users\NIKHIL\OneDrive\Desktop\image steganography\images\bird img.png"
output_path ="C:\Users\NIKHIL\OneDrive\Desktop\image steganography\images\bird encrypted img.jpg"
msg = input("Enter secret message: ")
password = input("Enter a passcode: ")
encode_message_column_wise(image_path, msg, password, output_path)
