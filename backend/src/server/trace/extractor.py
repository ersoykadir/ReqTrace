"""
THE SIMPLE THE BETTER!!
Dont forget that we are looking for the obvious relations
Expect a related artifact to contain the same action and object from the req,
(most of the time syntactically same, sometimes similar or synonym) actors might be irrelevant

- Extract actor-action-object information from sentences
    - (beware req sentences have a certain structure, so doesnt have to be extremely generalized)
    - Maybe eliminate or ignore sentences that are not in this form
    - Beware of the passive voice, maybe actor and object are switched
    - Issues have multiple sentences, there might be a tree of actors, actions and objects
    - We might need a pruning system to eliminate unnecessary actors, actions and objects
    - EXPERIMENTAL: tfidf values might help to decide on importance
- Actors, actions and objects for requirements can be represented as a graph
- Actors, actions and objects for each artifact can be represented as a graph 
- Having actors, actions and objects for requirements and artifacts, we can match them
    - Matching can be a direct string comparison (or a similarity comparison 
      but that might blur the purpose, simplicity)
        - Synonyms
    - @uskudarli mentioned we might need a graph search or matching algorithm

"""
# import spacy
# from spacy import displacy
# nlp = spacy.load("en_core_web_sm")


# def extract_actor_action_object_from_sentence(sentence):
#     """
#     Extracts actors, actions and objects from a sentence
#     """
#     doc = nlp(sentence)
#     for token in doc:
#         print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
#             token.shape_, token.is_alpha, token.is_stop)

#     displacy.serve(doc, style="dep")


# extract_actor_action_object_from_sentence("Members shall be able to view annotations in other polls.")

# from nltk.parse import CoreNLPParser

# text = "Members shall be able to view annotations in other polls."

# # pos_tagger = CoreNLPParser(url='http://localhost:9000', tagtype='pos')

# # print(list(pos_tagger.tag(text.split())))

# from nltk.parse.corenlp import CoreNLPDependencyParser
# dep_parser = CoreNLPDependencyParser(url='http://localhost:9000')
# parses = dep_parser.parse(text.split())
# res = [[(governor, dep, dependent) for governor, dep, dependent in parse.triples()] for parse in parses]
# print(res)


# import dotenv

# dotenv.load_dotenv()

# import spacy
# from spacy import displacy
# # from stanfordnlp.server import CoreNLPClient
# from stanza.server import CoreNLPClient
# from corenlp_dtree_visualizer.converters import _corenlp_dep_tree_to_spacy_dep_tree


# # Input text
# text = 'Jim killed John with a joke.'

# # Get a dependency tree from a Stanford CoreNLP pipeline endpoint="http://localhost:9000", start_server="DONT_START",
# with CoreNLPClient(
#         annotators=['tokenize','ssplit','pos','lemma','ner','parse','depparse'],
#         timeout=60000, memory='8G', output_format='json') as client:
#     # submit the request to the server
#     ann = client.annotate(text)

# # get the first sentence
# print(ann)
# sentence = ann.sentence[0]

# # get the constituency parse of the first sentence
# constituency_parse = ann.parseTree
# print(constituency_parse)

from stanfordcorenlp import StanfordCoreNLP
# Use an existing server
nlp = StanfordCoreNLP('http://localhost', port=9000)

sentence = 'Members shall be able to view annotations in other polls.'
# sentence = 'She is reading a book'
# print('Tokenize:', nlp.word_tokenize(sentence))
# print( 'Part of Speech:', nlp.pos_tag(sentence))
# print( 'Named Entities:', nlp.ner(sentence))
# print( 'Constituency Parsing:', nlp.parse(sentence))
# print( 'Dependency Parsing:', nlp.dependency_parse(sentence))

class Token:
    text: str
    index: int
    tag: str
    links: list
    root: bool
    def __init__(self, text=None, index=None, tag=None, links=None):
        self.text = text
        self.index = index
        self.tag = tag
        self.links = links
        self.root = False
    def __str__(self):
        return self.text + "." + self.tag + "." + str(self.index)
    def __repr__(self):
        return self.text + "." + self.tag + "." + str(self.index)

def parse_sentence(sentence):
    """ Parses a sentence and creates a tree of tokens """   
    tree = {} # Maybe also create a tree class
    root = None
    pos_tags = nlp.pos_tag(sentence)
    index = 1
    for tag in pos_tags:
        token = Token(text=tag[0], index=index, tag=tag[1], links=[])
        tree[index] = token
        index += 1
        print(token)
    
    dependencies = nlp.dependency_parse(sentence)
    print(dependencies)
    for dep in dependencies:
        relation = dep[0]
        governor = dep[1]
        dependent = dep[2]
        if relation == "ROOT":
            tree[dependent].root = True
            root = tree[dependent]
            continue
        print(relation, governor, dependent)
        tree[governor].links.append((relation, tree[dependent]))

    return root

def list_verbs(tree):
    for index, token in tree.items():
        if token.tag[0:2] == "VB" or token.root == True:
            print(token.text, token.tag, token.links)

def get_actions(root):
    """Extracts the action from the sentence"""
    # TODO: Maybe there are multiple actions
    if root.tag[0:2] == "VB":
        # root might be the action
        return root
    else:
        # root is not the action, find the verb that is connected to root
        for link in root.links:
            if link[0] == "xcomp":
                return link[1]
            elif link[0] == "ccomp":
                return link[1]
            elif link[0] == "dep":
                print("The link is ambiguous, might be the action, should check")
                return None
            else:
                continue
        print("The sentence might not be in the correct form")
        print("or we might need to improve the algorithm")
        return None

def get_actors(root):
    """Extracts the actor from the sentence"""
    # TODO: Maybe there are multiple actors
    for link in root.links:
        if link[0][0:5] == "nsubj":
            return link[1]
        else:
            continue
    print("The sentence might not be in the correct form")
    print("or we might need to improve the algorithm")
    return None

def get_objects(action):
    """Extracts the object from the sentence"""
    # TODO: Maybe there are multiple objects
    if action is None:
        print("The sentence might not be in the correct form")
        print("or we might need to improve the algorithm")
        print("or there might be no object")
        return None
    for link in action.links:
        if link[0] == "obj":
            return link[1]
        else:
            continue
    print("The sentence might not be in the correct form")
    print("or we might need to improve the algorithm")
    return None

def get_actor_action_object(sentence):
    """Extracts actors, actions and objects from a sentence"""
    root = parse_sentence(sentence)
    actor = get_actors(root)
    action = get_actions(root)
    obj = get_objects(action)
    return root, actor, action, obj
    print("ROOT:", root)
    print("Links:", root.links)
    print("ACTION:", action)
    print("Links:", action.links)
    print("ACTOR:", actor)
    print("Links:", actor.links)
    print("OBJECT:", obj)
    print("Links:", obj.links)

# def list_verbs(sentence):
#     """Extracts verbs from a sentence"""
#     doc = nlp.pos_tag(sentence)
#     verbs = []
#     for token in doc:
#         if token[1][0:2] == "VB":
#             verbs.append(token[0])
#     return verbs

from server.data.get_files import get_file
from server.artifacts.artifacts import get_requirements
def parse_all_groups():
    """"""
    for i in range(1, 10):
        file = get_file(i)
        requirements = get_requirements(file)
        parse_requirements(requirements["data"], i)


# get_actor_action_object(sentence)

def parse_requirements(requirements, group):
    """Parses requirements and extracts actors, actions and objects"""
    output = open(f"output{group}.md", "w")
    for requirement in requirements:
        number = requirement["number"]
        description = requirement["description"]
        print(number, description)
        output.write(number + " " + description + "\n")
        root, actor, action, obj = get_actor_action_object(description)
        output.write("ROOT: " + str(root) + "\n")
        if root is not None:       
            output.write("Links: " + str(root.links) + "\n")
        output.write("ACTION: " + str(action) + "\n")
        if action is not None:
            output.write("Links: " + str(action.links) + "\n")
        output.write("ACTOR: " + str(actor) + "\n")
        if actor is not None:
            output.write("Links: " + str(actor.links) + "\n")
        output.write("OBJECT: " + str(obj) + "\n")
        if obj is not None:
            output.write("Links: " + str(obj.links) + "\n")
        output.write("----------------------\n")
    output.close()

parse_all_groups()
# parse_requirements()
nlp.close() # Do not forget to close! The backend server will consume a lot memery.

"""
DONT FORGET SIMPLEEEE!!!!
Q1: Should root be checked like verbs?
Q2: Which relations should be checked?
    ex: root able.JJ --xcomp--> view.VB 
        able.JJ --nsubj--> view.VB
Q3: Maybe go over the important relations instead of starting from root/verbs
Q4: Not all verbs are helpful, I think go to root, if root is not a verb, find the verb that is connected to root
    This seems to be the answer, go to root, get nsubj, get verb and its object relations,
        rest is extra info, improving the details

Valuable relations:
nsubj: nominal subject, may provide the actor
obj: object, may provide the object
obl: oblique nominal, provides extra information about the object
nmod: nominal modifier, provides extra information about the object or actor
    case: case marker, provides extra information about nmod type, ex: in, on, at, as
amod: adjectival modifier, provides extra information about the object or actor
compound: compound noun, provides extra information about the object or actor
conj: conjunct, and/or relation between two actors, actions or objects
compound:prt: phrasal verb particle, verb and particle(RP) form a compound verb
advcl: adverbial clause modifier, provides extra information about the verb
    mark: marker, provides extra information about advcl type, ex: if, when, while

From root:
xcomp: open clausal complement
    dependent word is the main verb of a subordinate clause(verb is missing in the clause)
    - He made her sing
      - made.VB --xcomp--> sing.VB
    - User shall be able to view annotations in other polls.
      - able.JJ --xcomp--> view.VB
ccomp: clausal complement
    dependent word is the main verb of a subordinate clause
    - She believes that he will succeed.
      - believes.VB --ccomp--> succeed.VB
cop: copula
    copula is a verb that connects the subject of a sentence to a subject complement, 
    often expressing a state of being or identity.
    - The sky is clear
      - sky is subject, clear is subject complement
      - 'is' is the copula, connects the subject and subject complement
      - is.VB --cop--> sky.NN
aux: auxiliary
    represent auxiliary verbs in a sentence
    - She is reading a book
      - is.VB --aux--> reading.VBG
"""

