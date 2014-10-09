from parser import FloorplanParser
import math

__author__ = 'pawel'


class NetMaker(object):
    # Default net parameters
    area = 0
    # Init kwargs names

    def __init__(self, file_name):
        self.floorplan = FloorplanParser(file_name)
        self.area = Area(end_row=self.floorplan.rows, end_col=self.floorplan.cols)

    def createNet(self, thermometers_num, **kwargs):

        if "area" in kwargs:
            self.area = kwargs['area']

        # Check number of rows and columns
            width = self.area.getAreaWidth()
            hight = self.area.getAreaHight()

        # Find number of thermometers in row
            term_in_row = math.sqrt((width*thermometers_num)/hight)
            term_in_col = thermometers_num/term_in_row


class Area(object):
    # Area borders parameters
    start_row = 0
    end_row = 0
    strat_col = 0
    end_col = 0

    init_kwargs = ["start_row", "end_row", "start_column", "end_column"]

    def __init__(self, **kwargs):

        for kwarg in self.init_kwargs:
            if kwarg in kwargs:
                try:
                    if vars()["self.{}".format(kwarg)] < 0:
                        raise NetMakerException(NetMakerException.NEGATIVE_VALUE_EXCEPTION)
                    vars()["self.{}".format(kwarg)] = kwargs[kwarg]
                except NetMakerException as e:
                    print(e)

    def getAreaWidth(self):
        return self.end_col - self.start_row

    def getAreaHight(self):
        return self.end_row - self.start_row


class NetMakerException(Exception):

    def __init__(self, value):
        self.value = value


class NetMakerExceptionsEnum():

    NEGATIVE_VALUE_EXCEPTION = "Area parameters cannot have negative values"