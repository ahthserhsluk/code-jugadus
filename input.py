from whisper import voice
def input():
    print("Hey! Help us in the few details we require about the website\n")
    print("What is your name?\n")
    name = voice()
    print("Tell us a little about yourself\n")
    about = voice()
    print("Tell us your skills\n")
    skills = voice()
    print("Describe your skills\n")
    skild = voice()
    email = input("Enter your email please\n")
    phone = input("Enter your phone number please\n")
    opt=1
    while(opt!=7):
        print("Do you want to change any details?\n")
        opt = int(input("1.Name\n2.About\n3.Skills\n4.About skills\n5.Email\n6.Phone\n7.Quit\n"))
        match opt:
            case 1: 
                print(name,'\n')
                name = input("Enter your name\n")
            case 2: 
                print(about,'\n')
                about = input("Enter your description\n")
            case 3: 
                print(skills,'\n')
                skills = input("Enter your skills, comma seperated\n").split(",")
            case 4: 
                print(skild,'\n')
                skild = input("Describe your skills in a few words\n")
            case 5: 
                print(email,'\n')
                email = input("Enter your email\n")
            case 6: 
                print(phone,'\n')
                phone = input("Enter your phone number\n")
            case 7: break
    code = "".join(open('template 1\index.html','r').readlines())
    prompt = code + f"Please edit this detail for {name} who is {about} having skills as {skills}. The description of the skills are {skild}. The contact details are {email},{phone}"
    return prompt