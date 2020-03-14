# b2w_api
api para o desafio b2w challenger

## Como desenvolver?

1. Clone o repositório.
1. Crie um virtualenv com Python 3.7
1. Ative o virtualenv.
1. Instale as dependências.
1. Configure a instância com o .env
1. Execute os testes.
1. Execute o migrate.
1. Execute o runserver.

```console
git <git url>
cd gespag
virtualenv env --python=python3 # python 3.7 ou mais atual
source env/bin/activate
pip install -r requirements_dev.txt
python manage.py migrate
python manage.py runserver
```

## Testes
```console
python manage.py test
```

## Observações:
* Api disponibilizada em https://b2w-api.herokuapp.com/api/v1/planets/
* Como nenhum método foi subscrito, criei uma collection no postman que se encontra na raiz do projeto
