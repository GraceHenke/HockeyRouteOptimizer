import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

class TourNetwork:
    def __init__(self, division, start):
        self.mStart = start
        self.mDivision = division
        
        self.updatedivisionData(self.mDivision)
        
        self.mEntireNetwork =  nx.from_pandas_edgelist(self.mDistanceTable, 'Start', 'End', edge_attr="Distance", create_using=nx.DiGraph())
        
        self.mPossibleCities = self.getPossibleCities()
        self.mTotalCost = 0
        self.mPath = []
        
        
    def getPath(self):
        return self.mPath
        
    def getTotalCost(self):
        return self.mTotalCost
    
    def getStart(self):
        return self.mStart

    
    def getDivision(self):
        return self.mDivision
    
    def getTable(self):
        return self.mDistanceTable
    
    def getEntireNetwork(self):
        return self.mEntireNetwork

    def getPossibleCities(self):
        # returns a list of all possible cities
        cities = self.mDistanceTable['Start'].tolist()
    
        cities = self.remove_dup(cities)
        
        return cities
    
    def remove_dup(self, cities):
        possible_cities = []
        for location in cities :
            if location not in possible_cities:
                possible_cities.append(location)
            
        return possible_cities
    

    
    def addCityToPath(self, neighbor):
        self.mPath.append(neighbor)
        
        
        
    def calculateCost(self, path):
        
      cost = nx.path_weight(self.mEntireNetwork, path, weight="Distance")
      return cost
            
    def calculateEnvPath(self):
        self.mCost = nx.path_weight(self.mEntireNetwork, self.mPath, weight="Distance")
    
    def getNeighbors(self, node):
        # gets all the neighbors connected to the node
        return nx.neighbors(self.mEntireNetwork, node)
    
    def updateStartingTeam(self,team):
        # allows the user to start from any city in the network, assumes the user has uploaded correct division infomation
        self.mStart = team
        
        

        
    def updatedivisionData(self, division):
        # updates division infomation
        
        self.mDivision = division
        
        if division == "Pacific":
            self.mDistanceTable = pd.read_csv("Data/hockey_distances_pacific.csv")
            
        elif division == "Atlantic":
            self.mDistanceTable = pd.read_csv("Data/hockey_distances_atlantic.csv")
        

        elif division == "Central":
            self.mDistanceTable = pd.read_csv("Data/hockey_distances_central.csv")
        
      
        else:
            self.mDistanceTable = pd.read_csv("Data/hockey_distances_metro.csv")
            
            
            
            self.updateNetwork()
            
    def updateNetwork(self):
        self.mEntireNetwork =  nx.from_pandas_edgelist(self.mDistanceTable, 'Start', 'End', edge_attr="Distance")
    
            
        
    def displayPathPerfomance(self, cost, path):
        # displays the final path with the total cost of the path
         
        print("The total cost of path: " + str(cost) + "Least Cost Path: " + str(path))
    
    
    def displayNetwork(self):
        # displays the network of nodes in a visual display 
        
        # used a geek for geeks tutorial for this code!

        pos = nx.shell_layout(self.mEntireNetwork)
        edge_width = [0.001 * self.mEntireNetwork[u][v]['Distance'] for u, v in self.mEntireNetwork.edges()]
        nx.draw(self.mEntireNetwork, pos, with_labels=True, node_size=2000, node_color="#A8C9DA",node_shape="o", alpha=0.5, linewidths=20, width=edge_width)
        
        
    def displaydivisionMap(self):
        # Basemap Implementation?
        
        pass
    
    
    