#!/usr/bin/env python

import csv
import os
import urllib.request
import sqlite3
import zipfile


url = 'http://download.geonames.org/export/zip/BR.zip'
zip_path = '/tmp/BR.zip'
unzip_path = '/tmp/cidades/'
cidades_db = '/tmp/cidades.db'

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

# Cria o bando de dados
conn = sqlite3.connect(cidades_db)
conn.execute('CREATE TABLE IF NOT EXISTS cidades '
             '(cep text PRIMARY KEY, nome text, estado text);')
conn.commit()

# Le arquivo CSV
with open(unzip_path + 'BR.txt') as cidades_file:
    for linha in csv.reader(cidades_file, delimiter='\t'):
        try:
            conn.execute('INSERT INTO cidades (cep, nome, estado) '
                         'VALUES (?, ?, ? )', (linha[1], linha[2], linha[3]))
        except sqlite3.IntegrityError:
            continue

    conn.commit()
