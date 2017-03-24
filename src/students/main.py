from hierclustering01 import hierCluster
from decisionTree import decisionTree
from clustering import clustering
import sqlite3
from createDataCard import createTable, insertValuesInTable, createDataCard
from pythonToJSON import translator

con = sqlite3.connect('../../data/database')
print "The database opened successfully"

cursor = con.cursor()

createTable(cursor) 						# Create a table into database

insertValuesInTable(con) 					# insert all the valid values of the initial file in the table

filename = createDataCard(cursor) 			# The data card is created using the data of the bd 
#filename = "../../data/dataCard.txt"
clusters = hierCluster(filename)			# Normalization and hierarchical clustering are performed

#clustering(clusters, filename)				# A file is created with a solution to hierarchical clustering

#decisionTree(clusters, filename)			# The decision tree is made from the clusters obtained 
											# and is translated to a python script

#translator("../results/python_tree.txt")	# the python script in translated to json node-rules

con.close()