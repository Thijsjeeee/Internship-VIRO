from zipfile import ZipFile
zf = ZipFile('Data.zip', 'r')
zf.extractall('Data/')
zf.close()
