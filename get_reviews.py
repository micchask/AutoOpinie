"""
Get Reviews from Google Maps
Pobieranie opinii z ostatnich 7 dni
"""

from datetime import datetime, timedelta
import time

def get_place_reviews(client, place_name, location=None):
    """
    Pobiera opinie z ostatnich 7 dni dla wybranego miejsca
    
    Args:
        client: Google Maps API client
        place_name: Nazwa miejsca
        location: Lokalizacja (opcjonalnie)
    
    Returns:
        Lista opinii z ostatnich 7 dni
    """
    
    try:
        # Wyszukiwanie miejsca
        if location:
            query = f'"{place_name}" {location}'
        else:
            query = f'"{place_name}"'
        
        print(f"🔍 Wyszukiwanie: {place_name}")
        
        # Wyszukiwanie miejsc
        places_result = client.places(query)
        places = places_result.get('results', [])
        
        if not places:
            print("❌ Nie znaleziono miejsca!")
            return None
        
        # Wybieranie pierwszego miejsca
        place = places[0]
        place_id = place['place_id']
        
        print(f"✅ Znaleziono: {place.get('name', 'Nieznane')}")
        print(f"📍 Adres: {place.get('formatted_address', 'Brak adresu')}")
        
        # Pobieranie szczegółów miejsca z opiniami
        place_details = client.place(
            place_id,
            fields=['name', 'formatted_address', 'rating', 'user_ratings_total', 'reviews']
        )
        
        place_info = place_details.get('result', {})
        reviews = place_info.get('reviews', [])
        
        if not reviews:
            print("❌ Brak opinii dla tego miejsca!")
            return None
        
        print(f"📊 Znaleziono {len(reviews)} opinii")
        
        # Filtrowanie opinii z ostatnich 7 dni
        recent_reviews = filter_recent_reviews(reviews)
        
        if not recent_reviews:
            print("❌ Brak opinii z ostatnich 7 dni!")
            return None
        
        print(f"✅ Znaleziono {len(recent_reviews)} opinii z ostatnich 7 dni")
        
        return {
            'name': place_info.get('name', place_name),
            'address': place_info.get('formatted_address', ''),
            'rating': place_info.get('rating', 0),
            'total_ratings': place_info.get('user_ratings_total', 0),
            'recent_reviews': recent_reviews
        }
        
    except Exception as e:
        print(f"❌ Błąd podczas pobierania opinii: {e}")
        return None

def filter_recent_reviews(reviews):
    """
    Filtruje opinie z ostatnich 7 dni
    
    Args:
        reviews: Lista opinii z Google Maps
    
    Returns:
        Lista opinii z ostatnich 7 dni
    """
    
    # Data 7 dni temu
    seven_days_ago = datetime.now() - timedelta(days=7)
    recent_reviews = []
    
    for review in reviews:
        # Sprawdzanie czasu opinii
        time_desc = review.get('relative_time_description', '')
        
        # Sprawdzanie czy opinia jest z ostatnich 7 dni
        if is_recent_review(time_desc):
            recent_reviews.append(review)
    
    return recent_reviews

def is_recent_review(time_description):
    """
    Sprawdza czy opinia jest z ostatnich 7 dni
    
    Args:
        time_description: Opis czasu (np. "2 dni temu")
    
    Returns:
        True jeśli opinia jest z ostatnich 7 dni
    """
    
    if not time_description:
        return False
    
    time_desc_lower = time_description.lower()
    
    # Sprawdzanie różnych formatów czasu
    if 'dziś' in time_desc_lower or 'today' in time_desc_lower:
        return True
    
    if 'wczoraj' in time_desc_lower or 'yesterday' in time_desc_lower:
        return True
    
    # Sprawdzanie dni
    if 'dzień' in time_desc_lower or 'dni' in time_desc_lower or 'day' in time_desc_lower or 'days' in time_desc_lower:
        # Wyciąganie liczby dni
        import re
        numbers = re.findall(r'\d+', time_description)
        if numbers:
            days = int(numbers[0])
            return days <= 7
    
    # Sprawdzanie tygodni
    if 'tydzień' in time_desc_lower or 'tygodni' in time_desc_lower or 'week' in time_desc_lower or 'weeks' in time_desc_lower:
        numbers = re.findall(r'\d+', time_description)
        if numbers:
            weeks = int(numbers[0])
            return weeks == 1  # Tylko 1 tydzień
    
    return False

def format_reviews_output(place_data):
    """
    Formatuje opinie do wyświetlenia
    
    Args:
        place_data: Dane miejsca z opiniami
    
    Returns:
        Sformatowany tekst z opiniami
    """
    
    if not place_data:
        return "Brak danych do wyświetlenia"
    
    output = []
    output.append(f"Nazwa miejsca: {place_data['name']}")
    output.append(f"Adres: {place_data['address']}")
    output.append(f"Ogólna ocena: {place_data['rating']:.1f}/5.0 ({place_data['total_ratings']} opinii)")
    output.append("")
    output.append("Opinie z ostatnich 7 dni:")
    output.append("=" * 50)
    output.append("")
    
    for review in place_data['recent_reviews']:
        # Formatowanie oceny gwiazdkami
        rating = review.get('rating', 0)
        stars = "⭐" * int(rating)
        
        # Informacje o autorze
        author = review.get('author_name', 'Anonimowy')
        time_desc = review.get('relative_time_description', '')
        
        # Tekst opinii
        text = review.get('text', 'Brak tekstu')
        
        # Dodawanie do wyjścia
        output.append(f"{stars} {author} ({time_desc})")
        output.append(text)
        output.append("")
    
    return "\n".join(output) 