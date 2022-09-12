import os
import psutil
import platform
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
        self.System=uname.system
        self.Node_Name=uname.node
        self.Release=uname.release
        self.Version=uname.version
        self.Machine=uname.machine
        self.Processor=uname.processor

    def print_Server(self):
        print(f"System: {self.System}")
        print(f"Node Name: {self.Node_Name}")
        print(f"Release: {self.Release}")
        print(f"Version: {self.Version}")
        print(f"Machine: {self.Machine}")
        print(f"Processor: {self.Processor}")

