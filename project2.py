from graph import Graph, Vertex
from sys import maxsize

class ISPNetwork:
    def __init__(self):
        self.network = Graph()
        self.MST = Graph()

    def buildGraph(self, filename):
        pass

    def pathExist(self, router1, route2, hops):
        pass

    def buildMST(self, source):
        pass

    def findPath(self, router1, router2):
        pass

    def findForwardingPath(self, router1, router2):
        pass

    def findPathMaxWeight(self, router1, router2):
        pass

    def checkLoop(self, route):
        pass


