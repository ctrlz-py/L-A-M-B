from socket import *
import struct
import sys
import re
import time
import datetime
from rich import print as rprint


def ls(check_time,protocol_file,is_capcure):
    
    x = "[green bold][[red]+[/red]][/green bold]"

    while True :

        def receiveData(s):
            data = ''
            try:
                data = s.recvfrom(65565)
            except timeout:
                data = ''
            except:
                print("An error happened: ")
                sys.exc_info()
            return data[0]



        def getTOS(data):
            precedence = {0: "Routine", 1: "Priority", 2: "Immediate", 3: "Flash", 4: "Flash override", 5: "CRITIC/ECP",
                        6: "Internetwork control", 7: "Network control"}
            delay = {0: "Normal delay", 1: "Low delay"}
            throughput = {0: "Normal throughput", 1: "High throughput"}
            reliability = {0: "Normal reliability", 1: "High reliability"}
            cost = {0: "Normal monetary cost", 1: "Minimize monetary cost"}

            D = data & 0x10
            D >>= 4
            T = data & 0x8
            T >>= 3
            R = data & 0x4
            R >>= 2
            M = data & 0x2
            M >>= 1

            tabs = '\n\t\t\t'
            TOS = precedence[data >> 5] + tabs + delay[D] + tabs + throughput[T] + tabs + \
                reliability[R] + tabs + cost[M]
            return TOS



        def getFlags(data):
            flagR = {0: "0 - Reserved bit"}
            flagDF = {0: "0 - Fragment if necessary", 1: "1 - Do not fragment"}
            flagMF = {0: "0 - Last fragment", 1: "1 - More fragments"}

            R = data & 0x8000
            R >>= 15
            DF = data & 0x4000
            DF >>= 14
            MF = data & 0x2000
            MF >>= 13

            tabs = '\n\t\t\t'
            flags = flagR[R] + tabs + flagDF[DF] + tabs + flagMF[MF]
            return flags


        
        def getProtocol(protocolNr):
            x = open(f'{protocol_file}.txt', 'a')
            x.write("")
            x.close()
            protocolFile = open(f'{protocol_file}.txt', 'r')
            protocolData = protocolFile.read()
            protocol = re.findall(r'\n' + str(protocolNr) + ' (?:.)+\n', protocolData)
            if protocol:
                protocol = protocol[0]
                protocol = protocol.replace("\n", "")
                protocol = protocol.replace(str(protocolNr), "")
                protocol = protocol.lstrip()
                return protocol

            else:
                return 'No such protocol.'


        HOST = gethostbyname(gethostname())

        s = socket(AF_INET, SOCK_RAW, IPPROTO_IP)
        s.bind((HOST, 0))

        s.setsockopt(IPPROTO_IP, IP_HDRINCL, 1)
        s.ioctl(SIO_RCVALL, RCVALL_ON)
        data = receiveData(s)

        unpackedData = struct.unpack('!BBHHHBBH4s4s', data[:20])

        version_IHL = unpackedData[0]
        version = version_IHL >> 4                  
        IHL = version_IHL & 0xF                     
        TOS = unpackedData[1]                       
        totalLength = unpackedData[2]
        ID = unpackedData[3]                        
        flags = unpackedData[4]
        fragmentOffset = unpackedData[4] & 0x1FFF
        TTL = unpackedData[5]                      
        protocolNr = unpackedData[6]
        checksum = unpackedData[7]
        sourceAddress = inet_ntoa(unpackedData[8])
        destinationAddress = inet_ntoa(unpackedData[9])

        
        print("\n\nAn IP packet with the size %i was captured." % (unpackedData[2]))
        rprint("\n"+x+"[magenta1]Raw data: [/magenta1]"+str(data))
        rprint("\n"+x+"[magenta1]\nParsed data[/magenta1]"+str(data))
        rprint("\n"+x+"[magenta1]Version:\t\t[/magenta1]"+str(version))
        rprint("\n"+x+"[magenta1]Header Length:\t\t[/magenta1]"+ str(IHL*4) + " bytes")
        rprint("\n"+x+"[magenta1]Type of Service:\t[/magenta1]"+getTOS(TOS))
        rprint("\n"+x+"[magenta1]Length:\t\t\t[/magenta1]"+str(totalLength))
        rprint("\n"+x+"[magenta1]ID:\t\t\t[/magenta1]"+ str(hex(ID)) + " (" + str(ID) + ")")
        rprint("\n"+x+"[magenta1]Flags:\t\t\t[/magenta1]"+getFlags(flags))
        rprint("\n"+x+"[magenta1]Fragment offset:\t[/magenta1]"+str(fragmentOffset))
        rprint("\n"+x+"[magenta1]TTL:\t\t\t[/magenta1]"+str(TTL))
        rprint("\n"+x+"[magenta1]Protocol:\t\t[/magenta1]"+getProtocol(protocolNr))
        rprint("\n"+x+"[magenta1]Checksum:\t\t[/magenta1]"+str(checksum))
        rprint("\n"+x+"[magenta1]Source:\t\t\t[/magenta1]"+sourceAddress)
        rprint("\n"+x+"[magenta1]Destination:\t\t[/magenta1]"+destinationAddress)
        rprint("\n"+x+"[magenta1]Payload:\n[/magenta1]"+str(data[20:]))



        s.ioctl(SIO_RCVALL, RCVALL_OFF)

        


        e = datetime.datetime.now()

        if is_capcure == "1":
            f = open("sniff_log.txt", "a")
            f.write("\n\n---------------------- %s:%s:%s "%(e.hour, e.minute, e.second)+"----------------------")
            f.write("\nAn IP packet with the size %i was captured." % (unpackedData[2]))
            f.write("\nRaw data: " + str(data))
            f.write("\nParsed data")
            f.write("\nVersion:\t\t" + str(version))
            f.write("\nHeader Length:\t\t" + str(IHL*4) + " bytes")
            f.write("\nType of Service:\t" + getTOS(TOS))
            f.write("\nLength:\t\t\t" + str(totalLength))
            f.write("\nID:\t\t\t" + str(hex(ID)) + " (" + str(ID) + ")")
            f.write("\nFlags:\t\t\t" + getFlags(flags))
            f.write("\nFragment offset:\t" + str(fragmentOffset))
            f.write("\nTTL:\t\t\t" + str(TTL))
            f.write("\nProtocol:\t\t" + getProtocol(protocolNr))
            f.write("\nChecksum:\t\t" + str(checksum))
            f.write("\nSource:\t\t\t" + sourceAddress)
            f.write("\nDestination:\t\t" + destinationAddress)
            f.write("\nPayload:\n" + str(data[20:]))
            f.write("\n\n-----------------------------------------------------")
            f.close()
        else :
            pass
        time.sleep(check_time)