import glob
import os

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


FONT = ImageFont.truetype(r"fonts/OpenSans-Medium.ttf", 24)
IMAGE_FILES = glob.glob("./source-images/*.jpg")
PATH_FOR_OUTPUT = "./output-images/"

# Checking if the folder for output exists
if not os.path.exists(PATH_FOR_OUTPUT):
    os.makedirs(PATH_FOR_OUTPUT)

for image_file in IMAGE_FILES:
    image_name = os.path.basename(image_file)
    sign_text = "@" + image_name.split(".")[0].replace("-", " ").title()
    with open(image_file, "rb") as file:
        image = Image.open(file)
        draw = ImageDraw.Draw(image)

        # Getting image sizes
        image_width, image_height = image.size
        # Getting sign sizes
        text_width, text_height = FONT.getsize(sign_text)

        # Calculating a position for the sign
        sign_position_X = image_width * 0.99 - text_width
        sign_position_Y = image_height * 0.99 - text_height

        draw.text(
            (sign_position_X, sign_position_Y), sign_text, font=FONT, fill="white"
        )
        image.save("output-images/" + image_name, "PNG")
