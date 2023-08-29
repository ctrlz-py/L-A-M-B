from rich import print as rprint
import pyfiglet

import conection_checker
import ipTracker
import localSniffer

while True :
    result = pyfiglet.figlet_format("L A M B")
    rprint('\n\n[red]Powered by[/red][green bold] CTRL + Z[/green bold]')
    print(f"\n{result}")
    rprint("[cyan1 bold]it doesn't matter where you are ! . all connected...[/cyan1 bold]")
    rprint("\n[magenta2 bold]------------------------------------------[/magenta2 bold]")
    


    rprint("\n[green bold][[red]1[/red]][/green bold]-[magenta3]Local Sniff[/magenta3]\n[green bold][[red]2[/red]][/green bold]-[magenta3]Real-Time Connection Check[/magenta3]\n[green bold][[red]3[/red]][/green bold]-[magenta3]IP Tracker[/magenta3]\n[]-Abouut CTRL + Z")
    rprint("\n[green bold][[red]5[/red]][/green bold]-[red bold]Exit[/red bold]")
    x = input("\ntype : ")
    

    if x =="1":
        try:
            t = input("Enter Check time (second) : ")
            pn = input("Enter protocol file name or Skip : ")
            if pn == "" or pn == " ":
                pn = "default"
            x = input("You Wanna save data as .txt file (Y,N)?! : ")
            if x == "Y" or x == "y" or x == "yes" or x == "YES"or x == "Yes":
                ic = "1"
            else :
                ic = "0"
            localSniffer.ls(int(t),pn,ic)
        except :
           pass 


    elif x == "2":
        try :
            host = input("\nhost exp(8.8.8.8): ")
            port = input("port exp(53): ")
            print("\nclick Ctrl+c to return")
            conection_checker.rtcc(Host =host ,Port =port )
        except:
            pass
    elif x == "3":
        try:
            ipTracker.it()
        except:
            pass
    if x == "5":
            break


print("\nhave a nice day <3 ....")