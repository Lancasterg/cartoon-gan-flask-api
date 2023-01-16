# Flask CartoonGAN API [![Docker Image CI](https://github.com/Lancasterg/cartoon-gan-flask-api/actions/workflows/docker-image.yml/badge.svg)](https://github.com/Lancasterg/cartoon-gan-flask-api/actions/workflows/docker-image.yml)

An api for developing cartoon-style images with
[CartoonGAN (CVPR 2018)](http://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_CartoonGAN_Generative_Adversarial_CVPR_2018_paper.pdf), 
powered by [TensorFlow 2.0](https://www.tensorflow.org/). Deployed using Flask and Flask-RESTful.

![Before and after](https://github.com/Lancasterg/cartoon-gan-flask-api/blob/main/docs/maz.png)

## Setup
Clone the repository.
```
$ git clone https://github.com/Lancasterg/cartoon-gan-flask-api.git 
```

Install the requirements (cpu).
```
$ python -m virtualenv cartoon-gan-venv     // create a venv

$ source activate cartoon-gan-venv          // init venv

$ pip install -r requirements-server.txt    // install requirements for flask server

$ pip install -r requirements-cpu.txt       // install requirements for ml
```

## API

### Dev 
Start the API in development mode.
```
$ python flask_api/app.py
```

Test the API.
```
$ bash shell_scripts/hit_api.sh 
```

### Backend

Run the `cartoonize.py` command to test the GAN.

```commandline
python cartoonize.py \
    --input_dir input_images \
    --output_dir output_images \
    --styles shinkai hayao \
    --comparison_view horizontal
```


## Acknowledgements
- Thanks to the author `[Chen et al., CVPR18]` who published this great work
- Massive thank you to the authors of the tensorflow implementation of [CartoonGan-tensorflow](https://github.com/mnicnc404/CartoonGan-tensorflow) 
- [CartoonGAN-Test-Pytorch-Torch](https://github.com/Yijunmaverick/CartoonGAN-Test-Pytorch-Torch) where we extracted pretrained Pytorch model weights for TensorFlow usage
