import sys
import requests
import hashlib
import os


def request_api_data(first_5_char_hashed_password):
    '''requesting the data from the api'''
    url = "https://api.pwnedpasswords.com/range/" + first_5_char_hashed_password
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f"Error fetching the data, Response code : {response.status_code}. Check the api and try again later")
    return response


def check_my_password_pwned_count(response_from_api, our_hashed_password_suffix):
    '''Cheking if password has ever been pwned or hacked and returning the count'''
    password_tuple = (line.split(":")
                      for line in response_from_api.text.splitlines())
    for suffix, count in password_tuple:
        if suffix == our_hashed_password_suffix:
            return count
    return 0


def check_my_password(password):
    '''hashes the password and checks if the password is present in the api reponse'''
    sha1_hashed_password = hashlib.sha1(
        password.encode('utf-8')).hexdigest().upper()
    first_5_char = sha1_hashed_password[:5]
    suffix = sha1_hashed_password[5:]
    response = request_api_data(first_5_char)
    return check_my_password_pwned_count(response, suffix)


def main_user_input():
    '''Call this function if you want to manually give the password as input'''
    while(True):
        print("Enter to \"-1\" Exit")
        print("Enter the password you want to check")
        try:
            password = input().strip()
        except:
            print("You must enter a string")
            continue
        if(password == "-1"):
            break
        count = check_my_password(password)
        if count:
            print(
                f"The password {password} has been seen {count} times... You should probably change your password!")
        else:
            print(
                f"The password {password} has not been seen before... You can choose this password ")
    return "Done!"

main_user_input()

