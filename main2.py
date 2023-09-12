import yaml as ym
from PIL import Image as img


def main():
    infile = 'image.jpg'
    with img.open(infile) as im:
        im.thumbnail(128, 128)
        im.save(infile + ".thumbnail", "JPEG")
    
    with open('config.yaml') as f:
        dict = ym.full_load(f)
        print(dict)

    with open('config.yaml') as f:
        dict = ym.load(f, Loader=ym.FullLoader)
        print(dict)


if __name__ == "__main__":
    main()