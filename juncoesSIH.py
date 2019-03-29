from pymongo import MongoClient

#pega a database 
projeto=MongoClient().projeto

#indexa o campo que sofrera a primeira juncao, que deve ser a juncao mais cara computacionalmente
projeto.sih.create_index("CODMUNNASC") 

#array com as juncoes a serem feitas
pipeline=[]

#projecao que seleciona campos usados
camposUsados={'APGAR1':1,'APGAR5':1,'CODANOMAL':1,'CODBAINASC ':1,'CODBAIRES':1,'CODESTAB':1,'CODMUNNASC':1,'CODMUNNATU':1,'CODMUNRES':1,'CODPAISRES':1,
				'CODUFNATU':1,'CONSULTAS':1,'DTNASC':1,'DTNASCMAE':1,'DTULTMENST':1,'ESCMAE':1,'ESCMAE2010':1,'ESCMAEAGR1':1,'ESTCIVMAE':1,'GESTACAO':1,
				'GRAVIDEZ':1,'HORANASC':1,'IDADEMAE':1,'IDADEPAI':1,'IDANOMAL':1,'LOCNASC':1,'MESPRENAT':1,'NATURALMAE':1,'NUMERODN':1,'PARTO':1,'PESO':1,
				'QTDFILMORT':1,'QTDFILVIVO':1,'QTDGESTANT':1,'QTDPARTCES':1,'QTDPARTNOR ':1,'RACACOR ':1,'RACACORMAE ':1,'SEXO':1,'SEMAGESTAC':1,
				'SERIECMAE':1,'STCESPARTO':1,'STDNEPIDEM':1,'STDNNOVA':1,'STTRABPART':1,'TPAPRESENT':1,'TPMETESTIM':1,'TPNASCCASSI':1}

project={ "$project" : camposUsados}
pipeline.append(project)

#juncao de MUNICBR- codmunnasc
projeto["municbr_cnv"].create_index("codigo")
lookup={"$lookup": { "from": "municbr_cnv", "localField": "CODMUNNASC", "foreignField": "codigo", "as": "CODMUNNASC"}}
unwind1={ "$addFields": {"CODMUNNASC": { "$arrayElemAt": [ "$CODMUNNASC", 0 ] }}}
pipeline.append(lookup)
project1={ "$project" : {"CODMUNNASC._id" : 0}} #tira id, projeta codmunnasc ocm zero

#juncao de CODESTAB - campo de juncao codigo
projeto['estab06_cnv'].create_index("codigo")
lookup={"$lookup": { "from": 'estab06_cnv', "localField": "CODESTAB", "foreignField": "codigo", "as": "CODESTAB"}}
unwind2={ "$addFields": {"CODESTAB": { "$arrayElemAt": [ "$CODESTAB", 0 ] }}}
pipeline.append(lookup)
project2={ "$project" : {"CODESTAB._id" : 0}}

#juncao de PESO - campo de juncao codigo
projeto['peso_cnv'].create_index("codigo")
lookup={"$lookup": { "from": 'peso_cnv', "localField": "PESO", "foreignField": "codigo", "as": "PESO"}}
unwind3={ "$addFields": {"PESO": { "$arrayElemAt": [ "$PESO", 0 ] }}}
pipeline.append(lookup)
project3={ "$project" : {"PESO._id" : 0}}





#executa os unwinds para retirar dos arrays os dados
pipeline.append(unwind1)
pipeline.append(unwind2)
pipeline.append(unwind3)


pipeline.append(project1)
pipeline.append(project2)
pipeline.append(project3)


out={ "$out" : "sinasc_completa" }
pipeline.append(out)

#agregacao onde ocorrem as juncoes
projeto.sinasc15_inicial.aggregate(pipeline)

cursor=projeto.sinasc_completa.find()
if __name__ == '__main__':
	i=0
	saida=open("juncoes.out","w")
	for ele in cursor:
		#print(ele)
		if(i==100):break
		saida.write(str(ele)+"\n")
		i=i+1
	saida.close()

