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
