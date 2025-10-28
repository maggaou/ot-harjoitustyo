import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)
    
    def test_luodun_kassapaatteen_rahamaara_on_luku(self):
        self.assertTrue(isinstance(self.kassapaate.kassassa_rahaa_euroina(), (int, float)))

    def test_luodun_kassapaatteen_rahamaara_on_1000euroa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)