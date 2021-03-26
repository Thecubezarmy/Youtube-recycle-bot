import queryfunction

print ("enter username")
username = input()
print("enter password")
password= input()
print("enter youtbe v3 data API key")
APIkey=input()
print("enter the number of songs")
videonumber=int(input())
listofsongs=[]
while videonumber > 0:
    print ("please type the name of the song")
    locallist=input()
    listofsongs.append(locallist)
    videonumber =  videonumber - 1


