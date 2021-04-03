import PIL
import random


class ImageUnifier:

    def __init__(self, image=None, random_from=0, random_to=0):
        self.image = image
        self.result_image = None

    def get_random_value(self, value):
        k = -1 if random.randint(0, 1) else 1
        r = value + (random.randint(50, 100) * k)
        if r < 0:
            return 0
        if r > 255:
            return 255
        return value

    def get_random_rgb(self, rgb):
        return tuple([self.get_random_value(x) for x in rgb])

    def create_new_image(self):
        result_image = PIL.Image.open(self.image.file.file).convert('RGB')
        width, height = result_image.size[0], result_image.size[1]
        for y in range(height):
            for x in range(0, width):
                rgb = result_image.getpixel((x, y))
                r, g, b = rgb
                random_rgb = self.get_random_rgb(rgb)
                result_image.putpixel((x, y), random_rgb)
        self.result_image = result_image
        return self.result_image
