# Workprogress
#### Done

- Turing Maschine ( a^n b^n c^n; Addition; Paldindrom)
- 3-Col
```python
# Datenstruktur von Graphen | directed
nodes = ['A', 'B', 'C', 'D', 'E']
neighbors = {}
neighbors['A'] = ['B']
neighbors['B'] = ['A']
neighbors['C'] = ['A']
neighbors['D'] = ['A']
neighbors['E'] = ['D', 'A', 'C']
# Datenstruktur von Graphen | undirected
nodes = ['A', 'B', 'C', 'D', 'E']
neighbors = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'E')]
```
- SAT-Solver
- QBF-Solver (im SAT-Solver)
- SUBSETSUM 
- CLIQUE
- Inverted Graph
- RANDOM Median
- Zero-Knowlege Beweis für 3-Col = In Text

#### Unfinished

- RANDOM Primes PARTIALLY DONE (Jakobisymbol)
- Vertex Cover ODER Set Cover
- COOK-LEVIN Theorem (ggf falsches Handling für 'k' UND Übergang Regel fehlt noch)
- CLIQUE auf INDSET FORMALLY DONE (muss nur implementiert werden)

#### To Be Done

- Reduktionen
  - INDSET auf CLIQUE
  - 3CNF-SAT auf INDSET
- 2-SAT NL-complete beweis
- Rekursive Erreichbarkeit Satz von Savitch auf Graphen
- Reduktion 3-SAT < SUBSETSUM
- Traveling Salesman Strategien

## Papers
Zu lesen:
- [On Computable Numbers](https://www.cs.virginia.edu/~robins/Turing_Paper_1936.pdf)
- [Karp 21 NP Probleme](https://people.eecs.berkeley.edu/~luca/cs172/karp.pdf)
- [Immerman-Szelepscenyi Theorem]()
- [Minesweeper NP-Completeness](http://web.math.ucsb.edu/~padraic/ucsb_2014_15/ccs_problem_solving_w2015/NP3.pdf)
### Reduktionen
#### CLIQUE auf INDSET
[source1](https://math.stackexchange.com/questions/61963/clique-and-independent-set-proof),
[source2](https://cs.stackexchange.com/questions/7120/reducing-clique-to-independent-set)

Gegeben sei ein Graph G mit einer k-CLIQUE. Der invertierte Graph ~G hat dann genau k Punkte, die nicht miteinander verbunden sein können.

Ergo stellen die Punkte der k-CLIQUE das Independent Set von ~G dar.

Die Reduktion
- Invertierung des Graphs von G zu ~G
- max(CLIQUE(~G)) = INDSET von G

Also gilt: Für jede k-Clique von ~G gibt es ein INDSET der größe k in G

INDSET auf CLIQUE existiert vice versa: für einen Graphen G mit einem INDSET der Größe k existiert im inversiven Graph ~G eine CLIQUE der Größe k

#### Zero Knowledge 3-Col

[soruce](http://web.mit.edu/~ezyang/Public/graph/svg.html)

Sei ein Graph G gegeben. Der Prover kennt bereits die 3 Färbbarkeit des Graphen.

- Ein Verifier wählt eine Kante in G
- Der Solver zeigt ihm, die Farben der beiden Punkte
- wählt der Verifier eine bereits gewählte Kante, so kann der Solver ihm andere Farben zeigen, der unterschied bleibt aber bestehen
- Je mehr Kanten der Verifier gesehen hat, desto höher ist die Wahrscheinlichkeit, dass der Beweis akzeptiert wird
