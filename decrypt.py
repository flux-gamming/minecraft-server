from Crypto.Cipher import AES
from Crypto import Random
import zipfile
import base64
import shutil
import sys
import os

key = sys.argv[2]

class AESCipher:
    def __init__( self, key ):
        self.key = key

    def encrypt( self, raw ):
        raw = pad(raw)
        iv = Random.new().read( AES.block_size )
        cipher = AES.new( self.key, AES.MODE_CBC, iv )
        return base64.b64encode( iv + cipher.encrypt( raw ) ) 

    def decrypt( self, enc ):
        enc = base64.b64decode(enc)
        iv = enc[:16]
        cipher = AES.new(self.key, AES.MODE_CBC, iv )
        return unpad(cipher.decrypt( enc[16:] ))

# Reading the aes256 encrypted zip
with open('SourceCode.zip.aes256', 'rb') as f:
    EncryptedRaw = f.read()

# Decrypting the aes256 data
AES = AESCipher(key)
DecryptedRaw = AES.decrypt(EncryptedRaw)

# Saving the DecryptedRaw data to a zip file
with open('SourceCode.zip', 'wb+') as f:
    f.write(DecryptedRaw)

# Unziping SourceCode.zip 
with zipfile.ZipFile("SourceCode.zip","r") as zip_ref:
    zip_ref.extractall("SourceCode")
