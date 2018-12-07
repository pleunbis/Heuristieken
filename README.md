# AmstelHaege
In this repository you can find our possible solutions for the case [AmstelHaege](http://heuristieken.nl/wiki/index.php?title=Amstelhaege), which deals with finding the right algorithm for the construction of a new residential area in a way that is as profitable as possible.
The requirements of the construction of this new residential area are as follows:
* The total amount of houses must consist of 60% single-family homes, 25% bungalows and 15% maisons, which not only differ in dimensions but also differ in what extent it must be free-standing with regard to other houses. The more extra distance in between houses, the higher the increase in value of the house, since every extra meter leads to a price improvement of 3% (single-family homes) , 4% (bungalows) or 6% (maisons).
* Twenty percent of the area is reserved for water surfaces that can be divided into a maximum of four bodies, each of which must have a height-width ratio between 1 and 4.

<table>
	<tr>
		<th> </th>
		<th>Dimensions (in m)</th>
		<th>Freespace (in m)</th>
		<th>Price</th>
		<th>Price improvement</th>
	</tr>
	<tr>
		<td>Singlefamily</td>
		<td>8 x 8</td>
		<td>2</td>
		<td>€285.000</td>
		<td>3%</td>
	</tr>
	<tr>
		<td>Bungalow</td>
		<td>10 x 7.5</td>
		<td>3</td>
		<td>€399.000</td>
		<td>4%</td>
	</tr>
	<tr>
		<td>Maison</td>
		<td>11 x 10.5</td>
		<td>6</td>
		<td>€610.000</td>
		<td>6%</td>
	</tr>
</table>

The objective is to eventually create a map with the most profitable layout of the residential area, for an amount of 20, 40 and 60 houses. The score for a map is the sum of the final values of the houses.

## Guide
This repository contains two main folders: *Code* and *Experiments*.
* *Code*  
	This folder contains a file with possible algorithms for the solution of our case (*algorithms.py*), separate supporting files (*helper.py, classes.py*), and a main file (*main.py*).
	* *Data*: contains a supporting file with the given requirements of the case
	* *Results*: contains outcomes and visualizations of the algorithms used

* *Experiments*  
	In this folder you will find our initial and non-final scripts, used for testing and experimenting.
	* *Data*: contains a supporting file with the given requirements of the case

## Approach
These are the steps we took in finding a solution for our case:  
1. CREATE MAP AND ADD HOUSES  
Using *Matplotlib* we plotted a map of AmstelHaege. Then we created classes for each housetype, containing attributes for the requirements (main class) and for the id, coordinates and extra freespace (subclasses). These classes are loaded into a script and being called upon, in order to be able to easily place multiple houses onto the map that each fulfill all requirements. When adding the houses to the map, a singlefamily house will appear as a blue rectangle, a bungalow as a pink one and a maison as a yellow one.
2. STATE SPACE  
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

3. CALCULATION OF THE MAP SCORE  
In order to find solutions within a correct range, we calculated an upperbound and lowerbound of the total map score of AmstelHaege (for 20 houses).
* Lowerbound (20 houses)  
Without any extra freespace, the total score of the map will be **€7.245.000**  

<table>
	<tr>
		<th> </th>
		<th>Price</th>
		<th>Amount of houses</th>
		<th>Total</th>
	</tr>
	<tr>
		<td>Singlefamily</td>
		<td>€285.000</td>
		<td>12</td>
		<td>€3.420.000</td>
	</tr>
	<tr>
		<td>Bungalow</td>
		<td>€399.000</td>
		<td>5</td>
		<td>€1.995.000</td>
	</tr>
	<tr>
		<td>Maison</td>
		<td>€610.000</td>
		<td>3</td>
		<td>€1.830.000</td>
	</tr>
	<tr>
		<td> </td>
		<td> </td>
		<td> </td>
		<td>€7.245.000</td>
	</tr>
</table>

* Upperbound (20 houses)  
The first table illustrates our calculation of the upperbound. First, the length, width and freespace (on both sides) of a house are subtracted from the map length and width. Furthermore, we assume the house to be in the middle of the map, since this would generate the most extra freespace (and thus a higher price). The middle position of the house explains why the space that is left from the earlier subtraction is divided by two (for both length and width). We then take the shortest distance to the edge of the map and round this number down. This number is counted as meters of extra freespace.

<table>
	<tr>
		<th> </th>
		<th>Length of house</th>
		<th>Width of house</th>
		<th>Freespace</th>
		<th>Price</th>
		<th>Price improvement</th>
		<th>Space left of map length</th>
		<th>Space left of map width</th>
		<th>Space left of map length / 2</th>
		<th>Space left of map width / 2</th>
		<th>Min. rounded</th>
	</tr>
	<tr>
		<td>Singlefamily</td>
		<td>8</td>
		<td>8</td>
		<td>2</td>
		<td>€285.000</td>
		<td>0.03</td>
		<td>137.5</td>
		<td>157</td>
		<td>68.75</td>
		<td>78.5</td>
		<td>68</td>
	</tr>
	<tr>
		<td>Bungalow</td>
		<td>10</td>
		<td>7.5</td>
		<td>3</td>
		<td>€399.000</td>
		<td>0.04</td>
		<td>148</td>
		<td>168</td>
		<td>72</td>
		<td>83.25</td>
		<td>72</td>
	</tr>
	<tr>
		<td>Maison</td>
		<td>11</td>
		<td>10.5</td>
		<td>6</td>
		<td>€610.000</td>
		<td>0.06</td>
		<td>144</td>
		<td>166.5</td>
		<td>74</td>
		<td>84</td>
		<td>74</td>
	</tr>
</table>  

The second table shows our final calculation of the upperbound:  

Objective function =
*price x (1 + (price improvement x rounded number of extra freespace))*  

(The rounded number of extra freespace is taken from last column of the first table)  

Adding up these calculated values for each housetype, this makes up a total of **€29.143.800**  

<table>
	<tr>
		<th> </th>
		<th>Amount of houses</th>
		<th>Total price</th>
	</tr>
	<tr>
		<td>Singlefamily</td>
		<td>12</td>
		<td>€13.543.200</td>
	</tr>
	<tr>
		<td>Bungalow</td>
		<td>5</td>
		<td>€6.304.200</td>
	</tr>
	<tr>
		<td>Maison</td>
		<td>3</td>
		<td>€9.296.400</td>
	</tr>
	<tr>
		<td> </td>
		<td> </td>
		<td>€29.143.800</td>
	</tr>
</table>


Now that we have calculated the state space of the total score, we can start looking to the calculation of a real map. To be able to calculate the total value of the map, it is needed to write a function that calculates the amount of extra freespace of a house relative to another house (the more extra freespace surrounding a house, the higher its value will be). Only after this, it is possible to calculate the final total value of a house, and later of the whole map.
* Calculate the extra freespace per house (*calculate_freespace()*)  
This function calculates the amount of freespace of a house relative to his closest neighbor. First the function makes sure the houses will not overlap or (partly) fall out of the map. Hereafter, from each side and corner, the house will loop over the surrounding coordinates until it comes across the position of its neighbor. Having identified this position, the function calculates the extra freespace of the house and stores the outcome in its matching class attribute.
* Calculate the total value per house (*calculateprice()*)  
In order for a house to be able to calculate its own improved value, a method is included in each of the subclasses. This method takes the original value of the house and multiplies it with the extra freespace multiplied by the percentage of price improvement.

4. ALGORITHMS  

**Random**  
The first task has been to place the houses on the map randomly. Using the function that calculates the extra freespace (as explained above),
The random function iterates over the assigned amount of houses of each different house type, and appends each houses' id, random coordinates and extra freespace to the total list of houses. Hereafter, using the functions *calculate_freespace()* and *calculateprice()*, the random algorithm calculates the extra freespace and price of each house and adds these values to the list. Having calculated these values, the rectangles can be created and added to the grid.
In order to merge every house of a different house type together to one list, the functions described above are used once more for the entire list of houses.  

Running the random algorithm for twenty houses should give you a plot like this:

![AmstelHaege random](https://github.com/pleunbis/Heuristieken/blob/master/Code/Results/Random/amstelhaege.png)

**Hill climbing**  
The hill climber algorithm works as follows.  
Loop until the demanded number of iterations has been executed:  
1. Calculate the value of the current map
2. Randomly pick a house that will get a new position
3. Calculate the freespace and value of the new map
4. Check if this solution is valid (enough freespace)
	* If the new value is better than or equal to the old value, the new map is accepted
	* If the old value is better than the new value, continue with the old map

**Simulated annealing**  
The simulated annealing algorithm works as follows.  
Loop until the demanded number of iterations has been executed:  
1. Calculate the value of the  current map
2. Randomly pick a house will get a new position
3. Randomly pick a new x and y coordinate to place the house
4. Calculate the freespace and value of the new map
5. Check if this solution is valid (enough freespace)
	* If the new value is better than or equal to the old value, the new map is accepted
	* If the old value is better than the new value, the acceptance probability determines whether or not this solution is accepted.

* Acceptance probability  
	The acceptance probability is calculated with the following formula:  
	p = e ^ reduction/temperature  
	Where reduction = (new value – old value) * 0.6  
	[Source](https://www.dropbox.com/sh/g40noo93tnhy7jq/AAAW22CPLIPu_tHR2sfAq6T2a?dl=0&preview=3+-+Iteratieve+Zoekmethoden.pdf)

* Cooling scheme   
	The cooling scheme used in the simulated annealing algorithm is the following:  
	Start temperature = 0.3 x objective function of start map

	For every iteration the temperature will be recalculated with this function:  
	Temperature = temperature x 0.99

5. ADD WATER TO THE MAP  
![AmstelHaege water](https://github.com/pleunbis/Heuristieken/blob/master/Code/Results/Random/amstelhaege_water.png)

## Prerequisites
* [Python 3.6](https://www.python.org/downloads/)
* [Atom 1.32](https://atom.io/)
* [Matplotlib 2.1.2](https://matplotlib.org/2.1.2/users/installing.html)
* [Numpy](https://scipy.org/install.html)

## Authors
Philline Dikker

Pleun Bisseling

Vera Nijmeijer
