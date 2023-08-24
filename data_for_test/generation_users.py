import datetime

def generation_users():
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    login_gen = f"user_{str(timestamp)}"
    email_gen = f"user_{timestamp}@qw.ru"
    password_gen = str(timestamp)

    with open("emails.txt", "a") as file:
        file.write(email_gen + "\n")

    generation_users = {
        "login": login_gen,
        "email": email_gen,
        "password": password_gen
    }

    return generation_users
