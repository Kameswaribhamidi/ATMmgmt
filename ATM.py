username='kameswari'
password='python123'
print("""username='kameswari'
password='python123'""")
c_name=input("Enter your name: ")
c_pass=str(input("Ennter your password: "))
if c_name==username and c_pass==password:
    print('''
    1. Deposit
    2. Withdraw
    3. Ministatemwnt
    4. Exit
    ''')
    amt=50000
    print(f"The Available Balance is: {amt}")
    ch=int(input("select your option from above: "))
    if ch==1:
        dep=int(input("Enter amount to deposit: "))
        amt+=dep
        print("The available balance is ",amt)
    elif ch==2:
        wtd=int(input("Enter amount to withdraw: "))
        amt-=wtd
        print("Final amount is ",amt)
    elif ch==3:
        print("======ATM======")
        print("Username: ",username)
        print("Total amount: ",amt)
        print("Thanks for visiting")
        print("==============")
    elif ch==4:
        exit()        
else:
    print("Please enter correct details.")
        