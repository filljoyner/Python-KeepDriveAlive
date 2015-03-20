from time import sleep, gmtime, strftime

drives = ['D', 'E']


def writeFile(_drives):
	filename = '___kda___.txt'
	strToWrite = strftime('%Y-%m-%d %H:%M:%S', gmtime())

	print('---')

	for d in drives:
		filepath = d + ':/' + filename

		try:
			_file = open(filepath, 'w+')
			_file.write(strToWrite)
			_file.close()

			print(d + ' | ' + strToWrite)
		except:
			print(d + ' | ' + strToWrite + ' UNAVAILABLE')


if __name__=="__main__":
	while True:
		writeFile(drives)
		sleep(30)