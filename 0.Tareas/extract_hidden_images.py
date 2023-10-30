# ----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# Date: 25-Aug-2023
# Authors:
#           A01753729 Marco Antonio Caudillo Morales
#           A01754412 Adolfo Sebastián González Mora
# ----------------------------------------------------------

from PIL import Image
import sys

OUTPUT_FILE_NAME1 = 'scarlett_channel_1_red.png'
OUTPUT_FILE_NAME2 = 'scarlett_channel_2_green.png'
OUTPUT_FILE_NAME3 = 'scarlett_channel_3_blue.png'


def process_image(INPUT_FILE_NAME) -> None:
    if not INPUT_FILE_NAME.endswith('.png'):
        print(f"The file '{INPUT_FILE_NAME}' doesn’t have a .png extension")
        return

    try:
        with Image.open(INPUT_FILE_NAME) as input_file:
            pixin = input_file.load()
            width, height = input_file.size

            if input_file.mode != 'RGB':
                print(f"The mode of the file '{INPUT_FILE_NAME}' is not RGB")
                return

    except FileNotFoundError:
        print(f'The file {INPUT_FILE_NAME} was not found in the directory')
        return

    except Exception as error:
        print(f"An error occurred: {str(error)}")
        return

    scarlett_red = Image.new('1', (width, height))
    scarlett_green = Image.new('1', (width, height))
    scarlett_blue = Image.new('1', (width, height))

    for y in range(height):
        for x in range(width):
            r, g, b = pixin[x, y]
            scarlett_red.putpixel((x, y), r & 1)
            scarlett_green.putpixel((x, y), g & 1)
            scarlett_blue.putpixel((x, y), b & 1)

    scarlett_red.save(OUTPUT_FILE_NAME1)
    scarlett_green.save(OUTPUT_FILE_NAME2)
    scarlett_blue.save(OUTPUT_FILE_NAME3)


if __name__ == '__main__':
    # Check if file name was provided as command line argument
    if len(sys.argv) < 2:
        print("Please provide a PNG file name as a command line argument.")
    else:
        process_image(sys.argv[1])
