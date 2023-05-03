
# Problem Description 
Hockey teams typically play every team in their division 3-4 times, this program simulates how a team could play each team in their division the most effective way possible (the efficentcy is based upon distance traveled) This program was modeled after the Traveling Salesman problem. 

This program can be used to generate paths for any starting city and division. This program uses two different searching algothims, Simple Hill Climbing and Random Restart Hill Climbing. 

## Searching Techniques
The searching techniques I used are Simple Hill Climbing and Random Restart Hill Climbing. Additionally, each search algorthim had two options to generate the neighboring solutions. One way created a completely random path, and the other randomly swapped elements. Both of these options tried to remove duplicates and results that had back-to-back node visitation (since I allowed the path to return to the starting city)

## File Descriptions

### Model.py
- __init__: creates the model object. generates a model of the tour network object.
- __result__: returns the result of an action 
- __getLegalActions__: returns all possible actions (what neighbors can the state travel to)
- __GoalTest__: takes the current state and path, determines if it meets the requirements
- __updatePercepts__: updates the percepts.
- __applyAction__: takes an action. applies the desired action.
- __getObserveable__: gets all of the observable percepts.
- __done__: determines whether or not the algorthim should be done.
-
### SearchAgent.py
- __RandomRestartHillClimbSearch__: using Random Restart and Simple Hill Climbing, finds the best possible path, untill the models preset cutoff is triggered. Returns the best cost path, and the cost of that path.

- __SimpleHillClimb__: takes the current state and a randomly created path. Generates and compares possible neigbors until it runs out. Returns the best possible cost and path. 

- __GenerateRandomPath__: takes the state and generates a random path. Returns the randomly generated path.

- __GenerateNeighbors__: takes the path. Generates a new random neighbor, swapping different positions. Returns 100 newly generated neighbor.

- __GenerateRandomSolutions__: takes the path and state. Randomly generates possible paths. Returns 100 unique paths.

- __remove-duplicates__: removes duplicate. Returns a list without duplicates

- __DisplayStats__: opens the generated CSV files, then displays different statistics on each of the divisions results. Doesn't return anything 

- __main__: generates and saves the results of 500 runs of Simple Hill Climbing and Random Restart.


### enviorment.py
All of these listed below are contained in a Class called TourNetwork
- __init__: Takes a division name and a starting city. Sets up the NX network used to keep track of node connections

__Getters__
- __getPath__: returns the path
- __getTotalCost__: returns the total cost
- __getStart__: returns the start city
- __getDivision__: returns the current division
-__getTable__: returns the table of distance data 
- __getEntireNetwork__:returns the nx network
- __getPossibleCities__: returns the list of possible city nodes 
- __getNeighbors__: returns all possible neighbors (requires the starting node)

__Setters__
- __updateStartingTeam__: updates the starting team. 
- __updatedivisionData__:updates the distance table to the correct division. Also updates the network.
-__updateNetwork__: updates the NX network object.

__Additional Methods__
- __remove_dup__: removes duplicates from a list
- __addCityToPath__: adds the desired city to the path
- __calculateCost__: caculates the cost of the path
- __displayPathPerfomance__: displays the ending performace of the path
- __displayNetwork__: visually displays the nx network.
- __displaydivisionMap__: visually depiction of the all of the divisions. (currently not implemented!)


# Generated Networkx Graph Example
![Pacific Division](/Digital%20Assets/Pacific_Division_Connections.png)
