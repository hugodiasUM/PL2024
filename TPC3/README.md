# TPC4: Analisador léxico

## Autor

- Hugo Dias
- 100758

## Resumo

Este código em Python lê linhas de entrada do stdin, processa os símbolos encontrados e realiza operações de soma ou desligamento com base nesses símbolos.

1. Se encontrar 'on', em qualquer combinação de maiúsculas e minúsculas, define a variável somador como True.
2. Se encontrar 'off',em qualquer combinação de maiúsculas e minúsculas, define a variável somador como False.
3. Se encontrar um número (dígitos) e somador for True, adiciona o número à variável current.
4. Se encontrar '=', imprime a soma acumulada (current).