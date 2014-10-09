# -*- coding: utf-8 -*-
from pyatspi import Enum
import sys

__author__ = 'pawel'

from xml.dom.minidom import parse

# Create the minidom document
class FloorplanParser:

    def __init__(self,file):
        xml_file = open(file)
        self.doc = parse(xml_file)

    #Metoda sprawdzająca czy dany plik XML jest plikiem opisu płytki
    def isDescriptionFile(self):
        if self.doc.getElementsByTagName("device"):
            return True
        else:
            return False

    #Metoda parusjąca plik opisu płytki
    def parseFile(self, file="des", floorplan=None):
        if (file=="des"):
            size = self.doc.getElementsByTagName("size")[0]
            self.cols = int(size.getAttribute("cols"))
            self.rows = int(size.getAttribute("rows"))
            self.obstacles = self.doc.getElementsByTagName("obstacle")
            self.units = self.doc.getElementsByTagName("unit")

            self.floorplan = []

            '''Zdefiniowanie pustego floorplanu'''
            '''Wyczysczenie listy'''
            for i in range(self.rows):
                for j in range(self.cols):
                    self.floorplan.append(Blocks.empty_clb)

            '''Wczytanie obstacli'''
            for obs in self.obstacles:
                x = int(obs.getAttribute("x"))
                y = int(obs.getAttribute("y"))
                self.floorplan[y * (self.cols) + x] = Blocks.obstacle

            '''Wczytywanie unitów '''
            for uni in self.units:
                x = int(uni.getAttribute("x"))
                y = int(uni.getAttribute("y"))
                self.floorplan[y * (self.cols) + x] = Blocks.unit

    '''Metoda wypisująca tekstowo wyglad płytki'''
    def printTextFloorplan(self):
        k = 0
        for i in range(self.rows):
            if i != 0:
                sys.stdout.write(str(i) + "\t")
            for j in range(self.cols):
                if i == 0:
                    sys.stdout.write("\t" + str(j+1))
                else:
                    sys.stdout.write(str(self.floorplan[self.cols*(i-1) + j]) + " ")
                    k += 1
            sys.stdout.write("\n")
        print("Razem bloków funkcyjnych: " + str(k))

    '''Metoda podająca zawartość danego bloku'''
    def getElement(self, x, y):
        return self.floorplan(self.cols*y + x)


class Blocks(Enum):
    empty_clb = 0
    obstacle = 1
    unit = 2