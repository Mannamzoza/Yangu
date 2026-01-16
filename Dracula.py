name = input("Type your name: ")
print("Welcome", name, " to this adventure")

answer = input("You are on dracula's zone; What are gonna do(run , fight) :")

if answer == "run":
    answer = input("You can run but you cannot (hide) or you can make it (simplier): ")

    if answer == "hide":
        print("You can't hide from me !!!!!")
    elif answer == "simplier":
        print("ha! ha! ha! ha! you weakling")
    else:
        print("Become my minion")


elif answer == "fight":
    answer = input("i give you 5 mins you give me all you have got but after that, you shall fell my rath: (bring it on, despair)")

    if answer == "bring it on":
        print("nothing scarier than a man with no fear")
    elif answer == "despair":
        answer = input("after the 5 min match up yuo fell the diffrence in power, do you continue (yes,no)").lower()

        if answer == "yes":
            print("You got some balls,i will give you that kid :)")

        elif answer == "no":
            print("Despair!!! Despair!!!! Despair!!!")

        
        else:
            print("Draculaaa!!!!!")

        print("you shall feel my power till the depth of you heart for defying me!!!")
    else:
        print("")


else:
    print("Dracula bite you")

print("Thank you for trying", name)