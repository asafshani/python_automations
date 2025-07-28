import shutil   # For checking disk usage
import smtplib  # For sending email via SMTP
from email.message import EmailMessage  # For formatting the email message
import getpass   # For secure password input without echoing to the terminal

# Function to check disk usage and compare it to the user-defined threshold
def check_disk_usage(path,threshold):
    total,used,free=shutil.disk_usage(path)
    percent_used = used / total * 100
    print(f"Disk usage on {path}: {percent_used:.2f}%")
    return percent_used>threshold

# Function to send an alert email if disk usage is above the threshold
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

# Prompt the user to enter disk path and threshold
path = input("Enter disk path to monitor (e.g. /): ")
threshold_input = input("Enter usage threshold (as a percentage): ")
threshold = float(threshold_input)  # Convert string to a float number

# Email setup: define sender address and securely read app password
email = "asafsenator@gmail.com"
app_password = getpass.getpass("Enter your Gmail App Password: ")


# Run disk check and send alert if usage exceeds threshold

if check_disk_usage(path, threshold):
    send_alert(email, app_password, path, threshold)



    
