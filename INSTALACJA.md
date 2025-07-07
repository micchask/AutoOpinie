# Instrukcja instalacji AutoOpinie

## Krok 1: Instalacja zależności
```bash
pip install -r requirements.txt
```

## Krok 2: Konfiguracja Google Maps API

1. **Idź do Google Cloud Console:**
   - Otwórz https://console.cloud.google.com/
   - Zaloguj się na swoje konto Google

2. **Utwórz projekt:**
   - Kliknij "Select a project" → "New Project"
   - Podaj nazwę projektu (np. "AutoOpinie")
   - Kliknij "Create"

3. **Włącz API:**
   - W menu po lewej kliknij "APIs & Services" → "Library"
   - Wyszukaj i włącz:
     - **Places API**
     - **Geocoding API**

4. **Utwórz klucz API:**
   - W menu po lewej kliknij "APIs & Services" → "Credentials"
   - Kliknij "Create Credentials" → "API Key"
   - Skopiuj wygenerowany klucz API

5. **Skonfiguruj klucz API:**
   - Utwórz plik `.env` w głównym katalogu
   - Dodaj linię: `GOOGLE_MAPS_API_KEY=twój_klucz_api_tutaj`

## Krok 3: Uruchomienie programu
```bash
python main.py
```

## Przykład pliku .env
```
GOOGLE_MAPS_API_KEY=AIzaSyC1234567890abcdefghijklmnopqrstuvwxyz
```

## Uwaga
- Klucz API jest darmowy dla pierwszych 1000 zapytań dziennie
- Nie udostępniaj swojego klucza API publicznie
- Możesz ograniczyć klucz API do konkretnych API w Google Cloud Console 