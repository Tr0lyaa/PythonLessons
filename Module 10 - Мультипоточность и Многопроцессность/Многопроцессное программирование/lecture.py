import multiprocessing
from PIL import Image
import datetime
# 0:00:00.248638
# 0:00:00.106963


def resize_image(image_path):
    image = Image.open(image_path)
    image = image.resize((800, 600))
    image.save(f"./images_2{image_path[8:]}")


if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        all_images = []
        for i in range(7, 13):
            all_images.append(f"./images/img_{i}.jpg")
        start = datetime.datetime.now()
        pool.map(resize_image, all_images)
        end = datetime.datetime.now()
        print(end - start)

    start = datetime.datetime.now()
    for i in range(1, 7):
        image_path = f"./images/img_{i}.jpg"
        resize_image(image_path)
    end = datetime.datetime.now()
    print(end - start)
