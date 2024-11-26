
# 📨 Aplicativo de Notificação de Pagamentos em Atraso

[![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![SendGrid](https://img.shields.io/badge/Email-SendGrid-blue)](https://sendgrid.com/)

Aplicativo em Python que automatiza o envio de e-mails para clientes com pagamentos em atraso, lendo dados de uma planilha Excel e utilizando o serviço **SendGrid** para o envio das notificações.

## 📋 Sumário

- [💡 Funcionalidades](#-funcionalidades)
- [🏗️ Estrutura de Diretórios](#️-estrutura-de-diretórios)
- [📄 Descrição dos Arquivos](#-descrição-dos-arquivos)
- [🛠️ Pré-requisitos](#️-pré-requisitos)
- [⚙️ Instalação](#️-instalação)
- [🚀 Uso](#-uso)
- [🔧 Configuração](#-configuração)
- [📈 Exemplos](#-exemplos)
- [🤝 Contribuindo](#-contribuindo)
- [📄 Licença](#-licença)
- [📞 Contato](#-contato)
- [🌟 Agradecimentos](#-agradecimentos)

---

## 💡 Funcionalidades

- **Leitura de Planilha Excel**: Lê dados de um arquivo `.xlsx` contendo informações de clientes.
- **Filtragem de Pagamentos em Atraso**: Identifica clientes com pagamentos marcados como "atraso".
- **Envio Automatizado de E-mails**: Envia notificações por e-mail para os clientes em atraso utilizando o SendGrid.
- **Personalização de Mensagens**: Permite personalizar o conteúdo do e-mail enviado.

---

## 🏗️ Estrutura de Diretórios

```
Projeto/
│
├── app.py
├── .gitignore
├── README.md
├── dados.xlsx
└── pyemailexcel_service.py
```

---

## 📄 Descrição dos Arquivos

- **app.py**: Script principal que executa a leitura da planilha, filtra os clientes em atraso e envia os e-mails.
- **.gitignore**: Arquivo que especifica quais arquivos ou pastas devem ser ignorados pelo Git.
- **README.md**: Este arquivo, contendo informações detalhadas sobre o projeto.
- **dados.xlsx**: Planilha Excel com os dados dos clientes.
- **pyemailexcel_service.py**: Cria o serviço para executar o envio diario dos emails.

---

## 🛠️ Pré-requisitos

- **Python 3.x**: Certifique-se de ter o Python instalado em sua máquina.
- **Conta no SendGrid**: Necessária para o envio de e-mails através da API.
- **Ambiente Virtual (opcional, mas recomendado)**: Para isolamento das dependências do projeto.

---

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu_usuario/seu_repositorio.git
cd seu_repositorio
```

### 2. Crie e ative um ambiente virtual

```bash
# No Windows
python -m venv venv
venv\Scriptsctivate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install pandas
pip install sendgrid
pip install pywin32
pip install openpyxl
```

---

## 🚀 Uso

### 1. Configuração do SendGrid

- **Crie uma conta** no [SendGrid](https://sendgrid.com/).
- **Obtenha uma API Key** e **verifique o remetente** conforme instruções na documentação do SendGrid.

### 2. Configure as Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```ini
SENDGRID_API_KEY=YOUR_SENDGRID_API_KEY
FROM_EMAIL=seu_email_verificado@seudominio.com
```

**Nota**: Não compartilhe o arquivo `.env` ou suas credenciais.

### 3. Adicione a Planilha de Dados

- Coloque o arquivo `dados.xlsx` na raiz do projeto.
- Certifique-se de que a planilha contém as colunas: `nome`, `endereço`, `telefone`, `e-mail`, `pagamento`.

### 4. Execute o Script

```bash
python app.py
```

---

### 5. Crie o Serviço no Windows

- Com credenciais de Administrador execute:

```bash
python pyemailexcel_service.py install
python pyemailexcel_service.py start
```

---

## 🔧 Configuração

- **Personalizar o E-mail**: Edite o conteúdo da mensagem no arquivo `src/enviar_email.py`.
- **Log de Atividades**: Os logs são registrados em `logs/app.log`.
- **Agendamento**: Para automatizar a execução diária, use o Agendador de Tarefas do Windows ou crie um serviço conforme descrito na documentação.

---

## 📈 Exemplos

- **Saída Esperada**:

  ```
  API Key carregada com sucesso.
  E-mail enviado para João Silva - joao@exemplo.com
  E-mail enviado para Carlos Souza - carlos@exemplo.com
  ```


## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

1. Faça um fork do projeto.
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`).
3. Faça commit de suas alterações (`git commit -m 'Adiciona nova feature'`).
4. Envie para a branch principal (`git push origin feature/nova-feature`).
5. Abra um Pull Request.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## 📞 Contato

- **Autor**: Rodney Victor Siqueira Soares
- **E-mail**: ordabelem@hotmail.com

---

## 🌟 Agradecimentos

Agradeço a todos que contribuíram para este projeto e à comunidade Python por fornecer recursos incríveis.
