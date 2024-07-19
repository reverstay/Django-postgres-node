FROM node:14

# Define o diretório de trabalho dentro do contêiner
WORKDIR /usr/src/app

# Copia o package.json e package-lock.json para o diretório de trabalho
COPY package.json ./
# Instala as dependências do projeto
RUN npm install

# Copia o restante dos arquivos da aplicação para o diretório de trabalho
COPY . .

# Expõe a porta na qual a aplicação irá rodar
EXPOSE 3456

# Comando para iniciar a aplicação
CMD ["npm", "start"]
