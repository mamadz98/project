import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	password = "123",
	database = "members" )

mycursor = mydb.cursor()
#mycursor.execute("DROP TABLE students")
#mycursor.execute("DROP TABLE lessons")
#mycursor.execute("CREATE DATABASE members")
#mycursor.execute("CREATE TABLE students (num INTEGER(10),name VARCHAR(255),year INTEGER(10), field VARCHAR(255), user VARCHAR(255), pass VARCHAR(255))")
#mycursor.execute("CREATE TABLE dr (num INTEGER(10),name VARCHAR(255),year INTEGER(10), field VARCHAR(255), user VARCHAR(255), pass VARCHAR(255))")
#mycursor.execute("CREATE TABLE admin (num INTEGER(10),name VARCHAR(255),year INTEGER(10), field VARCHAR(255), user VARCHAR(255), pass VARCHAR(255))")
#mycursor.execute("CREATE TABLE rank (user VARCHAR(255), lesson VARCHAR(255), mark INTEGER(10))")
#mycursor.execute("CREATE TABLE lessons (leson VARCHAR(255), teacher VARCHAR(255))")
#mycursor.execute("CREATE TABLE waiting (user VARCHAR(255), confirmed VARCHAR(255))")
#sqlformula = "INSERT INTO students(num, name, year, field, user, pass) VALUES (%s, %s, %s, %s, %s, %s)"
#sqlformula2 = "INSERT INTO dr(num, name, year, field, user, pass) VALUES (%s, %s, %s, %s, %s, %s)"
#sqlformula3 = "INSERT INTO admin(num, name, year, field, user, pass) VALUES (%s, %s, %s, %s, %s, %s)"
#sqlformula4 = "INSERT INTO rank(user, lesson, mark) VALUES (%s, %s, %s)"
#sqlformula5 = "INSERT INTO lessons(leson, teacher) VALUES (%s, %s)"


students = [(1, "mahdi mazloum", 1397, "math", "mzlm","12345"),
	    (2, "ali mohammadpour", 1396, "statics", "sas", "asw1"),
	    (3, "masoud shohani", 1398, "math", "hmsj", "1235"),
	    (4, "hamed marvi", 1394, "cs", "hmdmr", "6789")]

lessons = [("analys", "asadi"),
	    ("bp", "kheradpishe"),
	    ("ap", "khorasani"),
	    ("farsi", "molayi"),
	    ("calcules", "rokni"), 
	    ("algebra", "derafshe"), 
	    ("diffrential", "khaje")]

masters = [(1, "x", 1397, "math", "mzlmw","1d2345"),
	    (2, "y", 1396, "statics", "ssas", "adsw1"),
	    (3, "z", 1398, "math", "hmsaj", "123d5"),
	    (4, "w", 1394, "cs", "hmdmar", "678f9")]
ranks = [("mzlm", "bp", 19),
	  ("sas", "bp", 14)]

admins =[(1, "yasemi", 1365, "sd", "12345785", "fsfsddf")]



#mycursor.executemany(sqlformula, students)
#mycursor.executemany(sqlformula2, masters)
#mycursor.execute(sqlformula3, admins[0])
#mycursor.executemany(sqlformula4, ranks)
#mycursor.executemany(sqlformula5, lessons)
mydb.commit()

#mycursor.execute("SHOW TABLES")

#for tb in mycursor:
#    print(tb)




