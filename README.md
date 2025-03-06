#Digidex

#Digidex é um sistema desenvolvido com Django, HTML, CSS e JavaScript que permite aos usuários criar, editar, detalhar e excluir Digimons. O projeto oferece uma plataforma interativa onde os usuários podem personalizar seus Digimons, incluindo características como nome, tipo, habilidades e aparência.

Funcionalidades
Criação de Digimons: Os usuários podem criar novos Digimons, escolhendo suas características e aparência.
Edição de Digimons: Após criar um Digimon, os usuários podem editar suas informações a qualquer momento.
Detalhamento de Digimons: Veja detalhes completos sobre os Digimons criados, com uma visão detalhada de suas características.
Exclusão de Digimons: Permite que os usuários excluam Digimons quando desejado.
Interface Personalizável: O sistema permite personalizar as informações dos Digimons, como tipo, poderes e outras características únicas.
Antes de rodar o projeto, você precisa ter o seguinte instalado:

Tecnologias Utilizadas
Backend: Django
Frontend: HTML, CSS, JavaScript
Banco de Dados: PostgreSQL
Outras Bibliotecas:
psycopg2 (para integração com PostgreSQL)
Requisitos
Python 3.x
Django 5.x
PostgreSQL (ou outro banco de dados compatível)
psycopg2 (para conexão com PostgreSQL)

Como Rodar o Projeto
1. Criar um ambiente virtual
Recomendado usar o virtualenv para isolar as dependências do projeto.
python -m venv .venv

2. Ativar o ambiente virtual
No Windows:
.venv\Scripts\activate
No Linux/macOS:
source .venv/bin/activate

3. Instalar as dependências
pip install -r requirements.txt

4. Configurar o Banco de Dados
Configure o banco de dados PostgreSQL (ou outro banco de sua preferência) no arquivo settings.py de Django. Se estiver usando PostgreSQL, certifique-se de ter o banco de dados criado e com as credenciais corretas.

python
Copiar
Editar
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'digidex',
        'USER': 'seu_usuario',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

5. Rodar as migrações do banco de dados
python manage.py migrate

6. Criar um superusuário (opcional, mas recomendado para acessar o admin)
python manage.py createsuperuser

7. Rodar o servidor de desenvolvimento
python manage.py runserver
O projeto estará disponível em http://127.0.0.1:8000/.
