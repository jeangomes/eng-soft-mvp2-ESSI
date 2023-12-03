from pydantic import BaseModel


class CriancaSchema(BaseModel):
    """ Define como uma nova criança a ser classificado deve ser representada
    """
    allAnswers: str
    name: str
    age: int
    sex: int
    jaundice: int
    family_mem_with_ASD: int


class CriancaViewSchema(BaseModel):
    """Define como um paciente será retornado
    """
    name: str = "Maria"
    outcome: int = None


# Apresenta o nome e a classificação
def apresenta_crianca(paciente):
    """ Retorna uma representação da predição seguindo o schema definido em
        CriancaViewSchema.
    """
    return {
        "name": paciente["name"],
        "outcome": paciente["outcome"]
    }
