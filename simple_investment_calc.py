print("10 Year investment Calculator\n")
amnt, invest_rate = input("Please Enter Investment Amount and expected interest: ").split()
amnt, invest_rate = float(amnt), float(invest_rate)
invest_rate = invest_rate / 100
for i in range(10):
    amnt = amnt + (amnt * invest_rate)
print("Your profit is {:.2f} ".format(amnt))