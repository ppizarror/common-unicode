"""
Generate unicode tests.
"""

myunicodes=''.join(open('commonunicode.sty', 'r', encoding='utf8').readlines())

f = open('commonunicode_list.tex', 'w', encoding='utf8')
f.write('\\begin{itemize}\n')
added = []
for j in myunicodes.split('\n'):
	if 'DeclareUnicodeCharacter' not in j or '\\def' in j or '\\ifdefined' in j or '\ifx' in j:
		continue
	if j[0] == '%':
		continue
	kcode = j.split('}{')[0].split('{')[1]
	if kcode not in added:
		added.append(kcode)
	else:
		print(f'Error, {kcode} repeated')
	char = chr(int(f'0x{kcode}', 16))
	kcode = '\\href{https://decodeunicode.org/en/u+' + kcode + '}{U+' +kcode + '}' 
	f.write(f'\t\\item {kcode}: {char}\n')
f.write('\end{itemize}')
f.close()