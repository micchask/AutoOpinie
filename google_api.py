"""
Google Maps API Connection
"""
import os
import googlemaps
from dotenv import load_dotenv

def setup_google_api():
    """
    Konfiguracja Google Maps API
    1. Utwórz klucz API (Credentials -> Create Credentials -> API Key)
    2. Do pliku .env dodaj: GOOGLE_MAPS_API_KEY=twój_klucz_api
    """
    # Ładowanie zmiennych środowiskowych
    load_dotenv()
    # Pobieranie klucza API
    api_key = os.getenv('GOOGLE_MAPS_API_KEY')
    
    if not api_key:
        print("Błąd: Brak klucza API Google Maps! Pobierz go z Google Cloud Console")
        return None
    
    try:
        # Tworzenie klienta Google Maps
        client = googlemaps.Client(key=api_key)
        print("✅ Połączenie z Google Maps API udane!")
        return client
    except Exception as e:
        print(f"Błąd połączenia z Google Maps API: {e}")
        return None 