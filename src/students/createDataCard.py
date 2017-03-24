from hierclustering01 import hierCluster
from sklearn import tree
from decisionTree import decisionTree
from clustering import clustering

"""
	The STUDENTS table is created in the sqlite database
"""
def createTable(cursor):
	cursor.execute('''CREATE TABLE STUDENTS 
		(ROW 						INT 	PRIMARY KEY NOT NULL,
		ID_STUDENT					TEXT 	NOT NULL,
		UNIT 						TEXT 	NOT NULL,
		PROBLEM 					TEXT 	NOT NULL,
		PROBLEM_VIEW 				INT		NOT NULL,
		STEP 						TEXT 	NOT NULL,
		STEP_START_TIME				TEXT	NOT NULL,
		FIRST_TRANSACTION 			TEXT	NOT NULL,
		CORRECT_TRANSACTION_TIME 	TEXT	NOT NULL,
		STEP_END_TIME 				TEXT 	NOT NULL,
		STEP_DURATION 				INT		NOT NULL,
		CORRECT_STEP 				INT 			,
		ERROR_STEP					INT 			,
		CORRECT_FIRST_STEP			INT 	NOT NULL,
		INCORRECTS					INT 	NOT NULL,
		HINTS						INT 	NOT NULL,
		CORRECTS 					INT 	NOT NULL,
		KC							TEXT	NOT NULL,
		OPPORTUNITY					TEXT	NOT NULL)''')
	print "Table created correctly"

"""
	Enter all the valid values of the file 
	"algebra_2005_2006_train.txt" in the table STUDENTS
"""
def insertValuesInTable(con):
	cursor = con.cursor()
	file = open("../../data/algebra_2005_2006_train.txt")
	file_read = file.read()
	txt_rows = file_read.split("\n")[1:]
	file.close()
	for txt_row in txt_rows:
		row = txt_row.split("\t")
		if row[0] != '' and row[1] != '' and row[2] != '' and row[3] != '' and row[4] != '' and row[5] != '' and row[6] != '' and row[7] != '' and row[8] != '' and row[9] != '' and row[10] != '' and row[13] != '' and row[14] != '' and row[15] != '' and row[16] != '' and row[17] != '' and row[18] != '':
			unit = row[2].split(',')[0].split(" ")[1]
			row[2] = unit
			cursor.execute('INSERT INTO STUDENTS VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)', row)
			
	con.commit()
	print "Data included in DB correctly"

"""
	Function to get the different skills of a String
"""	
def obtainSkills(skills):
	ret = []
	mySkills = skills.split("~~")
	for mySkill in mySkills:
		typeSkill = mySkill.find("[SkillRule: ")
		if typeSkill != -1:
			aux = mySkill.split(";")[0]
			ret.append(aux[12:])
		else:
			ret.append(mySkill)
	return ret

"""
	Function to calculate the different values of which the data card is composed
"""
def createDataCard(cursor):
	cursor.execute("SELECT ID_STUDENT, COUNT(DISTINCT(UNIT)), COUNT(DISTINCT(PROBLEM)), COUNT(STEP), SUM(CORRECT_FIRST_STEP), SUM(STEP_DURATION), SUM(HINTS) FROM STUDENTS GROUP BY ID_STUDENT")
	filename = "../../data/dataCard.txt"
	file_write = open(filename, 'w')
	students = []
	for i in cursor:
		student = [str(i[0]),str(i[1])]
		
		averageProblems = float(i[2]) / float(i[1])
		averageSteps = float(i[3]) / float(i[2])
		averageStepsCorrect = float(i[4]) / float(i[2])
		averageDuration = float(i[5]) / float(i[2])
		averageHints = float(i[6]) / float(i[2])
		percentStepsCorrect = (averageStepsCorrect * 100) / averageSteps
		
		student.append(str(averageProblems))
		student.append(str(averageSteps))
		student.append(str(percentStepsCorrect))
		student.append(str(averageDuration))
		student.append(str(averageHints))

		students.append(student)
	cont = 0
	bool = False
	boolproblem = False
	skillsProblems = []
	while cont < len(students):
		student = students[cont]
		cursor.execute("SELECT KC, PROBLEM FROM STUDENTS WHERE ID_STUDENT='"+student[0]+"'")
		skillsProblem = []
		problems = []
		# Loop to get the different skills per problem	
		for i in cursor:
			for problem in problems:
				if problem == i[1]:
					boolproblem = True
					index = problems.index(problem)
					skills = skillsProblem[index]
					newSkills = obtainSkills(str(i[0]))
					for newSkill in newSkills:
						for skill in skills:
							if newSkill == skill:
								bool = True
						if bool == False:
							skills.append(newSkill)
						else:
							bool = False
			if boolproblem == False:
				problems.append(i[1])
				skillsProblem.append([])
			else:
				boolproblem = False
		skills = 0
		for item in skillsProblem:
			skills += len(item)

		averageSkills = float(skills) / len(skillsProblem)
		student.append(str(averageSkills))
		if cont == len(students)-1 :
			file_write.write("\t".join(student))
		else: 
			file_write.write("\t".join(student)+"\n")
		cont += 1
	file_write.close()
	print "data card created correctly"
	return filename
	




























