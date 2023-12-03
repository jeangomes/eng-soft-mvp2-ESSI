from model.avaliador import Avaliador
from model.carregador import Carregador
from model.modelo import Model


# Instanciação das Classes
carregador = Carregador()
modelo = Model()
avaliador = Avaliador()

# Parâmetros
url_dados = "dataset/mydata_autism.csv"
colunas = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'Age', 'Sex', 'Jaundice', 'Family_mem_with_ASD',
           'target_class']

# Carga dos dados
dataset = carregador.carregar_dados(url_dados, colunas)

# Separando em dados de entrada e saída
X = dataset.iloc[:, 0:-1]
Y = dataset.iloc[:, -1]


# Método para testar o modelo usando SVM a partir do arquivo correspondente
def test_modelo_lr():
    # Importando o modelo
    model_path = 'ml_model/tea_classificador_svm_orig.pkl'
    modelo_svm = Model.carrega_modelo(model_path)

    # Obtendo as métricas do SVM
    acuracia_svm, recall_svm, precisao_svm, f1_svm = avaliador.avaliar(modelo_svm, X.values, Y)

    # Testando as métricas para o SVM
    # Modifique as métricas de acordo com seus requisitos
    assert acuracia_svm >= 0.75
    assert recall_svm >= 0.5
    assert precisao_svm >= 0.5
    assert f1_svm >= 0.5
