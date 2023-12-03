from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect

from model import Model
from schemas import *
from flask_cors import CORS

from schemas.crianca import apresenta_crianca

# from schemas.crianca import CriancaViewSchema, CriancaSchema

# Instanciando o objeto OpenAPI
info = Info(title="Minha API", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Definindo tags para agrupamento das rotas
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
crianca_tag = Tag(name="Criança", description="Predição de crianças com TEA")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# Rota de predição de criança com traços de TEA
@app.post('/crianca', tags=[crianca_tag],
          responses={"200": CriancaViewSchema, "400": ErrorSchema, "409": ErrorSchema})
def predict(form: CriancaSchema):
    """Realiza uma nova classificação com os dados informados
    Retorna o nome e a classificação.

    Args:
        name (str): nome do paciente
        preg (int): número de vezes que engravidou: Pregnancies
        plas (int): concentração de glicose no plasma: Glucose
        pres (int): pressão diastólica (mm Hg): BloodPressure

    Returns:
        dict: representação do paciente e diagnóstico associado
        :param form:
    """

    input_string = form.allAnswers
    result_array = []

    for answer in input_string.split(','):
        result_array.append(int(answer))

    result_array.append(form.age)
    result_array.append(form.sex)
    result_array.append(form.jaundice)
    result_array.append(form.family_mem_with_ASD)

    my_tuple = tuple(result_array)
    print(my_tuple)
    # print(len(my_tuple))

    # Carregando modelo
    ml_path = 'ml_model/tea_classificador_svm_orig.pkl'
    modelo = Model.carrega_modelo(ml_path)

    paciente = {
        "name": form.name,
        "outcome": Model.preditor(modelo, my_tuple)
    }
    print('outcome:' + str(paciente["outcome"]))
    return apresenta_crianca(paciente), 200


if __name__ == '__main__':
    app.run()
