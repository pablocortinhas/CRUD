from PyQt5 import  uic,QtWidgets

# O título é identificado por: lineEdit_0
def funcao_principal():
    linha1 = formulario.lineEdit_1.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()
    linha4 = formulario.lineEdit_4.text()
    linha5 = formulario.lineEdit_5.text()

    print("Código:",linha1)
    print("Nome:",linha2)
    print("Descricao:",linha3)
    print("Estoque:",linha4)
    print("Preço:",linha5)

app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()
