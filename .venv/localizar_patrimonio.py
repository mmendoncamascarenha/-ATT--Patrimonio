from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys 
import csv

class localizar_patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        #ajuste da tela
        self.setGeometry(500,300,400,300)

        #texto para a barra
        self.setWindowTitle("Patrimônio")

        #Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()
       
       
        #os dados dos equipamentos
        self.label_id = QLabel("ID do equipamento:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")









        #dados dos equipamentos
        self.label_numero = QLabel("Número de série:")
        self.label_numero.setStyleSheet("QLabel{font-size:12pt}")

        #dados dos equipamentos
        self.label_nome = QLabel("nome do patrimônio:")
        self.label_nome.setStyleSheet("QLabel{font-size:12pt}")

        #dados dos equipamentos
        self.label_tipo = QLabel("tipo do patrimônio:")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")

        #dados dos equipamentos
        self.label_descricao = QLabel("Descrição do equipamento:")
        self.label_descricao.setStyleSheet("QLabel{font-size:12pt}")

        #dados dos equipamentos
        self.label_localizacao = QLabel("Localização do produto:")
        self.label_localizacao.setStyleSheet("QLabel{font-size:12pt}")

        #dados dos equipamentos
        self.label_fabricacao = QLabel("Data de Fabricação:")
        self.label_fabricacao.setStyleSheet("QLabel{font-size:12pt}")

        #dados dos equipamentos]
        self.label_aquisicao = QLabel("Data de Aquisição:")
        self.label_aquisicao.setStyleSheet("QLabel{font-size:12pt}")

##########################################################################################################################################################
        # LineEdit para o id  
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o numero do produto
        self.edit_numero = QLineEdit()
        self.edit_numero.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o nome do produto 
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o tipo do produto
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para a descrição do produto
        self.edit_descricao = QLineEdit()
        self.edit_descricao.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para a localização do produto 
        self.edit_localizacao = QLineEdit()
        self.edit_localizacao.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para a data da fabricação
        self.edit_fabricacao = QLineEdit()
        self.edit_fabricacao.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o nome do cliente 
        self.edit_aquisicao= QLineEdit()
        self.edit_aquisicao.setStyleSheet("QLineEdit{font-size:12pt}")
##########################################################################################################################################################
        

        #Adicionar a label o nome e o lineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)
        self.btnbuscar = QPushButton("Buscar Patrimônio")
        self.layout_v.addWidget(self.btnbuscar)
        self.btnbuscar.clicked.connect(self.localizar)
        #Adicionar a label o nome e o lineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_numero)
        self.layout_v.addWidget(self.edit_numero)

        #Adicionar a label o nome e o lineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        #Adicionar a label o nome e o lineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        #Adicionar a label o nome e o lineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_descricao)
        self.layout_v.addWidget(self.edit_descricao)

        #Adicionar a label o nome e o lineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_localizacao)
        self.layout_v.addWidget(self.edit_localizacao)
        
        #Adicionar a label o nome e o lineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_fabricacao)
        self.layout_v.addWidget(self.edit_fabricacao)

        #Adicionar a label o nome e o lineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_aquisicao)
        self.layout_v.addWidget(self.edit_aquisicao)
  
        #adicionar o layout_v a tela
        self.setLayout(self.layout_v)
    
    def localizar(self):
        # abrir o arquivo csv e atribuir a uma variavel
        arquivo = open("cadastros.csv","r",encoding="utf8")
        linhas = csv.reader(arquivo) 



        for i in linhas: 
            lin = str(i).replace("['","").replace("']","").split(";")
            if(lin[0]==self.edit_id.text()):
                self.edit_numero.setText(lin[1])
                self.edit_nome.setText(lin[2])
                self.edit_tipo.setText(lin[3])
                self.edit_descricao.setText(lin[4])
                self.edit_localizacao.setText(lin[5])
                self.edit_fabricacao.setText(lin[6])
                self.edit_aquisicao.setText(lin[7]) 

#app = QApplication(sys.argv)
#para iniciar a tela
#tela =Patrimonio()
#exibir a tela
#tela.show()
#fechar e sair da memoria
#app.exec()