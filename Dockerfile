# Usar a imagem base do Python 2.7
FROM python:2.7

# Instalar dependências de sistema
RUN apt-get update && apt-get install -y \
    python-dev \
    libpq-dev \
    build-essential

# Configurar o diretório de trabalho
WORKDIR /app

# Copiar os arquivos do projeto para o contêiner
COPY . /app

# Atualizar setuptools e pip, instalar virtualenv e virtualenvwrapper
RUN python -m pip install --upgrade setuptools pip
RUN pip install virtualenv virtualenvwrapper

# Setar variáveis de ambiente para virtualenvwrapper
ENV WORKON_HOME=/root/.virtualenvs
ENV VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python
ENV VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv

# Adicionar virtualenvwrapper ao shell
COPY requirements.txt /app/

# Criar e ativar o ambiente virtual, atualizar pip
RUN /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh && mkvirtualenv env && workon env && python -m pip install --upgrade pip"

# Criar o arquivo local de configurações do Django
RUN touch /app/django_files/atlas/settings.py

# Expor a porta que o Django usará
EXPOSE 9797
EXPOSE 6379

# Comando para instalar dependências, rodar o script a1.py e iniciar o servidor Django
CMD /bin/bash -c "source /usr/local/bin/virtualenvwrapper.sh && \
                  workon env && \
                  pip install -r requirements.txt && \
                  python /app/a1.py && \
                  python /app/a2.py && \
                  python /app/a3.py && \
                  python /app/a4.py && \
                  python django_files/manage.py runserver 0.0.0.0:9797"