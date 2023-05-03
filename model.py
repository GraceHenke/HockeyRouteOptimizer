from copy import deepcopy

class Model:
    def __init__(self, state):
        # Tour is a TourNetwork Class Obj
        self.mTourNetwork = state
        
        
        
        self.mTotalCost = 0
        self.mPath = []
        
        
        self.mStart = self.mTourNetwork.getStart()

        
        self.mTable = self.mTourNetwork.getTable()
        self.mPossibleCities =  self.mTourNetwork.getPossibleCities()
        self.mNetwork = self.mTourNetwork.getEntireNetwork()
        
        self.mCost = self.mTourNetwork.getTotalCost()
        self.mCurrentNode = None
        self.mFound = 0

        
    def result(self, city):
        state_copy = deepcopy(self)
        
        state_copy.addToPath(city)
        
        
        return state_copy
        
       

        
    
    def getLegalActions(self, current_node):
        
        return self.mTourNetwork.getNeighbors(current_node)

       
            
    
        
    
    def GoalTest(self,state, current_path):
        if current_path[-1] == self.mEnd:  # check the last added location, and determines if it's the ending location
            return True
        
        else:
            return False
        
        
    
    def updatePercepts(self, percepts):
        self.mTourNetwork = percepts[0]
        self.mTotalCost = percepts[1]
        self.mPath = percepts[2]
        
        
        self.mStart = percepts[3]

        
        self.mTable = percepts[4]
        self.mPossibleCities = percepts[5]
        self.mNetwork = percepts[6]
        
        self.mCost = percepts[7]
        self.mCurrentNode = percepts[8]
        
        
        
        
        
      
    def applyAction(self, city):
         self.mTourNetwork.addToPath(city)

    
    
    def getObserveable(self):
         self.mTourNetwork = self.getEntireNetwork()
        
         self.mTotalCost = self.getCost()
         self.mPath = self.mTourNetwork.getCurrentPath()
        
        
         self.mStart = self.mTourNetwork.getStart()

        
         self.mTable = self.mTourNetwork.getTable()
         self.mPossibleCities =  self.mTourNetwork.getPossibleCities()
         self.mNetwork = self.mTourNetwork.getEntireNetwork()
        
         self.mCost = self.mTourNetwork.getTotalCost()
         self.mCurrentNode = self.mTourNetwork.getCurrentNode()

         
        
        
    
    def done(self):
        if self.mFound >= 700:
            return True
        
        else:
            return False