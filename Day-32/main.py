import smtplib
import datetime as dt

# my_email = "yuvraj21testemail@yahoo.com"
# password = "testemail_#"
#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="yuvrajtestemail1@gmail.com", msg="Subject:Test\n\n"
#                                                                                        "Testing code")


now = dt.datetime.now()
year = now.year
month = now.month
dob = dt.datetime(year=2002, month=12, day=9, hour=17)
print(dob)
print(year, month, type(year))
