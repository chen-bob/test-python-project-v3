import yaml
from PIL import Image


def main():
    infile = 'image.jpg'
    with Image.open(infile) as im:
        im.thumbnail(128, 128)
        im.save(infile + ".thumbnail", "JPEG")
    
    with open('config.yaml') as f:
        dict = yaml.full_load(f)
        print(dict)

    with open('config.yaml') as f:
        dict = yaml.load(f, Loader=yaml.FullLoader)
        print(dict)


if __name__ == "__main__":
    main()