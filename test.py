from app import app
import unittest

class Test(unittest.TestCase):
    
    def setUp(self):
        # cria uma instancia do unittest, precisa do nome "setUp"
        self.app = app.test_client()

    def test_requisicao(self):
        # envia uma requisicao GET para a URL
        result = self.app.get('/')

        # compara o status da requisicao (precisa ser igual a 200)
        self.assertEqual(result.status_code, 200) 

    def test_conteudo(self):
        # envia uma requisicao GET para a URL
        result = self.app.get('/') 

        # verifica o retorno do conteudo da pagina
        self.assertRegex(result.data.decode(), "Seja bem vindo ao meu portifolio DevOps :D")


if __name__ == "__main__":
    print ('INICIANDO O TESTE')
    print('----------------------------------------------------------------------')
    unittest.main(verbosity=2)
