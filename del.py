import os, time
from cryptography.fernet import Fernet

detail = []
detail.append(str(input("Enter username ")))
detail.append(str(input("Enter password ")))

search = ""
for i in range(0,len(detail[0])):
    search += chr(ord(detail[0][i:i+1])+113)
    
try:
    search = search+".txt"
    info = open(os.getcwd()+"\data\Ü¥¦"+search,"rb")
except FileNotFoundError:
    print("The username or password password is incorrect")
    time.sleep(5)
    quit
key = info.readline()
real = info.readline()
dob = info.readline()
fav = info.readline()
store = info.readline()
info.close()

f = Fernet(key)
real = real = f.decrypt(real)
real = real.decode()

dob = dob = f.decrypt(dob)
dob = dob.decode()

fav = fav = f.decrypt(fav)
fav = fav.decode()

store = store = f.decrypt(store)
store = store.decode()

if "\n" in real:
    real = real[0:-1]

if "\n" in dob:
    dob = dob[0:-1]

if "\n" in fav:
    fav = fav[0:-1]

if "\n" in store:
    store = store[0:-1]

if real == detail[1]:
    login = True
else:
    login = False

storage = [""]
storage[0] = store
run = True



if login == True:
    if len(storage[0]) != 6:
        storage[0] = storage[0].replace("Store:","")
        while run:
            if "," in storage[0]:
                coma = int(storage[0].find(","))
                storage.append(storage[0][0:coma])
                storage[0] = storage[0][coma+1:len(storage[0])]
            else:
                run = False
    print("Select which password to delete")
    for i in range(0,len(storage)):
        print("press:",i,"to delete","'",storage[i],"'")
    op = int(input())
    new = str(storage[op])

    coma = int(store.find(","))
    if coma != -1:
        if store[6:6+len(new)] == new:
            new = storage[op]+","
            store = store.replace(new,"")
        else:
            new = ","+storage[op]
            store = store.replace(new,"")
    elif store[6:len(store)] == new:
        store = store.replace(new,"")
    else:
        print("What now")

    key = key = Fernet.generate_key()
    f = Fernet(key)

    real = real.encode()
    real = f.encrypt(real)

    dob = dob.encode()
    dob = f.encrypt(dob)

    fav = fav.encode()
    fav = f.encrypt(fav)

    store = store.encode()
    store = f.encrypt(store)
    
    info = open(os.getcwd()+"\data\Ü¥¦"+search,"wb")
    
    info.write(key)
    info.write(b'\n')
    info.write(real)
    info.write(b'\n')
    info.write(dob)
    info.write(b'\n')
    info.write(fav)
    info.write(b'\n')
    info.write(store)

    info.close()
    saved = ""
    for i in range(1,len(storage [op])):
        saved += chr(ord(storage [op][i-1:i])+133)
    saved += ".txt"
    os.remove(os.getcwd()+"\data\Ü¥¦"+saved)






    
