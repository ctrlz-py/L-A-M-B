import socket
import datetime
import time
from rich import print as rprint


def rtcc(Host,Port):
    x = Host
    y = int(Port)
    
    def ping(Host = x,Port = y):
        try:
            socket.setdefaulttimeout(3)


            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            host = Host
            port = Port

            server_address = (host, port)
            s.connect(server_address)

        except OSError as error:
            return False

        else:
            s.close()
            return True

    def calculate_time(start, stop):

        difference = stop - start
        seconds = float(str(difference.total_seconds()))
        return str(datetime.timedelta(seconds=seconds)).split(".")[0]

    def first_check():

        if ping():
            rprint('[green]\nCONNECTION ACQUIRED\n[/green]')
            connection_acquired_time = datetime.datetime.now()

            rprint("[green][+][/green][red]connection acquired at:[/red] " +
                   str(connection_acquired_time).split(".")[0])

            return True

        else:

            rprint('[red]\nCONNECTION NOT ACQUIRED\n[/red]')

            return False

    def main():

        monitor_start_time = datetime.datetime.now()

        if first_check():
            rprint("[green][+][/green][red bold]monitoring started at:[/red bold]" +
                   str(monitor_start_time).split(".")[0])

        else:
            while True:

                if not ping():

                    time.sleep(1)
                else:

                    first_check()
                    rprint("[green][+][/green][red bold]monitoring started at:[/red bold]" +
                           str(monitor_start_time).split(".")[0])
                    break

        while True:

            if ping():

                time.sleep(1)

            else:
                down_time = datetime.datetime.now()
                rprint('[green][+][/green][red bold]disconnected at:[/red bold]' +
                       str(down_time).split(".")[0])

                while not ping():

                    time.sleep(1)

                up_time = datetime.datetime.now()


                down_time = calculate_time(down_time, up_time)

                rprint(
                    "[green][+][/green][red bold]connected again:[/red bold] "+str(up_time).split(".")[0])
                rprint(
                    "[green][+][/green][red bold]connection was unavailable for:[/red bold] " + down_time)

    main()
