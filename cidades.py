#!/usr/bin/env python

import urllib.request
import zipfile


url = 'http://download.geonames.org/export/zip/BR.zip'
zip_path = '/tmp/BR.zip'
unzip_path = '/tmp/cidades/'

# Download das cidades brasileiras
print('Baixando cidades brasileiras (BR.zip)')
urllib.request.urlretrieve(url, zip_path)

# Descompacta zip das cidades
with zipfile.ZipFile(zip_path) as cidades_zip:
    print('Descompactando arquivo de cidades')
    cidades_zip.extractall(unzip_path)
