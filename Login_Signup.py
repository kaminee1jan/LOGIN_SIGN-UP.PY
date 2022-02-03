import json 
import os

print("1.Signup\n 2.Login")

user=int(input("enter your choice = "))

list=[]
dict={"user":list}
dict1={}

if user==1:
    username=input("enter name = ")
    password1=input("enter password = ")
    password2=input("enter password again = ")
    if password1 == password2:
        digit=0
        special_chr=0
        upper=0
        lower=0
        for i in password1:
            if i.isdigit():
                digit+=1
            if i.isupper():
                upper+=1
            if i.islower():
                lower+=1
            if "#" in i or "@" in i or "$" in i:
                special_chr+=1
        if lower>=1 and upper>=1 and special_chr>=1 and digit>=1:
            if os.path.exists("userdetails.json")==True:
                with open("userdetails.json") as file_1:
                    m=json.load(file_1)
                    n=m["user"]
                    for i in n:
                        if i["username"]==username:
                            print("this username already exists, choose another username")
                            break

                        else:
                            print("congrats!", username,"you sucessfully registered")
                            birthdate = input("enter your birthdate = ")
                            hobbies = input("enter your hobbiees = ")
                            gender = input("enter your gender = ")
                            dict1={"password":password1,"username":username,"birthdate":birthdate,"hobbies":hobbies,"gender":gender}

                            if os.path.exists("userdetails.json")==True:
                                with open("userdetails.json") as file:
                                    k=json.load(file)
                                    l=k["user"]
                                    l.append(dict1)
                                    dict["user"]=l
                                    with open("userdetails.json","w") as file1:
                                        json.dump(dict,file1,indent=4)
                            else:
                                list.append(dict1)
                                k=open("userdetails.json","w")
                                json.dump(dict,k,indent=4)
                                break
            else:
                print("congrats!", username,"you sucessfully registered")
                birthdate = input("enter your birthdate = ")
                hobbies = input("enter your hobbiees = ")
                gender = input("enter your gender = ")
                dict1["password"]=password1
                dict1["username"]=username
                dict1["birthdate"]=birthdate
                dict1["hobbies"]=hobbies
                dict1["gender"]=gender

                if os.path.exists("userdetails.json")==True:
                    with open("userdetails.json") as file:
                        k=json.load(file)
                        l=k["user"]
                        l.append(dict1)
                        dict["user"]=l
                        with open("userdetails.json","w") as file1:
                            json.dump(dict,file1,indent=4)
                else:
                    list.append(dict1)
                    k=open("userdetails.json","w")
                    json.dump(dict,k,indent=4)
        else:
            print("at least password should contain one special character,number,lowercase and uppercase character")

    else:
        print("both password are not same")


###############################  LOGIN   ###########################################

elif user == 2:
    username=input("enter your username = ")
    password=input("enter your password = ")
    if os.path.exists("userdetails.json")==True:
        with open("userdetails.json") as file:
            a=json.load(file)
            k=a["user"]
            for i in k:
                if i["username"]==username and i["password"]==password:
                    print( username, "you have logged in sucessfully")
                    break
            if i["username"]!=username and i["password"]!=password:
                print("Invalid username and password")