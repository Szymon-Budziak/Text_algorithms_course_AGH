## Zadanie dotyczy wykorzystania odległości edycyjnej.

1. Zaimplementuj algorytm obliczania odległości edycyjnej w taki sposób, aby możliwe było określenie przynajmniej jednej
   sekwencji edycji (dodanie, usunięcie, zmiana znaku), która pozwala w minimalnej liczbie kroków, przekształcić jeden
   łańcuch w drugi.
2. Na podstawie poprzedniego punktu zaimplementuj prostą wizualizację działania algorytmu, poprzez wskazanie kolejnych
   wersji pierwszego łańcucha, w których dokonywana jest określona zmiana. "Wizualizacja" może działać w trybie
   tekstowym. Np. zmiana łańcuch "los" w "kloc" może być zrealizowana następująco:
    - *k*los (dodanie litery k)
    - klo*c* (zamiana s->c)
3. Przedstaw wynik działania algorytmu z p. 2 dla następujących par łańcuchów:
    - los - kloc
    - Łódź - Lodz
    - kwintesencja - quintessence
    - ATGAATCTTACCGCCTCG - ATGAGGCTCTGGCCCCTG
4. Zaimplementuj algorytm obliczania najdłuższego wspólnego podciągu dla pary ciągów elementów.
5. Korzystając z gotowego tokenizera (np spaCy - https://spacy.io/api/tokenizer) dokonaj podziału załączonego tekstu na
   tokeny.
6. Stwórz 2 wersje załączonego tekstu, w których usunięto 3% losowych tokenów.
7. Oblicz długość najdłuższego podciągu wspólnych tokenów dla tych tekstów.
8. Korzystając z algorytmu z punktu 4 skonstruuj narzędzie, o działaniu podobnym do narzędzia diff, tzn. wskazującego w
   dwóch plikach linie, które się różnią. Na wyjściu narzędzia powinny znaleźć się elementy, które nie należą do
   najdłuższego wspólnego podciągu. Należy wskazać skąd dana linia pochodzi (< > - pierwszy/drugi plik) oraz numer linii
   w danym pliku.
9. Przedstaw wynik działania narzędzia na tekstach z punktu 6. Zwróć uwagę na dodanie znaków przejścia do nowej linii,
   które są usuwane w trakcie tokenizacji.