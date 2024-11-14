import os
from PIL import Image
from tqdm import tqdm
import time

# function to convert decimal to binary
def decimalToBinary(n):
    return bin(n).replace("0b", "")

# function to convert binary to decimal
def binaryToDecimal(n):
    return int(n, 2)

# function to hide a message in an image
def hideMessage(image_path, message):
    # open the image file
    img = Image.open(image_path)
    # convert message to binary
    binary_message = ''.join([format(ord(i), "08b") for i in message])
    # get the width and height of the image
    width, height = img.size
    # calculate the maximum number of bits that can be hidden
    max_bits = width * height * 3
    if len(binary_message) > max_bits:
        raise ValueError("Message too large to hide in image")
    # add a sentinel value to indicate the end of the message
    binary_message += '1111111111111110'
    # iterate over each pixel in the image
    index = 0
    progress_bar = tqdm(total=max_bits, unit='bit', ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}')
    for row in range(height):
        for col in range(width):
            # get the RGB values of the pixel
            r, g, b = img.getpixel((col, row))
            # convert the RGB values to binary
            r_bin = decimalToBinary(r)
            g_bin = decimalToBinary(g)
            b_bin = decimalToBinary(b)
            # hide the message in the least significant bit of each color channel
            if index < len(binary_message):
                r_bin = r_bin[:-1] + binary_message[index]
                index += 1
            if index < len(binary_message):
                g_bin = g_bin[:-1] + binary_message[index]
                index += 1
            if index < len(binary_message):
                b_bin = b_bin[:-1] + binary_message[index]
                index += 1
            # convert the binary back to decimal
            r = binaryToDecimal(r_bin)
            g = binaryToDecimal(g_bin)
            b = binaryToDecimal(b_bin)
            # update the pixel with the new RGB values
            img.putpixel((col, row), (r, g, b))
            # update the progress bar
            progress_bar.update(3)
    # save the modified image
    new_image_path = os.path.splitext(image_path)[0] + '_hidden.png'
    img.save(new_image_path)
    # close the progress bar
    progress_bar.close()

# function to retrieve a message from an image
def retrieveMessage(image_path):
    # open the image file
    img = Image.open(image_path)
    # get the width and height of the image
    width, height = img.size
    # iterate over each pixel in the image
    binary_message = ''
    for row in range(height):
        for col in range(width):
            # get the RGB values of the pixel
            r, g, b = img.getpixel((col, row))
            # convert the RGB values to binary
            r_bin = decimalToBinary(r)
            g_bin = decimalToBinary(g)
            b_bin = decimalToBinary(b)
            # retrieve the least significant bit from each color channel
            binary_message += r_bin[-1]
            binary_message += g_bin[-1]
            binary_message += b_bin[-1]
            # check if the sentinel value has been reached
            if binary_message[-16:] == '1111111111111110':
                binary_message = binary_message[:-16]
                # convert the binary message back to ASCII
                message = ''
                for i in range(0, len(binary_message), 8):
                    message += chr(binaryToDecimal(binary_message[i:i+8]))
                return message


print("Welcome to Image Steganography!")
print('\n')
# the path to the image you want to hide the message in
image_path = 'steganography/image.jpg'

# get the message from the user
message = input("Enter the message you want to hide: ")
print('\n')
# hide the message in the image
print("Hiding message...")
hideMessage(image_path, message)
print("Message hidden successfully!")

# the path to the modified image that contains the hidden message
modified_image_path = 'steganography/image_hidden.png'
print('\n')
print(f"Encoded Image with secret message is created at {modified_image_path}")
print('\n')
# retrieve the hidden message from the image
print("Retrieving message...")
retrieved_message = retrieveMessage(modified_image_path)
print("Message retrieved successfully!")
print('\n')
# print the hidden message
print("The hidden message is:", retrieved_message)
