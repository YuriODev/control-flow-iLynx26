# ans_1 = input("Do you remember the person's name? ")
# if ans_1 == "yes":
#     ans_2 = input("Is it an ex? ")
#     if ans_2 == "yes":
#         ans_3 = input("Are you drunk? ")
#         if ans_3 == "yes":
#             ans_4 = input("Do youy want to rekindle and/or give 'em what for? ")
#             if ans_4 == "yes":
#                 print("Say hi.")
#             else:
#                 print("Don't say hi.")
#         else:
#             ans_yes_yes_1 = input("Are you in a convertible with Brad Pitt and/or Rihanna? ")
#             if ans_yes_yes_1 == "yes":
#                 print("Say hi.")
#             else:
#                 print("Don't say hi.")
#     else:
#         ans_yes_no_1 = input("A friend's ex? ")
#         if ans_yes_no_1 == "yes":
#             print("Don't say hi.")
#         else:
#             ans_yes_no_2 = input("An enemy or frenemy? ")
#             if ans_yes_no_2 == "yes":
#                 ans_yes_no_3 = input("Are you in a convertible with Brad Pitt and/or Rihanna? ")
#                 if ans_yes_no_3 == "yes":
#                     print("Say hi.")
#                 else:
#                     print("Don't say hi.")
#             else:
#                 ans_yes_no_4 = input("Are you robbing a bank? ")
#                 if ans_yes_no_4 == "yes":
#                     print("Don't say hi.")
#                 else:
#                     ans_yes_no_5 = input("Are you in a bathrobe? ")
#                     if ans_yes_no_5 == "yes":
#                         print("Don't say hi.")
#                     else:
#                         print("Say hi.")
# else:
#     ans_no_2 = input("Is there time to flee? ")
#     if ans_no_2 == "yes":
#         print("Run for it.")
#     else:
#         ans_no_3 = input("Could you pretend to get a call on your cell? ")	
#         if ans_no_3 == "yes":
#             print("Hello, doctor. What are my test results? ")
#         else:
#             ans_no_4 = input("Are you wearing sunglasses? ")
#             if ans_no_4 == "yes":
#                 print("Keep walking.")
#             else:
#                 print("Adress the person using an amusing nickname sush as \"Sarge\", \"Slugger\" or \"Master Blaster\".")

# Predefined outcomes as constants
SAY_HI = "Say hi."
DONT_SAY_HI = "Don't say hi."
RUN_FOR_IT = "Run for it."
KEEP_WALKING = "Keep walking."
ADDRESS_WITH_NICKNAME = "Address the person using an amusing nickname such as 'Sarge', 'Slugger', or 'Master Blaster.'"
HELLO_DOCTOR = "Hello, doctor. What are my test results?"

# Start of the decision tree
remember_name = input("Do you remember the person's name? (yes/no): ").lower()

if remember_name == 'yes':
    is_ex = input("Is it an ex? (yes/no): ").lower()
    if is_ex == 'yes':
        are_you_drunk = input("Are you drunk? (yes/no): ").lower()
        if are_you_drunk == 'yes':
            rekindle = input("Do you want to rekindle and/or give 'em what for? (yes/no): ").lower()
            output = SAY_HI if rekindle == 'yes' else DONT_SAY_HI
        else:
            in_convertible = input("Are you in a convertible with Brad Pitt and/or Rihanna? (yes/no): ").lower()
            output = SAY_HI if in_convertible == 'yes' else DONT_SAY_HI
    else:
        friend_ex = input("A friend's ex? (yes/no): ").lower()
        if friend_ex == 'yes':
            output = DONT_SAY_HI
        else:
            enemy_or_frenemy = input("An enemy or frenemy? (yes/no): ").lower()
            if enemy_or_frenemy == 'yes':
                in_convertible = input("Are you in a convertible with Brad Pitt and/or Rihanna? (yes/no): ").lower()
                output = SAY_HI if in_convertible == 'yes' else DONT_SAY_HI
            else:
                robbing_bank = input("Are you robbing a bank? (yes/no): ").lower()
                if robbing_bank == 'yes':
                    output = DONT_SAY_HI
                else:
                    in_bathrobe = input("Are you in a bathrobe? (yes/no): ").lower()
                    output = DONT_SAY_HI if in_bathrobe == 'yes' else SAY_HI

else:  # Don't remember the person's name
    time_to_flee = input("Is there time to flee? (yes/no): ").lower()
    if time_to_flee == 'yes':
        output = RUN_FOR_IT
    else:
        pretend_call = input("Could you pretend to get a call on your cell? (yes/no): ").lower()
        if pretend_call == 'yes':
            output = HELLO_DOCTOR
        else:
            wearing_sunglasses = input("Are you wearing sunglasses? (yes/no): ").lower()
            if wearing_sunglasses == 'yes':
                output = KEEP_WALKING
            else:
                output = ADDRESS_WITH_NICKNAME

print(output)