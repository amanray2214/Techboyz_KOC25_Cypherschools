print("note that the format of the date should be = DD/MM/YYYY")
print("Please enter your date of birth")
dob = input("Date of birth")
print("Please enter date of present day")
pday = input("Present day")
x = 365 *(int(pday[6:10]) - int(dob[6:10]))
y = 31 * (int(pday[3:5]) - int(dob[3:5])) - 4 * (int(pday[3:5]) - int (dob[3:5]))
z = int(pday[0:2]) - int(dob[0:2])+4
print("Total number of days you survived in the world are: " , str(x + y + z)+"days" )