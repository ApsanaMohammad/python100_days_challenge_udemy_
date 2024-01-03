# #string by default from input function
# s=input("Enter a STRing :")
# print(s+f"{type(s)}")#type function 

# a=10
# b=int(input("enter value of b: "))
# print (a+b)

amount=float(input("Enter the amount : "))
tip_per=int(input("Enter the tip percentage : "))
tip=(amount/100)*tip_per
amount=amount+tip
n=amount/int(input("Enter the number of ppl to divide the amount among : "))

print(f"(The amoont per person to pay :: {n}")

