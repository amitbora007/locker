import sqlite3, sys, os
#from pyfiglet import Figlet   #use this to generate different figlets on local system and copy them from terminal or visit http://patorjk.com/software/taag/#p=display&f=Rectangles&t=PLOCKER%0A
import colorama
from colorama import Fore, Back, Style
from getpass import getpass
#standar,starwars,stop,tubular,twin-cob,univers,block,avatar,arrows,,sansi,sblood,script,shadow,slant,slscript,smshadow,speed,rozzo
#text = Figlet(font='shadow') #jazmine,lean,marquee,npn_____,o8,peaks,pawp,pebbles,pepper,poison,puffy,radical_,rectangles,roman,rounded
#print(text.renderText('PLocker'))
width = os.get_terminal_size().columns
print(width)
colorama.init()
text='''                                       

			  _ \  |                |
			 |   | |      _ \   __| |  /  _ \  __|
			 ___/  |     (   | (      <   __/ |
			_|    _____|\___/ \___|_|\_\\___|_|                                        

'''
print(Fore.GREEN + text)                                          
										 

conn = sqlite3.connect("locker.db")
table =  conn.execute("CREATE TABLE IF NOT EXISTS plocker(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, SITE TEXT NOT NULL, USER TEXT NOT NULL, PWD TEXT NOT NULL)")
#if table:
#	print("Table created successfully.".center(width))
	
def insert_():
	site = input("enter sitename: ")
	user = input("enter Username: ")
	pwd = input("enter password: ")

	query = "INSERT INTO plocker(SITE, USER, PWD) VALUES(?,?,?)"
	value = (f'{site}',f'{user}',f'{pwd}')
	store = conn.execute(query,value)
	conn.commit()
	if(store):
		#print(Fore.yellow+"Data saved".center(width))
		print(Fore.yellow+"Data saved")
	print("\n")
	menu()
	
def retrieve_():	
	retrieve = conn.execute("Select * from plocker")
	for i in retrieve:
		print(i)
	print("\n")
	menu()
	
def delete_():	
	value = int(input("Enter ID of user you want to delete: "))
	query = "delete from plocker where ID=?"
	values = f'{value}'
	delete = conn.execute(query,values)
	conn.commit()
	if(delete):
		print(f"ID {value} removed")
	print("\n")	
	menu()

def update_():
	value = int(input("Enter ID of user you want to update: "))
	npass = input("Enter New Password: ")
	query = "UPDATE plocker set PWD=? where ID=?"
	values = (f'{npass}',f'{value}')
	update = conn.execute(query,values)
	conn.commit()
	if(update):
		print(f"ID {value} updated")
	print("\n")	
	menu()
	
def menu():
	print(Style.RESET_ALL)    
	print('''1. Insert data		2. Retrieve data
3. Delete data 		4. Update Password
5. Exit \n''')	

	opt = int(input("Enter choice: "))

	if(opt==1):
		insert_()
	elif(opt==2):
		retrieve_()
	elif(opt==3):
		delete_()
	elif(opt==4): 			
		update_()
	elif(opt==5):
		sys.exit()
	else: 
		print(Fore.RED+"Wrong input provided!!!")
	
if __name__=="__main__":	
	luser, lpass= "admin", "mypwdlocker"
	print(Style.RESET_ALL)
	uname = input("enter login username: ")
	upass = getpass("enter login password: ") 
	
	if((uname==luser) and (upass==lpass)):
		print(Fore.YELLOW+"Welcome to locker\n")
		menu()				
	else:
		print(Fore.RED+"Incorrect Credentials!!!")
		
		
		