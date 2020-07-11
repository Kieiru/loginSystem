def reg():
   name = input("[+] Enter your name: ")
   password = input("[+] Enter your password: ")
   myData = open("Data.txt","a+")

   myData.write('\n')
   tb = (name, password)
   myData.write(str(tb))
   print("[+] Your account was created successfully")

    

def login():
   while 1:
      print("[+] login to your account")
      Name = input("[+] enter your name: ")
      password = input("[+] enter your password: ")
      with open("Data.txt") as f:
            datafile = f.readlines()
      for line in datafile:
         if Name and password in line:
            print("login successfully")
            break
         else:
            continue
                          


       
print("welcome to basic login system by (Kieiru)")
print("select what you wanna do")
print("1.login")
print("2.register")
print("3.exit")

selectedOption = input("select option: ")
if (selectedOption == "1"):
     login()
elif (selectedOption == "2"):
    reg
else:
   exit()
    
    


