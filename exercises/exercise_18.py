ans_1 = input("Do you remember the person's name?")
if ans_1 == "Yes":
    ans_2 = input("Is it an ex?")
    if ans_2 == "Yes":
        ans_3 = input("Are you drunk?")
        if ans_3 == "Yes":
            ans_4 = input("Do youy want to rekindle and/or give 'em what for?")
            if ans_4 == "Yes":
                print("Say hi.")
            else:
                print("Don't say hi.")
        else:
            ans_yes_yes_1 = input("Are you in a convertible with Brad Pitt and/or Rihanna?")
            if ans_yes_yes_1 == "Yes":
                print("Say hi.")
            else:
                print("Don't say hi.")
    else:
        ans_yes_no_1 = input("A friend's ex?")
        if ans_yes_no_1 == "Yes":
            print("Don't say hi.")
        else:
            ans_yes_no_2 = input("An enemy or frenemy?")
            if ans_yes_no_2 == "Yes":
                ans_yes_no_3 = input("Are you in a convertible with Brad Pitt and/or Rihanna?")
                if ans_yes_no_3 == "Yes":
                    print("Say hi.")
                else:
                    print("Don't say hi.")
            else:
                ans_yes_no_4 = input("Are you robbing a bank?")
                if ans_yes_no_4 == "Yes":
                    print("Don't say hi.")
                else:
                    ans_yes_no_5 = input("Are you in a bathrobe?")
                    if ans_yes_no_5 == "Yes":
                        print("Don't say hi.")
                    else:
                        print("Say hi.")
else:
    ans_no_2 = input("Is there time to flee?")
    if ans_no_2 == "Yes":
        print("Run for it.")
    else:
        ans_no_3 = input("Could you pretend to get a call on your cell?")	
        if ans_no_3 == "Yes":
            print("Hello, doctor. What are my test results?")
        else:
            ans_no_4 = input("Are you wearing sunglasses?")
            if ans_no_4 == "Yes":
                print("Keep walking.")
            else:
                print("Adress the person using an amusing nickname sush as \"Sarge\", \"Slugger\" or \"Master Blaster\".")