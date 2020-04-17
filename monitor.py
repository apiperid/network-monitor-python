import speedtest
from datetime import datetime
import sys
import time
import csv
import visualize

def getStatistics():
	s = speedtest.Speedtest()
	s.get_servers()
	s.get_best_server()
	s.download()
	s.upload()
	res = s.results.dict()
	return res

if __name__ == "__main__":
	try:
		assert(len(sys.argv)==2)
		int(sys.argv[1])
	except AssertionError:
		print("Arguments must be 2\n1st Argument : .py script\n2nd Argument : sampling rate in seconds")
		sys.exit()
	except ValueError:
		print("Sampling rate MUST BE integer ONLY")
		sys.exit()
	filename = 'network-monitor-'+str(int(round(time.time()*1000,1)))+".csv"
	try:
		with open(filename, 'w', newline='') as file:
			writer = csv.writer(file)
			writer.writerow(["Sample", "Download", "Upload","Ping"])
			while True:
				now = datetime.now()
				dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
				print(f"Sample taken at : {dt_string}")
				statistics = getStatistics()
				writer.writerow([dt_string,round(statistics['download']/1000/1000,3),round(statistics['upload']/1000/1000,3),statistics['ping']])
				print(f"Download Speed : {round(statistics['download']/1000/1000,3)} Mbps\nUpload Speed : {round(statistics['upload']/1000/1000,3)} Mbps\nPing (optimal) : {statistics['ping']} ms\n\n")
				time.sleep(int(sys.argv[1]))
	except KeyboardInterrupt:
		print("Keyboard Interrupt Occured : Procedure is finished")
	except:
		print("An Error Occurred : Procedure is finished")
	finally:
		file.close()
		visualize.visualize(filename,sys.argv[1])