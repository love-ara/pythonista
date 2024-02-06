num = int(input("Enter any number to go to the main menu: "))
 
print(" ")
print("   MAIN MENU ")
print("1.  Phone book \n2.  Messages \n3.  Chat \n4.  Call Register \n5.  Tones \n6.  Settings \n7.  Call Divert \n8.  Games \n9.  Calculator \n10. Remainders \n11. Clock \n12. Profiles \n13. SIM services")

print(" ")

menu = int(input("Press a number from (1-13) to select: "))

if menu == 1:
	print("Phone Book")
	print(" ")
	print("1.  Search \n2.  Service Nos \n3.  Add Name \n4.  Erase \n5.   Edit \n6.  Assign Tone \n7.  Send B'Card \n8.  Options \n9.  Speed Dials \n10. Voice Tags")
	phone_book = int(input("Enter a number from 1-10 to select: "))
	if phone_book == 1:
		print("Search")
	elif phone_book == 2: 
		print("Service Nos")
	elif phone_book == 3:
		print("Add Name")
	elif phone_book == 4:
		print("Erase")
	elif phone_book == 5:
		print("Edit")
	elif phone_book == 6:
		print("Assign Tone")
	elif phone_book == 7:
		print("Send B'Card")
	elif phone_book == 8:
		print("Options")
		print("1.Type of view \n2.Memory Status")
		options = int(input("Enter 1 or 2: "))
		if options == 1:
			print("Type of view")
		if options == 2:
			print("Memory Status")
	elif phone_book == 9:
		print("Speed Dials")
	elif phone_book == 10:
		print("Voice Tags")

elif menu == 2:
	print("Messages")
	print("1.Write messages \n2.  Inbox \n3.  Outbox \n4.  Picture messages \n5.  Templates \n6.  Smileys \n7.  Message settings \n8.  Info service \n9.  Voice mailbox number \n10. Service command editor")
	Messages = int(input("Enter a number from 1-10 to select: "))
	if Messages == 1:
		print("Write messages")
	elif Messages == 2: 
		print("Inbox")
	elif Messages == 3:
		print("Outbox")
	elif Messages == 4:
		print("Picture messages")
	elif Messages == 5:
		print("Templates")
	elif Messages == 6:
		print("Smileys")
	elif Messages == 7:
		print("Message settings")
		print("1. Set 1 \n2. Common")
		message_settings = int(input("Enter 1 or 2: "))
		if message_settings  == 1:
			print("Set")
			print("1. Message centre number \n2. Message sent as \n3. Message settings")
			set = int(input("To select enter 1, 2 or 3: "))
			if set == 1:
				print("Message centre number")
			elif set == 2:
				print("Message sent as")
			elif set == 3:
				print("Message settings")
			
		elif message_settings  == 2:
			print("Common")
			print("1. Delivery reports \n2. Reply via same centre \n3. Character support")
			common = int(input("To select enter 1, 2 or 3: "))
			if common == 1:
				print("Delivery reports")
			elif common == 2:
				print("Reply via same centre")
			elif common == 3:
				print("Character support")
	elif Messages == 8:
		print("Info service")
	elif Messages == 4:
		print("Voice mailbox number")
	elif Messages == 5:
		print("Service command editor")
			



elif menu == 3:
	print("Chat")

elif menu == 4:
	print("Call Register")
	print("1. Missed calls \n2. Received calls \n3. Dialled numbers \n4. Erase recent call lists \n5. Show call duration \n6. Show call costs \n7. Call cost settings \n8. Prepaid credit")
	call_register = int(input("Enter a number from 1-10 to select: "))
	if call_register == 1:
		print("Missed calls")
	elif call_register == 2: 
		print("Received calls")
	elif call_register == 3:
		print("Dialled numbers")
	elif call_register == 4:
		print("Erase recent call lists")
	elif call_register == 5:
		print("Show call duration")
		print("1. Last call duration \n2. All calls' duration \n3. Recieved calls' duration \n4. Dialled calls' duration \n5. Clear timers")
		show_call = int(input("To select enter 1, 2 or 3 or 4 or 5: "))
		if show_call == 1:
			print("Last call duration")
		elif show_call == 2:
			print("All calls' duration")
		elif show_call == 3:
			print("Recieved calls' duration")
		elif show_call == 4:
			print("Dialled calls' duration")
		elif show_call == 5:
			print("Clear timers")
	elif call_register  == 6:
		print("Show call costs")
		print("1. Last call costs \n2. All calls' cost \n3. Clear counter")
		show_call_cost = int(input("To select enter 1, 2 or 3: "))
		if show_call_cost == 1:
			print("Last call costs")
		elif show_call_cost == 2:
			print("All calls' cost")
		elif show_call_cost == 3:
			print("Clear counter")
	elif call_register  == 7:
		print("Call cost settings")
		print("1. Call cost limit \n2. Show costd in")
		call_cost_setting = int(input("To select enter 1 or 2: "))
		if call_cost_setting == 1:
			print("Call cost limit")
		elif call_cost_setting == 2:
			print("Show costs in")
elif menu == 5:
	print("Tones")
	print("1. Ringing tone \n2.  Ringing volume \n3.  Incoming call alert \n4.  Composer \n5.  Message alert tone \n6.  Keypad tones  \n7.  Warning and game tone \n8. Vibrating alert \n9.  Screen saver")
	tones_settings = int(input("Enter a number from 1-10 to select: "))
	if tones_settings == 1:
		print("Ringing tone")
	elif tones_settings == 2: 
		print("Ringing volume")
	elif tones_settings == 3:
		print("Incoming call alert")
	elif tones_settings == 4:
		print("Composer")
	elif tones_settings == 5:
		print("Message alert tone")
	elif tones_settings == 6:
		print("Keypad tones")
	elif tones_settings == 7:
		print("Warning and game tone")
	elif tones_settings == 8:
		print("Vibrating alert")
	elif tones_settings == 9:
		print("Screen saver")

elif menu == 6:
	print("Settings")
	print("1. Call settings \n2. Phone settings \n3. Security settings \n4. Restore factory settings")
	settings = int(input("Enter a number to select (1-4): "))
	if settings == 1:
		print("Call settings")
		print("1. Automatic redial  \n2. Speed dialling \n3. Call waiting options \n4. Own number sending \n5. Phone line in use \n6. Automatic answer")
		call_settings = int(input("Enter a number to select (1-6) "))
		if tones_settings == 1:
			print("Automatic redial")
		elif call_settings == 2: 
			print("Speed dialling")
		elif call_settings == 3:
			print("Call waiting options")
		elif call_settings == 4:
			print("Own number sending")
		elif call_settings == 5:
			print("Phone line in use")
		elif call_settings == 6:
			print("Automatic answer")

	elif settings == 2: 
		print("Phone settings")
		print("1. Language \n2. Cell info display \n3. Welcome note \n4. Network selection \n5. Lights \n6. Confirm SIM service actions")
		phone_settings = int(input("Press a number to select (1-6): "))
		if phone_settings == 1:
			print("Language")
		elif phone_settings == 2: 
			print("Cell info display")
		elif phone_settings == 3:
			print("Welcome note")
		elif phone_settings == 4:
			print("Network selection")
		elif phone_settings == 5:
			print("Lights")
		elif phone_settings == 6:
			print("Confirm SIM service actions")

	elif settings == 3:
		print("Security settings")
		print("1. PIN code request \n2. Call barring service \n3. Fixed dialling \n4. Closed user group \n5. Phone security \n6. Change access codes")
		security_settings = int(input("Press a number to select (1-6): "))

		if security_settings == 1:
			print("PIN code request")
		elif security_settings == 2: 
			print("Call barring service")
		elif security_settings == 3:
			print("Fixed dialling")
		elif security_settings == 4:
			print("Closed user group")
		elif security_settings == 5:
			print("Phone security")
		elif security_settings == 6:
			print("Change access codes")
	
	elif settings == 4:
		print("Restore factory settings")
	elif settings == 5:
		print("Message alert tone")
	elif settings == 6:
		print("Keypad tones")
	elif settings == 7:
		print("Composer")
	elif settings == 8:
		print("Message alert tone")
	elif settings == 9:
		print("Keypad tones")



 
elif menu == 7:
	print("Call Divert")	

elif menu == 8:
	print("Games")

elif menu == 9:
	print("Calculator")

elif menu == 10:
	print("Reminders")

elif menu == 11:
	print("Clock")
	print("1. Alarm clock \n2. Clock settings \n3. Date settings \n4. Stopwatch \n5. Countdown timer \n6. Auto update of date and time")
	clock_setting = int(input("Press a number from 1-6 to select: "))
	if clock_settings == 1:
		print("Ringing tone")
	elif clock_settings == 2: 
		print("Ringing volume")
	elif clock_settings == 3:
		print("Date settings")
	elif clock_settings == 4:
		print("Stopwatch")
	elif clock_settings == 5:
		print("Countdown timer")
	elif clock_settings == 6:
		print("Auto update of date and time")

elif menu == 12:
	print("Profiles")

elif menu == 13:
	print("SIM services")


















