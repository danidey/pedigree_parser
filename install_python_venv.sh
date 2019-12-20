# AUTHOR: Daniela Dey
# (tested on Ubuntu 18.04.2 LTS)

# Script to create a virtual python3.6 environment with the needed python packages installed. Needs python3-venv installed:
# sudo apt install python3-venv

# if primer3-py fails due to x86_64-linux-gnu-gcc error, run:
# sudo apt-get install libxml2-dev libxslt1-dev

virtualenv --python=python3.6 .env && source .env/bin/activate && pip install -r requirements.txt

