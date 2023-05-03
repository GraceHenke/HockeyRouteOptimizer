from model import Model
from enviorment import TourNetwork
import random
from copy import deepcopy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



# Main Algrothim Functions
def RandomRestartHillClimbSearch(state):
    
    current_best_path = GenerateRandomPath(state)
    while current_best_path[0] == current_best_path[1]:
        current_best_path = GenerateRandomPath(state)
        
        
    current_path_cost = state.mTourNetwork.calculateCost(current_best_path)

    while not state.done():
        
        random_path = GenerateRandomPath(state)
    
        while random_path[0] == random_path[1]:
            random_path = GenerateRandomPath(state)
            
        
        found_path_cost, found_path  = SimpleHillClimb(state,random_path)  #examines 100 paths
        
        if found_path_cost < current_path_cost:
            current_best_path = found_path
            current_path_cost = found_path_cost
            
        state.mFound += (100)

        
    return current_best_path, current_path_cost


    
    


def SimpleHillClimb(state, path):
    all_possible_neighbors = GenerateNeighbors(path) # could also use Generate Random Neighbors function (compare the different generation methods)
    
    cost = 1000000000000
    best_next_state = None
    
    
    for neighbor in all_possible_neighbors:
            
        if neighbor[0] == neighbor[1]:
            neighbor[1], neighbor[8] = neighbor[8], neighbor[1]
            
       
        temp_cost = state.mTourNetwork.calculateCost(neighbor)
        
    

        if temp_cost < cost:
            cost = temp_cost
            best_next_state = neighbor
            
    return cost, best_next_state



def GenerateRandomPath(state):
    all_cities = state.mTourNetwork.getPossibleCities()
    path = [state.mStart]
    
    for i in range(len(all_cities)):
        random_city = random.choice(all_cities)
        path.append(random_city)
        all_cities.remove(random_city)
        
    return path


# Different Ways to Generate Comparitive Paths


def GenerateNeighbors(path):
    # randomly select two positions and swap the elements (won't swap start city)
    possible_solutions = []
    
    for i in range(100):
        path_copy = deepcopy(path)
        
        pos1 = random.randint(5,8) # 5- 9
        pos2 = random.randint(1, 4)  # 1-4
        
        path_copy[pos1], path_copy[pos2] = path[pos2], path[pos1]


        
        possible_solutions.append(path_copy)
        
    return possible_solutions
    
    
def GenerateRandomSolutions(state, path):
    # returns a unique set of possible solutions 
    random_solutions = []
    random_path = []
     
    end = path[1::]
    
    
    for i in range(100):
        random_path = random.sample(end, len(end))

        
        random_path.insert(0, state.mStart)
        random_solutions.append(random_path)
        
    random_results = remove_duplicates(random_solutions)
     
    return random_results


def remove_duplicates(solutions):
    result = []
    for solution in solutions:
        if solution not in result:
            result.append(solution)
            
    return result




def DisplayStats(division):

   results = pd.read_csv("Data/{}_results.csv").format(division)

   # Paths With Different Starting Cities 
   sns.scatterplot(x="Cost", y="Start", data = results, hue="Function-Type")
   plt.show()
   
   simple = results.query('`Function-Type` == "Simple"')
   random =  results.query('`Function-Type` == "Random"')
   
   random_sample = simple.sample(n=25)
   simple_sample = simple.sample(n=25)
   
   # Samples of Random and Simple 
   sns.lineplot(x="Iteration", y="Cost", data = random_sample)
   plt.show()

   sns.lineplot(x="Iteration", y="Cost", data = simple_sample)
   plt.show()

   print(simple.describe())
   print(random.describe())
   print("Lowest Cost Found For Simple: ", simple['Cost'].min())
   print("Lowest Cost Found For Random: ", random['Cost'].min())
   print(results.describe())
    
    
def GenerateSearch(start_city, division):         
    network = TourNetwork(division, start_city)
    network.displayNetwork()
    model_network = Model(network)
                
    paths = []
    functions_used = []
    costs = []
                
        
    for i in range(500):
        random_starting_path = GenerateRandomPath(model_network)
        cost, path = SimpleHillClimb(model_network, random_starting_path)
                        
        paths.append(path)
        costs.append(cost)
        functions_used.append("Simple")
                        
                    
        
    for i in range(500):
        path, cost = RandomRestartHillClimbSearch(model_network)
                        
        paths.append(path)
        costs.append(cost)
        functions_used.append("Random")
     
  
    
    df = pd.DataFrame({"Cost": costs,
                        "Path": paths,
                        "Function-Type": functions_used})
    
    df.to_csv('%s_results.csv'%(division), mode='a')  
    
    

# Main Function
def main():
    central = ["Jets", "Blues", "Wild", "Avalanche", "Blackhawks", "Predators", "Stars", "Coyotes"]
    pacific = ["Golden Knights", "Kraken", "Ducks","Oilers","Flames","Sharks","Kings", "Canucks"]
    metro = ["Devils", "Islanders", "Hurricanes", "Penguins", "Rangers", "Capitals", "Flyers", "Blue Jackets"]
    atlantic = ["Bruins", "Maple Leafs", "Panthers", "Senators", "Sabres", "Canadiens", "Red Wings", "Lightning"]
    
    GenerateSearch("Lightning", "Atlantic")

    
    DisplayStats("Atlantic")
            
        
    
    
main()

    

            
                
    
