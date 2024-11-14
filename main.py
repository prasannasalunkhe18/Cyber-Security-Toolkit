header = """   ______      __             ______            __
  / ____/_  __/ /_  ___  ____/_  __/___  ____  / /
 / /   / / / / __ \/ _ \/ ___// / / __ \/ __ \/ / 
/ /___/ /_/ / /_/ /  __/ /   / / / /_/ / /_/ / /  
\____/\__, /_.___/\___/_/   /_/  \____/\____/_/   
     /____/                                       """

print(header)
print('\n')
print("Welcome to CyberTool! What are you looking for?")
print('\n')
print("1. Website Vulnerability Scanner")
print("2. Image Steganography")
print("3. Dictionary Attack")
print('\n')
choice = input("Enter your choice: ")

if choice == "1":
    exec(open("webvulnscanner/WebVulnScanner.py").read())
elif choice == "2":
    exec(open("steganography/steganography.py").read())
elif choice == "3":
    exec(open("seltool/dict.py").read())
else:
    print("Invalid choice!")
