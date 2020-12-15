#use disk SN as code

import win32api
import hashlib     #use MD5 to encrypt

def getSN():
    SN = win32api.GetVolumeInformation("C:\\")[1]     #get disk SN from C:
    #print(SN)
    return SN

def encr(str):
    m = hashlib.md5()   #use md5 funktion
    m.update(str.encode(encoding='utf-8'))   #encoding
    n = m.hexdigest()    #转换为16进制字符串cover to hex
    return n

def codegen():
    SNcode = getSN()
    SNcode = str(SNcode)   #conover to string
    Mcode = encr(SNcode)
    return Mcode

if __name__ == '__main__':
    print(codegen())
