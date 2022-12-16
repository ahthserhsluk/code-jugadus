def voice_input():
    print("Hey! Help us in the few details we require about the website\n")
    print("tell your name?\n")
    name = input()
    print("Tell us a little about yourself\n")
    about = input()
    print("Tell us your skills\n")
    skills = input()
    print("Enter Email\n")
    email = input()
    print("Enter Phone number\n")
    phone = input()
    code = "".join(open('template 1\index.html','r').readlines())
    prompt = code + f"change this website for {name} who is {about} having skills as {skills}. The contact details are {email},{phone} dont change images"
    return prompt


     