# AmstelHaege
In this repository you can find our possible solutions for the case [AmstelHaege](http://heuristieken.nl/wiki/index.php?title=Amstelhaege), which deals with finding the right algorithm for the construction of a new residential area in a way that is as profitable as possible.
The requirements of the construction of this new residential area are as follows:
* The total amount of houses must consist of 60% single-family homes, 25% bungalows and 15% maisons, which not only differ in dimensions but also differ in what extent it must be free-standing with regard to other houses. The more extra distance in between houses, the higher the increase in value of the house, since every extra meter leads to a priceincrease of 3% (single-family homes) , 4% (bungalows) or 6% (maisons).
* Twenty percent of the area is reserved for water surfaces that can be divided into a maximum of four bodies, each of which must have a height-width ratio between 1 and 4.

The objective is to eventually create a map with the most profitable layout of the residential area, for an amount of 20, 40 and 60 houses. The score for a map is the sum of the final values of the houses.

## Guide
This repository contains two main folders: *Code* and *Experiments*.
* *Code*  
	This folder contains scripts with algorithms for a possible solution of our case and seperate supporting files needed to run these scripts.
	* *Data*: contains a supporting file with the given requirements of the case
	* *Results*: contains outcomes and visualisations of our code

* *Experiments*  
	In this folder you will find our initial and non-final scripts, used for testing and experimenting.
	* *Data*: contains a supporting file with the given requirements of the case

## Approach
These are the steps we took in finding a solution for our case:
1. Create a map and add houses  
	Using *Matplotlib* we plotted a map of AmstelHaege. Then we created classes for each housetype, containing attributes for the requirements (main class) and for the id, coordinates and extra freespace (subclasses). These classes are loaded into a script and being called upon, in order to be able to easily place multiple houses onto the map that each fullfill all requirements. When adding the houses to the map, a singlefamily house will appear as a blue rectangle, a bungalow as a pink one and a maison as a yellow one.
2. Calculation of the state space  
	In order to determine in how many ways twenty houses can be placed onto the map (160 x 180), we used this calculation of the state space:
<table>
	<tr>
		<th>House on grid (160 x 180 m)</th>
		<th>Possibilities</th>
		<th>Total</th>
	</tr>
	<tr>
		<td>Singlefamily (8 x 8 m)</td>
		<td>(160 x 180) ^ 12</td>
		<td>3,26E + 53</td>
	</tr>
	<tr>
		<td>Bungalow (10 x 7.5 m)</td>
		<td>(160 x 180) ^ 5</td>
		<td>1,98E + 22</td>
	</tr>
	<tr>
		<td>Maison (11 x 10.5)</td>
		<td>(160 x 180) ^ 3</td>
		<td>2,39E + 13</td>
	</tr>
	<tr>
		<td> </td>
		<td> </td>
		<td>1,54E + 89</td>
	</tr>
</table>			
3. Calculation of the map score  
	To be able to calculate the total value of the map, it is needed to write a function that calculates the amount of extra freespace of a house relative to another house (the more extra freespace surrounding a house, the higher its value will be). Only after this, it is possible to calculate the final total value of a house, and later of the whole map.
	* Calculate the extra freespace per house
	This function calculates the amount of freespace of a house relative to his closest neighbour. First the function makes sure the houses will not overlap or (partly) fall out of the map. Hereafter, from each side and corner, the house will loop over the surrounding coordinates until it comes across the position of its neighbour. Having identified this position, the function calculates the extra freespace of the house and stores the outcome in its matching class attribute.
	* Calculate the total value per house
	In order for a house to be able to calculate its own improved value, a method is included in each of the subclasses. This method takes the original value of the house and multiplies it with the extra freespace multiplied by the percentage of priceimprovement.
4. Random walk  
	The first task has been to place the houses on the map randomly.
	![Random walk](https://github.com/pleunbis/Heuristieken/blob/master/Code/Results/randomwalk.png)
5. Algorithms
	* [Hill climbing](https://www.geeksforgeeks.org/introduction-hill-climbing-artificial-intelligence/)
	1. Evaluate the intitial state. If it is a goal state then stop and return success. Otherwise, make initial state as current state.
	2. Loop until the solution state is found or there are no new operators present which can be applied to the current state.
		* Select a state that has not been applied yet to the current state and apply it to produce a new state.
		* Perform these to evaluate the new state
			* If the current state is the goal state: stop and return success.
			* If it is better than the current state: make it current state and proceed further
			* If it is not better than the current state: continue in the loop until a solution is found
	* Simulated annealing
6. Add water to the map

## Prerequisites
* [Python 3.6](https://www.python.org/downloads/)
* [Atom 1.32](https://atom.io/)
* [Matplotlib 2.1.2](https://matplotlib.org/2.1.2/users/installing.html)
* [Numpy](https://scipy.org/install.html)

## Authors
Philline Dikker

Pleun Bisseling

Vera Nijmeijer

