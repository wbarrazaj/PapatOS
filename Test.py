#!/usr/bin/env python
#_*_ coding: utf-8 _*_

from http import server
from modulos.funciones import print_ , bytes2human , printlog
from clases.clases import Server
#import platform

Servidor = Server()

Servidor.print_Server()

Servidor.uso_Memoria()

Servidor.uso_Disco()

Servidor.uso_Red()

print("Termino")