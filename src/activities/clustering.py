
"""
	Function to get the minimum value of a list
"""
def minimun_value(listValues): 
    minimun = listValues[0] 
    for value in listValues: 
        if value < minimun: 
            minimun = value 
    return minimun 

"""
	Function to get the maximum value of a list
"""
def maximun_value(listValues): 
    maximun = listValues[0] 
    for value in listValues: 
        if value > maximun: 
            maximun = value 
    return maximun 

"""
	Function to get the average value of a list
"""
def average_value(listValues):
	average = 0
	for value in listValues: 
		average = average + value
	average = average / len(listValues)
	return average

"""
	Function to calculate the minimum, average and maximum value of a list
"""
def calcValues(listValues):
	minimun = minimun_value(listValues)
	average = average_value(listValues)
	maximun = maximun_value(listValues)
	return minimun, average, maximun


"""
	Function that creates a file with the hierarchical clustering solution
"""
def clustering(clusters, filename):
	n_clusters = maximun_value(clusters)
	clusters_index = clusters
	clusters_rows = []
	file = open(filename)
	file_read = file.read()
	txt_rows = file_read.split("\n")
	file.close()
	file_write = open("../results/solutions.txt", 'w')
	for i in range(n_clusters+1):
		clusters_rows.append([])
		
	for i in range(len(clusters_index)):
		clusters_rows[clusters_index[i]].append(txt_rows[i])

	clusters_rows.pop(0)
	for cluster_row in clusters_rows:
		students_array = []
		units_array = []
		problems_array = []
		steps_array = []
		corrects_array = []
		duration_array = []
		hints_array = []
		skills_array = []
		for cluster in cluster_row:
			splitted_cluster = cluster.split("\t")
			students_array.append(txt_rows.index(cluster))
			units_array.append(float(splitted_cluster[1]))
			problems_array.append(float(splitted_cluster[2]))
			steps_array.append(float(splitted_cluster[3]))
			corrects_array.append(float(splitted_cluster[4]))
			duration_array.append(float(splitted_cluster[5]))
			hints_array.append(float(splitted_cluster[6]))
			skills_array.append(float(splitted_cluster[7]))
		file_write.write(str(students_array) + "\n" + str(calcValues(units_array)) + "\n" + str(calcValues(problems_array)) + "\n" + str(calcValues(steps_array)) + "\n" + str(calcValues(corrects_array)) + "\n" + str(calcValues(duration_array)) + "\n" + str(calcValues(hints_array)) + "\n" + str(calcValues(skills_array)) + "\n\n")
	file_write.close()
	print("File with the clustering solution created correctly")





