import random
import time
 
energi = 100
kissnödighet = 0
löpta_km = 0
tid = 0
varv = 0
print("Redy, set GOOOO!!!! ")
while löpta_km < 42:
    tid =  tid + 4
    varv = varv + 1
    löpta_km = löpta_km + 1
    print(f"You have run {löpta_km}km")
    if löpta_km == 42:
        Mål_tid_timmar = tid // 60
        mål_tid_minuter = tid%60
        print(f"You finnished in: {Mål_tid_timmar} hours and {mål_tid_minuter} minutes.")
        break

    kissnödighet = kissnödighet + random.randint(1,3)
    energi = energi - random.randint(1,7)
    if kissnödighet >= 100:
        print("You hade an accident and went home..")
        break
    if energi <= 0:
        print("You got too tired and hitchhiked home!")
        break
    if varv%2 == 0:
        if kissnödighet > 80:
            print("You took a bathroom break!")
            kissnödighet = 0
            tid = tid + 5
    if varv == 6:
        Antal_Varv = löpta_km // 6
        Varv_Kvar = 7 - Antal_Varv
        
        print(f"You have run {Antal_Varv} laps around Nydala! Keep the good work, only {Varv_Kvar} left!")
        print(f"Your energy level is at: {energi} %") 
        Antal_Bullar = int(input("How many cinnamon buns do you wanna eat? \n Enter a number: "))
        if Antal_Bullar == 1:
            print("You eat one cinnamon bun!")
        else:
            print(f"You eat {Antal_Bullar} cinnamon buns")
        energi = energi + (5 * Antal_Bullar)
        if energi > 100:
            energi = 100
        kissnödighet = kissnödighet + 10
        tid = tid + Antal_Bullar
        varv = 0
    time.sleep(1)
