import csv

# abrir o arquivo csv e atribuir a uma variavel
arquivo = open("cadastros.csv","r",encoding="utf8")
linhas = csv.reader(arquivo) 



for i in linhas: 
    lin = str(i).replace("['","").replace("']","").split(";")
    if(lin[0]==self.edit_id.text()):
        print(lin)


