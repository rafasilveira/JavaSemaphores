# Exercício de Concorrência

Considere a existência de uma ponte em um desfiladeiro, com capacidade para passar somente uma pessoa de cada vez. Viajantes da região da Floresta Alta possuem prioridade em relação aos viajantes da região do Grande Rio. Somente após cinco viajantes da Floresta Alta terem atravessado a ponte é que um viajante da região do Grande Rio pode atravessar em sentido contrário. Desenvolva uma solução para este problema. Modele os viajantes como threads e utilize semáforos para sincronização.








```
< High Forest                 Great River >
-------------------------------------------
 o o o o o x         x         x o
-------------------------------------------
```
