# Projeto Atlas IFRS9

Este projeto é uma aplicação para visualização de dados econômicos globais e um painel IFRS9. A aplicação é composta por dois serviços principais: `painel-ifrs9` e `globe`. Abaixo estão as instruções para configurar e iniciar o projeto.

## Estrutura do Projeto

├── globe/
│ ├── data/
│ ├── images/
│ ├── PDF/
│ ├── scripts/
│ ├── wiki/
│ ├── Dockerfile
│ ├── package.json
│ ├── server.js
│ ├── style.css
│ ├── index.html
│ ├── select2.css
│ └── README.md
├── django_files/
│ ├── manage.py
│ ├── ...
├── a1.py
├── a2.py
├── a3.py
├── a4.py
├── a5.py
├── Dockerfile
├── docker-compose.yaml
├── bower.json
├── gulpfile.js
├── html/
├── media/
├── package.json
├── requirements.txt
└── README.md



## Tecnologias Utilizadas

- **Docker**: Para conteinerização das aplicações.
- **PostgreSQL**: Banco de dados para armazenamento de dados.
- **Redis**: Armazenamento em cache.
- **Django**: Framework web para o painel IFRS9.
- **Node.js** e **Express.js**: Servidor para a aplicação de visualização de dados.
- **HTML**, **CSS** e **JavaScript**: Tecnologias front-end para a interface de usuário.
- **Three.js**: Biblioteca JavaScript para renderização 3D.

## Configuração e Inicialização

### Pré-requisitos

- Docker e Docker Compose instalados na máquina.

### Passos para Inicialização

1. Clone o repositório:
    ```sh
    git clone <URL do repositório>
    cd evertec-sinqia-atlas-risk-ifrs9
    ```

2. Inicialize o Docker Compose:
    ```sh
    docker-compose up --build
    ```

3. Acesse a aplicação no navegador:
    - Painel IFRS9: `http://localhost:9797`
    - Visualização de Dados: `http://localhost:3456`

## Descrição dos Serviços

### Painel IFRS9

- Serviço Django rodando na porta 9797.
- Depende do serviço de banco de dados PostgreSQL e do serviço Redis.

### Globe

- Aplicação Node.js utilizando Express para servir uma visualização 3D de dados econômicos.
- Rodando na porta 3456.

### Banco de Dados

- PostgreSQL configurado para rodar na porta 5432.

### Redis

- Serviço Redis rodando na porta 6379.

## Contribuição

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/fooBar`).
3. Faça commit das suas mudanças (`git commit -am 'Add some fooBar'`).
4. Faça push para a branch (`git push origin feature/fooBar`).
5. Crie um novo Pull Request.

## Licença

Este projeto é licenciado sob a MIT License - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
