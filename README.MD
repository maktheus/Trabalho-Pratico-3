#Algoritmos de Substituição de Página
Este projeto simula a alocação de páginas de processos na memória e compara o número de "page faults" para três algoritmos de substituição de página: FIFO (First-In, First-Out), LRU (Least Recently Used) e Segunda Chance (ou Relógio).

##Descrição
O sistema simula uma memória de 32MB, representada por um vetor de 8.000 elementos (8.000 quadros de 4KB). O programa lê uma string de referência, que é uma sequência de pares de números que representam um processo e uma página, respectivamente. A string de referência é usada para simular os acessos de página pelos processos.

###Exemplo de string de referência:

```

1,0;1,1;2,0;1,1;2,1;3,0;1,3;...;0,0;

```

Isto representa o acesso à página 0 do processo 1, seguido da página 1 do processo 1, e assim por diante. A página 0 do processo 0 significa o fim da string.

##Como Executar
Certifique-se de ter Python instalado em sua máquina.
Clone o repositório ou baixe os arquivos.
Execute o arquivo principal (por exemplo, main.py) usando o comando:

```
python main.py

```

O programa exibirá os resultados dos "page faults" para cada algoritmo.


##Resultados
Os resultados são exibidos no formato:

```
FIFO Page Faults: XXXX
LRU Page Faults: XXXX
SecondChance Page Faults: XXXX

```

Contribuições
Este é um projeto acadêmico. Contribuições e feedback são bem-vindos!