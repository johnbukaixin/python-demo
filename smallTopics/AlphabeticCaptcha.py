# Author:panta
# CreateDate:2019/10/29
# FileName:AlphabeticCaptcha
# IDE:PyCharm

# 生成字母验证码图片
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rnd_char():
    return chr(random.randint(65, 90))


def rnd_color():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


def rnd_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


width = 60 * 4
height = 60
# 新建一个画布
image = Image.new('RGB', (width, height), (255, 255, 255))
# 设置字体
font = ImageFont.truetype("C:\\Windows\\Fonts\\STXINGKA.TTF", 32)
#  画
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rnd_color())
for t in range(4):
    draw.text((60 * t + 10, 10), rnd_char(), font=font, fill=rnd_color2())
image = image.filter(ImageFilter.BLUR)
image.save('image\\code.jpg', 'jpeg')
