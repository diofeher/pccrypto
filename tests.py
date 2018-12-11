import unittest
from pccrypto import PCCrypto


class TestCrypto(unittest.TestCase):
    def setUp(self):
        self.crypto = PCCrypto()

    def test_simple_encrypt(self):
        self.assertEqual(self.crypto.encrypt('salve irs'), '4M9CK9F7CK XT6594M')
    
    def test_decrypt_simple_word(self):
        self.assertEqual(self.crypto.decrypt('4M9CK9F7CK'), 'salve')

    def test_decrypt_text(self):
        text = '4M9CK9F7CK XT6594M P29C 659HN9C (A)'
        decoded = 'salve irs da rua (A)'
        self.assertEqual(self.crypto.decrypt(text), decoded)
    
if __name__ == "__main__":
    unittest.main()