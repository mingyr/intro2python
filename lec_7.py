import re

try:
    email_ptn = r"^([\da-zA-Z\-_\.]+)@([\da-zA-Z\-_\.]+)$"
    email_ptn = re.compile(email_ptn)

    domain_ptn = r"[\da-z]+\.(ac|edu)\.[a-z]{2}$"
    domain_ptn = re.compile(domain_ptn)
except:
    print("double check your regular expression")
    exit
    
while True:
    email = input("\nPlease input your email address, or q to quit:")
    if email == 'q':
        break
    
    match = re.search(email_ptn, email)
    if match == None:
        continue
    
    user = match.groups()[0]
    domain = match.groups()[1]
    
    match = re.search(domain_ptn, domain)
    if match:
        print(f"Hello {user}, you are qualified for a student discount")
    else:
        print(f"Hello {user}, you are not qualified for a student discount")