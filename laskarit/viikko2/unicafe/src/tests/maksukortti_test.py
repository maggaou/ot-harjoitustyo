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
