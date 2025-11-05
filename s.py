import sys
import os
from pathlib import Path

file_paths=  list(Path.cwd().glob('*.*'))
path= './a.jpg'

def encode(path:str): 
    with open(path,'rb') as f:
        secret ='hossien014'.encode('utf-8').hex()
        binary_data = f.read()
        hex_data = binary_data.hex();
        already_encoded = hex_data.startswith(secret)
        if (already_encoded):
            print('this file already encoded you can decode this file.')
            return;

        start  = hex_data[:100]
        end = hex_data[-100:]
        hex_data=secret+end+hex_data
        hex_data
        final= bytes.fromhex(hex_data)
        # print(start,'   +++    ')
    with open(path,'wb') as f:
        f.write(final)

def decode(path:str): 
    secret ='hossien014'.encode('utf-8').hex()
    
    with open(path,'rb') as f:
        binary_data = f.read()
        hex_data = binary_data.hex()
        if(not hex_data.startswith(secret)):
            print("this is not encoded file ") 
            return
        hex_data=hex_data[100+secret.__len__():]
        final= bytes.fromhex(hex_data)


        # print(start,'   +++    ')
    with open(path,'wb') as f:
        f.write(final)

# vvv = list(Path.cwd().glob('*.*'))[2]
# aaa = vvv.name

print(f'current dirctory is : {os.getcwd()}')
print('\n enter 1 to encode all file in this directory \n enter 2 to decode all file in this directory ')

i = input();
file_paths=  list(Path.cwd().glob('*.*'))
if(i=='1'):
    for path in file_paths :
        if(Path.is_file(path) and path.name != 's.py'):
            encode(path)
            print(f'{path.name} was encoded')

elif (i=='2'):
    for path in file_paths:
        if(Path.is_file(path)):
            decode(path)
            print(f'{path.name} was decoded')
else:
    print(f'you should only type 1 or 2 your input was {i}')
# decode(path)
# encode(path)
# secret = 'hossien014'.encode('utf-8').hex().__len__();
# print(secret)
