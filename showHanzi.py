from PIL import Image, ImageDraw, ImageFont
import numpy as np 
import time
im02 = Image.open("./Hello.png")
draw = ImageDraw.Draw(im02)
print(im02.size)
# ft = ImageFont.truetype("./启功字体简体.TTF", 50)
# draw.text((30,int((1-0.618)*im02.height)-50), u"这是我第一次在天空里使用启功字体。",font = ft, fill = 'black')

# ft = ImageFont.truetype("./王羲之书法字体.ttf", 50)
# draw.text((30,70), u"永和九年 岁在癸丑 王羲之",font = ft, fill = 'black')

ft = ImageFont.truetype("./赵孟頫楷书.ttf", 50)
draw.text((30,130), u"欲穷千里目 更上一层楼",font = ft, fill = 'black')



im02.show()
im02.save('Zhaomengfu.png')
time.sleep(3)
