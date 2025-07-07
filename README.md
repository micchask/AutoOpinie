# AutoOpinie - Simple Google Maps Reviews Tool

Prosty program do pobierania opinii z Google Maps z ostatnich 7 dni.

## Opis
AutoOpinie to prosty program Python, który:
- Łączy się z Google Maps API
- Pobiera opinie z ostatnich 7 dni dla wybranego miejsca
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
   - Idź do https://console.cloud.google.com/
   - Utwórz nowy projekt lub wybierz istniejący
   - Włącz API: Places API, Geocoding API
   - Utwórz klucz API
   - Skopiuj klucz API

3. **Uruchom program:**
```bash
python main.py
```

## Użycie

1. Uruchom program: `python main.py`
2. Podaj nazwę miejsca (np. "Restauracja XYZ")
3. Program wyświetli opinie z ostatnich 7 dni z ocenami gwiazdkowymi

## Przykład wyjścia
```
Nazwa miejsca: Restauracja XYZ

⭐⭐⭐⭐⭐ Jan Kowalski
Świetna restauracja! Jedzenie pyszne, obsługa miła.

⭐⭐⭐⭐ Anna Nowak  
Dobra restauracja, ale trochę drogo.

⭐⭐⭐ Piotr Wiśniewski
Przeciętna jakość, nic specjalnego.
```

## Wymagania
- Python 3.8+
- Google Maps API key
- Zainstalowane zależności z requirements.txt
