import random, string,os
from colorama import Fore, init
init(convert=True)

def main():
    os.system('cls&title [Discord Nitro Generator] By The_G ^| Welcome :)')
    print("Welcome to the Discord Nitro Generator / Creator \n\n")
    print(Fore.BLUE + """\
    ▓█████▄  ██▓  ██████  ▄████▄   ▒█████   ██▀███  ▓█████▄     ███▄    █  ██▓▄▄▄█████▓ ██▀███   ▒█████  
    ▒██▀ ██▌▓██▒▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██ ▒ ██▒▒██▀ ██▌    ██ ▀█   █ ▓██▒▓  ██▒ ▓▒▓██ ▒ ██▒▒██▒  ██▒
    ░██   █▌▒██▒░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▓██ ░▄█ ▒░██   █▌   ▓██  ▀█ ██▒▒██▒▒ ▓██░ ▒░▓██ ░▄█ ▒▒██░  ██▒
    ░▓█▄   ▌░██░  ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░▒██▀▀█▄  ░▓█▄   ▌   ▓██▒  ▐▌██▒░██░░ ▓██▓ ░ ▒██▀▀█▄  ▒██   ██░
    ░▒████▓ ░██░▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██▓ ▒██▒░▒████▓    ▒██░   ▓██░░██░  ▒██▒ ░ ░██▓ ▒██▒░ ████▓▒░
    ▒▒▓  ▒ ░▓  ▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░ ▒▓ ░▒▓░ ▒▒▓  ▒    ░ ▒░   ▒ ▒ ░▓    ▒ ░░   ░ ▒▓ ░▒▓░░ ▒░▒░▒░
    ░ ▒  ▒  ▒ ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░   ░▒ ░ ▒░ ░ ▒  ▒    ░ ░░   ░ ▒░ ▒ ░    ░      ░▒ ░ ▒░  ░ ▒ ▒░ 
    ░ ░  ░  ▒ ░░  ░  ░  ░        ░ ░ ░ ▒    ░░   ░  ░ ░  ░       ░   ░ ░  ▒ ░  ░        ░░   ░ ░ ░ ░ ▒  
    ░     ░        ░  ░ ░          ░ ░     ░        ░                ░  ░              ░         ░ ░     
    ░                   ░                           ░                                                                                
    
    
    """ + Fore.RESET)
    print(Fore.GREEN + "Finished Loading !" + Fore.RESET)
    
    amount = int(input('Amount of nitro codes to generate: )
    value = 1
    while value <= amount:
        code = "https://discord.gift/" + (').join(random.choices(string.ascii_letters + string.digits, k=16))
        f = open('Codes.txt', "a+")
        f.write(f'{code}\n')
        f.close()
        print(Fore.GREEN + "[GENERATED] " + Fore.RESET , code)
        value += 1
    print("Done Generating " + str(value-1) + " Codes !\nPlease Check the " + Fore.RED + "Codes.txt " + Fore.RESET + "file in the Directory!")
    input('Press Enter key to Exit')
    
try:
    main()
except Exception as e:
    print("If you're facing any issue with .py file, try the .exe file !")
    print(e)
    pass    
