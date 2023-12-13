
class Patient():
  
  def __init__(self, ID,fName,lName, sex, age, lineNum, phoneNum, symptoms,emergency,location):
    self.ID = ID
    self.firstName = fName
    self.lastName = lName
    self.age = age
    self.sex = sex
    self.lineNum = lineNum
    self.phoneNum = phoneNum
    self.symptoms = symptoms
    self.emergencyLevel = emergency
    self.location = location

  def toString(self):
    return "ID: " + str(self.ID) + "\n" + "First Name: " + str(self.firstName) + "\t" + "Last Name: " + str(self.lastName) + "\t" + "Age: " + str(self.age) + "\t" + "Sex: " + str(self.sex) + "\t" + "Line Number: " + str(self.lineNum) + "\n" + "Phone Number: " + str(self.phoneNum) + "\n" + "Symptoms: " + str(self.symptoms) + "\n" + "Emergency Level: " + str(self.emergencyLevel) + "\n" + "Location: " + str(self.location) + "\n"

  #Getters
  def getID(self):
    return self.ID

  def getFirstName(self):
    return self.firstName

  def getLastName(self):
    return self.lastName

  def getAge(self):
    return self.age

  def getSex(self):
    return self.sex

  def getLineNum(self):
    return self.lineNum

  def getPhoneNum(self):
    return self.phoneNum

  def getSymptoms(self):
    return self.emergencyLevel

  def getLocation(self):
    return self.location

  #Setters

  def setID(self, ID):
    self.ID = ID

  def setFirstName(self, fName):
    self.firstName = fName

  def setLastName(self,lName):
    self.lastName = lName

  def setAge(self, age):
    self.age = age

  def setSex(self, sex):
    self.sex = sex

  def setLineNum(self, lineNum):
    self.lineNum = lineNum

  def setPhoneNum(self, phoneNum):
    self.phoneNum = phoneNum

  def setSymptoms(self, symptoms):
    self.symptoms = symptoms

  def setLocation(self,location):
    self.location = location

userData = open("user.dat", "r")

userList = []
aList = []
while True:
  lines = userData.readline()

  if lines == "":
    break

  aList = lines.split("/")
  userList.append(Patient(aList[0],aList[1],aList[2],aList[3],aList[4],aList[5],aList[6],aList[7],aList[8], aList[9]))

userData.close()

print(userList[0].toString())

roomCount = [0,0,0,0]
for i in range(len(userList)):

  if userList[i].getLocation() == "1":
    roomCount[0] += 1
  elif userList[i].getLocation() == "2":
    roomCount[1] += 1
  elif userList[i].getLocation() == "3":
    roomCount[2] += 1
  elif userList[i].getLocation() == "4":
    roomCount[3] += 1
