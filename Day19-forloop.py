print('Loan Calculator')
loan = 1000
interest = 0.05  # 5% as decimal
years = 10
print('$1000 over 10 years at 5% APR')
for year in range(1, 11):
  loan = loan * (1 + interest)
  # .2f format to 2 decimal places
  print(f'Year {year}: ${loan:.2f}')