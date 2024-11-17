p=float(input("Enter the Principal amount -> "))
r=float(input("Enter the Rate of Interest -> "))
t=float(input("Enter the Time Period (in years) ->"))
si=(p*r*t)/100
ci=p * (1 + r/100) ** t - p
print("The Simple Interest of given values is -> %.2f"%si)
print("The Cumulative Interest of given values is -> %.2f "%(ci))
