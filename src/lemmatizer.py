from concraft_pl2 import Concraft
from morfeusz2 import Morfeusz


class Lemmatizer():
    def __init__(self, morfeusz: Morfeusz, concraft: Concraft):
        self.concraft = concraft
        self.morfeusz = morfeusz

    def analyse(self, string):
        return self.concraft.disamb(self.morfeusz.analyse(string))

    def lemmatize(self, string):
        dags = self.analyse(string)
        lemmas = self.most_probable_lemmas(dags)
        return ' '.join(lemmas)

    def fast_lemmatize(self, string):
        dags = self.analyse(string)
        lemmas = []
        current_idx = 0
        current_idx_biggest_probability = -1
        current_idx_biggest_probability_lemma = ''
        for dag in dags:
            if not dag:
                continue
            dag_idx = self.dag_idx(dag)
            dag_lemma = self.dag_lemma(dag)
            dag_probability = self.dag_probability(dag)
            if dag_idx == current_idx:
                if dag_probability > current_idx_biggest_probability:
                    current_idx_biggest_probability = dag_probability
                    current_idx_biggest_probability_lemma = dag_lemma
            if dag_idx > current_idx:
                lemmas.append(current_idx_biggest_probability_lemma)
                current_idx = dag_idx
                current_idx_biggest_probability = dag_probability
                current_idx_biggest_probability_lemma = dag_lemma
        return ' '.join(lemmas)


    def dag_idx(self, dag):
        return dag[0]

    def dag_lemma(self, dag):
        return dag[2][1].split(':')[0]

    def dag_probability(self, dag):
        return float(dag[3])

    def dags_for_idx(self, dags, idx):
        return list(filter(lambda x: (x[0] if len(x) > 0 else None) == idx, dags))

    def most_probable_dag(self, dags):
        biggest_probability = -1
        biggest_probability_idx = 0
        for idx, dag in enumerate(dags):
            dag_probability = float(dag[3])
            if dag_probability > biggest_probability:
                biggest_probability = dag_probability
                biggest_probability_idx = idx

        return dags[biggest_probability_idx]

    def most_probable_lemmas(self, dags):
        idx = 0
        lemmas = []
        while True:
            dags_for_idx = self.dags_for_idx(dags, idx)
            if len(dags_for_idx) > 0:
                most_probable_dag = self.most_probable_dag(dags_for_idx)
                lemmas.append(self.dag_lemma(most_probable_dag))
                idx = idx + 1
                continue
            break
        return lemmas
