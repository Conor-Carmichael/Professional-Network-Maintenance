# # Professional-Network-Maintenance

# Main Idea:

The idea behind the project, is that as one works in more and more places, their professional network will grow. As a consequence it becomes more dificult to stay in touch with everyone you would like to. This python projects aims to gently remind individuals of how long it has been since they have talked to their network, and send notifications (emails or texts) when it is a good time to reconnect with them and learn about what has been going on in their lives.

# Implementation:

The script brings the user through a series of initialization steps at first collecting information on the user and the contacts of which they would like to be reminded about. It stores this data in a folder called data/ which contains an excel spreadsheet of contact information, and a text file which allows for storage and retrieval of personal infomation. 

# Ideas to Further the Project:

Connecting with linkedin-
To ease the burden of the intialization, it would be great if it grabbed information of contacts from linked in, since most use that to aggregate their network.
User interface-
Since most of the time this project is meant to run in the background (after initialization it will only need to be opened to add/update contacts) I decided a terminal based script would be sufficient for now. It would be nice to create a UI through tkinter to make it overall more appealing.

# How to Use This Project yourself:

Download the code, store it in a place of your choice. Run the code for initializing with 'python Driver.py'. Enter 1 to go through initialization. Data will be store withing a directory data/ that will be made within the directory you place the rest of the code in. After setting everyting up, you can move to scheduling the emailing and (soon) texting.

How To Schedule:
For ubuntu (how I wrote it to work)- you can schedule it with cron, to run at a certain time each day. 
Step by step instructions:
1) open a terminal
2) 'crontab -e' this opens the crontab editing screen (crontab is a list of cronjobs, which are tasks scheduled to be run)
3) (Good reference to understand format of scheduling: http://www.adminschoice.com/crontab-quick-reference)
at the top of the window type->
'0 8 * * * cd path/to/where/scripts-are-downloaded && usr/bin/python /path/to-scripts/ScheduledTasks.py'
This will run the script at 8 am everyday. 'cd' to the files because the files are dependent on the relative paths of the files.

Windows instructions coming soon.
