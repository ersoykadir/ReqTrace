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