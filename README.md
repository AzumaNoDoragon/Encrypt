# Encrypt
Um sistema de criptografia personalizado em Python que utiliza matriz de transposição para codificar e verificar senhas. Ideal para explorar conceitos básicos de segurança e lógica programacional.

# Sistema de Criptografia Personalizada em Python

Este projeto implementa um sistema de criptografia personalizado, desenvolvido como uma abordagem prática para explorar conceitos de lógica e segurança da informação. O algoritmo utiliza uma matriz de transposição de caracteres para codificar e verificar senhas, oferecendo uma visão detalhada de como funcionam os mecanismos básicos de criptografia.

Embora este sistema não seja destinado ao uso em produção, ele demonstra os fundamentos de operações criptográficas, manipulação de strings e lógica programacional.

## Funcionalidades
- **Codificação Personalizada:** Cria uma senha criptografada a partir de uma combinação de senha e codificador fornecidos pelo usuário.
- **Verificação de Senhas:** Permite autenticação comparando a senha inserida com o valor criptografado armazenado.
- **Alteração de Senhas:** Inclui a opção de redefinir a senha criptografada e testar sua validade.

## Características Técnicas
1. A senha e o codificador fornecidos pelo usuário são processados para garantir o alinhamento de seus tamanhos.
2. Uma matriz de transposição é gerada para realizar o mapeamento entre caracteres.
3. A senha é codificada utilizando a matriz e armazenada em um arquivo de texto (`senha.txt`).
4. O sistema permite que a senha seja alterada e testada dinamicamente.

## Configuração Inicial
- **Senha padrão:** `12345`  
- **Codificador padrão:** `teste`  

Esses valores podem ser modificados diretamente no sistema ao executar o script.

## Aviso
Este sistema não é projetado para aplicações de produção ou armazenamento de informações sensíveis. Para projetos reais, recomenda-se o uso de bibliotecas como `hashlib` para algoritmos robustos como SHA-256 ou bcrypt. Este projeto tem como objetivo demonstrar conceitos fundamentais de criptografia e lógica aplicada.

## Como Utilizar
1. Clone este repositório.
2. Execute o script `codification.py`.
3. Siga as instruções no terminal para codificar, verificar ou redefinir senhas.

## Contribuições
Contribuições são bem-vindas! Caso tenha sugestões de melhorias ou novas funcionalidades, sinta-se à vontade para abrir uma *issue* ou enviar um *pull request*.
