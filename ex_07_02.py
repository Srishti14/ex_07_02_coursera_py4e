fname = input("Enter file name:")
thefile = open(fname)
count = 0
sum_of_numbers = 0
for line in thefile:
    line1 = line.rstrip()
    if line1.startswith("X-DSPAM-Confidence:"):
        colon = line1.find(":")
        thenumber = line1[colon+1:]
        number_in_float = float(thenumber)
        count += 1
        sum_of_numbers += number_in_float
avg = sum_of_numbers/count
print("Average spam confidence: "+ str(avg))
