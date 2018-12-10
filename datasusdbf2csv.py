#!/usr/bin/python
import sys
import os

from ftplib import FTP
from pysus.utilities.readdbc import dbc2dbf

def download(state, year):
    ftp = FTP('ftp.datasus.gov.br')
    ftp.login()
    if year < 1994:
        raise ValueError("SINASC does not contain data before 1994")
    if year >= 1996:
        ftp.cwd('/dissemin/publicos/SINASC/NOV/DNRES/')
        fname = ('DN{}{}.dbc'.format(state, year))
    else:
        ftp.cwd('/dissemin/publicos/SINASC/ANT/DNRES/')
        fname = ('DNR{}{}.dbc'.format(state, str(year)[-2:]))

    ftp.retrbinary('RETR {}'.format(fname), open(fname, 'wb').write)

    filename = format(fname)
    return filename 

def dbc2csv(filename):
    #DBC -> DBF -> CSV
    shortname = format(filename[:-4])
    dbc2dbf('./'+filename,'./'+ shortname +'.dbf')
    os.system("dbf2csv "+ shortname+".dbf > "+ shortname+".csv")




estado = str(sys.argv[1])
ano    = int(sys.argv[2])
tabela = str(sys.argv[3])

#@TODO : Colocar cores 
print("Fazendo Download da Tabela " + tabela)
print(str(sys.argv[1]),str(sys.argv[2]))
#https://github.com/akadan47/dbf2csv
filename = download(estado,ano)

#@TODO : Por clausula de erro no dbc2csv
dbc2csv(filename)

#DOWNLOAD SO FAZ DOWNLOAD
#CONVERTER PRA DBF
#CONVERTER PRA CSV

# #PROBLEMA# LOCAL PRA ONDE ELE BAIXA SOBRESCREVER
#@TODO : CRIAR PASTAS
#run : python3.6 sinasc.py SP 2016 SINASC

#@TODO : CHECAR POR ERROS, ISSO EH IMPORTANTE K7

