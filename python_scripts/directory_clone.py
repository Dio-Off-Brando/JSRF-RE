import os
from os.path import join, getsize


for root, dirs, files in os.walk('../'):
    print(dirs)