# Recipe Manager

- O Recipe Manager é uma aplicação web desenvolvida em Python Django com o objetivo de gerenciar receitas e alimentos disponíveis na despensa. O sistema permite organizar melhor os itens da cozinha, criar receitas personalizadas e até gerar receitas criativas utilizando a API do Gemini, uma inteligência artificial avançada.
- Com um design intuitivo, a aplicação oferece funcionalidades de CRUD (Criar, Ler, Atualizar e Deletar) para alimentos e receitas, login seguro, personalização de perfil e integração com o banco de dados para armazenamento.

## Funcionalidades

### Principais Recursos

1. **Sistema de login e cadastro de usuários**
    - Backend em Python Django e frontend com HTML, CSS e JavaScript.
    - Criação e autenticação segura de usuários.
2. **Gerenciamento de Despensa (CRUD de Alimentos)**
    - Adicione, edite, visualize e exclua itens da despensa virtual.
3. **Gerenciamento de Receitas (CRUD de Receitas)**
    - Crie receitas personalizadas, edite ou exclua as já existentes.
4. **Conexão com a API do Gemini**
    - Gere receitas criativas com base nos alimentos disponíveis na despensa.
    - Salve receitas geradas pela IA diretamente no sistema.
5. **Personalização de Perfil**
    - Edite informações pessoais, como nome, e-mail e senha.
6. **Sistema de Logout**
    - Finalize a sessão com segurança.

## Instalação

### Pré-Requisitos

- Python 3.9 ou superior
- Bibliotecas listadas no arquivo [requirements.txt](./requirements.txt)

### Passos de Instalação

1. **Clone o repositórtio:**
    ```bash
    git clone https://github.com/mpizanii/Recipe-Manager
    cd Recipe-Manager
    ```
2. **Crie um ambiente virtual**
    ```bash
    python -m venv env
    source env/bin/activate # Para macOS/Linux
    env/Scripts/activate # Para Windows
    ```
3. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```
4. **Configure suas variáveis de ambiente**
- Crie um arquivo `.env` na raiz do projeto.
- Adicione as variáveis necessárias seguindo o exemplo em [.env.example](./.env.example)
- **Substitua**: 
    - `GOOGLE_API_KEY` pela chave da API Gemini (Consulte a sua chave [aqui](https://aistudio.google.com/app/apikey).)

## Uso

1. **Execute o projeto**
    ```bash
    python manage.py runserver
    ```
2. **Acesse a aplicação**
    - Após iniciar o projeto, abra o navegador e acesse: http://127.0.0.1:8000/.
    - Utilize as credenciais cadastradas para fazer login ou cadastre-se como novo usuário.
3. **Funcionalidades Disponíveis**
    1. **Adicionar alimentos:** Insira itens disponíveis na despensa.
    2. **Deletar alimentos:** Mantenha a despensa atualizada.
    3. **Criar receitas:** Desenvolva receitas personalizadas.
    4. **Criar receitas com ajuda de IA:** Utilize a API Gemini para criar receitas com os itens disponíveis.
    5. **Salvar sua receita criada pela IA:** Salve as receitas criadas pela IA.
    6. **Editar ou deletar receitas:** Gerencie receitas existentes.
    7. **Personalize seu perfil:** Atualize informações pessoais.
    8. **Saia da Aplicação:** Encerre a sessão com segurança.

## Contribuindo
Contribuições são bem-vindas! Siga as etapas abaixo para colaborar:
1. Faça um fork do repositório.
2. Crie uma branch para sua funcionalidade ou correção (git checkout -b minha-feature).
3. Faça commit das mudanças (git commit -m 'Adiciona minha nova funcionalidade').
4. Faça o push para a branch (git push origin minha-feature).
5. Abra um Pull Request e descreva suas alterações.

## Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE)  para mais informações.
