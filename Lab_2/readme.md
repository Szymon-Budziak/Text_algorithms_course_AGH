## Lab 2
1. Przyjmij następujący zbiór danych wejściowych:
 - bbb$
 - aabbabd
 - ababcd
 - abcbccd
 - załączony plik (`1997_714_head.txt`).
2. Upewnij się, że każdy łańcuch na końcu posiada unikalny znak (marker), a jeśli go nie ma, to dodaj ten znak.
3. Zaimplementuj algorytm konstruujący strukturę trie, która przechowuje wszystkie sufiksy łańcucha danego na wejściu.
4. Zaimplementuj algorytm konstruujący drzewo sufiksów.
5. Upewnij się, że powstałe struktury danych są poprawne. Możesz np. sprawdzić, czy struktura zawiera jakiś ciąg znaków i porównać wyniki z algorytmem wyszukiwania wzorców.
6. Porównaj szybkość działania algorytmów konstruujących struktury danych dla danych z p. 1 w następujących wariantach:
 - Trie - czas budowy O(n^2), rozmiar drzewa O(n^2), n - długość tekstu (można wykorzystać fragment załączonego tekstu);
 - Drzewo sufiksów bez wykorzystania procedury fast_find oraz elementów "link" - czas budowy O(n^2), rozmiar drzewa O(n) (w trakcie tworzenia drzewa rozmiar ten nie może być większy).
