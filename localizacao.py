from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
import sys 

class localizar(QWidget):
    def __init__(self):
        super().__init__()

        # Vamos ajustar a geometria da tela
        # Setando valores da posição x e y, além da largura e altura
        self.setGeometry(500,30,400,300)

        # Texto para a barra de título
        self.setWindowTitle("Localização")
        
        # Gerenciador de layout vertical
        self.layout_v = QVBoxLayout()

        # Labels para os dados do produto
        self.label_id = QLabel("ID do Produto:")
        self.label_id.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para cadastrar a empresa onde está o produto
        self.label_emp = QLabel("Empresa:")
        self.label_emp.setStyleSheet("QLabel{font-size:12pt}")
        
        # Labels para cadastrar o logradouro
        self.label_log = QLabel("Logradouro:")
        self.label_log.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para cadastrar o número do produto
        self.label_num = QLabel("Número:")
        self.label_num.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para cadastrar o Prédio do produto
        self.label_pred = QLabel("Prédio:")
        self.label_pred.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para cadastrar o andar do produto
        self.label_and = QLabel("Andar:")
        self.label_and.setStyleSheet("QLabel{font-size:12pt}")

        # Labels para cadastrar a sala do produto
        self.label_sala = QLabel("Sala:")
        self.label_sala.setStyleSheet("QLabel{font-size:12pt}")

        # LineEdit para o id do produto
        self.edit_id = QLineEdit()
        self.edit_id.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para a empresa
        self.edit_emp = QLineEdit()
        self.edit_emp.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o logradouro
        self.edit_log = QLineEdit()
        self.edit_log.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o número
        self.edit_num = QLineEdit()
        self.edit_num.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o prédio
        self.edit_pred = QLineEdit()
        self.edit_pred.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para o andar
        self.edit_and = QLineEdit()
        self.edit_and.setStyleSheet("QLineEdit{font-size:12pt}")

        # LineEdit para a sala
        self.edit_sala = QLineEdit()
        self.edit_sala.setStyleSheet("QLineEdit{font-size:12pt}")
        
        self.button = QPushButton("Cadastrar")
        self.button.setStyleSheet("QPushButton{background-color:green;color:white;font-size:12pt;font-weight:bold}")

        # Chamar a função de cadastro do cliente ao clicar no botão
        self.button.clicked.connect(self.cadastrar)

        # Adicionar a label o ID e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_id)
        self.layout_v.addWidget(self.edit_id)

        # Adicionar a label o emp e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_emp)
        self.layout_v.addWidget(self.edit_emp)
        
        # Adicionar a label o log e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_log)
        self.layout_v.addWidget(self.edit_log)

        # Adicionar a label o num e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_num)
        self.layout_v.addWidget(self.edit_num)

        # Adicionar a label o pred e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_pred)
        self.layout_v.addWidget(self.edit_pred)

        # Adicionar a label a and e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_and)
        self.layout_v.addWidget(self.edit_and)

        # Adicionar a label o sala e o LineEdit ao layout vertical 
        self.layout_v.addWidget(self.label_sala)
        self.layout_v.addWidget(self.edit_sala)

        self.layout_v.addWidget(self.button)
        

        # Adicionar o layout_v a tela
        self.setLayout(self.layout_v)
    
    def cadastrar(self):
        # vamos criar uma variavel que fará referência ao um arquivo de texto
        arquivo = open("Localização.txt" ,"+a")
        arquivo.write(f"ID: {self.edit_id.text()}/n")
        arquivo.write("-----")
        arquivo.write(f"Empresa: {self.edit_emp.text()}/n")
        arquivo.write("-----")
        arquivo.write(f"Logradouro: {self.edit_log.text()}/n")
        arquivo.write("-----")
        arquivo.write(f"Número: {self.edit_num.text()}/n")
        arquivo.write("-----")
        arquivo.write(f"Prédio: {self.edit_pred.text()}/n")
        arquivo.write("-----")
        arquivo.write(f"Andar: {self.edit_and.text()}/n")
        arquivo.write("-----")
        arquivo.write(f"Sala: {self.edit_sala.text()}/n")
        arquivo.write("------------------------------------------------------------")
        arquivo.close()
        
#app = QApplication(sys.argv)
# Em instância da classe  CadastroCliente para iniciar a janela

#tela = localizar()
# Exibir  a tela durante a execução 
#tela.show()
# Ao clicar no botão fechar a tela deve fechar e sair da memória

#app.exec()