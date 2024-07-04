symbols='AAPL GOO MSFT IBM YOO'

#String indexing
print(symbols[0])
print(symbols[1])

#Negative indexing

print(symbols[-1])
print(symbols[-2])

#Sicing
print(symbols[4:])
print(symbols[:4])
symbols=symbols + 'AAO'

print('AA0L' in symbols)

print(symbols.lower())
print(symbols.isalnum())
print(symbols.capitalize())
print(symbols.casefold())
print(symbols.encode('utf-8'))
print(symbols.isalpha())