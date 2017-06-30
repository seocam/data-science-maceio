#!/usr/bin/env python

import os
import urllib.request
import zipfile


url = 'http://download.geonames.org/export/zip/BR.zip'
zip_path = '/tmp/BR.zip'
unzip_path = '/tmp/cidades/'

if not os.path.exists(zip_path):
    # Download das cidades brasileiras
    print('Baixando cidades brasileiras (BR.zip)')
    urllib.request.urlretrieve(url, zip_path)
else:
    print('Arquivo de cidades brasileiras já existe')

# Descompacta zip das cidades
with zipfile.ZipFile(zip_path) as cidades_zip:
    print('Descompactando arquivo de cidades')
    cidades_zip.extractall(unzip_path)
