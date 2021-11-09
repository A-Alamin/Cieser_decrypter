import pyperclip
plain_message = input('Type the message you  want encrypt: ')
lock_key = 30
mode = 'encrypt'
cryptos = 'A!BCDEFG@HIJK#LMNOPQR STUVW$$$XY?Zabcd%efghijkl&mnopq*rstuv(wxy)z1234=567890[].,^&_-+='
translated = ''
for symbol in plain_message:
	if symbol in cryptos:
	    symbolIndex = cryptos.find(symbol)
	if mode == 'encrypt':
	    translatedIndex = symbolIndex + lock_key
	elif mode == 'decrypt':
	    translatedIndex = symbolIndex - lock_key
	if translatedIndex >= len(cryptos):
	    translatedIndex = symbolIndex - len(cryptos)
	elif translatedIndex < 0:
	    translatedIndex = symbolIndex + len(cryptos)
	    
	translated = translated + cryptos[translatedIndex]
else:
	translated = translated + symbol
print(translated)
pyperclip.copy(translated)
