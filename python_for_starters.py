# Q1
a = 13
b = 5
print(a)
print(b)
x = int(input("-"))
y = int(input("-"))
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)

# Q2
a = 1
b = 0.5
c = "hello"
print(type(a))
print(type(b))
print(type(c))

x = input("Write an integer: ")
y = input("Write a float: ")
z = input("Write a string: ")
print(x)
print(y)
print(z)

# Q3
first_int = int(input("First integer: "))
sec_int = int(input("Second integer: "))
third_int = int(input("Third integer: "))
sum = first_int + sec_int + third_int
mean = sum / 3
multiple = first_int * sec_int * third_int
print(sum)
print(mean)
print(multiple)

# Q4

A = int(input("principal amount (A): "))
i = int(input("interest rate (i): "))
n = int(input("duration (n): "))
S = A*(1+i/100)** n
print(S)

# Q5

R1 = int(input("first resistance (R): "))
R2 = int(input("second resistance (R): "))
V = int(input("voltage (V): "))
I1 = V // R1
I2 = V // R2
print(I1)
print(I2)

# Q6
years = int(input("Number of years: "))
months = int(input("Number of months: "))
days = int(input("Number of days: "))
hours = int(input("Number of hours: "))
minutes = int(input("Number of minutes: "))
sec_in_min = 60 * minutes
sec_in_hour = 60 ** 2 * hours
sec_in_day = 60 ** 2 * 24 * days
sec_in_month = 60 ** 2 * 24 * 30 * months
sec_in_year = 60 ** 2 * 24 * 30 * 365 * years
print(sec_in_year + sec_in_month + sec_in_day + sec_in_hour + sec_in_min)



