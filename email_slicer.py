def main():
    print('Welcome to email Slicer !')
    email_adress=input("Enter Your Email Adress: ")

    (username,domain)=email_adress.split('@')
    (domain,extension)=domain.split('.')
    print(f'Username: {username}\n Domain: {domain}\n Extension: {extension}')

main()