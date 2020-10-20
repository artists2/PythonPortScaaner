#-*-coding: utf-8-*-
import optparse
from socket import *
from threading import Thread
 
# Make a Connection
def ConnScan(Target_Host, Target_Port):
    try: 
        connskt = socket(AF_INET, SOCK_STREAM) 
        connskt.connect((Target_Host, Target_Port)) 
        connskt.send('Vionlent python\r\n')
        result = connskt.recv(1024) # 값 결과저장
        print "[+] %d / TCP OPEN" % Target_Port
        print "\n" + str(result) 
        connskt.close()
    except: # 예외처리 
        print "[-] %d TCP CLosed\n" % Target_Port
 

def PortScan(Target_Host, Target_Port):
    try: # 예외처리 
        Target_IP = gethostbyname(Target_Host) 
    except:
        print "[-] Cannot Resolve '%s' : Unknown Host\n" % Target_Host
        return
 
    try:
        Target_Name = gethostbyname(Target_IP) 
        print "\n[+] Scan Result For : " + Target_Name[0] # 출력 
    except:
        print "\n[+] Scan Result For : " + Target_IP
    setdefaulttimeout(1)
 
    for port in Target_Port: # 여러개의 포트를 입력받을수 있도록 함 
        print "Scanning Port \n" + port
        t = Thread (target=ConnScan, args=(Target_Host, int(port))) # t 메소드를 스레드로 정의한다 스레드의 내용물은 target=ConnScan, args=(Target_Host, int(port)?
        t.start() # start?
 
# Main Function Area
def main(): # Main함수 optparser를 통한 파싱작업을 하여 사용자에게 옵션을 제공함과 동시에 입력값에 대한 확장성을 보장한다. 
 
    parser = optparse.OptionParser(usage='Usage %Prog -H <Target Host> -p <Target Port>')
    parser.add_option('-H', dest = 'Target_Host', type ='string', help = 'Specify Target IP')
    parser.add_option('-p', dest = 'Target_Port', type ='string', help = 'Specify Target Port')
    (options, args) = parser.parse_args()
 
    Target_Host = options.Target_Host
    Target_Port = str(options.Target_Port).split(',')
 
    if (Target_Host == None) | (Target_Port == None):
        print parser.usage
        exit (0)
    PortScan(Target_Host, Target_Port)
 
if __name__ == '__main__':
    main()
