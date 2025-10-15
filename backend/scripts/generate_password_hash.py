from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
# Enter the password to be hashed
password = ""
hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

print(f"Hashlenmiş Şifre: {hashed_password}")