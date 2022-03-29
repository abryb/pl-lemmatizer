import unittest
from lemmatizer import Lemmatizer

dags_to_filter = [(0, 1, ('Kaczorowski', 'Kaczorowski', 'subst:sg:nom:m1', ['nazwisko'], []), '1.0000', None, 'disamb'), (0, 1, ('Kaczorowski', 'Kaczorowski', 'subst:sg:voc:m1', ['nazwisko'], []), '0.0000', None, None), (1, 2, ('na', 'na:I', 'interj', [], []), '0.0000', None, None), (1, 2, ('na', 'na:P', 'prep:acc', [], []), '0.9998', None, 'disamb'), (1, 2, ('na', 'na:P', 'prep:loc', [], []), '0.0002', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:acc:f:rec:ncol', [], []), '0.0000', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:acc:m2:rec:ncol', [], []), '0.0000', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:acc:m3:rec:ncol', [], []), '0.9999', None, 'disamb'), (2, 3, ('siedem', 'siedem', 'num:pl:acc:n:rec:ncol', [], []), '0.0000', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:nom:f:rec:ncol', [], []), '0.0000', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:nom:m2:rec:ncol', [], []), '0.0000', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:nom:m3:rec:ncol', [], []), '0.0000', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:nom:n:rec:ncol', [], []), '0.0000', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:voc:f:rec:ncol', [], []), '0.0000', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:voc:m2:rec:ncol', [], []), '0.0000', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:voc:m3:rec:ncol', [], []), '0.0001', None, None), (2, 3, ('siedem', 'siedem', 'num:pl:voc:n:rec:ncol', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:acc:m1:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:gen:f:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:gen:m1:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:gen:m2:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:gen:m3:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:gen:n:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:loc:f:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:loc:m1:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:loc:m2:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:loc:m3:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:A', 'adj:pl:loc:n:pos', [], []), '0.0000', None, None), (3, 4, ('karnych', 'karny:S', 'subst:pl:gen:m2', ['nazwa_pospolita'], ['sport.']), '0.0000', None, None), (3, 4, ('karnych', 'karny:S', 'subst:pl:gen:m3', ['nazwa_pospolita'], ['sport.']), '0.9996', None, 'disamb'), (3, 4, ('karnych', 'karny:S', 'subst:pl:loc:m2', ['nazwa_pospolita'], ['sport.']), '0.0000', None, None), (3, 4, ('karnych', 'karny:S', 'subst:pl:loc:m3', ['nazwa_pospolita'], ['sport.']), '0.0004', None, None), (4, 5, (',', ',', 'interp', [], []), '1.0000', None, 'disamb'), (5, 6, ('siedem', 'siedem', 'num:pl:acc:f:rec:ncol', [], []), '0.0000', None, None), (5, 6, ('siedem', 'siedem', 'num:pl:acc:m2:rec:ncol', [], []), '0.0000', None, None), (5, 6, ('siedem', 'siedem', 'num:pl:acc:m3:rec:ncol', [], []), '0.8126', None, 'disamb'), (5, 6, ('siedem', 'siedem', 'num:pl:acc:n:rec:ncol', [], []), '0.0000', None, None), (5, 6, ('siedem', 'siedem', 'num:pl:nom:f:rec:ncol', [], []), '0.0000', None, None), (5, 6, ('siedem', 'siedem', 'num:pl:nom:m2:rec:ncol', [], []), '0.0000', None, None), (5, 6, ('siedem', 'siedem', 'num:pl:nom:m3:rec:ncol', [], []), '0.1874', None, None), (5, 6, ('siedem', 'siedem', 'num:pl:nom:n:rec:ncol', [], []), '0.0000', None, None), (5, 6, ('siedem', 'siedem', 'num:pl:voc:f:rec:ncol', [], []), '0.0000', None, None), (5, 6, ('siedem', 'siedem', 'num:pl:voc:m2:rec:ncol', [], []), '0.0000', None, None), (5, 6, ('siedem', 'siedem', 'num:pl:voc:m3:rec:ncol', [], []), '0.0000', None, None), (5, 6, ('siedem', 'siedem', 'num:pl:voc:n:rec:ncol', [], []), '0.0000', None, None), (6, 7, ('razy', 'raz:Sm3~a~u', 'subst:pl:acc:m3', ['nazwa_pospolita'], []), '0.0379', None, None), (6, 7, ('razy', 'raz:Sm3~a~u', 'subst:pl:gen:m3', ['nazwa_pospolita'], ['po_liczebniku']), '0.9621', None, 'disamb'), (6, 7, ('razy', 'raz:Sm3~a~u', 'subst:pl:nom:m3', ['nazwa_pospolita'], []), '0.0000', None, None), (6, 7, ('razy', 'raz:Sm3~a~u', 'subst:pl:voc:m3', ['nazwa_pospolita'], []), '0.0000', None, None), (6, 7, ('razy', 'raz:Sm3~u', 'subst:pl:acc:m3', ['nazwa_pospolita'], []), '0.0379', None, None), (6, 7, ('razy', 'raz:Sm3~u', 'subst:pl:nom:m3', ['nazwa_pospolita'], []), '0.0000', None, None), (6, 7, ('razy', 'raz:Sm3~u', 'subst:pl:voc:m3', ['nazwa_pospolita'], []), '0.0000', None, None), (7, 8, ('przed', 'przed', 'prep:acc:nwok', [], []), '0.0000', None, None), (7, 8, ('przed', 'przed', 'prep:inst:nwok', [], []), '1.0000', None, 'disamb'), (8, 9, ('strałem', 'strałem', 'brev:pun', [], []), '0.0000', None, None), (8, 9, ('strałem', 'strałem', 'ger:sg:inst:n:perf:aff', [], []), '0.0000', None, None), (8, 9, ('strałem', 'strałem', 'pact:sg:inst:m3:imperf:aff', [], []), '0.0000', None, None), (8, 9, ('strałem', 'strałem', 'ppas:pl:inst:f:perf:aff', [], []), '0.0000', None, None), (8, 9, ('strałem', 'strałem', 'ppas:sg:inst:m3:perf:aff', [], []), '0.0000', None, None), (8, 9, ('strałem', 'strałem', 'ppron3:sg:inst:f:ter:akc:praep', [], []), '0.0000', None, None), (8, 9, ('strałem', 'strałem', 'subst:pl:inst:m3', [], []), '0.0007', None, None), (8, 9, ('strałem', 'strałem', 'subst:pl:inst:n:pt', [], []), '0.0000', None, None), (8, 9, ('strałem', 'strałem', 'subst:sg:inst:m1', [], []), '0.0002', None, None), (8, 9, ('strałem', 'strałem', 'subst:sg:inst:m3', [], []), '0.9991', None, 'disamb'), (8, 9, ('strałem', 'strałem', 'ign', [], []), '0.0000', None, None), (9, 10, ('w', 'w', 'prep:acc:nwok', [], []), '0.9985', None, 'disamb'), (9, 10, ('w', 'w', 'prep:loc:nwok', [], []), '0.0015', None, None), (10, 11, ('swoje', 'swoje', 'subst:pl:acc:n:ncol', ['nazwa_pospolita'], []), '0.0000', None, None), (10, 11, ('swoje', 'swoje', 'subst:pl:nom:n:ncol', ['nazwa_pospolita'], []), '0.0000', None, None), (10, 11, ('swoje', 'swoje', 'subst:pl:voc:n:ncol', ['nazwa_pospolita'], []), '0.0000', None, None), (10, 11, ('swoje', 'swoje', 'subst:sg:acc:n:ncol', ['nazwa_pospolita'], []), '0.0003', None, None), (10, 11, ('swoje', 'swoje', 'subst:sg:nom:n:ncol', ['nazwa_pospolita'], []), '0.0000', None, None), (10, 11, ('swoje', 'swoje', 'subst:sg:voc:n:ncol', ['nazwa_pospolita'], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:acc:f:pos', [], []), '0.0008', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:acc:m2:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:acc:m3:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:acc:n:pos', [], []), '0.0001', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:nom:f:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:nom:m2:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:nom:m3:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:nom:n:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:voc:f:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:voc:m2:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:voc:m3:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:pl:voc:n:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:sg:acc:n:pos', [], []), '0.9988', None, 'disamb'), (10, 11, ('swoje', 'swój', 'adj:sg:nom:n:pos', [], []), '0.0000', None, None), (10, 11, ('swoje', 'swój', 'adj:sg:voc:n:pos', [], []), '0.0000', None, None), (11, 12, ('lewo', 'lewa', 'subst:sg:voc:f', ['nazwa_pospolita'], []), '0.0000', None, None), (11, 12, ('lewo', 'lewo:D', 'adv:pos', [], []), '0.0019', None, None), (11, 12, ('lewo', 'lewo:S', 'subst:sg:acc:n:ncol', ['nazwa_pospolita'], []), '0.9981', None, 'disamb'), (11, 12, ('lewo', 'lewo:S', 'subst:sg:nom:n:ncol', ['nazwa_pospolita'], []), '0.0000', None, None), (11, 12, ('lewo', 'lewo:S', 'subst:sg:voc:n:ncol', ['nazwa_pospolita'], []), '0.0000', None, None), (12, 13, ('.', '.', 'interp', [], []), '1.0000', 'eos', 'disamb'), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:pl:acc:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:pl:dat:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:pl:gen:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:pl:inst:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:pl:loc:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:pl:nom:f', ['nazwisko'], []), '0.0002', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:pl:voc:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:sg:acc:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:sg:dat:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:sg:gen:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:sg:inst:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:sg:loc:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:sg:nom:f', ['nazwisko'], []), '0.0107', None, None), (13, 14, ('Śmiech', 'Śmiech:Sf', 'subst:sg:voc:f', ['nazwisko'], []), '0.0000', None, None), (13, 14, ('Śmiech', 'Śmiech:Sm1', 'subst:sg:nom:m1', ['nazwisko'], []), '0.7480', None, 'disamb'), (13, 14, ('Śmiech', 'śmiech:S', 'subst:sg:acc:m3', ['nazwa_pospolita'], []), '0.0004', None, None), (13, 14, ('Śmiech', 'śmiech:S', 'subst:sg:nom:m3', ['nazwa_pospolita'], []), '0.2406', None, None), (13, 14, ('Śmiech', 'śmiech:V', 'pred', [], []), '0.0000', None, None), (14, 15, ('z', 'z:P', 'prep:gen:nwok', [], []), '0.0000', None, None), (14, 15, ('z', 'z:P', 'prep:inst:nwok', [], []), '1.0000', None, 'disamb'), (14, 15, ('z', 'z:T', 'part:nwok', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:pl:dat:f:pos', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:pl:dat:m1:pos', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:pl:dat:m2:pos', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:pl:dat:m3:pos', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:pl:dat:n:pos', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:sg:inst:m1:pos', [], []), '0.9997', None, 'disamb'), (15, 16, ('takim', 'taki:A', 'adj:sg:inst:m2:pos', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:sg:inst:m3:pos', [], []), '0.0003', None, None), (15, 16, ('takim', 'taki:A', 'adj:sg:inst:n:pos', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:sg:loc:m1:pos', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:sg:loc:m2:pos', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:sg:loc:m3:pos', [], []), '0.0000', None, None), (15, 16, ('takim', 'taki:A', 'adj:sg:loc:n:pos', [], []), '0.0000', None, None), (16, 17, ('bramkarzem', 'bramkarz', 'subst:sg:inst:m1', ['nazwa_pospolita'], []), '1.0000', None, 'disamb'), (17, 18, ('na', 'na:I', 'interj', [], []), '0.0000', None, None), (17, 18, ('na', 'na:P', 'prep:acc', [], []), '1.0000', None, 'disamb'), (17, 18, ('na', 'na:P', 'prep:loc', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:acc:f:pos', [], []), '0.0950', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:acc:m2:pos', [], []), '0.0175', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:acc:m3:pos', [], []), '0.1088', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:acc:n:pos', [], []), '0.0794', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:nom:f:pos', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:nom:m2:pos', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:nom:m3:pos', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:nom:n:pos', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:voc:f:pos', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:voc:m2:pos', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:voc:m3:pos', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:A', 'adj:pl:voc:n:pos', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:A', 'adj:sg:acc:n:pos', [], []), '0.6950', None, 'disamb'), (18, 19, ('karne', 'karny:A', 'adj:sg:nom:n:pos', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:A', 'adj:sg:voc:n:pos', [], []), '0.0000', None, None), (18, 19, ('karne', 'karny:S', 'subst:pl:acc:m2', ['nazwa_pospolita'], ['sport.']), '0.0005', None, None), (18, 19, ('karne', 'karny:S', 'subst:pl:acc:m3', ['nazwa_pospolita'], ['sport.']), '0.0038', None, None), (18, 19, ('karne', 'karny:S', 'subst:pl:nom:m2', ['nazwa_pospolita'], ['sport.']), '0.0000', None, None), (18, 19, ('karne', 'karny:S', 'subst:pl:nom:m3', ['nazwa_pospolita'], ['sport.']), '0.0000', None, None), (18, 19, ('karne', 'karny:S', 'subst:pl:voc:m2', ['nazwa_pospolita'], ['sport.']), '0.0000', None, None), (18, 19, ('karne', 'karny:S', 'subst:pl:voc:m3', ['nazwa_pospolita'], ['sport.']), '0.0000', None, None), (19, 20, ('.', '.', 'interp', [], []), '1.0000', 'eos', 'disamb'), '', '']
dags_to_filter_idx_0 = [(0, 1, ('Kaczorowski', 'Kaczorowski', 'subst:sg:nom:m1', ['nazwisko'], []), '1.0000', None, 'disamb'), (0, 1, ('Kaczorowski', 'Kaczorowski', 'subst:sg:voc:m1', ['nazwisko'], []), '0.0000', None, None)]
dags = [
    (0, 1, ('Jasiek', 'Jasiek:Sm1', 'subst:sg:nom:m1', ['imię', 'nazwisko'], []), '0.9989', None, 'disamb'),
    (0, 1, ('Jasiek', 'jasiek', 'subst:sg:nom:m3', ['nazwa_pospolita'], []), '0.0011', None, None),
    (1, 2, ('upadł', 'upaść:Vp~dnę', 'praet:sg:m1:perf', [], []), '0.9989', None, 'disamb'),
    (1, 2, ('upadł', 'upaść:Vp~dnę', 'praet:sg:m3:perf', [], []), '0.0011', None, None)
]

dag1, dag2, dag3, dag4 = dags

lemmatizer = Lemmatizer()

class TestUtil(unittest.TestCase):
    def test_lemma_from_dag(self):
        self.assertEqual('Jasiek', lemmatizer.dag_lemma(dag1))

    def test_dags_for_idx(self):
        self.assertEqual([dag1, dag2], lemmatizer.dags_for_idx(dags, 0))
        self.assertEqual([dag3, dag4], lemmatizer.dags_for_idx(dags, 1))
        self.assertEqual([], lemmatizer.dags_for_idx(dags, 2))
        self.assertEqual(dags_to_filter_idx_0, lemmatizer.dags_for_idx(dags_to_filter, 0))

    def test_most_probable_dag(self):
        self.assertEqual(dag1, lemmatizer.most_probable_dag([dag1, dag2]))

    def test_most_probable_lemmas(self):
        self.assertEqual(['Jasiek', 'upaść'], lemmatizer.most_probable_lemmas(dags))

if __name__ == '__main__':
    unittest.main()