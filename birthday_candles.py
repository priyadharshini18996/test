def birthday_candles(no_of_candle):
    count=0
    big_candle=max(no_of_candle)
    for i in range(len(no_of_candle)):
        if(no_of_candle[i])== big_candle:
            count+=1
    return count
   

age = int(input("enter the count of candle,which represents ur niece_b'day:"))

no_of_candle = list(map(int, input("enter the array of candle in integer:").rstrip().split()))

result=birthday_candles(no_of_candle)
print("maximum count of candle ,in which she blows is:",birthday_candles(no_of_candle))