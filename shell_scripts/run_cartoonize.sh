#!/bin/bash
PYTHONPATH=..
python ../cartoon_gan/cartoonize.py \
    --input_dir ../cartoon_gan/input_images \
    --output_dir ../cartoon_gan/output_images \
    --styles shinkai hayao \
    --comparison_view horizontal