#Bulk Email Sender
print('''
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                                   This is a Bulk Email Sender.
                                   Use this to send emails in bulk.
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                                   
                                   ''')

#importing
try:
    import smtplib
    import time
    from email.message import EmailMessage
    print("All modules installed")
    print('Starting')
except:
    print("ERROR")
    print("Some of requried modules may not be present")
    print("Exiting")
    exit(0)

#Defining
def msg():
    while True:
        a = int(input('''
Do you have a msg file prepared or you want to create one??
1)  Create One
2)  Have One
>>>'''))
        if a==1:
            name = input('Enter Name Of File:')
            ms = input('Start Writing Your Msg Here:\n>>>')
            with open(name,'w+') as f:
                f.write(ms)
                f.close()
            print("File Created And Will Be Used For Now")
            return name
            break
        elif a==2:
            name = input('Enter Name Of File:')
            return name
            break
        else:
            print("Enter a valid arrgument")
def rec():
    while True:
        ask = int(input('''
Do you have a file with emails of all recievers or want to create one??
1)  Have One
2)  Create One
>>>'''))
        if ask==1:
            name=input("Enter name of file:")
            return name
            break
        elif ask==2:
            name=input("Enter name of file:")
            print("Press ctrl+C to stop")
            with open(name,'w+') as f:
                while True:
                    try:
                        f.write(input("Enter an email:"))
                        f.write('\n')
                    except:
                        f.close()
                        break
            return name
            break
        else:
            print('Enter a valid arrgument')
def send(a,b):
    with open(a) as fp:
    # Create a text/plain message
        msg = EmailMessage()
        msg.set_content(fp.read())
        fp.close()

    msg['Subject'] = input('Enter Subject of your mail:')
    mail = input('Enter Your Email Address:')
    msg['From'] = mail
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    passwd = input('Enter Your Password:')
    s.login(mail, passwd)
    with open(b) as f:
        x = f.read().splitlines()
        msg['To'] = x
        s.send_message(msg)
        print('Sent')
        s.quit()
#main_block
a = msg()
b = rec()
send(a,b)              

    
