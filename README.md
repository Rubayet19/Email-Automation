# Password Checker

## Introduction
The Password Checker is a Python tool designed to help users determine if their passwords have been exposed in data breaches. By leveraging the "Have I Been Pwned" API, this tool allows individuals to check if their passwords are secure or need changing. This project aims to enhance online security and awareness by providing an easy-to-use interface for password vulnerability checks.

## Features
- Utilizes the "Have I Been Pwned" API to check password security.
- Securely checks passwords without sending the complete password over the network.
- Simple and straightforward CLI interface for easy use.

## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.7 installed on your machine
- `requests` library installed in your Python environment

## Usage
To use the Password Checker, follow these steps:

Clone this repository to your local machine.
Navigate to the directory containing the script.
Run the script followed by the passwords you wish to check as arguments. For example:
bash
Copy code
python password_checker.py password1 password2 password3
Replace password1 password2 password3 with the actual passwords you want to check.

## How It Works
The Password Checker works by converting the input password into a SHA-1 hash. This hash is partially sent to the "Have I Been Pwned" API to check if it's been part of known data breaches. The tool then reports back on the security of the password without ever exposing the actual password.

## Contributing
Contributions to the Password Checker project are welcome! If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

Please ensure your pull request adheres to the following guidelines:

Non-trivial changes should be discussed in an issue first
Update the README.md with details of changes to the interface, if applicable
