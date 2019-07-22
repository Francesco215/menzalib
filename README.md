# TexPy

### Descrizione rapida della libreria
Questa libreria e' stata creata da studenti del corso di Laboratorio 3 dell'universita' di Pisa per velocizzare la stesura delle relazioni, contiene funzioni che potrebbero risultare utili pure a corsi come Laboratorio 1 e 2  
In particolare permettono di stampare una tabella in LaTeX senza dover riscrivere tutti i dati tra $ ed &

Ad esempio creiamo una tabella con misure ed errori:
```python
import texpy as tp
import numpy as np
x = np.linspace(1, 2, 10) # Genero dei dati
y = 5*x
dx, dy = x*0.01, y*0.01 # Suppongo che l'errore sia l'1% della misura
misure = [x, y] # Creo la matrice con i valori
errori_misure = [dx, dy] # Creo la matrice con gli errori
A = tp.ne(misure, errori_misure) # Crea una matrice del tipo misura +- errore come spiegato sotto
tp.mat(tab)
```
Output:
```latex
Copia tutto quello che c'è tra le linee
--------------------------
\begin{tabular}{cc}
\hline
	$1.00 \pm 0.01$ & $5.00 \pm 0.05$ \\
	$1.11 \pm 0.01$ & $5.56 \pm 0.06$ \\
	$1.22 \pm 0.01$ & $6.11 \pm 0.06$ \\
	$1.33 \pm 0.01$ & $6.67 \pm 0.07$ \\
	$1.44 \pm 0.01$ & $7.22 \pm 0.07$ \\
	$1.56 \pm 0.02$ & $7.78 \pm 0.08$ \\
	$1.67 \pm 0.02$ & $8.33 \pm 0.08$ \\
	$1.78 \pm 0.02$ & $8.89 \pm 0.09$ \\
	$1.89 \pm 0.02$ & $9.44 \pm 0.09$ \\
	$2.00 \pm 0.02$ & $(1.00 \pm 0.01) \times 10^{1}$ \\
	\hline
\end{tabular}
--------------------------
```

### Installazione
Scrivere su terminale `pip install texpy`

## Descrizione dettagliata delle funzioni  
Tutte le funzioni sono vettorizzate, ovvero possono prendere in input numeri, vettori, matrici, tensori ecc... e li trattano secondo le regole di numpy, per maggiori informazioni: [numpy broadcasting](https://www.numpy.org/devdocs/user/theory.broadcasting.html)  
In pratica puoi dare anche array alle funzioni e queste fanno quello che ci aspetta

### Notazione scientifica con errore
`ne(x,dx)` Ritorna una stringa latex con il valore x e l'errore
Parametri:
- x: valore della misura
- dx: errore

```python
# Es: misuro x=45.897 +- 135
>>> import texpy as tp
>>> tp.ne(45897,135)
```
Output:
```latex
$(4.59\pm0.01)\times 10^{4}$
```

### Notazione scientifica di valore con errore
`nes(x,dx)`
```python
# Es: misuro x=45.897 +- 135
>>> tp.nes(45897,135)

#Es: voglio solo il valore di x=45.897
>>> tp.nes(45897)
```
Output:
```latex
$4.59\\times 10^{4}$', '$0.01\\times 10^{4}$

$4.59\times 10^{4}$
```
### Tabella per latex
`mat(Matrice,titolo=None,file=None)`
Stampa su terminale una matrice fatta di stringhe per latex
- Matrice: matrice fatta di stringhe contenente tutti i valori
- titolo: Opzionale, il titolo della tabella
- file: Opzionale, file in cui la matrice viene stampata (ATTENZIONE SOVRASCRIVE IL FILE!)

```python
# Esempio:
>>> import texpy as tp
>>> M=[['guardati','l\'attacco'],
		['dei','giganti']]
>>> tp.mat(M,'titolo & a caso')
```
Output:
```latex
Copia tutto quello che c'è tra le linee
 --------------------------
 \begin{tabular}{cc}
 \hline
	titolo & a caso\\ 
 \hline
	guardati & l'attacco \\
	dei & giganti \\
 \hline
 \end{tabular}
--------------------------
```

### Notazione scientifica
`ns(n,nrif=,nult=Null)`  
Funzione della notazione scientifica di un singolo numero con un numero di riferimento nrif scritto in latex.
I parametri sono:
- n: numero da portare in notazione scientifica
- nrif: Opzionale, serve a dire a che ordine di grandezza deve essere portato il numero, se non specificato assume il valore di n
- nult: Opzionale, serve a dire quante cifre scrivere dopo la virgola 

```python
# Es: Porto in notazione scientifica 45.897.241
>>> import texpy as tp
>>> tp.ns(45897)

# Es: Porto in notazione scientifica 45.897 con l'ordine di grandezza di 135
>>> tp.ns(45897,135)

#Es:Porto in notazione scientifica 45.897 con l'ordine di grandezza di 135 e
#scrivo i numeri dopo la virgola fino all'ordine di grandezza di 3 (assicurati che quelle cifre esistano)
>>> tp.ns(45897,135,3)
```
Output:
```latex
$4.59\times 10^{7}$

$458\times 10^{2}$

$458.97\\times 10^{2}$
```