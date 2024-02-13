str = 'X-DSPAM-Confidence:0.8475'
colon_pos = str.find(':')
snum = str[colon_pos + 1:]
fnum = float(snum)
print(fnum)
print(type(fnum))