import subprocess, webbrowser

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
    
