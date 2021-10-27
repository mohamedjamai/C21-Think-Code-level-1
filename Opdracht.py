print ("Try yourself")
print ("ANSWERS IN ENGLISH PLEASE.")

x = input ("Enter your username")


def end(eyecolor, ap, a, adress, x):
    show = input ("We need absolute to know whats your favorite show? on netflix, videoland or youtube tell us!")
    print ("OMG, we also like " + show )
    print ("The main character is so sexy right!")

    car = input ("Whats about your dream car can you tell us more about it? wich CAR do you want to have later in your life. ")
    print ("The amazing, " + car )
    print ("WOW, thats the same as me? we need to know each other more!")

    print ("Do you have seen the new iPhone 13 with the camera its so amazing!")
    print ("Wowow, the next generation samsung they are on another level wow!")
    print ("I need to know wiche one do you prefer!")
    prefer = input ("Do you prefer the iPhone or Samsung")
    if prefer == 'iPhone' or prefer == 'iphone' or  prefer == 'IPHONE':
        print ("Wow, I have bought the new iphone 13 yesterday we are soulmates I think.")
    if prefer == 'Samsung' or prefer == 'SAMSUNG' or prefer == 'samsung':
        print ("I know it, I know it and I know it we are definitly like soulmates the newest samsung its perfect so comfortable!")

    print ("Okay, okay I know now a lot about you, we need to meet eachtother! ")
    con = input ("Do you want to the conclusion about you?")
    if con == 'yes' or con == 'YES':
        print (" you have a beautiful name its called " + x + "you are so young.. " + a + "I wish I had eyes like you its so perfect" + eyecolor + " and you living on a nice street its so silent and calm pure rest" + adress)
        print ("You said that you like yourself its okay to do that you give yourself a " + ap )
        print ("No we dont forget your favorite show its called" + show + "and your dreamcar its amazing " + car + "and you have a " + prefer + "We like you a lot we want to know more about you the next time!")

    print ("You did it Amazing do I have already said Amazing? it was me a pleassure to meet you and know more about you!")
    ex = input ("On a scale from 0 tot 10 how good was this excerise?")
    print("Wow thank you again! it was a " + ex )

def start():
   
    x = input ("Enter your username")
    print("Hello, " + x)
    a = input ( "Enter your age:")

    print ("Your age is " + a) 

    print (" Your name is"  + x + " and your age is " + a ) 

    adress = input ("Enter your adress")

    print (" Your name is " + x + " and your age is " + a + " you living at = " + adress )

    eyecolor = input ("Enter your color eye") 

    print ("You have a  nice eyecolor" + eyecolor)
    print ("We have some details about you we need to know more!")
    print ("Now we going to ask you some questions about your confident")

    ao = input ("On a scale from 0 tot 10 how much do you like yourself?")
    print ("Now we continue with another question. ")

    ap = input ("Whats your favorite memory about your self? (begin with space)")
    print ("its an amazing memory about your self we like that. ")

    ok = input ("We want to know more about you is that oke?") 
    if ok == 'yes' or  ok == 'Yes':
        print ("Yes glad to hear that lets continue")
        print ("You like the questions right, we have a couple of questions left and then you see your conclusion!")
        end()
    if ok == 'no' or ok == 'NO':
        print ("Awhfull okay thank you for your storys!")
        print ("You have answered No right, its okay dissapointed in you but its not a problem again thankyou! ")
        start(eyecolor, ap, a, adress, x)

start()
