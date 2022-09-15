import os
import psutil
import platform
from modulos.funciones import print_ , bytes2human , printlog, get_size
from datetime import datetime
import unittest
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
        uname                   = platform.uname()
        Cpu_Freq                = psutil.cpu_freq()
        ServerMem               = psutil.virtual_memory()
        SwapMem                 = psutil.swap_memory()
        self.System             = uname.system
        self.Node_Name          = uname.node
        self.Release            = uname.release
        self.Version            = uname.version
        self.Machine            = uname.machine
        self.Processor          = uname.processor
        self.Physical_cores     = psutil.cpu_count(logical=False)
        self.Total_cores        = psutil.cpu_count(logical=True)
        self.Cpu_Max_Freq       = Cpu_Freq.max
        self.Cpu_Min_Freq       = Cpu_Freq.min
        self.Cpu_Current_Freq   = Cpu_Freq.current
        self.Memory_Total       = bytes2human(ServerMem.total)
        self.Swap_Total         = bytes2human(SwapMem.total)

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
        print(f"Memoria Swap Total  : {self.Swap_Total}")

    def uso_Cpu (self):
        pass
    
    def uso_Memoria (self):
        print("="*10, "Memory Information", "="*10)
        svmem = psutil.virtual_memory()
        print(f"Memoria Total       : {self.Memory_Total}")
        print(f"--->Available       : {get_size(svmem.available)}")
        print(f"--->Used            : {get_size(svmem.used)}")
        print(f"--->Percentage      : {svmem.percent}%")
        print("="*20, "SWAP", "="*20)
        swap = psutil.swap_memory()
        print(f"Memoria Swap Total  : {self.Swap_Total}")
        print(f"--->Free            : {get_size(swap.free)}")
        print(f"--->Used            : {get_size(swap.used)}")
        print(f"--->Percentage      : {swap.percent}%")

    def uso_Disco (self):
        #INFORMACIÓN DEL DISCO DURO
        print("="*40, "Disk Information", "="*40)
        print("Partitions and Usage:")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            print(f"=== Device: {partition.device} ===")
            print(f"  Mountpoint: {partition.mountpoint}")
            print(f"  File system type: {partition.fstype}")
            try:
                partition_usage = psutil.disk_usage(partition.mountpoint)
            except PermissionError:
                continue
            print(f"  Total Size: {get_size(partition_usage.total)}")
            print(f"  Used: {get_size(partition_usage.used)}")
            print(f"  Free: {get_size(partition_usage.free)}")
            print(f"  Percentage: {partition_usage.percent}%")
        disk_io = psutil.disk_io_counters()
        print(f"Total read: {get_size(disk_io.read_bytes)}")
        print(f"Total write: {get_size(disk_io.write_bytes)}")

    def uso_Red (self):
        #INFORMACIÓN DE REDES
        print("="*40, "Network Information", "="*40)
        if_addrs = psutil.net_if_addrs()
        for interface_name, interface_addresses in if_addrs.items():
            for address in interface_addresses:
                print(f"=== Interface: {interface_name} ===")
                if str(address.family) == 'AddressFamily.AF_INET':
                    print(f"  IP Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast IP: {address.broadcast}")
                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    print(f"  MAC Address: {address.address}")
                    print(f"  Netmask: {address.netmask}")
                    print(f"  Broadcast MAC: {address.broadcast}")
        net_io = psutil.net_io_counters()
        print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
        print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

    def test_users(self):
        users = psutil.users()
        #self.assertNotEqual(users, [])
        for user in users:
            assert user.name, user
            self.assertIsInstance(user.name, str)
            self.assertIsInstance(user.terminal, (str, type(None)))
            if user.host is not None:
                self.assertIsInstance(user.host, (str, type(None)))
            user.terminal
            user.host
            assert user.started > 0.0, user
            datetime.datetime.fromtimestamp(user.started)
            if WINDOWS or OPENBSD:
                self.assertIsNone(user.pid)
            else:
                psutil.Process(user.pid) 