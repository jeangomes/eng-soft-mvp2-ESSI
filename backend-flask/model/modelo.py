import numpy as np
import pickle
import joblib


class Model:

    def carrega_modelo(path):
        """Dependendo se o final for (.pkl) ou (.joblib), carregamos
        """

        if path.endswith('.pkl'):
            model = pickle.load(open(path, 'rb'))
        elif path.endswith('.joblib'):
            model = joblib.load(path)
        else:
            raise Exception('Formato de arquivo não suportado')
        return model

    def preditor(model, input_data):
        """Realiza a predição de um paciente com base no modelo treinado
        """
        x_input = np.asarray(input_data)
        # Faremos o reshape para que o modelo entenda que estamos passando
        diagnosis = model.predict(x_input.reshape(1, -1))
        return int(diagnosis[0])