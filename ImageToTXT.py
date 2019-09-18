from PIL import Image

def img_txt():
    for each in range(0, 100):
        org_img = Image.open('/Users/jingjing/Documents/Python_file/projects/face/face_img/' + str(each) + '.JPG')
        org_img = org_img.transpose(Image.FLIP_LEFT_RIGHT).rotate(90)
        img = org_img.resize((32, 32), Image.NEAREST)
        length = img.size[0]
        width = img.size[1]

        img_file = open('/Users/jingjing/Documents/Python_file/projects/face/face_txt/' + str(each) + '.txt', 'a')
        for i in range(0, length):
            for j in range(0, width):
                color = img.getpixel((i,j))
                all_color = color[0] + color[1] + color[2]
                if all_color == 0:
                    img_file.write('1')
                else:
                    img_file.write('0')
            img_file.write('\n')
        img_file.close()
