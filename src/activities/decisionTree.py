from sklearn import tree
from sklearn.tree import _tree
import pydot

"""
	Function to draw the decision tree corresponding to 
	clustering. Create a .dot file and a .pdf file
"""
def decisionTree(clusters, filename):
	X = []
	Y = clusters
	file = open(filename)
	file_read = file.read()
	txt_rows = file_read.split("\n")
	for row in txt_rows:
		X.append(row.split("\t")[1:])

	clf = tree.DecisionTreeClassifier()
	clf = clf.fit(X, Y)
	names = ['units', 'problems', 'steps', 'corrects_steps', 'duration', 'hints', 'skills']
	with open('../results/graph.dot', 'w') as f:
		f = tree.export_graphviz(clf, out_file=f,feature_names=names)

	graphs = pydot.graph_from_dot_file('../results/graph.dot')
	print("Tree .dot file created correctly")

	graphs[0].write_pdf('../results/graph.pdf')
	print("Tree .pdf file created correctly")

	tree_to_code(clf, names)
	print("Tree translated to python script correctly")

"""
	Function that translates the decision tree to a python script
"""
def tree_to_code(tree, feature_names):
	tree_ = tree.tree_
	feature_name = [
		feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
		for i in tree_.feature
	]
	file_write = open("../results/python_tree.txt", 'w')
	file_write.write("def tree({}):\n".format(", ".join(feature_names)))

	def recurse(node, depth, file):
		indent = "  " * depth
		if tree_.feature[node] != _tree.TREE_UNDEFINED:
			name = feature_name[node]
			threshold = tree_.threshold[node]
			file.write("{}if {} <= {}:\n".format(indent, name, threshold))
			recurse(tree_.children_left[node], depth + 1, file)
			file.write("{}else:  # if {} > {}\n".format(indent, name, threshold))
			recurse(tree_.children_right[node], depth + 1, file)
		else:
			file.write("{}return {}\n".format(indent, tree_.value[node]))

	recurse(0, 1, file_write)
	file_write.close()