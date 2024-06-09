# Importa il modulo sys per gestire l'input da tastiera
import sys

# Chiede all'utente di inserire un valore
print("Inserisci un valore:")

# Legge il valore inserito dall'utente
valore = sys.stdin.readline()

# Rimuove eventuali caratteri di nuova linea alla fine del valore
valore = valore.strip()

# Stampa il valore inserito dall'utente
print("Hai inserito:", valore)