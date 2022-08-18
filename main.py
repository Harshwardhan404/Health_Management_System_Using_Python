# Health Management System
#  3 clients UserA , UserB and UserC
#  1 for UserA , 2 for UserB , 3 for UserC
#  4 for exercise , 5 for food
#  6 to Add data about User, 7 to View data about user
#  8,9,10 to view data about particular User

# f = open("UserA.txt", 'w')
# f.write("Exercise for UserA - \n")
# f.close()
# s = open("UserA1.txt", 'w')
# s.write("Food for UserA - \n")
# s.close()
# d = open("UserB.txt", 'w')
# d.write("Exercise for UserB - \n")
# d.close()
# r = open("UserB1.txt", 'w')
# r.write("Food for UserB - \n")
# r.close()
# m = open("UserC.txt", 'w')
# m.write("Exercise for UserC - \n")
# m.close()
# n = open("UserC1.txt", 'w')
# n.write("Food for UserC - \n")
# n.close()


def getdate():
    import datetime
    return datetime.datetime.now()


name = int(input("For UserA enter 1 for UserB enter 2 for UserC 3 - "))

addUserdata = int(
    input("Press 6 to add data about user and press 7 to view data about user - "))

work = ""

if addUserdata == 6:
    work = int(
        input("For Exercise enter 4 and for food enter 5 - "))


def readUserdData(a, b):

  if a == 7:
    if b == 8:
      fileH = open("UserA.txt")
      fileH2 = open("UserA1.txt")
      read1 = fileH.read()
      read2 = fileH2.read()
      print("The Data for UserA is as follows - \n ", read1 + "\n" + read2)

    elif b == 9:
      FileR = open("UserB.txt")
      FileR2 = open("UserB1.txt")
      Read1 = FileR.read()
      Read2 = FileR2.read()
      print("The Data for UserB is as follows - \n ", Read1 + "\n" + Read2)

    elif b == 10:
      FileH = open("UserB.txt")
      FileH2 = open("UserB1.txt")
      Read3 = FileH.read()
      Read4 = FileH2.read()
      print("The Data for UserC is as follows - \n ", Read3 + "\n" + Read4)

    else:
      print("Wrong Input")

  else:
    print("Wrong Input")




def addData(x, y):
  
  readuserdata = ""

  if addUserdata == 6:
      if x == 1 and y == 4:
          fileopen1 = open("UserA.txt", "a",)
          fileopen1.write(
              str(getdate()) + "\t" + input("Write the exercises for UserA  - "))
          fileopen1.write("\n")
          print(getdate(), "Added Succesfully")
          fileopen1.close()

      elif x == 1 and y == 5:
          fileopen2 = open("UserA1.txt", "a")
          fileopen2.write("\n")
          fileopen2.write(
              str(getdate()) + "\t" + input("Write the Food for UserA - "))
          print(getdate(), "Added Succesfully")
          fileopen2.close()

      elif x == 2 and y == 4:
          fileopen3 = open("UserB.txt", "a")
          fileopen3.write("\n")
          fileopen3.write(
              str(getdate()) + "\t" + input("Write the exercises for UserB  - "))
          fileopen3.write("\n")
          print(getdate(), "Added Succesfully")
          fileopen3.close()

      elif x == 2 and y == 5:
          fileopen4 = open("UserB1.txt", "a")
          fileopen4.write("\n")
          fileopen4.write(
              str(getdate()) + "\t" + input("Write the Food for UserB - "))
          print(getdate(), "Added Succesfully")
          fileopen4.close()

      elif x == 3 and y == 4:
          fileopen5 = open("UserC.txt", "a")
          fileopen5.write("\n")
          fileopen5.write(
              str(getdate()) + "\t" + input("Write the exercises for UserC  - "))
          print(getdate(), "Added Succesfully")
          fileopen5.close()

      elif x == 3 and y == 5:
          fileopen6 = open("UserC1.txt", "a")
          fileopen6.write("\n")
          fileopen6.write(
              str(getdate()) + "\t" + input("Write the Food for UserC - "))
          print(getdate(), "Added Succesfully")
          fileopen6.close()

      else:
          print("Wrong Input")
  elif addUserdata == 7:
    readuserdata = int(input(
        "To read UserA's Exercise and Food press - 8 for UserB Press - 9 for UserC press 10 - "))

    readUserdData(addUserdata, readuserdata)

    return


addData(name, work)
