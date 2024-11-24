import random,time,os
from cryptography.fernet import Fernet
text = 242903#yyddmm
master = 0

while True:
    ran = int(random.random()*1000000)
    if ran >= 100000 and ran < 1000000:
        break
master = ran +text


ans = str(ran)+str(master)

print(ans)

    
