
import pandas as pd
from googletrans import Translator

df = pd.read_csv("20220523-FULL-1_1.csv", sep=';', low_memory=False)
df.dropna(subset=['NameAlias_WholeName'], inplace=True)
df = df.reset_index()

#--| instancia tradutor
translator = Translator()#raise_exception=True)

nao_traduzidos = []
initCounter = (df.shape[0]-1)
for n in range(0,initCounter):
    try: 
        
        traduzido = translator.translate(df['NameAlias_WholeName'][n], dest='en')
        
        idAtual = df['Entity_LogicalId'][n]
        saida = 'ID-EUEA: {}\n'.format( idAtual )
        saida+= 'Lingua Original: {}'.format( df['NameAlias_WholeName'][n] )
        saida+= '\nTraduzido: {}'.format( traduzido.text )
        saida+= '\n------\n'
        
        print( saida )
        
    except:
        print("Eitah ... timeout")
        nao_traduzidos.append(df['NameAlias_WholeName'][n])
        pass

print( "\nNomes não traduzidos devido a timeout: "+str( len(nao_traduzidos) ),'\n'  )
for nnt in nao_traduzidos:
    print(nnt)
