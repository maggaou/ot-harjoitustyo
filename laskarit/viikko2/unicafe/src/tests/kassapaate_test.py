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

    def test_luodun_kassapaatteen_lounaiden_lukumaara_on_nolla(self):
        lounaat_lkm = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(lounaat_lkm, 0)