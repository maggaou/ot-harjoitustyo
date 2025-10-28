import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti_paljon_rahaa = Maksukortti(100*100)
        self.kortti_vahan_rahaa = Maksukortti(0)

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

    def test_syo_edullisesti_kateisella_jos_maksu_on_riittava_niin_kassan_rahamaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000+2.4)

    def test_syo_maukkaasti_kateisella_jos_maksu_on_riittava_niin_kassan_rahamaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000+4.0)

    def test_syo_edullisesti_kateisella_jos_maksu_ei_ole_riittava_niin_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_syo_maukkaasti_kateisella_jos_maksu_ei_ole_riittava_niin_kanssan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000)

    def test_syo_edullisesti_kateisella_jos_maksu_on_riittava_niin_vaihtorahan_suuruus_on_oikein(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 500-240)

    def test_syo_maukkaasti_kateisella_jos_maksu_on_riittava_niin_vaihtorahan_suuruus_on_oikein(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(900)
        self.assertEqual(vaihtoraha, 900-400)

    def test_syo_edullisesti_kateisella_jos_maksu_ei_ole_riittava_niin_palauta_annettu_summa(self):
        summa = 1
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(summa)
        self.assertEqual(vaihtoraha, summa)

    def test_syo_maukkaasti_kateisella_jos_maksu_ei_ole_riittava_niin_palauta_annettu_summa(self):
        summa = 1
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(summa)
        self.assertEqual(vaihtoraha, summa)

    def test_syo_edullisesti_kortilla_jos_kortilla_on_katetta_niin_tee_veloitus_kortilta_ja_palauta_true(self):
        palautus = self.kassapaate.syo_edullisesti_kortilla(self.kortti_paljon_rahaa)
        self.assertEqual(palautus, True)
        self.assertEqual(self.kortti_paljon_rahaa.saldo_euroina(), 100-2.4)

    def test_syo_maukkaasti_kortilla_jos_kortilla_on_katetta_niin_tee_veloitus_kortilta_ja_palauta_true(self):
        palautus = self.kassapaate.syo_maukkaasti_kortilla(self.kortti_paljon_rahaa)
        self.assertEqual(palautus, True)
        self.assertEqual(self.kortti_paljon_rahaa.saldo_euroina(), 100-4.0)

    def test_syo_edullisesti_kortilla_jos_kortilla_on_katetta_niin_kasvata_lounaiden_maaraa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_paljon_rahaa)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_maukkaasti_kortilla_jos_kortilla_on_katetta_niin_kasvata_lounaiden_maaraa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_paljon_rahaa)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_edullisesti_kortilla_jos_kortilla_ei_ole_katetta_niin_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti_vahan_rahaa)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_jos_kortilla_ei_ole_katetta_niin_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti_vahan_rahaa)
        self.assertEqual(self.kassapaate.maukkaat, 0)