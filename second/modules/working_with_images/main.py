import glob
import os.path

from PIL import Image


def copy_to_this_folder(generic_path: str):
    image = Image.open(glob.glob(generic_path)[0])
    image_name = image.filename.split("\\")[-1]
    if not os.path.exists(image_name):
        image_copy = image.copy()
        image_copy.save(image_name)


copy_to_this_folder("../web_scrapping/images/*.jpg")
i = Image.open(glob.glob("*.jpg")[0])
i.show()
