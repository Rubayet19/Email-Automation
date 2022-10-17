import requests 
import hashlib
import sys

def check_pwned_api(query):
    url='https://api.pwnedpasswords.com/range/' + 'CBFDA'
    res=requests.get(url)
    if res.status_code!=200:
        raise RuntimeError(f'Error fetching{res.status_code}. Please try again')
    return res

def get_pass_leaks_count(hashes,myhash):
    hashes=(lines.split(':') for lines in hashes.splitlines())
    for h,count in hashes:
        if h==myhash:
            return count
    return 0

def check_pass(password):
    sha1pass=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail=sha1pass[:5],sha1pass[5:]
    response=check_pwned_api(first5_char)
    get_pass_leaks_count(response,tail)
    
    return response

def main(args):
    for password in args:
        count=check_pass(password)
        if count:
            print(f'{password} was found {count} times. You should probably change your password!')
        else:
            print(f"{password} was not found. Carry on!")
    return 'Done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))





 