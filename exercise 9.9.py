for agegap in range (12,92):
    matchcount = 0
    for age in range (0,100-agegap):
        agefill = (str(age).zfill(2))
        if int(agefill[::-1]) == age + agegap:
            print(age, age + agegap)
            matchcount += 1
    if matchcount >= 8:
        print('Solution ', agegap)
        print(matchcount , ' matches')