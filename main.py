import rsa

print(" _______  _______  _______  _______  _______ ")
print("|       ||       ||       ||       ||       |")
print("|  _____||    _  ||   _   ||    _  ||   _   |")
print("| |_____ |   |_| ||  | |  ||   |_| ||  | |  |")
print("|_____  ||    ___||  |_|  ||    ___||  |_|  |")
print(" _____| ||   |    |       ||   |    |       |")
print("|_______||___|    |_______||___|    |_______|")
print("\n\nspopo V0.1")


def helper():
	print("\nNo helper for now.")

def idengen(ide):
	if len(ide) > 0:
		print("You already have a loaded identity, if you generate a new one, the loaded one will be unloaded. Do you want to continue ? (y/n)")
		ch = input(">")
		if ch == "n":
			return ide
	print("\nIdentity generator")
	(pub, priv) = rsa.newkeys(1024)
	name = input("Identity username : ")
	print("Created and loaded identity, generate contact ? (y/n)")
	ch = input(">")
	if ch == "y":
		congen([[pub, priv], name])
	return [[pub, priv], name]

def congen(ide):
	if len(ide) > 0:
		con = "{name: '"+ide[1]+"', publickey: '"+str(ide[0][0])+"'}"
		print("\n\n"+con+"\n\n")
	else:
		print("You have no identity loaded. Load one before generating your contact.")

def menu(ide = [], cnt = []):
	identity = ide
	contacts = cnt
	print("\nspopo menu\n")
	if len(identity) > 0:
		print("Loaded identity :", ide[1],"\n")
	print("(0) Help")
	print("(1) Generate identity")
	print("(2) Generate contact")
	print("(3) Load contact")
	print("(4) Load identity")
	print("(5) Encrypt message")
	print("(6) Decrypt message")
	print("(7) Export identity")
	print("(8) Exit")
	ch = input(">")

	if ch == "0":
		helper()
	if ch == "1":
		identity = idengen(identity)
	if ch == "2":
		congen(identity)
	if ch == "3":
		conload()
	if ch == "4":
		idenload()
	if ch == "5":
		enc()
	if ch == "6":
		dec()
	if ch == "7":
		exp()
	if ch == "8":
		print("\nGoodbye!\n")
		exit()
	if ch == "d":
		print("\nDEBUG\n\nIdentity\n",identity,"\n\nContacts\n",contacts,"\n\n")

	menu(identity,contacts)

menu()