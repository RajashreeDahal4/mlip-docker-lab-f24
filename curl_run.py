import subprocess

# Define the curl command as a list
curl_command = [
    "curl.exe", 
    "--location", 
    "--request", "POST", 
    "http://localhost:8080/predict", 
    "--header", "Content-Type: application/json", 
    "--data", "{\"input\": [6.3, 3.3, 6, 2.5]}"
]

# Run the curl command using subprocess
response = subprocess.run(curl_command, capture_output=True, text=True)

# Print the response
print(response.stdout)
