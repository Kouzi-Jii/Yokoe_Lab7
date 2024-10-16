prgr = float(input("Enter your Preliminary Grade: "))
if prgr < 40 or prgr > 100:
    print("Your Preliminary Grade is invalid")
else:
        mdgr = float(input("Enter your Midterms Grade: "))
        if mdgr < 40 or mdgr > 100:
            print("Your Midterms Grade is invalid")
        else:
            fpgr = float(input("Enter your Finals Grade: "))
            if fpgr < 40 or fpgr > 100:
                print("Your Finals Grade is invalid")
            else:
                fprgr = prgr * 0.33
                fmdgr = mdgr * 0.33
                ffpgr = fpgr * 0.33
                avg = (fprgr + fmdgr + ffpgr) 
                ave = round(avg, 2)
                print("Your Final Grade is: ", ave)
if ave >= 99.00 or ave <= 100 and ave > 99.00:
    print("Your Grade Points are 1.0!")
elif ave >= 96.00 or ave >= 97.00 and ave > 96.00 or ave <= 98.00 and ave > 96.00:
    print("Your Grade Points are 1.25!")
elif ave >= 93.00 or ave >= 94.00 and ave > 93.00 or ave <= 95.00 and ave > 93.00:
    print("Your Grade Points are 1.50!")
elif ave >= 90.00 or ave >= 91.00 and ave > 90.00 or ave <= 92.00 and ave > 90.00:
    print("Your Grade Points are 1.75!")         
elif ave >= 87.00 or ave >= 88.00 and ave > 87.00 or ave <= 89.00 and ave > 87.00:
    print("Your Grade Points are 2.0!")
elif ave >= 84.00 or ave >= 85.00 and ave > 84.00 or ave <= 86.00 and ave > 84.00:
    print("Your Grade Points are 2.25!")
elif ave >= 81.00 or ave >= 82.00 and ave > 81.00 or ave <= 83.00 and ave > 81.00:
    print("Your Grade Points are 2.50!")
elif ave >= 78.00 or ave >= 79.00 and ave > 78.00 or ave <= 80.00 and ave > 78.00:
    print("Your Grade Points are 2.75!")
elif ave >= 75.00 or ave >= 76.00 and ave > 75.00 or ave <= 77.00 and ave > 75.00:
    print("Your Grade Points are 3.0!")
else:
    print("Your Grade Points are 5.0!")
    
