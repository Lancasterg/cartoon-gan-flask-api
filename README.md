# Flask CartoonGAN API [![Docker Image CI](https://github.com/Lancasterg/cartoon-gan-flask-api/actions/workflows/docker-image.yml/badge.svg)](https://github.com/Lancasterg/cartoon-gan-flask-api/actions/workflows/docker-image.yml)

An api for developing cartoon-style images with
[CartoonGAN (CVPR 2018)](http://openaccess.thecvf.com/content_cvpr_2018/papers/Chen_CartoonGAN_Generative_Adversarial_CVPR_2018_paper.pdf), 
powered by [TensorFlow 2.0](https://www.tensorflow.org/).

The api has been developed by myself using Flask and Flask-RESTful.

!(Before and after)[https://github.com/Lancasterg/cartoon-gan-flask-api/docs/max.png]

## How to run

```commandline
python cartoonize.py \
    --input_dir input_images \
    --output_dir output_images \
    --styles shinkai hayao \
    --comparison_view horizontal
```


## Acknowledgement
- Thanks to the author `[Chen et al., CVPR18]` who published this great work
- Massive thank you to the authors of the tensorflow implementation of [CartoonGan-tensorflow](https://github.com/mnicnc404/CartoonGan-tensorflow) 
- [CartoonGAN-Test-Pytorch-Torch](https://github.com/Yijunmaverick/CartoonGAN-Test-Pytorch-Torch) where we extracted pretrained Pytorch model weights for TensorFlow usage
- [TensorFlow](https://www.tensorflow.org/) which provide many useful tutorials for learning TensorFlow 2.0:
    - [Deep Convolutional Generative Adversarial Network](https://www.tensorflow.org/alpha/tutorials/generative/dcgan)
    - [Build a Image Input Pipeline](https://www.tensorflow.org/alpha/tutorials/load_data/images)
    - [Get started with TensorBoard](https://www.tensorflow.org/tensorboard/r2/get_started)
    - [Custom layers](https://www.tensorflow.org/tutorials/eager/custom_layers)
- [Google Colaboratory](https://colab.research.google.com/) which allow us to train the models and [cartoonize images](#cartoonize-using-colab-notebook) using free GPUs
- [TensorFlow.js](https://www.tensorflow.org/js) team which help us a lot when building the [online demo](https://leemeng.tw/generate-anime-using-cartoongan-and-tensorflow2-en.html) for CartoonGAN
- [taki0112/CartoonGAN-Tensorflow](https://github.com/taki0112/CartoonGAN-Tensorflow) where we modify [edge_smooth.py](https://github.com/taki0112/CartoonGAN-Tensorflow/blob/master/edge_smooth.py) to fit our needs 
