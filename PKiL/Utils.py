from sentence_transformers import SentenceTransformer
from math import exp,sqrt,prod

model = SentenceTransformer('all-MiniLM-L6-v2')

class Utils(object):

    @staticmethod
    def read_file(file):

        lines = []
        with open(file,'r') as fp:
            lines = fp.read().splitlines()

        return lines

    @staticmethod
    def split_list(li, n):

        if n == 0:
            n = 1
        
        k, m = divmod(len(li), n)
        return (li[i*k+min(i, m):(i+1)*k+min(i+1, m)] for i in range(n))

class Math(object):

    @staticmethod
    def product(li):

        return prod(li)

    @staticmethod
    def gaussim(encoding1, encoding2):

        l1, l2 = list(encoding1), list(encoding2)
        N = len(l1)
        z1 = sqrt(sum([l1[i]**2 for i in range(N)]))
        z2 = sqrt(sum([l2[i]**2 for i in range(N)]))
        
        unit_l1 = [l1[i]/float(z1) for i in range(N)]
        unit_l2 = [l2[i]/float(z2) for i in range(N)]

        return exp((sum([(unit_l1[i]-unit_l2[i])**2 for i in range(N)]))/float(2)) #2*sigma**2, sigma=1

    @staticmethod
    def cossim(encoding1, encoding2):

        l1,l2 = list(encoding1),list(encoding2)
        N = len(l1)
        dotp = sum([l1[i]*l2[i] for i in range(N)])
        z1 = sqrt(sum([l1[i]**2 for i in range(N)]))
        z2 = sqrt(sum([l2[i]**2 for i in range(N)]))
        return dotp/float(z1*z2)

class NLP(object):

    @staticmethod
    def repr(sentence):

        # model = SentenceTransformer('all-MiniLM-L6-v2')
        return model.encode([sentence])[0]
        
    @staticmethod
    def compare_sentences(sentence1, sentence2, kernel='dot'):
        
        
        encoding1 = NLP.repr(sentence1)
        encoding2 = NLP.repr(sentence2)
        
        if kernel == 'dot' or kernel == Math.cossim:
            sim = Math.cossim(encoding1,encoding2)
            return sim

        elif kernel == 'gauss' or kernel == Math.gaussim:
            sim = Math.gaussim(encoding1,encoding2)
            return sim
        

    
