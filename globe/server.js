const express = require('express');
const path = require('path');

const app = express();
const port = 3456;

// Servir arquivos estáticos (html, css, js)
app.use(express.static(path.join(__dirname)));

// Rota padrão para enviar o arquivo index.html
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'));
});

app.listen(port, () => {
    console.log(`Servidor rodando em http://localhost:${port}`);
});
