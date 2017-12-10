# scpAPI

## Dependências

* Python Pip

    `yum -y install python-pip`
    
* Falcon

    `pip install falcon`
    
* Psycopg2

    `pip install psycopg2`
    
* Gunicorn

    `pip install gunicorn`
    
## Execução

`gunicorn main:app --bind=IP_ADDRESS`