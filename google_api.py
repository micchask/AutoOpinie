"""
Google Maps API Connection
Proste połączenie z Google Maps API
"""

import os
import googlemaps
from dotenv import load_dotenv

def setup_google_api():
    """
    Konfiguracja Google Maps API
    
    INSTRUKCJA:
    1. Idź do https://console.cloud.google.com/
    2. Utwórz nowy projekt lub wybierz istniejący
    3. Włącz API: Places API, Geocoding API
    4. Utwórz klucz API (Credentials -> Create Credentials -> API Key)
    5. Skopiuj klucz API
    6. Utwórz plik .env i dodaj: GOOGLE_MAPS_API_KEY=twój_klucz_api
    """
    
    # Ładowanie zmiennych środowiskowych
    load_dotenv()
    
    # Pobieranie klucza API
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    
    if not api_key:
        print("❌ Błąd: Brak klucza API Google Maps!")
        print("\n📝 Instrukcja konfiguracji:")
        print("1. Idź do https://console.cloud.google.com/")
        print("2. Utwórz nowy projekt lub wybierz istniejący")
        print("3. Włącz API: Places API, Geocoding API")
        print("4. Utwórz klucz API (Credentials -> Create Credentials -> API Key)")
        print("5. Skopiuj klucz API")
        print("6. Utwórz plik .env i dodaj: GOOGLE_MAPS_API_KEY=twój_klucz_api")
        return None
    
    try:
        # Tworzenie klienta Google Maps
        client = googlemaps.Client(key=api_key)
        print("✅ Połączenie z Google Maps API udane!")
        return client
    except Exception as e:
        print(f"❌ Błąd połączenia z Google Maps API: {e}")
        return None 