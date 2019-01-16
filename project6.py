
import random
fileExtension = ".cmt"

def main():
    user = 0
    while True:
        print("1) Import, Clean and Convert File")
        print("2) Create a New File From Scratch")
        print("3) Search Player Stats")
        print("4) Quit\n")
        try:
            user = int(input("Enter Choice: "))
        except ValueError:
            print("Must enter a number")
        else:
            if user == 1:
                fileName = input("Enter a file name: ")
                data = readIn(fileName)
                newData = dataProcess(data)
                writeOut(newData)
                input("Press any key to return to the menu.\n")
            elif user == 2:
                fileName = input("Enter a file name: ")
                inputTeam(fileName)
            elif user == 3:
                fileName = input("Enter a file name: ")
                searchPlayer(fileName)
            elif user == 4:
                break
            else:
                print("Error - enter a valid choice\n")
        

def searchPlayer(fileName):
    playerid = input("Enter a Player ID: ")
    try:
        fr = open(fileName, 'r')
    except FileNotFoundError:
        print("File Not Found\n")
    else:
        repeat = True
        line = [' ']
        while repeat and line != '':
            line = fr.readline()
            if playerid in line:
                repeat = False
            else:
                repeat = True
        outputData(line)

def outputData(line):
    if line == '':
        print("Player not found\n")
    else:
        line = line.split('","')
        line[0] = line[0].lstrip('"')
        avg = int(line[4]) / int(line[2])
        avg = format(avg, '.3f')
        avg = avg.lstrip('0')
        print()
        print("Name:", line[0])
        print("Hits:", line[4])
        print("At Bats:", line[2])
        print("Average:", avg)
        print()


def inputTeam(fileName):
    fw = open(fileName + fileExtension, 'a') 
    repeat = True
    while repeat:
        header = ["the player's name", "G", "AB", "PA", "H", "1B", "2B", "3B", "HR",
                  "R", "RBI", "BB", "SO"]
        loop = []
        for x in header:
            stuff = input("Enter " + x + ": ")
            loop.append(stuff)
        playerID = random.randint(20000, 25000)
        loop.append(str(playerID))
        print("The Player ID is", playerID)
        
        try:
            avg = (format((int(loop[4]) / int(loop[2])), '.3f'))
        except ValueError:
            print("Value Error - Input Data Again\n")
        except ZeroDivisionError:
            print("Zero Division Error - Input Data Again\n")
        else:
            avg = avg.lstrip('0')
            loop.append(str(avg))
            string = ' '.join(loop)
            fw.write(string)
            fw.write('\n')
            user = input("Would you like to enter another player? y/n: ")
            if user == 'y' or user == 'Y':
                repeat = True
            else:
                repeat = False
    fw.close()
        

def readIn(fileName):
    data = []
    try:
        fr = open(fileName, 'r')
    except FileNotFoundError:
        print("File was not found.")
    else:
        line = fr.readline()
        line = fr.readline()
        while line != '':
            line = line.rstrip('\n')
            data.append(line)
            line = fr.readline()
        fr.close()
    return data


def dataProcess(oldData):
    newData = []
    index = 0
    for lines in oldData:
        line = oldData[index]
        line = line.split('","')
        try:
            avg = int(line[4]) / int(line[2])
        except ZeroDivisionError:
            avg = 0
        except ValueError:
            print("Value Error. Check original file.")
            break
    
        avg = (format(avg, '.3f'))
        avg = avg.lstrip('0')
        line[0] = line[0].lstrip('"')
        line[13] = line[13].rstrip('"')
        line.append(str(avg))
        newData.append(line)
        index = index + 1
    return newData


def writeOut(data):
    index = 0
    fw = open('kcStats.cmt', 'w')
    fw.write("Name G AB PA H 1B 2B 3B HR R RBI BB SO playerid AVG\n")
    for lines in data:
        line = data[index]
        string = ' '.join(line)
        fw.write(string)
        fw.write('\n')
        index += 1
    fw.close()



main()
