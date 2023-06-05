# receive miles and convert to km
# km = miles * 1.60934
# 5 miles equals 8.04km thereabout

miles = int (input("please enter amount of miles to convert to km: "))
km = miles * 1.60934
print("{} ".format(miles) + "miles equals " + "{} ".format(km))