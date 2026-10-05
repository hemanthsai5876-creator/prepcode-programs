blocked_usernames=["sai","kalyan","sri"]
username=input("enter the username:")
if username not in blocked_usernames:
    print("valid username")
else:
    print("invalid username")