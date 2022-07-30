RATE =1.03
TUITION = 8000
YEARS = 5
ANNUAL_COST = TUITION
print("Year 0: Annual cost = ${}".format(i+1, annual_cost))
for i in range(years):
    annual_cost *= RATE
    print("Year {}: Annual cost = ${}".format(i+1, annual_cost))
