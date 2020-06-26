menu = int(input("Options \n 1: Save to DB \n 2: Get from DB"))
 

import replitdb
client = replitdb.Client()
if menu == 1:
  name = input("What would you like to name your save in the database")
  value = input("What would you like to assign it to?")
  client.add(name=value)
 else:
