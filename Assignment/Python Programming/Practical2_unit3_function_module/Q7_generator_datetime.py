# Q7. Generator and Datetime Module 
# Create a generator function that generates dates for the next 7 days starting from
# today's date.
# Use the datetime module.


from datetime import date, timedelta

def generate_dates():   # Generator function
    today = date.today()
    for i in range(7):
        next_date = today + timedelta(days=i)
        yield next_date
for d in generate_dates():
    print(d)
