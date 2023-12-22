- `docker network create reqTrace`
- ```       
    docker run -d \
    --name reqTraceMysql \
    --network reqTrace --network-alias mysql \
    -v reqTrace-mysql-data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=secret \
    -e MYSQL_DATABASE=reqTrace \
    mysql:8.0
    ```
- ```       
    docker run -d \
    --name reqTraceMysql \
    -p 3306:3306 \
    -v reqTrace-mysql-data:/var/lib/mysql \
    -e MYSQL_ROOT_PASSWORD=secret \
    -e MYSQL_DATABASE=reqTrace \
    mysql:8.0
    ```
- `docker exec -it mysql_container mysql -u root -p`

Repo Creation
- Artifact fetchers implemented
  - Check if req file reader works, it was read from file before, taken from user request now
- neo4j connector implemented
  - copied from old repo
  - Add a func for create database
- populate db funcs implemented
- new plugin!! Dozerdb allows neo4j community to have multiple databases
  - Check if neo4j has user system, to avoid each user reaching every database
- UploadFile of fastapi has python-file like interface, better


Repo controller
- neo4j database naming allows only ascii, number and dots
- python empty dict gives false in bool check(nice info)

Don't forget to setup server as package
- pip install -e .

Somehow postman forgets the file uploaded after a restart. Dont panic when file field missing error occurs. Reupload file to postman.
Use MERGE instead of CREATE for putting links, avoids duplicates!

- Frontend
  - https://www.digitalocean.com/community/tutorials/how-to-bundle-a-web-app-with-parcel-js
- WordEmbeddings
  - BERT
    - https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/

- Word embeddings- bert

Having similarity threshold limits us? Also it introduces inconsistency based on threshold selection
Maybe we should just order links based on similarity, How can this be handled in visuals?
  - later on we can do classification based on true links??
- https://mccormickml.com/2019/05/14/BERT-word-embeddings-tutorial/ DONE
- https://huggingface.co/tasks/sentence-similarity
- https://huggingface.co/sentence-transformers

- pytorch requirements.txt configuration for no cpu
  - ```
    --extra-index-url https://download.pytorch.org/whl/cpu
    torch
    torchaudio
    torchvision
    ```

- Current embeddings taken from `roberta-base-nli-mean-tokens`
  - Check other options, maybe find most suitable one for our task?

- Frontend
  - Trace finding takes a lot of time, I might add a loading icon until api returns!

- IDEA: Evaluating all possible links, without threshold cutoff, we can have a section in dashboard 
  - where user can select a source artifact and play with threshold to view links

- ```
  match (r:Requirement)
  where size(r.number) > 1
  with r
  match (n)
  where (n:Issue or n:PullRequest) and n.text contains r.number
  return r.number as soruce, n.number as target, n.text as target_text
  ```
- Avoiding reqs with single digit (1,2) since they produce too many false positives(they match with any number in text)
- reqs with two digit(1.1, 1.2) can also produce false positives but acceptible
- This provided a weird feature that might be extremely helpful!! But also problematic
  - Looking for req number contains in text, for example 1.1
    - 1.1.2.3 is caught! Nice sub requirements are also related, so helpful
    - 1.2.1.1.3 is also caught! Not good, a mid part is catched, avoid having dots before the req number
- Cleaning false positive 
  - (?<![\.\d])(reqnumber) regex

- python -m spacy download en_core_web_sm

bert tokenizer

- actor-action-object for req
- issue,
  - do we have the same action on same object
