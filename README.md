Security Toolkit based on python. Tools included:

Website Vulnerability Scanner
Password De-hash
Image Steganography.
#Modules and Libraries Used The Cybersecurity Toolkit utilizes the following modules and libraries:

Requests: A Python HTTP library used for making HTTP requests to websites. BeautifulSoup: A library for parsing HTML and XML documents, used for web scraping and HTML manipulation. tqdm: A library for creating progress bars to track the progress of a task. PIL (Python Imaging Library): A library for image processing that enables image manipulation and analysis. os: A module providing a way to interact with the operating system, used for file handling. hashlib: A module providing various hashing algorithms, used for hashing and dehashing passwords.

#Program Descriptions #1. Website Vulnerability Scanner The Website Vulnerability Scanner aims to identify vulnerabilities in a given website. It performs two types of checks: Cross-Site Scripting (XSS) and SQL injection. Here's how it works:

The user provides the target website URL. The scanner sends a GET request to the target URL and receives the response. It parses the HTML code of the response using BeautifulSoup. For XSS vulnerabilities, the scanner injects a malicious JavaScript code into each input field and checks if the code is executed. For SQL injection vulnerabilities, the scanner injects a SQL command into each input field and checks if an error message is returned. The vulnerabilities detected are displayed to the user, specifying the vulnerability type and the vulnerable input field(s).

#2. Image Steganography The Image Steganography program allows users to hide a secret message within an image. The hidden message can later be retrieved from the modified image. Here's a brief overview of its functionality:

The user provides the path to the image where the message will be hidden. The user enters the message they want to hide. The program converts the message to binary and ensures it can fit within the image. Each pixel in the image is processed, and the least significant bit of the RGB channels is replaced with the message bits. The modified image with the hidden message is saved as a new image. The user can later retrieve the hidden message from the modified image using the same program.

#3. Dictionary Attack The Dictionary Attack program helps in cracking hashed passwords by comparing them to a dictionary of commonly used words. Here's how it operates:

The user provides a target hash value and the path to a dictionary file. The program reads the words from the dictionary file. Each word is hashed using the SHA-1 algorithm. The hashed word is compared to the target hash value. If a match is found, the password is returned. If no match is found, the program notifies the user that the password was not found in the dictionary.

#Documentation For detailed documentation and instructions on how to use each program in the Cybersecurity Toolkit, please refer to the respective files:

webvulnscanner/WebVulnScanner.py for the Website Vulnerability Scanner. steganography/steganography.py for the Image Steganography program. seltool/dict.py for the Dictionary Attack program. Make sure to install the required libraries by running pip install -r requirements.txt before executing the programs.

Feel free to explore the source code and customize the programs according to your needs. Stay vigilant and protect against potential vulnerabilities with this Cybersecurity Toolkit.
