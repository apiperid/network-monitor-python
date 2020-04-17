import pandas as pd
import matplotlib.pyplot as plt
import statistics
import numpy as np

def visualize(csv_file,sampling_rate):
	#print(f"Reading : {csv_file}")
	my_csv = pd.read_csv(csv_file)
	download = my_csv.Download
	upload = my_csv.Upload
	ping = my_csv.Ping
	samples = len(ping)
	period = f"({my_csv.Sample[0]} - {my_csv.Sample[len(ping)-1]})"
	try:
		max_speed = int(float(input("Insert your Subscribers line maximum speed (Mbps):\n")))
		if(max_speed<=0):
			raise ValueError
		#print(max_speed)
		max_speed_vector = np.ones(samples)*max_speed
		half_max_speed_vector = max_speed_vector/2 
		# begin plots
		plt.subplot(211)
		plt.plot(download,label="Download Speed (Mbps)")
		plt.plot(upload,label="Upload Speed (Mbps)")
		plt.plot(max_speed_vector,label=f"Max Speed ({max_speed} Mbps)")
		plt.plot(half_max_speed_vector,label=f"Half of Max Speed ({round(max_speed/2,2)} Mbps)")
		plt.title(f"{period}\nThroughput measured with sampling rate = {sampling_rate}s\nAverage Download Speed = {round(statistics.mean(download),2)} Mbps , Average Upload Speed = {round(statistics.mean(upload),2)} Mbps")
		plt.grid()
		plt.xlabel('Sample')
		plt.ylabel('Mbps')
		plt.ylim(0,max_speed+1)
		plt.legend(loc=1)

		plt.subplot(212)
		plt.plot(ping,label="Ping (ms)")
		plt.legend()
		plt.grid()
		plt.title(f"{period}\nPing measured with sampling rate = {sampling_rate}s\nAverage Ping = {round(statistics.mean(ping),2)} ms")
		plt.xlabel('Sample')
		plt.ylabel('milliseconds')
		plt.tight_layout()

		figure = plt.gcf()  # get current figure
		figure.set_size_inches(12,6) # 
		plt.savefig(csv_file+".png", bbox_inches='tight',dpi=300) # bbox_inches removes extra white spaces

		plt.show()
	except ValueError:
		print("The value inserted was not a number or it was not positive number... so the plots will contain only data from the csv file")
		# begin plots
		plt.subplot(211)
		plt.plot(download,label="Download Speed (Mbps)")
		plt.plot(upload,label="Upload Speed (Mbps)")
		plt.title(f"{period}\nThroughput measured with sampling rate = {sampling_rate}s\nAverage Download Speed = {round(statistics.mean(download),2)} Mbps , Average Upload Speed = {round(statistics.mean(upload),2)} Mbps")
		plt.grid()
		plt.xlabel('Sample')
		plt.ylabel('Mbps')
		plt.legend(loc=1)

		plt.subplot(212)
		plt.plot(ping,label="Ping (ms)")
		plt.legend()
		plt.grid()
		plt.title(f"{period}\nPing measured with sampling rate = {sampling_rate}s\nAverage Ping = {round(statistics.mean(ping),2)} ms")
		plt.xlabel('Sample')
		plt.ylabel('milliseconds')
		plt.tight_layout()

		figure = plt.gcf()  # get current figure
		figure.set_size_inches(12,6) # 
		plt.savefig(csv_file+".png", bbox_inches='tight',dpi=300) # bbox_inches removes extra white spaces

		plt.show()