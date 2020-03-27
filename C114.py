import urllib
import urllib.request
try:
    urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('ERRO AO CONECTAR AO SITE PUDIM')
else:
    print('SUCESSO AO CONECTAR AO SITE PUDIM')
