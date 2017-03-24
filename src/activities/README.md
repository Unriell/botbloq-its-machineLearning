# botbloq-its-machineLearning

Description of the machine learning scripts in order to main.py execution: 

1. createDataCard.py 

It contains 3 main functions:

- createTable(cursor):
	
	Creates STUDENTS table in sqlite database.

- insertValuesInTable(con):
	
	Enter all the valid values of the "algebra_2005_2006_train.txt" 
	file in the STUDENTS table.

- createDataCard(cursor):

	Calculates the different values contained in the data card 
	and returns the name of the created data card


2. hierclustering01.py

Function obtained from the 2016-2017 machine learning subject, 
it performs the data card normalization, hierarchical clustering and 
returns the clusters.


3. clustering.py

Performs the file that explains the results obtained from clustering 


4. decisionTree.py

It contains 2 main functions:

- decisionTree(clusters, filename):
	
	Makes the decision tree and returns it in a .dot and .pdf file

- tree_to_code(tree, feature_names):

	Translates the decision tree to a python script composed of' 'if else' conditions

5. pythonToJSON.py

	Translates the python script obtained in the previous function to JSON rules