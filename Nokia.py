def main_menu():
	print("1.  Phone book \n2.  Messages \n3.  Chat \n4.  Call Register \n5.  Tones \n6.  Settings \n7.  Call Divert \n8.  Games \n9.  Calculator \n10. Remainders \n11. Clock \n12. Profiles \n13. SIM services")
	menu = input("Select options: ")
	match menu :
		case "1":
			return phone_book()
		case "2":
			return messages()
		case "3":
			return chat()
		case "4": 
			return call_register() 
		case "5":
			return  tones()
		case "6": 
			return settings()
		case "7":
			return call_divert()
		case "8":
			return games()
		case "9":
			return calculator()
		case "10":
			return reminders()
		case "11": 
			return clock()
		case "12":
			return profiles()
		case "13":
			return sim_services()
		case _: 
			return main_menu()





def phone_book():
	print("1.  Search \n2.  Service Nos \n3.  Add Name \n4.  Erase \n5.   Edit \n6.  Assign Tone \n7.  Send B'Card \n8.  Options \n9.  Speed Dials \n10. Voice Tags")
	phone_book = input("press a number from 1-10 to select: ")
	if phone_book == "0": 
		return main_menu() 
	match phone_book:
		case "1":
			return search()
		case "2":
			return service_nos()
		case "3":
			return add_name()
		case "4":
			return erase()
		case "5":
			return edit()
		case "6":
			return assign_tone()
		case "7":
			return send_b_card()
		case "8":
			return options()
		case "9":
			return speed_dials()
		case "10":
			return voice_tags()
		case _:
			return main_menu()


def search():
	print("Search")
	search = input("Enter 0 to go back to the main menu: ")
	if search == "0":
		return main_menu()

def service_nos():
	print("Service Nos")
	service_nos = input("Enter 0 to go back to the main menu: ")
	if service_nos == "0":
		return main_menu()

def add_name():
	print("Add name")
	add_name = input("Enter 0 to go back to the main menu: ")
	if add_name == "0":
		return main_menu()

def erase():
	print("Erase")
	erase = input("Enter 0 to go back to the main menu: ")
	if erase == "0":
		return main_menu()

def edit():
	print("Edit")
	edit = input("Enter 0 to go back to the main menu: ")
	if edit == "0":
		return main_menu()



def assign_tone():
	print("Assign tone")
	services_nos = input("Enter 0 to go back to the main menu: ")
	if assign_tone == "0":
		return main_menu()

def send_b_card():
	print("Send b'card")
	send_b_card = input("Enter 0 to go back to the main menu: ")
	if send_b_card == "0":
		return main_menu()

def options():
	print("1. Types of view \n2. Memory status")
	options = input("Select an option: ")
	match options:
		case "1":
			return type_of_view()
		case "2":
			return memory_status()
		case _:
			return options()
	if options == "0":
		return main_menu()

def type_of_view():
	print("Type of view")
	type_of_view = input("Enter 0 to go back")
	if type_of_view == "0":
		return main_menu()

def memory_status():
	print("Memory status")
	memory_status = input("Enter 0 to go back")
	if memory_status == "0":
		return main_menu()

	
def speed_dials():
	print("Speed dials")
	speed_dials = input("Enter 0 to go back to the main menu: ")
	if speed_dials == "0":
		return main_menu()

def voice_tags():
	print("Voice tags")
	voice_tags = input("Enter 0 to go back to the main menu: ")
	if voice_tags == "0":
		return main_menu()






def messages():
	print("1.Write messages \n2.  Inbox \n3.  Outbox \n4.  Picture messages \n5.  Templates \n6.  Smileys \n7.  Message settings \n8.  Info service \n9.  Voice mailbox number \n10. Service command editor")
	messages = input("Select an option")
	if messages == "0":
		return main_menu()
	match messages:
		case "1":
			return write_messages()
		case "2":
			return inbox()
		case "3":
			return outbox()
		case "4":
			return picture_messages()
		case "5":
			return templates()
		case "6":
			return smileys()
		case "7":
			return message_settings()
		case "8":
			return info_service()
		case "9":
			return voice_malbox_number()
		case "10":
			return service_command_editor()
		case _: 
			return main_menu()

def write_messages():
	print("Write messages")
	write_messages = input("Enter 0 to go back to the main menu: ")
	if write_messages == "0":
		return main_menu()

def inbox():
	print("Inbox")
	inbox = input("Enter 0 to go back to the main menu: ")
	if inbox == "0":
		return main_menu()

def outbox():
	print("Outbox")
	outbox = input("Enter 0 to go back to the main menu: ")
	if outbox == "0":
		return main_menu()

def picture_messages():
	print("Picture messages")
	picture_messages = input("Enter 0 to go back to the main menu: ")
	if picture_messages == "0":
		return main_menu()

def templates():
	print("Templates")
	templates = input("Enter 0 to go back to the main menu: ")
	if templates == "0":
		return main_menu()

def smileys():
	print("Smileys")
	smileys = input("Enter 0 to go back to the main menu: ")
	if smileys == "0":
		return main_menu()


def message_settings():
	print("1. Set \n2. Common")
	message_settings = input("Select an option: ")
	if message_settings == "0":
		return phone_book()
	match message_settings:
		case "1":
			return set()
		case "2":
			return common()
		case _:
			return messages()

def set():
	print("1.Message centre number \n2. Messages sent as \n3. Message validity")
	set = input("Select an option: ")
	if set == "0":
		return main_menu()
	match set:
		case "1":
			return message_centre_number()
		case "2":
			return messages_sent_as()
		case "3":
			return message_validity()
		case _:
			return messages()

def message_centre_number():
	print("Message centre number")
	message_centre_number = input("Enter 0 to go back to the main menu: ")
	if message_centre_number == "0":
		return main_menu()


def messages_sent_as():
	print("Message sent as")
	messages_sent_as = input("Enter 0 to go back to the main menu: ")
	if messages_sent_as == "0":
		return main_menu()


def message_validity():
	print("Message validity")
	message_validity = input("Enter 0 to go back to the main menu: ")
	if message_validity == "0":
		return main_menu()


def common():
	print("1. Delivery reports \n2. Reply via same center \n3. Character support")
	common = input("Select an option: ")
	if common == "0":
		return main_menu()
	match common:
		case "1":
			return delivery_report()
		case "2":
			return reply_via_same_center()
		case "3":
			return character_support()
		case _:
			return messages()

def delivery_report():
	print("Delivery report")
	delivery_report = input("Enter 0 to go back to the main menu: ")
	if delivery_report == "0":
		return main_menu()


def reply_via_same_center():
	print("Reply vis same center")
	reply_via_same_center = input("Enter 0 to go back to the main menu: ")
	if reply_via_same_center == "0":
		return main_menu()


def character_support():
	print("Character support")
	character_support = input("Enter 0 to go back to the main menu: ")
	if character_support == "0":
		return main_menu()

def info_service():
	print("Info service")
	info_service = input("Enter 0 to go back to the main menu: ")
	if info_service == "0":
		return main_menu()

def voice_mailbox_number():
	print("Voice mailbox number")
	voice_mailbox_number = input("Enter 0 to go back to the main menu: ")
	if voice_mailbox_number == "0":
		return main_menu()

def service_command_editor():
	print("Service command editor")
	service_command_editor = input("Enter 0 to go back to the main menu: ")
	if service_command_editor == "0":
		return main_menu()


def chat():
	print("Chat")
	chat = input("Enter 0 to go back to the main menu: ")
	if chat == "0":
		return main_menu()



def call_register():
	print("1. Missed calls \n2. Received calls \n3. Dialled numbers \n4. Erase recent call lists \n5. Show call duration \n6. Show call costs \n7. Call cost settings \n8. Prepaid credit")
	call_register = input("Select an option: ")
	if call_register == "0":
		return main_menu()
	match call_register:
		case "1": 
			return missed_calls()
		case "2":
			return received_calls()
		case "3":
			return dialled_numbers()
		case "4": 
			return erase_recent_call_lists()
		case "5":
			return show_call_duration()
		case "6":
			return show_call_costs()
		case "7":
			return call_cost_settings()
		case "8":
			return prepaid_credit()
		case _:
			return call_register()

def missed_calls():
	print("Missed calls")
	missed_calls = input("Enter 0 to go back: ")
	if missed_calls == "0":
		return main_menu()

def received_calls():
	print("Received calls")
	received_calls = input("Enter 0 to go back: ")
	if received_calls == "0":
		return main_menu()

def dialled_numbers():
	print("Dialled calls")
	dialled_numbers = input("Enter 0 to go back: ")
	if dialled_numbers == "0":
		return main_menu()

def erase_recent_call_lists():
	print("Erase recent call lists")
	erase_recent_call_lists = input("Enter 0 to go back: ")
	if erase_recent_call_lists == "0":
		return main_menu()


def show_call_duration():
	print("1. Last call duration \n2. All calls' duration \n3. Received calls' duration \n4. Dialled calls' duration \n5. Clear timers")
	show_call_duration = input("Enter 0 to go back: ")
	if show_call_duration == "0":
		return main_menu()
	match show_call_duration:
		case "1":
			return last_call_duration()
		case "2": 
			return all_calls_duration()
		case "3":
			return received_calls_duration()
		case "4":
			return dialled_calls_duration()
		case "5":
			return clear_timers()
		case _: 
			return show_call_duration()


def last_call_duration():
	print("Last call duration")
	last_call_duration = input("Enter 0 to go back: ")
	if last_call_duration == "0":
		return show_call_duration()


def all_calls_duration():
	print("All calls' duration")
	all_calls_duration = input("Enter 0 to go back: ")
	if all_calls_duration == "0":
		return show_call_duration()


def received_calls_duration():
	print("Received calls' duration")
	received_calls_duration = input("Enter 0 to go back: ")
	if received_calls_duration == "0":
		return show_call_duration()



def dialled_calls_duration():
	print("Dialled calls' duration")
	dialled_calls_duration = input("Enter 0 to go back: ")
	if dialled_calls_duration == "0":
		return show_call_duration()


def clear_timers():
	print("Clear timers")
	clear_timers = input("Enter 0 to go back: ")
	if clear_timers == "0":
		return show_call_duration()



def show_call_costs():
	print("1. Last call cost \n2. All calls' cost \n3. Clear counters")
	show_call_costs = input("Enter 0 to go back: ")
	if show_call_costs == "0":
		return main_menu()
	match show_call_costs:
		case "1":
			return last_call_cost()
		case "2": 
			return all_calls_cost()
		case "3":
			return clear_counters()
		case _:
			return show_call_duration()

def last_call_cost():
	print("Last call duration")
	last_call_cost = input("Enter 0 to go back: ")
	if last_call_cost == "0":
		return show_call_costs()

def all_calls_cost():
	print("All calls' cost")
	all_calls_cost = input("Enter 0 to go back: ")
	if all_calls_cost == "0":
		return show_call_costs()

def clear_counters():
	print("Clear counters")
	clear_counters = input("Enter 0 to go back: ")
	if clear_counters == "0":
		return show_call_costs()


def call_cost_settings():
	print("1. Call cost limit \n2. Show costs in")
	call_cost_settings = input("Enter 0 to go back: ")
	if call_cost_settings == "0":
		return main_menu()
	match call_cost_settings:
		case "1":
			return call_cost_limit()
		case "2": 
			return show_costs_in()


def call_cost_limit():
	print("Call cost limit")
	call_cost_limit = input("Enter 0 to go back: ")
	if call_cost_limit == "0":
		return call_cost_settings()


def show_costs_in():
	print("Show costs in")
	show_costs_in = input("Enter 0 to go back: ")
	if show_costs_in == "0":
		return call_cost_settings()


def prepaid_credit():
	print("Prepaid credit")
	prepaid_credit = input("Enter 0 to go back: ")
	if prepaid_credit == "0":
		return main_menu()



def tones():
	print("1. Ringing tone \n2. Ringing volume \n3. Incoming call alert \n4. Composer \n5. Message alert tone \n6. Keypad tones \n7. Warning and game tone \n8. Vibrating alert \n9. Screen saver")
	tones = input("Select an option: ")
	if tones == 0:
		return main_menu()
	match tones:
		case "1":
			return ringing_tone()
		case "2":
			return ringing_volume()
		case "3":
			return incoming_call_alert()
		case "4":
			return composer()
		case "5":
			return message_alert_tone()
		case "6":
			return keypad_tones()
		case "7":
			return warning_and_game_tone()
		case "8":
			return vibrating_alert()
		case "9":
			return screen_saver()
		case _: 
			return tones()

def ringing_tone():
	print("Ringing tone")
	ringing_tone = input("Enter 0 to go back")
	if ringing_tone == "0":
		return tones()

def ringing_volume():
	print("Ringing volume")
	ringing_volume = input("Enter 0 to go back")
	if ringing_volume == "0":
		return tones()

def incoming_call_alert():
	print("Incoming call alert")
	incoming_call_alert = input("Enter 0 to go back")
	if incoming_call_alert == "0":
		return tones()

def composer():
	print("Composer")
	composer = input("Enter 0 to go back")
	if composer == "0":
		return tones()

def meassge_alert_tone():
	print("Message alert tone")
	meassge_alert_tone = input("Enter 0 to go back")
	if meassge_alert_tone == "0":
		return tones()

def keypad_tones():
	print("Keypad tones")
	keypad_tones = input("Enter 0 to go back")
	if keypad_tones == "0":
		return tones()

def warning_and_game_tones():
	print("Warning and game tones")
	warning_and_game_tones = input("Enter 0 to go back")
	if warning_and_game_tones == "0":
		return tones()


def vibrating_alert():
	print("Vibrating alert")
	vibrating_alert = input("Enter 0 to go back")
	if vibrating_alert == "0":
		return tones()

def screen_saver():
	print("Ringing tone")
	screen_saver = input("Enter 0 to go back")
	if screen_saver == "0":
		return tones()


def settings():
	print("1. Call settings \n2. Phone settings \n3. Security settings \n4. Restore factory settings")
	settings = input("Select an option: ")
	if settings == "0":
		return main_menu()
	match settings:
		case "1":
			return call_settings()
		case "2":
			return phone_settings()
		case "3":
			return security_settings()
		case "4":
			return restore_factory_settings()
		case _:
			return settings()

def call_settings():
	print("1. Automatic redial \n2. Speed dialling \n3. Call waiting options \n4. Own number sending \n5. Phone line in use \n6. Automatic answer")
	call_settings = input("Select an option: ")
	if call_settings == "0":
		return settings()
	match call_settings:
		case "1":
			return automatic_redial()
		case "2":
			return speed_dialling()
		case "3":
			return call_waiting_options()
		case "4":
			return own_number_sending()
		case "5":
			return phone_line_in_use()
		case "6":
			return automatic_answer()
		case _:
			return call_settings()

def automatic_redial():
	print("Automatic redial")
	automatic_redial = input("Enter 0 to go back to the main menu: ")
	if automatic_redial == "0":
		return call_settings()

def speed_dialling():
	print("Speed dialling")
	speed_dialling = input("Enter 0 to go back: ")
	if speed_dialling == "0":
		return call_settings()

def call_waiting_options():
	print("Call waiting options")
	call_waiting_options = input("Enter 0 to go back: ")
	if call_waiting_options == "0":
		return call_settings()

def own_number_sending():
	print("Own number sending")
	own_number_sending = input("Enter 0 to go back: ")
	if own_number_sending == "0":
		return call_settings()


def phone_line_in_use():
	print("Phone line in use")
	phone_line_in_use = input("Enter 0 to go back: ")
	if phone_line_in_use == "0":
		return call_settings()

def automatic_answer():
	print("Automatic answer")
	automatic_answer = input("Enter 0 to go back: ")
	if automatic_answer == "0":
		return call_settings()




def phone_settings():
	print("1. Language \n2. Cell info display \n3. Welcome note \n4. Network selection \n5. Lights \n6. Confirm SIM service actions")
	phone_settings = input("Select an option: ")
	if phone_settings == "0":
		return settings()
	match phone_settings:
		case "1":
			return language()
		case "2":
			return cell_info_display()
		case "3":
			return welcome_note()
		case "4":
			return network_selection()
		case "5":
			return lights()
		case "6":
			return confirm_sim_service_actions()
		case _:
			return main_menu()

def language():
	print("Language")
	language = input("Enter 0 to go back to the main menu: ")
	if language == "0":
		return phone_settings()

def cell_info_display():
	print("Cell info display")
	cell_info_display = input("Enter 0 to go back: ")
	if cell_info_display == "0":
		return phone_settings()

def welcome_note():
	print("Welcome note")
	welcome_note = input("Enter 0 to go back: ")
	if welcome_note == "0":
		return phone_settings()

def network_selection():
	print("Network selection")
	network_selection = input("Enter 0 to go back: ")
	if network_selection == "0":
		return phone_settings()


def lights():
	print("Lights")
	lights = input("Enter 0 to go back: ")
	if lights == "0":
		return phone_settings()

def confirm_sim_service_actions():
	print("Confirm SIM service actions")
	confirm_sim_service_actions = input("Enter 0 to go back: ")
	if confirm_sim_service_actions == "0":
		return phone_settings()


def security_settings():
	print("1. PIN code request \n2. Call barring service \n3. Fixed dialling \n4. Closed user group \n5. Phone security \n6. Change access codes")
	security_settings = input("Select an option: ")
	if security_settings == "0":
		return settings()
	match security_settings:
		case "1":
			return pin_code_request()
		case "2":
			return call_barring_service()
		case "3":
			return fixed_dialling()
		case "4":
			return closed_user_group()
		case "5":
			return phone_security()
		case "6":
			return change_access_code()
		case _:
			return main_menu()

def pin_code_request():
	print("PIN code request")
	restore_factory_settings = input("Enter 0 to go back to the main menu: ")
	if restore_factory_settings == "0":
		return security_settings()

def call_barring_service():
	print("Call barring service")
	call_barring_service = input("Enter 0 to go back to the main menu: ")
	if call_barring_service == "0":
		return security_settings()

def fixed_dialling():
	print("Fixed dialling")
	fixed_dialling = input("Enter 0 to go back to the main menu: ")
	if fixed_dialling == "0":
		return security_settings()

def closed_user_group():
	print("Closed user group")
	closed_user_group = input("Enter 0 to go back to the main menu: ")
	if closed_user_group == "0":
		return security_settings()


def phone_security():
	print("Phone security")
	phone_security = input("Enter 0 to go back to the main menu: ")
	if phone_security == "0":
		return security_settings()

def change_access_code():
	print("Change access code")
	change_access_code = input("Enter 0 to go back to the main menu: ")
	if change_access_code == "0":
		return security_settings()


def restore_factory_settings():
	print("Restore factory settings")
	restore_factory_settings = input("Enter 0 to go back to the main menu: ")
	if restore_factory_settings == "0":
		return call_settings()







def call_divert():
	print("Call divert")
	call_divert = input("Enter 0 to go back to the main menu: ")
	if call_divert == "0":
		return main_menu()
	

def games():
	print("Games")
	games = input("Enter 0 to go back to the main menu: ")
	if games == "0":
		return main_menu()


def calculator():
	print("Calculator")
	calculator = input("Enter 0 to go back to the main menu: ")
	if calculator == "0":
		return main_menu()



def reminders():
	print("Reminders")
	reminders = input("Enter 0 to go back to the main menu: ")
	if reminders == "0":
		return main_menu()


def clock():
	print("1. Alarm clock \n2. Clock settings \n3. Date settings \n4. Stopwatch \n5. Countdown timer \n6. Auto update of date and time"); 
	clock = input("Select an option: ")
	if clock == "0":
		return main_menu()
	match clock:
		case "1":
			return alarm_clock()
		case "2":
			return clock_settings()
		case "3":
			return date_settings()
		case "4":
			return stopwatch()
		case "5":
			return countdown_timer()
		case "6":
			return auto_update_date_and_time()
		case _:
			return main_menu()

def alarm_clock():
	print("Alarm clock")
	alarm_clock = input("Enter 0 to go back: ")
	if alarm_clock == "0":
		return clock()

def clock_settings():
	print("Clock settings")
	clock_settings = input("Enter 0 to go back: ")
	if clock_settings == "0":
		return clock()

def date_setting():
	print("Date setting")
	date_setting = input("Enter 0 to go back: ")
	if date_setting == "0":
		return clock()

def stopwatch():
	print("Stopwatch")
	stopwatch = input("Enter 0 to go back: ")
	if stopwatch == "0":
		return clock()

def countdown_timer():
	print("Countdown timer")
	countdown_timer = input("Enter 0 to go back: ")
	if countdown_timer == "0":
		return clock()

def auto_update_date_and_time():
	print("Auto update date and time")
	auto_update_date_and_time = input("Enter 0 to go back: ")
	if auto_update_date_and_time == "0":
		return clock()


def profiles():
	print("Profiles")
	profiles = input("Enter 0 to go back to the main menu: ")
	if profiles == "0":
		return main_menu()


def sim_services():
	print("SIM services")
	sim_services = input("Enter 0 to go back to the main menu: ")
	if sim_services == "0":
		return main_menu()




	

main_menu()
phone_book()
		
