#!/usr/bin/env python

import urllib.request

url = 'http://download.geonames.org/export/zip/BR.zip'
zip_path = '/tmp/BR.zip'

# Download das cidades brasileiras
print('Baixando cidades brasileiras (BR.zip)')
urllib.request.urlretrieve(url, zip_path)
