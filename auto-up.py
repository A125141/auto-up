import pywhatkit
import time
from colorama import Fore, Style
import time
import colorama
from sys import stdout as terminal
from time import sleep
from itertools import cycle
from threading import Thread
done = False

def animate():
    for c in cycle([Fore.LIGHTYELLOW_EX +'|',Fore.LIGHTYELLOW_EX + '/',Fore.LIGHTYELLOW_EX + '-',Fore.LIGHTYELLOW_EX + '\\']):
        if done:
            break
        terminal.write(Fore.LIGHTGREEN_EX + '\rloading ' + c)
        terminal.flush()
        sleep(0.1)
    terminal.flush()

t = Thread(target=animate)
t.start()
sleep(3)
done = True

print(Fore.LIGHTGREEN_EX + '''
 ______     __  __     ______   ______           __  __     ______  
/\  __ \   /\ \/\ \   /\__  _\ /\  __ \   ____  /\ \/\ \   /\  == \ 
\ \  __ \  \ \ \_\ \  \/_/\ \/ \ \ \/\ \ |____| \ \ \_\ \  \ \  _-/ 
 \ \_\ \_\  \ \_____\    \ \_\  \ \_____\        \ \_____\  \ \_\   
  \/_/\/_/   \/_____/     \/_/   \/_____/         \/_____/   \/_/   
                                                              
''' , Fore.YELLOW + "                                               By ABDALRAHMAN125141")
print(Fore.LIGHTBLUE_EX + "Welcome to the HIDEFILE Tool!")
print("                                                                                                        ")

def send_whatsapp_message(number, messages, delay=0):
    time.sleep(delay)
    for message in messages:
        pywhatkit.sendwhatmsg_instantly(f"+{number}", message)

def send_to_single_number():
    number = input(Fore.GREEN + '''
Enter the phone number:''')
    message_count = int(input(Fore.LIGHTBLUE_EX +'''
Enter the number of messages you want to send: '''))

    messages = []
    for i in range(message_count):
        message = input(Fore.LIGHTYELLOW_EX +f'''
Message {i+1}:''')
        messages.append(message)

    choice = input(Fore.LIGHTGREEN_EX + '------------------------------------------------\n' + Fore.LIGHTCYAN_EX + 'Choose an option:\n\n ' + Fore.LIGHTRED_EX + '[ 1 ]' + Fore.LIGHTYELLOW_EX + ' Send messages after a specific delay\n\n ' + Fore.LIGHTRED_EX + '[ 2 ]' + Fore.LIGHTYELLOW_EX + ' Send instant messages\n\n' + Fore.LIGHTGREEN_EX + '------------------------------------------------\n' + Fore.LIGHTMAGENTA_EX + 'Enter your choice: ')

    if choice == '1':
        delay = int(input(Fore.GREEN + '''
Enter the delay in seconds: '''))
                          
        send_whatsapp_message(number, messages, delay)
    elif choice == '2':
        send_whatsapp_message(number, messages)
    else:
        print(Fore.RED + "Invalid choice!")

def send_to_multiple_numbers():
    numbers = input(Fore.GREEN + '''
Enter the phone numbers separated by commas:''')
    phone_numbers = [number.strip() for number in numbers.split(",")]
    message_count = int(input(Fore.LIGHTBLUE_EX +'''
Enter the number of messages you want to send: '''))

    messages = []
    for i in range(message_count):
        message = input(Fore.LIGHTYELLOW_EX +f'''
Message {i+1}:''')
        messages.append(message)

    choice = input(Fore.LIGHTGREEN_EX + '------------------------------------------------\n' + Fore.LIGHTCYAN_EX + 'Choose an option:\n\n ' + Fore.LIGHTRED_EX + '[ 1 ]' + Fore.LIGHTYELLOW_EX + ' Send messages after a specific delay\n\n ' + Fore.LIGHTRED_EX + '[ 2 ]' + Fore.LIGHTYELLOW_EX + ' Send instant messages\n\n' + Fore.LIGHTGREEN_EX + '------------------------------------------------\n' + Fore.LIGHTMAGENTA_EX + 'Enter your choice: ')




    if choice == '1':
        delay = int(input(Fore.GREEN + '''
Enter the delay in seconds: '''))
        for number in phone_numbers:
            send_whatsapp_message(number, messages, delay)
    elif choice == '2':
        for number in phone_numbers:
            send_whatsapp_message(number, messages)
    else:
        print(Fore.RED + "Invalid choice!")


# Main program loop
while True:
    print(Fore.RED + "[ 1 ]", Fore.LIGHTYELLOW_EX + "Send messages to a single number")
    print(Fore.RED + "[ 2 ]", Fore.LIGHTYELLOW_EX  + "Send messages to a multiple number")
    print(Fore.RED + "[ 3 ]", Fore.LIGHTYELLOW_EX  + "Contact US for a problem")
    print(Fore.RED + "[ 4 ]", Fore.LIGHTYELLOW_EX  + "HELP")
    print(Fore.RED + "[ 0 ]", Fore.LIGHTYELLOW_EX  + "EXIT")
    print(Fore.GREEN + "-----------------------------")
    print()
    
    choice = input(Fore.LIGHTMAGENTA_EX + "Enter your choice: ")

    if choice == '1':
        send_to_single_number()
    elif choice == '2':
        send_to_multiple_numbers()
    elif choice == '3':
        print(Fore.LIGHTBLUE_EX + '''
-------------------------------------------------''')
        print(Fore.YELLOW + "Contact US for a problem at [a6291088@gmail.com]")
        print(Fore.LIGHTBLUE_EX + '''-------------------------------------------------
        ''')
    elif choice == '0':
        print("Exiting the program...")
        break
    elif choice == '4':
        print('''

        ''')
        print(Fore.WHITE + "Hello, you are using the latest version of the" , Fore.YELLOW + "Auto-up tool")
        print(Fore.MAGENTA + "With this tool you can:")
        print(Fore.GREEN + "------------------------------------------------------------------------------------")
        print(Fore.YELLOW + "Sending WhatsApp messages at a specific time that you specify - or immediately - to a person or to several people")
        print(Fore.GREEN + "------------------------------------------------------------------------------------")
        print(Fore.LIGHTRED_EX + "You just have to choose what suits you from the options and enjoy")
        print(Fore.LIGHTYELLOW_EX+ "It's free and always under development")
        print(Fore.GREEN + "------------------------------------------------------------------------------------")
        print(Fore.YELLOW + "Tool usage notes:")
        print(Fore.LIGHTBLUE_EX+ "When you put more than one number, you should put it like this:")
        print(Fore.MAGENTA + "+12345678910 , +98765432101 , ......")
        print(Fore.MAGENTA + "The number must be entered with the introduction of the country.")
        print(Fore.LIGHTCYAN_EX + "Enter the number of messages you want to send:")
        print(Fore.LIGHTGREEN_EX+ '''It means the number of messages - different - that you want to send, 
not how many times you repeat the same message.''')
        print(Fore.LIGHTGREEN_EX+ "You must enter the time in seconds, that is, you must convert the minutes or hours according to your desire to seconds")
        print(Fore.CYAN + '''for example, one hour = 3600 seconds and 1 minute = 60 seconds, meaning that if you want to send the message after an hour and a half, 
you must enter: 5400 seconds.''')
        print(Fore.GREEN + "------------------------------------------------------------------------------------")
        print(Fore.YELLOW + "--Note:" ,Fore.CYAN + "We are not responsible for any wrong or illegal use of the tool.")
        print(Fore.CYAN + "Tool developer and programmer :")
        print(Fore.LIGHTRED_EX + "Abdalrahman125141")
        print("                                                                                                                       ")
    else:
        print(Fore.RED + "Invalid choice!")


pywhatkit
colorama
