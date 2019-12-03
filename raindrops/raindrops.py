def convert(number):
    plung = ''
    if number % 3 == 0 :
        plung += 'Pling'
    if number % 5 == 0:
        plung += 'Plang'
    if number % 7 == 0:
        plung += 'Plong'
    if plung == '':
        plung = str(number)
    return plung