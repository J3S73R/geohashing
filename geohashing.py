import hashlib

lat = float(raw_input("insert latitude "))
estovest = raw_input("insert e for East or w for West ")
lon = float(raw_input("insert longitude "))
nordsud = raw_input("insert n for Nord or s for Sud ")
tollerance = input("insert tollerance ")

def latmanipulation(latitude,TD,estovest) :
    lat = latitude * 10000 / (TD * 6) #moltiplico per 10000 la latitudine e la divido per la tolleranza * 6
    lat1 = str(bin(int(lat)))
    if estovest == "e" :
        lat1 = lat1[:2] + "1" + lat1[2:]
    elif estovest == "o":
        lat1 = lat1[:2] + "0" + lat1[2:] #aggiungo uno zero o un 1 a seconda che la latitudine sia Est o Ovest
    lat2 = int(lat1,2)
    return lat2 #ritorno il valore manipolato della latitudine

def lonmanipulation(longitude,TD,nordsud) :
    lon = longitude * 10000 / (TD * 5.4) #moltiplico per 10000 la longitudine e la divido per la tolleranza * 5,4
    lon1 = str(bin(int(lon)))
    if nordsud == "n" :
        lon1 = lon1[:2] + "1" + lon1[2:]
    elif nordsud == "s"  :
        lon1 = lat1[:2] + "0" + lon1[2:] #aggiungo uno zero o un 1 a seconda che la longitudine sia Nord o Sud
    lon2 = int(lon1,2)
    return lon2 #ritorno il valore manipolato della longitudine

sumcoord = latmanipulation(lat,tollerance,estovest) + lonmanipulation(lon,tollerance,nordsud)

md5 = hashlib.md5(str(sumcoord)).hexdigest()
print md5
