sandwich_orders = ['Bacon', 'Pastrami', 'Bagel toast', 'Bararu', 'Pastrami',
                   'Limburger', 'Rachel', 'Tuna', 'Pastrami']
finished_sandwiches = []
print("Sorry, our Pastrami sandwiches are all sold out")
sold_out = 'Pastrami'

while sold_out in sandwich_orders:
    sandwich_orders.remove(sold_out)

while sandwich_orders:
    now_sandwich = sandwich_orders.pop()
    #if now_sandwich == 'Pastrami':
    #   continue
    
    print("I made your " + now_sandwich + " sandwich.")
    finished_sandwiches.append(now_sandwich)

print(finished_sandwiches)
