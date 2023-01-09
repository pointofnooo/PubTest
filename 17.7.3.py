per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Мой депозит:'))
deposit = []
for key in per_cent: deposit.append(int(per_cent[key] * money / 100))
max_deposit = max(deposit)
depositto = (str(deposit))
money_split = depositto.split()
money_lines = "\n".join(money_split)
print('Прибыль по депозитам:\n',(money_lines.strip('[]')))
print('Максимальная прибыль по депозиту:' + str(max_deposit))