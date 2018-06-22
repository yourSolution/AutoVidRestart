
This is a Star Wars Jedi Knight:Jedi Academy Speedrun Tool - https://www.speedrun.com/jka

In hopes of finding a solution to the constant memory leaks in JKA, I wrote this tool to be a LEGAL tool for speedrunners to use. Other people in the JKA speedrunning community have put together tools that change, inject, read/write, the game's source code , however have all be deemed illegal for submitted runs.
This tool simply reads how many times you use your load key and at a certain amount, which the user sets, presses the vid_restart key. 

When downloaded simply change config.py to your load button that you use, your vid restart button you use, and what amount of loads your computer can take before you crash. 

Steps:
	1. Download repo and unzip it. Save it somewhere you can find it. 
	2. Open config.py with notepad++ or any other code editor and change values to fit your needs.
	3. Set your keys and load amount.
		a. If you use mouse buttons for save/load go into your mouse profiles and save your mouse buttons to use other keys on the keyboard. Like so, https://gyazo.com/2a9fd1bb403445940a31c746a822ca79 .
	4.When you are ready to go, simply launch __main__.pyw and it should work. If you want to end the script hit your closeService button to end it. 
		a. OPTIONAL (Also Reccomended)  - Creat Shortcut with .bat file 
			1. Create JKA shortcut
			2. In a text file, 
				--- Start of text contents ----
				@echo
				start "" "path to jasp.exe""
				start "" "path to __main__.pyw"
				---End of text contents ----
			3. Save file as file.bat
			4. Right Click your JKA short cut 
			5. Under Target put path to file.bat 



Thank you! You can contact me on discord ( Your Solution) or at ryan.phillips.j@gmail.com.
			


