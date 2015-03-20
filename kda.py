# NOTE - has not been tested on a Mac

# add your drive letters in this array
drives = ['D', 'E']

# the number of seconds you'd like to wait before calling the drive
sleepInterval = 30

# this is the file the program will write at ever interval
# make sure you don't have a file of the same name on your drive and,
# if you do, rename this file below. you can delete the file when 
# you're done using the program
fileToWrite = '___kda___'


# ----------------------------------------------------------------------------
# All the boring stuff happens below here. Just edit the drives and
# sleepInterval values above unless you want to tweak the program.
# ----------------------------------------------------------------------------

# import modules
from time import sleep, gmtime, strftime


# this function writes the current time to a file titled ___kda___.txt
# to each drive in the drives array at the interval you select 
def writeFile(drives, writeFile):
	filename = fileToWrite

	strToWrite = strftime('%Y-%m-%d %H:%M:%S', gmtime())

	print('------------------------')

	for d in drives:
		filepath = d + ':/' + filename

		try:
			_file = open(filepath, 'w+')
			_file.write(strToWrite)
			_file.close()

			print(d + ' | ' + strToWrite)
		except:
			print(d + ' | ' + strToWrite + ' UNAVAILABLE')


# run the program and keep it alive to end, press ctrl+x (PC) or
# cmd+x (Mac), or just close the console window.
if __name__=="__main__":
	while True:
		writeFile(drives, fileToWrite)
		sleep(sleepInterval)