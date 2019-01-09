# datasus_collection

Em constande desenvolvimento 
===================================

1.0 : Objetivo principal
-----------------------------------
    > Swear by god, I don't know

1.1 : Programas/pacotes necessários 
------------------------------------      
    > mongodb
    > python3
    > pip 
    > libs do python  :
        > pysus (  pip install pysus --user )
 
1.2 : Fonte dos dados
------------------------------------   
[http://www2.datasus.gov.br/DATASUS/index.php?area=0901](http://www2.datasus.gov.br/DATASUS/index.php?area=0901). 
As tabelas que utilazamos são : 
        SIM = acho que é o numero de nascidos mortos  
        
        SINASC =  Número de nascidos vivos 
        algo me diz que para a sinasc também será preciso da CNES
        vamos precisar usar a cnes e a uf   (tabelas de junção ) 
  
  
  Os arquivos : (cnes,uf)?_campos_utilizados podem precisar de alterações


1.3 : Problema Inicial : 
------------------------------------   
O problema inicial que tivemos foi encontrar uma melhor forma de pegar os dados do datasus e importá-los para o mongodb

1.4 : Preparação dos dados : 
------------------------------------  
A princípio será feito para a tabela SINASC, em breve, SIM. 
Acredito que o grande problema seja saber os campos que devemos usar.







1.5 : 
------------------------------------  
1.6 : 
------------------------------------  

1.7 : 
------------------------------------  
1.8 : 
------------------------------------  
X.X : Site utilizado para documentação oficial
------------------------------------   

 [https://sites.google.com/a/ntt.ufrj.br/dados-na-saude-coletiva/?pli=1](https://sites.google.com/a/ntt.ufrj.br/dados-na-saude-coletiva/?pli=1). 
    > (such old, using webpages, fuck)
