from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


# image = Image.open("d:\\work\\python-pri\\weiimage.jpg")
# draw = ImageDraw.Draw(image)
# draw.text((100, 6), '4', fill=(255, 0, 0), font=ImageFont.truetype())
# image.show()

# 注意新建的图片模式要选择RGBA模式。 在将小图片合并到大图片是用paste方法时要制定mask参数。这样才可以保证png图片的半透明。
def white_to_transparent(img):
    img = img.convert('RGBA')  # 返回一个转换后的图像的副本
    datas = img.getdata()
    print(list(datas))
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)  # 赋给图片新的像素数据
    return img


if __name__ == "__main__":
    p1_name = "d:\\work\\python-pri\\weiimage.jpg"
    p2_name = "d:\\work\\python-pri\\1.jpg"
    # 打开两张png图片，注意为当前路径
    p1_image = Image.open(p1_name)
    p2_image = Image.open(p2_name)
    p2_transparent = white_to_transparent(p2_image)
    p1_image.paste(p2_transparent, (645, -35), p2_transparent)
    usr_font = ImageFont.truetype("C:\\Windows\\Fonts\\STXINGKA.TTF", 32)
    draw = ImageDraw.Draw(p1_image)  # 在p1_image上绘制文字，图像
    draw.text((0, 50), '', font=usr_font)  # 在新建的对象 上坐标（50,50）处开始画出红色文本 左上角为画布坐标（0,0）点
    p1_image.save("final.png", "PNG")


