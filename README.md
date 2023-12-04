# LegalConnect: Conectando Advogados

O LegalConnect é mais do que um aplicativo; é uma rede social para advogados, uma plataforma onde a comunidade jurídica se conecta, compartilha informações e colabora. Aqui estão os recursos principais:

## Perfis Profissionais

- **Registre-se e Conecte-se:**
    - Advogados podem criar perfis individuais, adicionando detalhes pessoais, como nome, bio e a empresa em que trabalham.
    - Proprietários de empresas podem criar perfis para suas organizações, detalhando informações sobre a empresa e sua atuação.

## Empresas de Advocacia

- **Criação e Exploração:**
    - Proprietários de empresas podem criar perfis para suas firmas, oferecendo uma visão detalhada dos serviços prestados e sua expertise.
    - Advogados individuais podem associar-se a essas empresas, facilitando a busca por profissionais especializados.

## Interações Profissionais

- **Conexões e Colaborações:**
    - Os usuários podem interagir através de posts, comentários e mensagens, compartilhando insights e conhecimento da área jurídica.

## Tecnologia e Desenvolvimento

O LegalConnect é construído com tecnologias de ponta:

- **Django:** Framework backend em Python que assegura robustez e escalabilidade.
- **Django Rest Framework (DRF):** Criação de APIs RESTful para uma interação suave.
- **Banco de Dados:** PostgreSQL.

## Experimente Localmente

Quer experimentar o LegalConnect em seu ambiente de desenvolvimento? Siga estes passos simples:

1. **Clone o Repositório:**
    ```bash
    git clone git@github.com:eduardomoschen/lawyers-company-api.git
    ```

2. **Instale as Dependências:**
    ```bash
    cd legal-connect
    pip install -r requirements.txt
    ```

3. **Configure o Banco de Dados:**
    - A configuração necessária para a conexão do banco de dados é baseada nas variáveis contidas em um arquivo `.env`.

4. **Inicie os contêineres**
    - Com o docker-compose instalado, inicie os conteineres:
    ```bash
    docker-compose up --build
    ```
    - As migrações serão executadas automaticamente por conta dos scripts.sh que estão dentro da pasta `scritps`.

5. **Inicie o Servidor:**
    -  Ainda com o comando `docker-compose up` em execução, abra um novo terminal e inicie o servidor da aplicação:
    ```bash
    docker-compose run --rm djangoapp python manage.py runserver    
    ```

6. Acesse o aplicativo em [http://localhost:8000/api/v1](http://localhost:8000/api/v1)
    - **Cria um Advogado:**
        - `POST /lawyers/` - Cria um advogado informando os dados abaixo.
            - Dados a serem enviados:
            - `company`: Campo para relacionar a empresa que o advogado trabalha.
            - `name`: Campo para o nome do advogado.
            - `username`: Campo para o username do advogado.
            - `bio`: Uma breve descrição sobre o advogado.
    - **Listar Advogados:**
        - `GET /lawyers/` - Lista todos os advogados cadastrados. Esta rota aceita um parâmetro de consulta para buscar advogados por username ou informações de biografia.
            - Parâmetros de consulta:
            - `query` (opcional): Filtra advogados por `username` ou `bio`.
            - Exemplo de uso:
            - `GET /lawyers/?query=termo_de_busca` - Retorna advogados cujo `username` ou `bio` contenha o termo de busca fornecido.
    - **Detalhes do Advogado:**
        - `GET /lawyers/<username>` - Retorna detalhes de um advogado específico com base no username.
    - **Atualiza o Advogado:**
        - `PUT /lawyers/<username>` - Atualiza os dados do advogado com base no username. 
    - **Deleta o Advogado:**
        - `DELETE /lawyers/<username>` - Deleta o advogado com base no username.
    - **Cria uma Empresa:**
        - `POST /companies/` - Cria a empresa com os dados apresentados abaixo:
            - Dados a serem preenchidos:
            - `name`: Campo para o nome da empresa.
            - `bio`: Campo para uma breve descrição da empresa.
    - **Listar Empresas:**
        - `GET /companies/` - Lista todas as empresas cadastradas.
    - **Detalhes da Empresa:**
        - `GET /company/name` - Retorna detalhes de uma empresa específica com base no nome.
    - **Atualiza a Empresa:**
        - `PUT /company/name` - Atualiza os dados da empresa com base no nome.
    - **Delete a Empresa:**
        - `DELETE /company/name` - Atualiza os dados da empresa com base no nome.
    - **Obter Token de Acesso:**
        - `POST /token/` - Obtém um token de acesso (JWT) fornecendo credenciais válidas.
    - **Atualizar Token de Acesso:**
        - `POST /token/refresh/` - Atualiza um token de acesso expirado para um novo token válido.
    - **Verificar Token de Acesso:**
        - `POST /token/verify/` - Verifica se um token de acesso é válido.

## Contribua e Compartilhe

Você tem ideias para melhorar o LegalConnect? Sinta-se à vontade para contribuir com novos recursos, correções ou melhorias no código. Siga estes passos:

1. Faça um fork do repositório.
2. Crie uma branch para sua contribuição: `git checkout -b minha-contribuicao`.
3. Commit as mudanças: `git commit -m 'Adicionando recurso novo'`.
4. Faça push da sua branch: `git push origin minha-contribuicao`.
5. Crie um pull request.

## Licença

Este projeto é licenciado sob os termos da MIT License, localizado no arquivo [LICENSE](https://github.com/eduardomoschen/lawyers-company-api/blob/main/LICENSE) neste repositório.
