# Keep Drives Alive
A little Python program to keep your external drives awake instead of falling to sleep. Wake up lazy bones!

To run the program you'll need Python installed. If you don't have it, download from http://www.python.org.

When ready add your drive letters to the "drives" array. By default there are two drives. Add a third like so:
drives = ['D', 'E', 'F']

Or just a single drive like so:
drives = ['D']

The program works by writing a file to each drive and changing the files contents at a set interval. The interval is set to 30 seconds by default. To make the interval longer or shorter, change the "sleepInterval" variable to the number of seconds you'd like to wait before writing to the drive again.

The program writes to a file titled ___kda___. It is unlikely you have this file on your drive but, if you do, you may want to update the filename to something else. Do this by changing the "writeFile" variable to anything you'd like.

When you're ready to go, double click on the file and a console window will pop up to run the program. When you're done, close the window.

## Please Note
This program has not been tested on a Mac. If you try it and have issues, let me know and I'll adjust to make it Mac friendly.