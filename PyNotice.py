import smtplib, os
from datetime import datetime
from dotenv import dotenv_values
from tkinter import messagebox

config = dotenv_values('config.env.secret') # This line is responsible for restoring environment values
datenow = datetime.now()
dt = datenow.strftime("%Y-%m-%d %H:%M:%S")


class email:
    def __init__(self, email):
        self.email = email

    def verify_gmail(self):
        return self.email.endswith(("@gmail.com", "@icloud.com"))
    
    def send_email(self):
        if self.verify_gmail():
            try:
                server = smtplib.SMTP("smtp.gmail.com", 587)
                server.starttls()
                server.login(config["EMAIL"], config["GOOGLE_KEY"])
                server.sendmail(config["EMAIL"], self.email, f"""Subject: NOTICE \n\nLog: Your Computer has been turn on\nDate: {dt}""")
                server.quit()
            except Exception as e:
                messagebox.showerror("Error", f"Error in sending email: {e}. Please Check your internet connection")
        else:
            messagebox.showerror("Error", "Invalid email address")

if __name__ == "__main__":
    email("Enter Your Email here.").send_email()
