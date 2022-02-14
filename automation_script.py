import subprocess, webbrowser, os

# Writing routine for macOS
def writing_macOS():
    subprocess.run(['open', '/System/Applications/Mail.app'], check = True)
    subprocess.run(['open', '/Applications/UlyssesMac.app'], check = True)
    subprocess.run(['open', '/Applications/Obsidian.app'], check = True)
    subprocess.run(['open', '/System/Applications/Music.app'], check = True)
    webbrowser.open("http://google.de")
    webbrowser.open("http://app.grammarly.com")
    webbrowser.open("http://medium.com")

# Writing routine for Windows
def writing_Windows():
    os.system('open', 'C:/Programme/Outlook/Outlook.exe')   # Path only obligatory

# Writing routine for Linux
def writing_Linux():
    # open iTunes
    # open Joplin
    # open email
    # open Firefox with Google, Grammarly, Medium

# Coding routine for macOS
def coding_macOS():
    subprocess.run(['open', '/System/Applications/Mail.app'], check = True)
    subprocess.run(['open', '/Applications/Visual\Studio\Code.app'], check = True)
    subprocess.run(['open', '/System/Applications/Music.app'], check = True)
    webbrowser.open('https://github.com')
    webbrowser.open('https://google.de')
    webbrowser.open('https://stackoverflow.com')
    subprocess.run(['open', '/System/Applications/Utilities/Terminal.app'], check = True)

# Coding routine for Windows
def coding_Windows():

# Coding routine for Linux
def coding_Linux():

# Working routine for macOS
def working_macOS():
    # open Outlook
    # open Safari with Google, Matlab
    webbrowser.open('https://google.de')
    webbrowser.open('https://matlab.com')
    # open Obsidian
    subprocess.run(['open', '/Applications/Obsidian.app'], check = True)
    # open Matlab
    # open Finder where the Matlab-Script is at
    # execute a git pull command to get the latest code from GitHub

# Working routine for Windows
def working_Windows():

# Working routine for Linux
def working_Linux():

work_type = input('Do you want to "write", "code", or "work"?: ')
os = input('Are you working on "Linux", "macOS", or "Windows"?: ')

if (work_type == 'write' and os == 'macOS'):
    writing_macOS()

elif (work_type == 'write' and os == 'Windows'):
    writing_Windows()

elif (work_type == 'write' and os == 'Linux'):
    writing_Linux()

elif (work_type == 'code' and os == 'macOS'):
    coding_macOS()

elif (work_type == 'code' and os == 'Windows'):
    coding_Windows()

elif (work_type == 'code' and os == 'Linux'):
    coding_Linux()

elif (work_type == 'work' and os == 'macOS'):
    working_macOS()

elif (work_type == 'work' and os == 'Windows'):
    working_Windows()

elif (work_type == 'work' and os == 'Linux'):
    working_Linux()
