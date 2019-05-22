
# Qrcode Deblur in PyTorch

We provide PyTorch implementations for both unpaired and paired image-to-image translation.
The code was written by [Jun-Yan Zhu](https://github.com/junyanz) and [Taesung Park](https://github.com/taesung89), and supported by [Tongzhou Wang](https://ssnl.github.io/).

This PyTorch implementation produces results comparable to or better than our original Torch software. If you would like to reproduce the same results as in the papers, check out the original [CycleGAN Torch](https://github.com/junyanz/CycleGAN) and [pix2pix Torch](https://github.com/phillipi/pix2pix) code

**Note**: The current software works well with PyTorch 0.4+. 
You may find useful information in [training/test tips](docs/tips.md) and [frequently asked questions](docs/qa.md).

## Prerequisites
- Linux or macOS
- Python 2 or 3
- CPU or NVIDIA GPU + CUDA CuDNN

## Getting Started
### Installation
- Install PyTorch 0.4+ and torchvision from http://pytorch.org and other dependencies (e.g., [visdom](https://github.com/facebookresearch/visdom) and [dominate](https://github.com/Knio/dominate)). You can install all the dependencies by
```bash
pip install -r requirements.txt
```
- Clone this repo:
```bash
git clone https://github.com/astrovida/pytorch-CycleGAN-and-pix2pix-qrcode.git
```
- For Conda users, we include a script `./scripts/conda_deps.sh` to install PyTorch and other libraries.

### CycleGAN train/test
- Download a Qrcode dataset (avaiable in):

- Train a model:
```
python train.py --dataroot ./datasets/qrcode --name deblurLightCycleGAN_4block_e6 --model deblurQr_cycle_gan  --batch_size 1 --resize_or_crop scale_width_and_crop --loadSize 372 --fineSize 372 --netG mobilenet_5blocks --norm instance --expand_radio 6 

```

The test results will be saved to a html file here: `./results/deblurLightCycleGAN_4block_e6/latest_test/index.html`.
- To view training results and loss plots, run `python -m visdom.server` and click the URL http://localhost:8097. To see more intermediate results, check out `./checkpoints/deblurLightCycleGAN_4block_e6/web/index.html`


- Test a model:
```
python test.py --dataroot ./datasets/qrcode --name deblurLightCycleGAN_4block_e6 --model deblurQr_cycle_gan  --batch_size 1 --resize_or_crop scale_width_and_crop --loadSize 372 --fineSize 372 --netG mobilenet_5blocks --norm instance --expand_radio 6

```


## [Datasets](docs/datasets.md)
Download Qrcode datasets from 

## [Training/Test Tips](docs/tips.md)
Best practice for training and testing your models.

## [Frequently Asked Questions](docs/qa.md)
Before you post a new question, please first look at the above Q & A and existing GitHub issues.


## Citation
If you use this code for your research, please cite our papers.
```
@inproceedings{CycleGAN2017,
  title={Unpaired Image-to-Image Translation using Cycle-Consistent Adversarial Networkss},
  author={Zhu, Jun-Yan and Park, Taesung and Isola, Phillip and Efros, Alexei A},
  booktitle={Computer Vision (ICCV), 2017 IEEE International Conference on},
  year={2017}
}


@inproceedings{isola2017image,
  title={Image-to-Image Translation with Conditional Adversarial Networks},
  author={Isola, Phillip and Zhu, Jun-Yan and Zhou, Tinghui and Efros, Alexei A},
  booktitle={Computer Vision and Pattern Recognition (CVPR), 2017 IEEE Conference on},
  year={2017}
}
```



## Related Projects
**[CycleGAN-Torch](https://github.com/junyanz/CycleGAN) |
[pix2pix-Torch](https://github.com/phillipi/pix2pix) | [pix2pixHD](https://github.com/NVIDIA/pix2pixHD) |
[iGAN](https://github.com/junyanz/iGAN) |
[BicycleGAN](https://github.com/junyanz/BicycleGAN)**

## Cat Paper Collection
If you love cats, and love reading cool graphics, vision, and learning papers, please check out the Cat Paper [Collection](https://github.com/junyanz/CatPapers).

## Acknowledgments
Code borrows heavily from [pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). 
