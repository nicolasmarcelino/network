from graph import Graph
from cc import CC

while True:
   total_v = int(input())

   if total_v == 0:
      break

   g = Graph(total_v)

   while True:
      conexoes = input().split()

      if conexoes[0] == "0":
         break

      for i in range(1, len(conexoes)):
         g.add_edge(int(conexoes[0]) - 1, int(conexoes[i]) - 1)

   criticos = 0

   for v in range(g.V):
      dfs_sem_v = CC(g, v)
      if dfs_sem_v.count > 1:
         criticos = criticos + 1

   print(criticos)

'''
total_v = int(input())

grafo = Graph(total_v)

conexoes = input().split()

for i in range(1, len(conexoes)):
   grafo.add_edge(int(conexoes[0]) - 1, int(conexoes[i]) - 1)

criticos = 0
g = grafo

for v in range(g.V):
   dfs_sem_v = CC(g, v)
   if dfs_sem_v.count > 1:
      criticos = criticos + 1

print(criticos)


g1 = Graph(6)

g1.add_edge(1, 0)
g1.add_edge(1, 2)

g1.add_edge(4, 3)
g1.add_edge(4, 5)
g1.add_edge(4, 1)

g2 = Graph(5)

g2.add_edge(4,0)
g2.add_edge(4,1)
g2.add_edge(4,2)
g2.add_edge(4,3)

g = g2

for v in range(g.V):
   dfs_sem_v = CC(g, v)
   if dfs_sem_v.count > 1:
      print("O vértice", v, "é crítico")


1-based indexing

1: [2]
2: [1, 3, 5]
3: [2]
4: [5]
5: [4, 6, 2]
6: [5]

0-based indexing

0: [1]
1: [0, 2, 4]
2: [1]
3: [4]
4: [3, 5, 1]
5: [4]

'''