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

f = open('unicode_replacer.py', 'w')
cmd = []
notcmd = []
addedjval = []
for j in myunicodes.split('\n'):
	if 'DeclareUnicodeCharacter' not in j or '\\def' in j or '\\ifdefined' in j or '\ifx' in j or 'COMMONUNICODE' in j:
		continue
	if j[0] == '%':
		continue
	jsp = j.split('}{')
	kcode = jsp.pop(0).split('{')[1]
	jval = '}{'.join(jsp).strip()[0:-1]
	char = chr(int(f'0x{kcode}', 16))
	if '\\ensuremath' in jval:
		jval = jval.replace('\\ensuremath{', '')[0:-1]
	if jval[0] == '{':
		continue
	if 'NOT' in jval or 'NONE' in jval or '\LOCALunknownchar' in jval:
		continue
	if '\hbox' in jval or '\else' in jval or '{ }' in jval or '\\,' in jval or '\\text{' in jval or '!' in jval:
		continue
	jval = jval.replace('\\', '\\\\')
	if jval in addedjval:
		# print(f'REPEATED {jval}')
		continue
	addedjval.append(jval)
	txt = f"\t('{jval}', '{char}'),\n"
	if jval == char:
		continue
	if '\\' not in jval:
		if len(jval) == 1 or "'" in jval:
			continue
		notcmd.append(txt)
	else:
		cmd.append(txt)
cmd.sort(key=lambda v: v.upper())
notcmd.sort(key=lambda v: v.upper())
for j in cmd:
	f.write(j)
for j in notcmd:
	f.write(j)
f.close()