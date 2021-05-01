import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django_image_field",
    version="1.0.0",
    author="NeuralDynamicsWeb",
    author_email="neuraldynamics.web@gmail.com",
    description="Custom image field for django 3",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NeuralDynamicsWeb/django-image-field",
    packages=setuptools.find_packages(),
    install_requires=[
        'Django>=3.2',
        'Pillow>=8.2.0'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)