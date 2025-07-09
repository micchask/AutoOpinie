# AutoOpinie - Simple Google Maps Reviews Tool

Prosty program do pobierania opinii z Google Maps (maksymalnie 5 opinii, wg ograniczeń API).

## Opis
AutoOpinie to prosty program Python, który:
- Łączy się z Google Maps API
- Pobiera maksymalnie 5 opinii dla wybranego miejsca (zgodnie z ograniczeniami API)
- Generuje prosty tekst z nazwą miejsca i opiniami wraz z ocenami

## Struktura plików
```
AutoOpinie/
├── google_api.py      # Połączenie z Google Maps API
├── get_reviews.py     # Pobieranie opinii z ostatnich 7 dni
├── main.py           # Interfejs użytkownika
└── requirements.txt  # Zależności
```

## Instalacja

1. **Zainstaluj zależności:**
```bash
pip install -r requirements.txt
```
2. **Skonfiguruj Google Maps API:**
   - pobierz klucz api 
## Użycie

1. Uruchom program: `python3 main.py`
2. Podaj nazwę miejsca (np. "Restauracja XYZ")
3. Program wyświetli do 5 opinii (zgodnie z ograniczeniami API) z ocenami gwiazdkowymi

## Przykład wyjścia
```
Nazwa miejsca: Restauracja XYZ

5/5 Jan Kowalski
Świetna restauracja! Jedzenie pyszne, obsługa miła.

4/5 Anna Nowak  
Dobra restauracja, ale trochę drogo.

3/5 Piotr Wiśniewski
Przeciętna jakość, nic specjalnego.
```

## Wymagania
- Python 3.8+
- Google Maps API key
- Zainstalowane zależności z requirements.txt

## Podsumowanie 
Program miał wyświetlać opinie sprzed ostatniu 7 dni lecz okazało się, ze googlemaps api
ma ograniczenie do wyswietlania tylko 5 opinii bazowanych na wyborze api
