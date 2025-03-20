This Python script checks if your password has been compromised in data breaches using the Have I Been Pwned API. It securely hashes your password using SHA-1 and only sends the first five characters of the hash to the API, ensuring your full password is never exposed. The script retrieves a list of hash suffixes from the API and checks if your password’s suffix is among them. If found, it displays the number of times the password has appeared in data breaches, helping users determine whether they should change their password. It features a simple command-line interface and ensures security through the k-Anonymity model. To use the script, install the requests library, run python password_checker.py, and enter a password when prompted. If the password has been found in breaches, the script will warn you; otherwise, it will indicate that the password is safe to use. Since security is critical, it is always recommended to choose strong and unique passwords.





