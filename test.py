from app import app
import unittest

class Test(unittest.TestCase):
    
    def setUp(self):
<<<<<<< HEAD
        # cria uma instância do unittest, precisa do nome "setUp"
=======
        # cria uma instancia do unittest, precisa do nome "setUp"
>>>>>>> 30d81b31546cdd5ca68b67de6bef3795f12e0451
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
<<<<<<< HEAD
        self.assertRegex(result.data.decode(), "Escreva uma Mensagem para o Cabeçalho da Página.")
=======
        self.assertRegex(result.data.decode(), "Escreva uma Mensagem para o Cabecalho da Pagina.")
>>>>>>> 30d81b31546cdd5ca68b67de6bef3795f12e0451


if __name__ == "__main__":
    print ('INICIANDO OS TESTES')
    print('----------------------------------------------------------------------')
    unittest.main(verbosity=2)