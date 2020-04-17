# network-monitor-python
This repository allows you to measure your **download speed , upload speed and your ping**.  
The steps followed are:
* Find server based on best ping in ms
* Measure download speed in Mbps
* Measure upload speed in Mbps

You can set a sampling rate as argument , so you will monitor your network until you stop the procedure (Crtl+C).
All data will be saved to a csv file.
When the procedure is stopped , a diagram will be exported visualizing all data from the csv created.

# Arguments

Run the script as followed:  
`python monitor.py sampling_rate`  

**sampling_rate** : an integer number which represents how often you want to take samples of your network (in seconds)

# Output

The **first output** of this script is a csv file containing four columns with names ['Sample','Download','Upload','Ping'].\
The "Sample" column will contain the timestamp of each sample (e.g 14/04/2020 22:20:40)\
The "Download" column will contain the download speed in Mbps\
The "Upload" column will contain the upload speed in Mbps\
The "Ping" column will contain the best ping in ms

The **second output** is an .png image with dpi=300 which contains two diagrams , the first will show the download and upload speed and the second will show the ping

# Example
Here i give you an example of excecuting the scripts.<br>
The followed image shows you how to run the monitor.py from cmd.<br>
![shell](/example/shell.png)
When you want to stop the procedure just press Ctrl+C.<br>
After this the script visualize.py will take action and show you the results from the csv
![visualize](/example/network-monitor-14_04_2020.png)
### Note!!!!!!!
The images are not from the same experiment , they exist only for display purposes
