import subprocess, os , time, sys, time, argparse

# Instantiate the parser
parser = argparse.ArgumentParser(description='Cron job to handle the LCM for the data in the stagging area')

# Required path argument
parser.add_argument('path', type=str,
                    help='A required str argument for path.')

# Optional positional argument
parser.add_argument('dataType', type=str,
                    help='A required str argument for type(file/directory).')

# Optional argument
parser.add_argument('ageOfData', type=int,
                    help='A required int argument that represents the age of the data that needs to be deleted. It shall be mroe than 10 days old.')

args = parser.parse_args()

if args.ageOfData < 10:
    parser.error("You are not allow to remove the data whose age is less than 10 days")

#dirPath = raw_input("Enter the path of your file: ")
user_args = sys.argv[1:]
dirPath, dataType, ageOfTheFile = user_args

# Time stamp fort he new log file
timestr = time.strftime("%Y%m%d_%H%M%S")

# Create log file
fileName =  "".join((timestr,"_info.log"))
print(fileName)
file = open(fileName, "w+")
sys.stdout = file

if os.path.isdir(dirPath):
        # The timestamp with folder last modified
        print("last modified: %s" % time.ctime(os.path.getmtime(dirPath)))

        # Print the command that has been executed
        print("find", dirPath, "-type", dataType, "-mtime", ageOfTheFile)

        #subprocess.call(["find", str(dirPath), "-type", type, "-mtime +", ageOfTheFile])
        # list the file older than X days and save in the file
        subprocess.call(["find", dirPath, "-type", dataType, "-mtime",ageOfTheFile,], stdout=file)

        # Delete the files that are X days old
        subprocess.call(["find", dirPath, "-type", dataType, "-mtime", ageOfTheFile, "-delete" ], stdout=file)

else:
    print("Directory not exists.")

file.close()


#find /tmp/* -mtime +7 -exec rm {} \;
#find /tmp/*/* -mtime +7 -type d -exec rmdir {} \;
#find /tmp/* -mtime +7 -exec rm -rf {} \;
#find /tmp/* -daystart -mtime +7 -delete
