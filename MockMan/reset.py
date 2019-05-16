import os 

print("This action will clear all the endpoints and mocks that you have added!")
print("Do you want to continue and reset MockMan?(YES/NO)")
consent = input()
if "y" in consent.lower():    
    os.system("git reset --hard")
    os.system("git clean -f -d")
    print("Hurrray!! Your MockMan reset to intial state successful")
else:
    print("Hurrray!! Your MockMan state is saved.")