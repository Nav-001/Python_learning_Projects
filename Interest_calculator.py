def SI(principal_amount, time, rate):
    si = principal_amount*time*rate/100
    print(si)
    return si

print("Enter principal amount : ")
principal = int(input())
print("Enter time : ")
time = int(input())
print("Enter rate : ")
rate = int(input())

SI(principal,time,rate)