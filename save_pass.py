import pickle, base64, sys, getpass

def main():
    password = getpass.getpass("Password:")
    password = base64.b64encode(password.encode())

    with open('creds.bin', 'wb') as writefile:
        creds = (password)
        pickle.dump(creds, writefile)

if __name__== '__main__':
    main()