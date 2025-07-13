import shutil   
import smtplib
from email.message import EmailMessage
import getpass


def check_disk_usage(path,threshold):
    total,used,free=shutil.disk_usage(path)
    percent_used = used / total * 100
    print(f"Disk usage on {path}: {percent_used:.2f}%")
    return percent_used>threshold


def send_alert(email_to,app_password,path, threshold):
    message=f"Disk usage on '{path}' exceeded {threshold}%!"
    email=EmailMessage()
    email.set_content(message)
    email["Subject"]="Disk Usage Alert"
    email["From"]=email_to
    email["To"]=email_to
    
    smtp=smtplib.SMTP("smtp.gmail.com",587)
    smtp.starttls()
    smtp.login(email_to, app_password)
    smtp.send_message(email)
    smtp.quit()

path = input("Enter disk path to monitor (e.g. /): ")
threshold_input = input("Enter usage threshold (as a percentage): ")
threshold = float(threshold_input)  # Convert string to a float number

email = "asafsenator@gmail.com"
app_password = getpass.getpass("Enter your Gmail App Password: ")



if check_disk_usage(path, threshold):
    send_alert(email, app_password, path, threshold)



    