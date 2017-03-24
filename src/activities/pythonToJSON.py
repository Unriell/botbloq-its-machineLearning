def translator(filename):
	file = open(filename);
	file_read = file.read()
	
	file_rows = file_read.split("\n")
	n = len(file_rows)-1
	rows = file_rows[1:n]
	
	row = 0
	array_condition = []
	consequence = ""
	indent_previus = 0
	group = 1
	JSON = open("../results/rules.json", 'w')
	JSON.write("[")
	for row in rows:
		splitted_row = row.split(" ")
		
		# count the row indentation to compare with the previous row indentation
		n_indent = 0
		while splitted_row[0] == '': 
			splitted_row.pop(0)
			n_indent+=1
		n_indent = n_indent / 2
		
		# If the first word in the list is "if", the condition is stored
		if splitted_row[0] == 'if':
			condition = " ".join(splitted_row[1:])
			array_condition.append(condition[:len(condition)-1])

		
		# If the first word in the list is "else:" delete the previous conditions 
		# of greater or equal indentation and store the condition corresponding to the "else"
		elif splitted_row[0] == 'else:':
			for i in range(indent_previus - n_indent):
				n = len(array_condition)-1
				array_condition.pop(n)

			condition = " ".join(splitted_row[4:])
			array_condition.append(condition)
		
		# If the first word is not any of the previous ones (return), the resulting 
		# group is obtained and the javascript rule is created
		else:
			string_row = "".join(splitted_row)
			n = len(string_row)-1
			array_groups = string_row[8:n-2].split(".")
			group = selectGroup(array_groups)
			
			if(rows.index(row) == len(rows)-1):
				JSON.write(createJSON(array_condition,group)+ "]")
			else:
				JSON.write(createJSON(array_condition,group)+ ",")

		indent_previus = n_indent
	JSON.close()
	print("Python script translated to Javascript node-rules correctly")


def selectGroup(array_groups):
	group = 1
	for i in range(len(array_groups)):
		if (int(array_groups[i]) > 0):
			group = i+1

	return group

def createJSON(array_condition, group):
	conditions = ") && (this.".join(array_condition)
	conditions = "(this." + conditions + ")"
	JSON = "{\n\t\"condition\": \"function(R) {   R.when(" + conditions + ");   }\",\n\n\t\"consequence\": \"function(R) {   this.group = "  + str(group) + ";   R.stop();   }\"\n}"
	return JSON

