import pytube
import os
import sys

RED = '\033[31m'
GREEN = '\033[32m'
CYAN = '\033[36m'
YEL = '\033[33m'
MAG = '\033[35m'
BOLD = '\033[1m'
STD = '\033[0m'

def header():
	os.system('clear')
	print(MAG)
	print("""                       
	      __       ___     
	     |  |\    /__/\    
	     |  |:|   \  \:\   
	     |  |:|    \__\:\  
	     |__|:|__  /  /::\ 
	     /  /::::\/  /:/\:\\
	    /  /:/~~~/  /:/__\/
	   /__/:/   /__/:/     
	   \__\/    \__\/      
                       """)

	print("	[+] Here is a simple youtube")
	print("	downloader.")
	print(f"	[+] Type {BOLD}{YEL}exit{STD}{MAG} to leave")
	print(f"	[+] Don't forget to paste yout link after {BOLD}{YEL}-->{STD}{MAG}")
	print("	[+] Please enjoy it")
	print(STD)


def progress_Check(chunk, file_handle, remaining):
	percent = (100 * (file_size - remaining)) / file_size
	print(f"\r	{GREEN}[+] " + "{:00.0f}% downloaded".format(percent), f"{STD}", end='')

def get_res(vid):
	data_vid = []
	res = []
	for stream in vid.streams.filter(progressive = True, file_extension = "mp4"):
		if "mp4" in str(stream):
			data_vid.append(list(str(stream).split(" ")))
			if data_vid[-1][3] not in ['res="1080p"', 'res="720p"', 'res="480p"', 'res="360p"', 'res="240p"', 'res="144p"']:
				data_vid.pop()
	for i, elem in enumerate(data_vid):
		print(f"	{CYAN}[{i}] {elem[3][5:-1]}{STD}")
		res.append([elem[1][6:-1], elem[3][5:-1]])
	choice = int(input(f"	[+]{YEL} Chose the quality {STD}: {YEL}"))
	print(STD, end='')
	return res[choice][0]

def yt_dl():
	url = input(f"{YEL}	--> ")
	if url == "exit":
		print("\n\n\n")
		exit(0)

	if url:
		try:
			vid = pytube.YouTube(url, on_progress_callback=progress_Check)
			itag = get_res(vid)
			stream = vid.streams.get_by_itag(itag)
			global file_size
			file_size = stream.filesize
			if stream:
				stream.download(filename=input(f"	[+] {YEL}Save name (without extension): {STD}"))
				print(f"\n	{GREEN}[+] Done{STD}\n")
				print(f"	{GREEN}[+] File saved at {YEL}{os.getcwd()}{STD}\n")
				choice = input(f"	Type {YEL}{BOLD}open{STD} to open the location else, type enter : ")
				if choice == "open" or choice == "Open":
					os.system('open . > /dev/null')
				print("\n\n\n")
		except Exception as error:
			print(f"{RED}	[-] Link doesn't work{STD}")
			yt_dl()
			
		return
	else:
		yt_dl()


header()
yt_dl()
