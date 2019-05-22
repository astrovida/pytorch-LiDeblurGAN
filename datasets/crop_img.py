from PIL import Image
import os

def cut(datasets_path,vx=62,vy=62):

   # path = "/home/ada/Music/gantest/pytorch-CycleGAN-and-pix2pix-master/datasets/test_qr/test_orig/"
    path =datasets_path+'/test_orig/'
    path_save = datasets_path+'/testA/'
    img_list = os.listdir(path)
    num_list =len(img_list)

    dx = vx
    dy = vy


    for i in range(num_list):
        x1 = 0
        y1 = 0
        x2 = vx
        y2 = vy
        n = 1
        name_A = img_list[i]
        name_save = name_A.replace('.png','_crop_')
        path_A = os.path.join(path, name_A)
        im = Image.open(path_A)
        while x2 <= 372:
            while y2 <= 372:
                name3 = path_save + name_save+ str(n) + ".jpg"
                # print n,x1,y1,x2,y2
                im2 = im.crop((y1, x1, y2, x2))
                im2.save(name3)
                y1 = y1 + dy
                y2 = y1 + vy
                n = n + 1
            x1 = x1 + dx
            x2 = x1 + vx
            y1 = 0
            y2 = vy


    return n-1

