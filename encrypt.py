from Crypto.Cipher import AES
from Crypto import Random
import base64
import shutil
import os

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

# Making a zip file of the `OpenSource` folder
shutil.make_archive('SourceCode.zip', 'zip', 'OpenSource')

# Reading the zip file
with open('SourceCode.zip', 'rb') as f:
    RawContent = f.read()

# Deleting the zip file
os.remove('SourceCode.zip')

# Encrypting the zip file
AES = AESCipher('MinecraftServerForeverAtFluxGamming-')
EncryptedRaw = AES.encrypt(RawContent)

# Saving the encrypted file
with open('SourceCode.zip.aes256', 'wb+') as f:
    f.write(EncryptedRaw)
