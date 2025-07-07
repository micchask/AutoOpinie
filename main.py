#!/usr/bin/env python3
"""
AutoOpinie - Main Application
Prosty program do pobierania opinii z Google Maps
"""

from google_api import setup_google_api
from get_reviews import get_place_reviews, format_reviews_output

def main():
    """
    Główna funkcja aplikacji
    """
    print("🚀 AutoOpinie - Opinie z Google Maps")
    print("=" * 40)
    print("Pobiera opinie z ostatnich 7 dni dla wybranego miejsca")
    print()
    
    # Konfiguracja Google Maps API
    client = setup_google_api()
    if not client:
        return
    
    print()
    
    while True:
        try:
            # Pobieranie nazwy miejsca od użytkownika
            place_name = input("🔍 Podaj nazwę miejsca (lub 'quit' aby wyjść): ").strip()
            
            if place_name.lower() in ['quit', 'exit', 'wyjdz', 'koniec']:
                print("👋 Do widzenia!")
                break
            
            if not place_name:
                print("❌ Nazwa miejsca jest wymagana!")
                continue
            
            # Opcjonalna lokalizacja
            location = input("📍 Podaj lokalizację (opcjonalnie, np. 'Warszawa'): ").strip()
            
            print()
            print("⏳ Pobieranie opinii...")
            print()
            
            # Pobieranie opinii
            place_data = get_place_reviews(client, place_name, location if location else None)
            
            if place_data:
                # Wyświetlanie sformatowanych opinii
                output = format_reviews_output(place_data)
                print(output)
                
                # Opcja zapisania do pliku
                save_choice = input("\n💾 Czy chcesz zapisać opinie do pliku? (t/n): ").strip().lower()
                if save_choice in ['t', 'tak', 'y', 'yes']:
                    save_to_file(output, place_data['name'])
            else:
                print("❌ Nie udało się pobrać opinii dla tego miejsca.")
            
            print()
            print("-" * 40)
            print()
            
        except KeyboardInterrupt:
            print("\n\n👋 Do widzenia!")
            break
        except Exception as e:
            print(f"❌ Wystąpił błąd: {e}")
            print()

def save_to_file(content, place_name):
    """
    Zapisuje opinie do pliku tekstowego
    
    Args:
        content: Zawartość do zapisania
        place_name: Nazwa miejsca
    """
    try:
        # Czyszczenie nazwy pliku
        safe_name = "".join(c for c in place_name if c.isalnum() or c in (' ', '-', '_')).rstrip()
        safe_name = safe_name.replace(' ', '_')
        
        filename = f"opinie_{safe_name}.txt"
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Opinie zapisane do pliku: {filename}")
        
    except Exception as e:
        print(f"❌ Błąd podczas zapisywania pliku: {e}")

if __name__ == "__main__":
    main() 