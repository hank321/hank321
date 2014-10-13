#if else
x = int(input(" 請輸入一個整數: \n "))

if x < 0:
	x=0 
	print ("Negative changed to zero")
elif x == 0:
    print("零")
elif x == 1:
    print("single")
else:
    print("more")
