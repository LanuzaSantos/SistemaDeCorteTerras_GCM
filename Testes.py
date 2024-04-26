import unittest
from datetime import datetime

from main import Funcionario, Motorista, Veiculo, Propriedade, Agricultor

class TestClasses(unittest.TestCase):

    def test_funcionario(self):
        # Teste para a classe Funcionario
        funcionario = Funcionario("João", 30, "12345", "123.456.789-00")

        self.assertEqual(funcionario.getNome(), "João")
        self.assertEqual(funcionario.getIdade(), 30)
        self.assertEqual(funcionario.getMatricula(), "12345")
        self.assertEqual(funcionario.getCpf(), "123.456.789-00")

    def test_motorista(self):
        # Teste para a classe Motorista
        funcionario = Funcionario("João", 30, "12345", "123.456.789-00")
        veiculo = Veiculo("ABC1234", "Fusca")
        motorista = Motorista(funcionario, "CNH123", veiculo)

        self.assertEqual(motorista.getCnh(), "CNH123")
        self.assertEqual(motorista.funcionario, funcionario)
        self.assertEqual(motorista.veiculo, veiculo)

    def test_veiculo(self):
        # Teste para a classe Veiculo
        veiculo = Veiculo("ABC1234", "Fusca")

        self.assertEqual(veiculo.getPlaca(), "ABC1234")
        self.assertEqual(veiculo.getModelo(), "Fusca")

    def test_propriedade(self):
        # Teste para a classe Propriedade
        propriedade = Propriedade("Fazenda Felicidade", "Rua A", "Centro", "123", "12345-678")

        self.assertEqual(propriedade.nome_propriedade, "Fazenda Felicidade")
        self.assertEqual(propriedade.nome_rua, "Rua A")
        self.assertEqual(propriedade.bairro, "Centro")
        self.assertEqual(propriedade.numero, "123")
        self.assertEqual(propriedade.cep, "12345-678")

    def test_agricultor(self):
        # Teste para a classe Agricultor
        propriedade = Propriedade("Fazenda Felicidade", "Rua A", "Centro", "123", "12345-678")
        agricultor = Agricultor("José", datetime(1980, 1, 1), "987.654.321-00", propriedade)

        self.assertEqual(agricultor.nome, "José")
        self.assertEqual(agricultor.data_nascimento, datetime(1980, 1, 1))
        self.assertEqual(agricultor.cpf, "987.654.321-00")
        self.assertEqual(agricultor.Propriedade, propriedade)

if __name__ == '__main__':
    unittest.main()