import sys,time
#sys.stdout = open("goat.txt", "w")

# Time stamp fort he new log file
timestr = time.strftime("%Y%m%d_%H%M%S")
# Create log file
fileName =  "".join((timestr,"_info.log"))
print(fileName)
file = open(fileName, "w")
sys.stdout = file
print ("test sys.stdout")
