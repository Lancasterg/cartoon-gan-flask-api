import glob
from os.path import splitext

import numpy as np
from PIL import Image
from flask import send_file
from flask_restful import reqparse, Resource
from werkzeug.datastructures import FileStorage

from cartoon_gan.cartoonize import pre_processing, post_processing
from cartoon_gan.style_transfer import cartoongan


class ModelEndpointResource(Resource):
    STYLE = "super_style"
    ENDPOINT = "super_endpoint"

    DIR_TMP = "/tmp/{}"
    STR_FILE = "file"
    STR_FILES = "files"
    STR_IMAGE_GIF = "image/gif"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = cartoongan.load_model(self.get_style())

    def get_style(self):
        return self.STYLE

    def get_endpoint(self):
        return self.ENDPOINT

    def post(self):
        parse = reqparse.RequestParser()
        parse.add_argument(self.STR_FILE, type=FileStorage, location=self.STR_FILES)
        args = parse.parse_args()
        request_image_file = args[self.STR_FILE]

        local_image_file_str = self.DIR_TMP.format(f"1_{splitext(request_image_file.filename)[-1]}")

        request_image_file.save(local_image_file_str)
        image_path = glob.glob(local_image_file_str)[0]

        input_image = pre_processing(image_path, style=self.get_style())
        save_dir = "/tmp/output.png"

        transformed_image = self.model.predict(input_image, use_multiprocessing=True)
        output_image = post_processing(transformed_image, style=self.get_style())
        im = Image.fromarray(output_image.astype(np.uint8))
        im.save(save_dir)

        return send_file(save_dir, mimetype=self.STR_IMAGE_GIF)
