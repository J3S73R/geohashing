import hashlib

lat = float(raw_input("insert latitude "))
estovest = raw_input("insert e for East or w for West ")
lon = float(raw_input("insert longitude "))
nordsud = raw_input("insert n for Nord or s for Sud ")
tollerance = input("insert tollerance ")

"""lat = 12134.5971
estovest = "e"
tollerance = 5"""
def latmanipulation(latitude,TD,estovest) :
    lat = latitude * 10000 / (TD * 6) #moltiplico per 10000 la latitudine e la divido per la tolleranza * 6
    lat = lat - (lat % 1)
    lat1 = str(bin(int(lat)))
    if estovest == "o":
        lat1 = lat1[:2] + "1" + lat1[2:] #aggiungo uno zero 0 un 1 a seconda che la latitudine sia Est o Ovest
    lat1 = lat1[:0] + lat1[2:]
    return lat1 #ritorno il valore manipolato della latitudine

"""lon = 2504.7314
nordsud = "n"
tollerance = 5"""
def lonmanipulation(longitude,TD,nordsud) :
    lon = longitude * 10000 / (TD * 5.4) #moltiplico per 10000 la longitudine e la divido per la tolleranza * 5,4
    lon = lon - (lon % 1)
    lon1 = str(bin(int(lon)))
    if nordsud == "n" :
        lon1 = lon1[:2] + "1" + lon1[2:]#aggiungo uno zero 0 un 1 a seconda che la latitudine sia Nord o Sud
    lon1 = lon1[:0] + lon1[2:]
    return lon1 #ritorno il valore manipolato della longitudine

latman = latmanipulation(lat,tollerance,estovest)

lonman = lonmanipulation(lon,tollerance,nordsud)

sumcoord = int(latman,2) ^ int(lonman,2)#Xor binario dei due valori ritornati dalle manipolazioni delle coordinare

md5 = hashlib.md5(str(sumcoord)).hexdigest()#md5 del valore dello Xor
print md5 

"""COMMENT: Nella sezione commentata sopra le funzioni sono stati aggiunti i valori dell'esperimento condotto nel paper, togliendo
gli inserimenti e scommantando tali valori lo script ritorna il risultato esatto riportato nell'esempio dello studio riportato a pg.66"""