## VENV Setup 

<sub> :warning: **Safety First** - You should always check the contents of the script before running it [here](bin/setup-project). :warning: </sub>

To setup your venv please do the following: 

```bash
bin/setup-venv
```
## VENV Activate 

To activate your venv please do the following: 

```bash
source venv/bin/activate
```

## Setup Project

To setup the project please do the following: 
```bash
bin/setup-project
```

## Saving Dependencies

<sub> :warning: **Safety First** - You should always check the contents of the script before running it [here](bin/save-dependencies). :warning: </sub>

If you have installed a new dependency for example let's say we are trying to install the [requests](https://pypi.org/project/requests/) package for testing: 

```bash 
pip install requests
pip install fastapi uvicorn
pip install python-multipart
pip install tortoise-orm
pip install passlib
pip install bcrypt
pip install PyJWT
pip install Faker
pip install jsonpath
```

Then please be sure to save your dependencies by running the following before committing to git:

```bash
bin/save-dependencies
```

If you forget, then this will create problems when other colleagues do a [git clone](https://git-scm.com/docs/git-clone) or [git pull](https://git-scm.com/docs/git-pull) after you have committed your changes to a [feature branch](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches) or merge your changes back into the [main](https://github.com/ivanovakatya/Fast-API/tree/main) branch. 

## To start the uvicorn (fastapi) server

```bash
bin/start-api-server
```

## To start the sqlite3 database

```bash
bin/start-db
```
After the database is started, the following SQL command can be run to extract the data from user table:

```bash
select * from user;
```

To exit the database, execute the following:

```bash
.exit
```