import mysql.connector
dados = mysql.connector.connect(user='root',password='71433969',host='127.0.0.1') #isso aqui conecta no MEU
                                                                             # banco de dados, mas se vc mudar
                                                                            #pros seus dados vc cria um banco pra vc
dadosexp = dados.cursor()
dadosexp.execute("CREATE DATABASE senhas_cripto")

#na estrutura fazer o programa dar call em SQL
#dar call no servidor "senhas_cripto"
#servidor "senhas_cripto" precisa reunir os dados em STR na table "senhas" e separar senha por senha em linhas distintas
#table "senhas" precisa armazanar de forma individual a cada linha (for linhas in senhas_cripto talves?)
#table senhas = [senhas] (precisa ser iteravel)

###dados.close()    # isso aqui usa pra fechar o acesso ao fim da operação