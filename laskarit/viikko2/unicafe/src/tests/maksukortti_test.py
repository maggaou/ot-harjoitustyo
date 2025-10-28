import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_alkusaldo_on_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10)

    def test_kortin_str_metodi_on_toimiva(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_palauttaa_true_jos_kortilla_on_katetta(self):
        self.assertEqual(self.maksukortti.ota_rahaa(200), True)

    def test_ota_rahaa_palauttaa_false_jos_kortilla_ei_ole_katetta(self):
        self.assertEqual(self.maksukortti.ota_rahaa(2000), False)

    def test_ota_rahaa_muuttaa_kortin_saldoa_jos_kortilla_on_katetta(self):
        self.maksukortti.ota_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 8.0)

    def test_ota_rahaa_ei_muuta_kortin_saldoa_jos_kortilla_ei_ole_katetta(self):
        self.maksukortti.ota_rahaa(10000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataa_rahaa_muuttaa_saldoa(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(self.maksukortti.saldo_euroina(), 12.0)