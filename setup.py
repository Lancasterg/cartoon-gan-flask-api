from setuptools import setup

setup(
   name='CartoonGanApi',
   version='0.1.0',
   author='George Lancaster',
   author_email='lancaster0180@gmail.com',
   packages=['cartoon_gan', 'flask_api'],
   scripts=['flask_api/app.py'],
   license='LICENSE',
   description='A web server for creating cartoons from photos',
   long_description=open('README.md').read(),
   install_requires=[
       "numpy == 1.16.0",
       "tensorflow == 2.0.0",
       'six == 1.11.0',
       'tqdm == 4.64.1',
       'imageio == 2.15.0',
       'tb-nightly == 1.5.0a20171120',
       'pytest == 7.0.1'
   ],
)