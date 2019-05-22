
import os
from PIL import Image
from pyzbar.pyzbar import decode


def decode_qrcode(url,file_name):
	decode_result = decode(Image.open(url))
	if len(decode_result):
		return str(decode_result[0].data, encoding='utf-8')
	else:

		fp.write(file_name+'\n')


		return 'cannot recognize------------'

#path = "/home/ada/Music/gantest/pytorch-CycleGAN-and-pix2pix-qrcode/results/qr_cyclegan/result_set"

path = "/home/ada/Music/gantest/pytorch-CycleGAN-and-pix2pix-qrcode/results/qr_code_full_20181023_deblurQr/result"

files = os.listdir(path)
fp =open('/home/ada/Music/gantest/pytorch-CycleGAN-and-pix2pix-qrcode/results/qr_code_full_20181023_deblurQr/miss_log.txt','a')
for file in files:
	print(file)
	# decode
	#qr = qrtools.QR()
	#qr.decode(path + '/' + file)

	print(decode_qrcode(path + '/' + file,file))






