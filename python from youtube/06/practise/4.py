# waf to convert usd to inr

def convert(usd_val):
    inr = usd_val*86
    print(usd_val,"USD = ",inr,"INR")

convert(100)