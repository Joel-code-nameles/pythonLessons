Age = int(input("Age"))
visa = True
passport = True
Ghana_Card = True
Experience_in_live_combat = True

if(Age >= 18):
    if(visa):
        if(passport):
            if(Ghana_Card):
                if(Experience_in_live_combat):
                    print("You can jion the american milla boot camp")

                else:
                    print("Sorry,you cant jion the milla")

            else:
                print("Get Ghana Card/Do national service")

        else:
            print("get passport")

    else:
        print("Go get your visa")

else:
    print("To young!")


      