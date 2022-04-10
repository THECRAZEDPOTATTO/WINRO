import json, requests 
import os
url1 =   requests.get("https://friends.roblox.com/v1/users/1613154235/friends/count")
text1 = url1.text
data1 = json.loads(text1)
user1 = data1
friends = user1['count']
print(friends)
url = requests.get("https://api.roblox.com/users/1613154235/friends")
text = url.text
data = json.loads(text)
x = range(friends)
for user in x:
  user = data[user]
  address = user['Username']
  Online = user['IsOnline']
  print(address)
  print(Online)
  print("")
  file1 = open("users.txt","w")
    file1.write(address)
    file1.write(Online)
    file1.close() 