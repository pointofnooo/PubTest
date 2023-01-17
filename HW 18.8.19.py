tickets = int(input('Сколько билетов:'))
visitors_age = []
for i in range(0, tickets):
    input_value = int(input(f'Введите возраст {i + 1} посетителя: '))
    visitors_age.append(input_value)
    def price(age):
        if age < 18:
            return 0
        elif 18 <= age < 25:
            return 990
        elif 25 <= age:
            return 1390
    ticket_sum = sum(map(price, visitors_age))
discount = int(ticket_sum * 0.1)
discounted = int(ticket_sum - discount)
if tickets > 3: print ('Итого', tickets, 'билетов со скидкой 10% на общую сумму в', discounted, 'RUB')
else: print ('Итого', tickets, 'билетов на общую сумму в', ticket_sum, 'RUB')