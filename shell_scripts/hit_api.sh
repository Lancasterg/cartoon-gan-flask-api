#!/bin/bash

echo -e "Using model: $1\n"

curl -F "file=@../cartoon_gan/input_images/maz.png" http://localhost:5000/v1/$1 >> /tmp/processed_image_$1.png

echo -e "\nImage written to: /tmp/processed_image_$1.png"