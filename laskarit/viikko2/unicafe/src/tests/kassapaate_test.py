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

    def test_syo_edullisesti_kateisella_jos_maksu_on_riittava_niin_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1) 

    def test_syo_maukkaasti_kateisella_jos_maksu_on_riittava_niin_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kateisella_jos_maksu_ei_ole_riittava_niin_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kateisella_jos_maksu_ei_ole_rittava_niin_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)