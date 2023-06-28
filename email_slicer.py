def main():
    print('Welcome to email Splicer !')
    email_adress=input("Enter Your Email Adress: ")

    (username,domain)=email_adress.split('@')
    (domain,extension)=domain.split('.')
    print(f'Username: {username}\n Domain: {domain}\n Extension: {extension}')

main()