

import os
from PIL import Image

UNIT_SIZE = 256 # the size of image
def pinjie(path,out_path,save_name):
   # path = "/home/ada/Music/gantest/pytorch-CycleGAN-and-pix2pix-qrcode/datasets/test_qr/orig/"
   # out_path = "/home/ada/Music/gantest/pytorch-CycleGAN-and-pix2pix-qrcode/datasets/test_qr/out_splice/"

    images = []  # images in each folder
    files = os.listdir(path)
    #print(files)
    files.sort(key=lambda x: int(x[17:-11]))  # 截取其中的数字部分
    for file in files:
        # print(file)
        images.append(Image.open(path + '/' + file))

    target = Image.new('RGB', (UNIT_SIZE*6, UNIT_SIZE*6))   # result is 2*5
    left1 = 0
    left2 = 0
    left3 = 0
    left4 = 0
    left5 = 0
    left6 = 0

    right1 = UNIT_SIZE
    right2 = UNIT_SIZE
    right3 = UNIT_SIZE
    right4 = UNIT_SIZE
    right5 = UNIT_SIZE
    right6 = UNIT_SIZE
    if not os.path.isdir(out_path):
        os.mkdir(out_path)

    for i in range(len(images)):
       # print(images[i].mode)
       # print(i)
        if  i//6==0:
           # print('left1:%d'%left1)
            target.paste(images[i], (left1, 0, right1, UNIT_SIZE))
            left1 += UNIT_SIZE #第一行左上角右移
            right1 += UNIT_SIZE #右下角右移
        elif i//6 ==1:
           # print('left2:%d'% left2)
            target.paste(images[i], (left2, UNIT_SIZE, right2, UNIT_SIZE*2))
            left2 += UNIT_SIZE #第二行左上角右移
            right2 += UNIT_SIZE #右下角右移
        elif i//6 ==2:
           # print('left3:%d'%left3)
            target.paste(images[i], (left3, UNIT_SIZE*2, right3, UNIT_SIZE*3))
            left3 += UNIT_SIZE #第三行左上角右移
            right3 += UNIT_SIZE #右下角右移
        elif i//6 ==3:
           # print('left4:%d'% left4)
            target.paste(images[i], (left4, UNIT_SIZE*3, right4, UNIT_SIZE*4))
            left4 += UNIT_SIZE #第四行左上角右移
            right4 += UNIT_SIZE #右下角右移
        elif i//6 ==4:
          #  print('left5:%d'% left5)
            target.paste(images[i], (left5, UNIT_SIZE*4, right5, UNIT_SIZE*5))
            left5 += UNIT_SIZE #第五行左上角右移
            right5 += UNIT_SIZE #右下角右移
        elif i//6 ==5:
          #  print('left6:%d'%left6)
            target.paste(images[i], (left6, UNIT_SIZE*5, right6, UNIT_SIZE*6))
            left6 += UNIT_SIZE #第六行左上角右移
            right6 += UNIT_SIZE #右下角右移
        else:
            continue





    quality_value = 100
    target.save(out_path+'result_'+save_name+'.jpg', quality = quality_value)




def splice_all_image(dir_path):
    dirlist = []  # all dir name
    for root, dirs, files in os.walk(dir_path):
        for dir in dirs :
            dirlist.append(dir)
    result_path ='./results/qr_cyclegan'
    for dir in dirlist:

       # for root, dirs, files in os.walk(dir_path+dir): # traverse each folder

        dir_path_crop =os.path.join(dir_path,dir)
      #  print(dir_path_crop)
        pinjie(dir_path_crop,result_path+'/result_set/',dir)





