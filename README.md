# network
Esboço de resolução do problema Network.

## Objetivo

Dado o mapa de uma rede telefônica, informar quantos pontos são críticos para manter a conectividade da rede. Em outras palavras, informar quantos vértices, ao serem removidos (junto com suas arestas incidentes), aumentam o número de componentes conexas do grafo.

## Estrutura

```
network/
├── cc.py (algoritmo de componentes conexas adaptado)
├── graph.py (grafo como lista de adjacência)
├── input.txt (casos de teste)
├── main.py (leitura e saída de dados/solução aplicada)
└── README.md
```

## Execução

```powershell
cat input.txt | python main.py
```

## Referência

A implementação teve como referência [algs4-py](https://github.com/carubbi/RPG/tree/main/algs4-py).