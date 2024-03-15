from Utils import NLP,Math,Utils
from copy import deepcopy
from tqdm import tqdm

class ProKnow(object):

    def __init__(self,window_size = 1,thetas = {}):

        self.pk = {}
        self.thetas = thetas
        self.satisfied = {}
        self.window_size = window_size
        self.annotate_rules = None

    def compute_from_data(self,train_data):

        pleaves = {}
        for item in self.annotate_rules:
            pleaves[tuple(item)] = 0.0

        for data_point in train_data:
            label = self.evaluate_pk(data_point,pk=False)
            for key in pleaves:
                if label in key:
                    pleaves[key] += 1

        return pleaves

    def evaluate_point_potential(self,pleaves,point_satisfied):

        point_potentials = deepcopy(pleaves)
        
        for item in point_potentials:
            item_path = item[1][1:-1].split(',')
            len_path = len(item_path)

            path_prod = 1
            
            for i in range(len_path):
                if str(item_path[i]) == '1':
                    path_prod *= (sum(point_satisfied[i+1]) - 0.5)
                    
                elif str(item_path[i]) == '0':
                    path_prod *= (sum([-1*x for x in point_satisfied[i+1]]) - 0.5)


    def forward(self,
                pleaves,
                kernel = Math.cossim,
                fragment_size = 1,
                repr_model = NLP.repr,
                point = None):

        point_potentials = deepcopy(pleaves)

        ps = point.split('.')
        N = len(ps)

        ws = fragment_size
        point_list = [ps[i:i+ws] for i in range(N) if i+ws <= N][:-1]
        point_list = [' '.join(item) for item in point_list]
        N = len(point_list)

        for item in point_potentials:
            item_path = item[1][1:-1].split(',')
            len_path = len(item_path)
        

            for i in tqdm(range(N)):
                point_item = point_list[i]
                point_satisfied = deepcopy(self.satisfied)
            
        

    def train(self,
              kernel = Math.cossim,
              fragment_size = 1,
              repr_model = NLP.repr,
              train_data = None):

        #refer Algorithm 1 here: https://arxiv.org/pdf/2204.12560.pdf
        
        fragment_size = self.window_size #set fragment size
        pleaves = self.compute_from_data(train_data) #compute leaf potential

        for point in train_data:
            self.forward(pleaves,
                         kernel = kernel,
                         fragment_size = fragment_size,
                         repr_model = repr_model,
                         point = point
                         )
        
        '''
        for point in train_data:

            

            potential = 0

            for i in tqdm(range(N)):
                point_item = point_list[i]
                point_satisfied = deepcopy(self.satisfied)
                for item in self.pk:
                    point_satisfied[item] = self.evaluate_item(item,point_item,kernel,train=True)
                #print (point_satisfied)
                #print (pleaves)
                potential = self.evaluate_point_potential(pleaves,point_satisfied)
                exit()
                point_annotations = self.annotate_point(point_satisfied)
                annotated_point.append((point_item,point_annotations))

            print (point)
            print (annotated_point)
            exit()
        '''

            

    def get_pk(self):

        return self.pk

    def get_thetas(self):

        return self.thetas

    def __repr__(self):

        return (str(self.pk))

    def process_knowledge(self,pk_file,pk_file_annotate):

        file_lines = Utils.read_file(pk_file)
        self.annotate_rules = [line.split(' ') for line in Utils.read_file(pk_file_annotate)]

        for line in file_lines:
            if not line:
                continue
            index = int(line.split('.')[0])
            text = line.split('.')[1].lower()
            if index not in self.pk:
                self.pk[index] = [text]
                self.thetas[index] = [0.3]
                self.satisfied[index] = False
            else:
                self.pk[index] += [text]
                self.thetas[index] += [0.3]


    def annotate_point(self,point_satisfied):

        annotations = []
        for item in point_satisfied:
            if point_satisfied[item]:
                annotations.append(item)
        return (tuple(annotations))

    def print_colors(self,colors):

        print ("color coding scheme")
        scheme = ""
        for color in colors:
            scheme += colors[color]+str(color)
        print (scheme+'\u001b[0m')

    def color_code(self,point_item,annotations):

        colors = {1: '\u001b[41m',
                  2: '\u001b[42m',
                  3: '\u001b[43m',
                  4: '\u001b[44m',
                  5: '\u001b[45m'}

        self.colors = colors

        chars = point_item.split()
        n_chars = len(chars)
        
        color_keys = [x for x in annotations if x in list(colors.keys())]
        n_colors = len(color_keys)

        index_list = list(Utils.split_list(range(n_chars),n_colors))

        #if not index_list:
        #return point_item
        
        color_coded = ""
        
        for li in index_list:
            if not color_keys:
                color_code = colors[1]
            else:
                color = color_keys[index_list.index(li)]
                color_code = colors[color]
            color_coded += ' '+color_code+' '.join(chars[li[0]:li[-1]+1])

        return color_coded+'\u001b[0m'
        

    def evaluate_item(self,item,point,kernel='dot',train=False):

        s_list = self.pk[item] #sentence list
        sims = [NLP.compare_sentences(i,point,kernel) for i in s_list]
        N = len(sims)
        if train:
            values = [(sims[i] - self.thetas[item][i]) for i in range(N)]
            return values
        truth_values = [sims[i] >= self.thetas[item][i] for i in range(N)]
        return (max([sims[i] >= self.thetas[item][i] for i in range(N)]) == 1)

    def get_label(self,annotated_point,pk=True):

        li = []
        for item in annotated_point:
            li += item[1]

        li = list(set(sorted(li)))

        n,m = len(li),len(self.pk)
        bool_annotation = [1 for i in range(n)] + [0 for i in range(m-n)]

        for item in self.annotate_rules:
            annotation = [int(x) for x in item[1][1:-1].split(',')]
            if bool_annotation == annotation:
                if not pk:
                    return item[-1]
                return (item[0],bool_annotation)
                
    def evaluate_pk(self,point,kernel='dot',pk=True,explanation=False):

        ps = point.split('.') #point sentences
        N = len(ps) #no of sentences in point
        annotated_point = []
        color_coded_point = ""
        ws = self.window_size
        point_list = [ps[i:i+ws] for i in range(N) if i+ws <= N][:-1]
        point_list = [' '.join(item) for item in point_list]
        N = len(point_list)
        for i in tqdm(range(N)):
            point_item = point_list[i]
            point_satisfied = deepcopy(self.satisfied)
            for item in self.pk:
                point_satisfied[item] = self.evaluate_item(item,point_item,kernel)
            point_annotations = self.annotate_point(point_satisfied)
            annotated_point.append((point_item,point_annotations))
            color_coded_point += (self.color_code(point_item,point_annotations)+'\n')
        if explanation:
            print ("="*40)
            print ("You entered: ",point)
            #print (annotated_point)
            print ("="*40)
            self.print_colors(self.colors)
            print ("="*40)
            print (color_coded_point)
            print ("="*40)
            for rule in self.annotate_rules:
                print (rule)
            #print (self.annotate_rules)
            print ("="*40)
            print ("Inference: ",self.get_label(annotated_point,pk=False))
        
        return (self.get_label(annotated_point,pk=pk))
            
