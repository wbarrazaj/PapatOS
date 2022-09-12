import os
import psutil
import platform
from modulos.funciones import print_ , bytes2human , printlog, get_size
class Procesos:
    pass

class Cpu:
    pass

class Memoria:
    pass

class Network:
    pass

class Disco:
    pass

class Employee:
    pass

class Server:
    """
    Server class Imprime infornacion de Servidor.
    print_Server    : Imprime informcion de Servidor.
        Systen      : Sistema Operativo.
        Node_Name   : 
        Release     : Release del Sistema Operativo.
        Version     : Version del Sistema Operativo.
        Machine     : Maquina.
        Processor   : Procesador.
    """

    def __init__(self):
        uname = platform.uname()
        Cpu_Freq = psutil.cpu_freq()
        ServerMem = psutil.virtual_memory()
        self.System=uname.system
        self.Node_Name=uname.node
        self.Release=uname.release
        self.Version=uname.version
        self.Machine=uname.machine
        self.Processor=uname.processor
        self.Physical_cores=psutil.cpu_count(logical=False)
        self.Total_cores=psutil.cpu_count(logical=True)
        self.Cpu_Max_Freq = Cpu_Freq.max
        self.Cpu_Min_Freq = Cpu_Freq.min
        self.Cpu_Current_Freq = Cpu_Freq.current
        self.Memory_Total = get_size(ServerMem.total)

    def print_Server(self):
        print(f"System              : {self.System}")
        print(f"Node Name           : {self.Node_Name}")
        print(f"Release             : {self.Release}")
        print(f"Version             : {self.Version}")
        print(f"Machine             : {self.Machine}")
        print(f"Processor           : {self.Processor}")
        print(f"Physical_cores      : {self.Physical_cores}")
        print(f"Totalcores          : {self.Total_cores}")
        print(f"Max Frequency       : {self.Cpu_Max_Freq:.2f}Mhz")
        print(f"Min Frequency       : {self.Cpu_Min_Freq:.2f}Mhz")
        print(f"Current Frequency   : {self.Cpu_Current_Freq:.2f}Mhz")
        print(f"Memoria Total       : {self.Memory_Total}")

    def uso_Cpu (self):
        pass

