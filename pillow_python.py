from PIL import Image , ImageFilter
before=Image.open('image.jpg')
box=(0,0,100,100)
after=before.crop(box)

after.show()