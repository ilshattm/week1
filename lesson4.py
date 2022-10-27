def salary(oklad, dk, df, prem, nalog, uderj):
    k = ((oklad / dk) * df + prem) * ((100 - nalog) / 100) - uderj
    return k


f = salary(10000, 30, 28, 5000, 13, 2000)
print("Salary: $", int(f))

