"""
Write a program to read through a file and print the contents
of the file (line by line) all in upper case. Executing the program will
look as follows:
python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
"""
file_name = input('Enter a file name: ')
try:
    file_handle = open(file_name)
except:
    print('File not found')
    quit()
    
for line in file_handle:
    uline = line.upper().rstrip()
    print(uline)