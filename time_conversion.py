def timeConversion(s):
    time = s.split(":")
    if s[-2:] == "PM":
        if time[0] != "12":
            time[0] = str(int(time[0])+12)
    else:
        if time[0] == "12":
            time[0] = "00"
    ntime = ':'.join(time)
    return str(ntime[:-2])
   
s = input("enter time in 12hour format:")

result = timeConversion(s)
print("time conversation in 24hour format is:",timeConversion(s))
