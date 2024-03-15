from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.2'
DESCRIPTION = 'CPR Package for PKiL'
LONG_DESCRIPTION = 'A package that allows for the use of PKiL in CPR'

# Setting up
setup(
    name="cpkil",
    version=VERSION,
    author="Jinendra Malekar",
    author_email="<jmalekar@email.sc.edu>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['certifi', 'charset-normalizer', 'click', 'filelock', 'Flask', 'Flask-Cors', 'gensim', 'huggingface-hub', 'idna', 'itsdangerous', 'Jinja2', 'joblib', 'MarkupSafe', 'nltk', 'numpy', 'packaging', 'Pillow', 'pyparsing', 'PyYAML', 'regex', 'requests', 'scikit-learn', 'scipy', 'sentence-transformers', 'sentencepiece', 'six', 'smart-open', 'threadpoolctl', 'tokenizers', 'torch', 'torchvision', 'tqdm', 'transformers', 'typing_extensions', 'urllib3', 'Werkzeug'],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)