<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Projeto Atlas IFRS9</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            line-height: 1.6;
        }
        h1, h2, h3 {
            color: #333;
        }
        pre {
            background: #f4f4f4;
            padding: 10px;
            border: 1px solid #ddd;
            overflow: auto;
        }
        code {
            font-family: 'Courier New', Courier, monospace;
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 4px;
        }
        ul {
            margin: 0;
            padding: 0 0 0 20px;
        }
        li {
            margin: 0 0 10px 0;
        }
    </style>
</head>
<body>
    <h1>Projeto Atlas IFRS9</h1>
    <p>Este projeto é uma aplicação para visualização de dados econômicos globais e um painel IFRS9. A aplicação é composta por dois serviços principais: <code>painel-ifrs9</code> e <code>globe</code>. Abaixo estão as instruções para configurar e iniciar o projeto.</p>

    <h2>Estrutura do Projeto</h2>
    <pre>
.
├── globe/
│   ├── data/
│   ├── images/
│   ├── PDF/
│   ├── scripts/
│   ├── wiki/
│   ├── Dockerfile
│   ├── package.json
│   ├── server.js
│   ├── style.css
│   ├── index.html
│   ├── select2.css
│   └── README.md
├── django_files/
│   ├── manage.py
│   ├── ...
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
    </pre>

    <h2>Tecnologias Utilizadas</h2>
    <ul>
        <li><strong>Docker</strong>: Para conteinerização das aplicações.</li>
        <li><strong>PostgreSQL</strong>: Banco de dados para armazenamento de dados.</li>
        <li><strong>Redis</strong>: Armazenamento em cache.</li>
        <li><strong>Django</strong>: Framework web para o painel IFRS9.</li>
        <li><strong>Node.js</strong> e <strong>Express.js</strong>: Servidor para a aplicação de visualização de dados.</li>
        <li><strong>HTML</strong>, <strong>CSS</strong> e <strong>JavaScript</strong>: Tecnologias front-end para a interface de usuário.</li>
        <li><strong>Three.js</strong>: Biblioteca JavaScript para renderização 3D.</li>
    </ul>

    <h2>Configuração e Inicialização</h2>
    <h3>Pré-requisitos</h3>
    <p>Docker e Docker Compose instalados na máquina.</p>

    <h3>Passos para Inicialização</h3>
    <ol>
        <li>Clone o repositório:
            <pre><code>git clone &lt;URL do repositório&gt;
cd evertec-sinqia-atlas-risk-ifrs9
            </code></pre>
        </li>
        <li>Inicialize o Docker Compose:
            <pre><code>docker-compose up --build
            </code></pre>
        </li>
        <li>Acesse a aplicação no navegador:
            <ul>
                <li>Painel IFRS9: <code>http://localhost:9797</code></li>
                <li>Visualização de Dados: <code>http://localhost:3456</code></li>
            </ul>
        </li>
    </ol>

    <h2>Descrição dos Serviços</h2>
    <h3>Painel IFRS9</h3>
    <p>Serviço Django rodando na porta 9797. Depende do serviço de banco de dados PostgreSQL e do serviço Redis.</p>

    <h3>Globe</h3>
    <p>Aplicação Node.js utilizando Express para servir uma visualização 3D de dados econômicos. Rodando na porta 3456.</p>

    <h3>Banco de Dados</h3>
    <p>PostgreSQL configurado para rodar na porta 5432.</p>

    <h3>Redis</h3>
    <p>Serviço Redis rodando na porta 6379.</p>

    <h2>Contribuição</h2>
    <ol>
        <li>Faça um fork do projeto.</li>
        <li>Crie uma branch para sua feature (<code>git checkout -b feature/fooBar</code>).</li>
        <li>Faça commit das suas mudanças (<code>git commit -am 'Add some fooBar'</code>).</li>
        <li>Faça push para a branch (<code>git push origin feature/fooBar</code>).</li>
        <li>Crie um novo Pull Request.</li>
    </ol>

    <h2>Licença</h2>
    <p>Este projeto é licenciado sob a MIT License - veja o arquivo <a href="LICENSE">LICENSE</a> para mais detalhes.</p>
</body>
</html>
