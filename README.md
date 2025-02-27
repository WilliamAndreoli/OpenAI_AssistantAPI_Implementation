# Assistente Pessoal de Treinamento

Este projeto implementa um assistente pessoal de treinamento utilizando a API da OpenAI. O assistente é projetado para fornecer orientações sobre exercícios físicos e nutrição, ajudando os usuários a alcançarem seus objetivos de fitness.

## Funcionalidades

- **Criação de Assistente**: O código permite a criação de um assistente personalizado que pode fornecer conselhos sobre treinamento e nutrição.
- **Interação em Threads**: O assistente pode interagir com os usuários em um formato de thread, permitindo um diálogo contínuo.
- **Mensagens Dinâmicas**: O assistente pode responder a perguntas específicas sobre treinamento, como "Quantas repetições eu preciso fazer para construir músculos magros?".
- **Monitoramento de Execução**: O código inclui uma função para monitorar a execução das interações com o assistente, garantindo que as respostas sejam recebidas antes de prosseguir.

## Tecnologias Utilizadas

- **OpenAI API**: Para a criação e gerenciamento do assistente e suas interações.
- **Python**: Linguagem de programação utilizada para implementar a lógica do assistente.
- **dotenv**: Para gerenciar variáveis de ambiente, como chaves de API.
- **Logging**: Para registrar informações e erros durante a execução do código.

## Aprendizados

Durante o desenvolvimento deste projeto, aprendi:

1. **Integração com APIs**: Como integrar e interagir com a API da OpenAI, incluindo a criação de assistentes e o gerenciamento de threads.
2. **Gerenciamento de Estado**: A importância de gerenciar o estado das interações, garantindo que as respostas sejam recebidas e processadas corretamente.
3. **Tratamento de Erros**: Como implementar um sistema de logging para capturar e registrar erros, facilitando a depuração e a manutenção do código.
4. **Estruturas de Dados**: A utilização de estruturas de dados para armazenar e manipular mensagens e respostas de forma eficiente.

## Como Usar

1. Clone o repositório.
2. Instale as dependências necessárias (ex: `openai`, `python-dotenv`).
3. Configure suas variáveis de ambiente com as chaves da API da OpenAI.
4. Execute o script `main.py` para interagir com o assistente.