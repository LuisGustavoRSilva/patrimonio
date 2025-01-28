from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
import sys 

class patrimonio(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos ajustar a geometria da tela
        # Setando valores da posição x e y, além da largura e altura
        self.setGeometry(500,30,400,300)

        # Texto para a barra de título
        self.setWindowTitle("Cadastrar Patrimônio")
        
        # Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # Labels para os dados do produto
        self.label_id = QLabel("ID do Produto:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para o número de série dos produtos
        self.label_num = QLabel("Número de série:")
        self.label_num.setStyleSheet("QLabel{font-size:12pt}")
        
        # Labels para os nomes dos produtos
        self.label_nome = QLabel("Nome do Patrimônio:")
        self.label_nome.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para os tipos de produtos
        self.label_tipo = QLabel("Tipo:")
        self.label_tipo.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para a descrição dos produtos
        self.label_desc = QLabel("Descrição:")
        self.label_desc.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para a localozação dos produtos
        self.label_loc = QLabel("Localização:")
        self.label_loc.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para as datas de fabricação dos produtos
        self.label_dataf = QLabel("Data de Fabricação:")
        self.label_dataf.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para as data de aquisição dos produtos
        self.label_dataq = QLabel("Data de Aquisição:")
        self.label_dataq.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o id do produto
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o número de série do produto
        self.edit_num = QLineEdit()
        self.edit_num.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o nome do produto
        self.edit_nome = QLineEdit()
        self.edit_nome.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o tipo do produto
        self.edit_tipo = QLineEdit()
        self.edit_tipo.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para a descrição do produto
        self.edit_desc = QLineEdit()
        self.edit_desc.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para a localização do produto
        self.edit_loc = QLineEdit()
        self.edit_loc.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para a data de fabricação do produto
        self.edit_dataf = QLineEdit()
        self.edit_dataf.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para a data de aquisição do produto
        self.edit_dataq = QLineEdit()
        self.edit_dataq.setStyleSheet("QLineEdit{font-size:12pt}")
        
        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:green;color:white;font-size:12pt;font-weight:bold}")

        # Chamar a função de cadastro do cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)

        # Adicionar a label o ID e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        # Adicionar a label o num e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_num)
        self.layout_v.addWidget(self.edit_num)
        
        # Adicionar a label o nome e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_nome)
        self.layout_v.addWidget(self.edit_nome)

        # Adicionar a label o tipo e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_tipo)
        self.layout_v.addWidget(self.edit_tipo)

        # Adicionar a label o descrição e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_desc)
        self.layout_v.addWidget(self.edit_desc)

        # Adicionar a label a loc e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_loc)
        self.layout_v.addWidget(self.edit_loc)

        # Adicionar a label o data de fabricação e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_dataf)
        self.layout_v.addWidget(self.edit_dataf)

        # Adicionar a label a data de aquisição e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_dataq)
        self.layout_v.addWidget(self.edit_dataq)

        self.layout_v.addWidget(self.button)
        

        # Adicionar o layout_v a tela
        self.setLayout(self.layout_v)
    
    def cadastrar(self):
        if(self.edit_id.text()=="" or
           self.edit_num.text()=="" or
           self.edit_nome.text()=="" or
           self.edit_tipo.text()=="" or
           self.edit_desc.text()=="" or
           self.edit_loc.text()=="" or
           self.edit_dataf.text()=="" or
           self.edit_dataq.text()==""):
           QMessageBox.critical(self,"Erro","Você deve preencher todos os campos")
        
        
        else:
            # vamos criar uma variavel que fará referência ao um arquivo de texto
            arquivo = open("produtos.txt" ,"+a")
            arquivo.write(f"ID: {self.edit_id.text()}/n")
            arquivo.write("-----")
            arquivo.write(f"NUM Serie: {self.edit_num.text()}/n")
            arquivo.write("-----")
            arquivo.write(f"Nome: {self.edit_nome.text()}/n")
            arquivo.write("-----")
            arquivo.write(f"Tipo: {self.edit_tipo.text()}/n")
            arquivo.write("-----")
            arquivo.write(f"Descricao: {self.edit_desc.text()}/n")
            arquivo.write("-----")
            arquivo.write(f"Localização: {self.edit_loc.text()}/n")
            arquivo.write("-----")
            arquivo.write(f"Data Fabricação: {self.edit_dataf.text()}/n")
            arquivo.write("-----")
            arquivo.write(f"Data Aquisição: {self.edit_dataq.text()}/n")
            arquivo.write("------------------------------------------------------------")
            arquivo.close()
            QMessageBox.information(self,"Salvo","Dados Salvos com sucesso")
        
# app = QApplication(sys.argv)
# Em instância da classe  CadastroCliente para iniciar a janela

# tela = patrimonio()
# Exibir  a tela durante a execução 
# tela.show()
# Ao clicar no botão fechar a tela deve fechar e sair da memória

# app.exec()