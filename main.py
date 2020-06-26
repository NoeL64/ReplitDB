menu = int(input("Options \n 1: Save to DB \n 2: Get from DB"))
#importing replit dB
#explorer only (I think)
#thx codermoney 51 for making this module 
import replitdb
client = replitdb.Client()
if menu == 1:
  name = input("What would you like to name your save in the database\n")
  value = input("What would you like to assign it to?\n")
  client.add(name=value)
 elif menu == 2:
  name = input("What name would you like to get from the database?\n")
  print(client.view(name))
else:
  print("not an option")
