import setuptools
with open("../README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='pythapi',  
     version='0.1',
     scripts=['pythapi'] ,
     author="Andy Geluykens",
     author_email="a.geluykens@gmail.com",
     description="A micro framework for API calls",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/geluyan/pythapi",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
     ],
)