"""
UWAGA: Google Places API zwraca maksymalnie 5 opinii dla danego miejsca.
"""

def get_place_reviews(client, place_name, location=None):
    """
    Pobiera opinie miejsca

    Args:
        client: Google Maps API client
        place_name: Nazwa miejsca
        location: Lokalizacja (opcjonalnie)
    
    Returns:
        
    """
    
    try:
        # Wyszukiwanie miejsca
        if location:
            query = f'"{place_name}" {location}'
        else:
            query = f'"{place_name}"'
        
        print(f"Wyszukiwanie: {place_name}")
        
        # Wyszukiwanie miejsc
        places_result = client.places(query)
        places = places_result.get('results', [])
        
        if not places:
            print("Nie znaleziono miejsca!")
            return None
        
        # Wybieranie pierwszego miejsca
        place = places[0]
        place_id = place['place_id']
        
        print(f"Znaleziono: {place.get('name', 'Nieznane')}")
        print(f"Adres: {place.get('formatted_address', 'Brak adresu')}")
        
        # Pobieranie szczegółów miejsca z opiniami
        place_details = client.place(
            place_id,
            fields=['name', 'formatted_address', 'rating', 'user_ratings_total', 'reviews'],
            reviews_no_translations=True
        )
        
        place_info = place_details.get('result', {})
        reviews = place_info.get('reviews', [])
        
        if not reviews:
            print("Brak opinii dla tego miejsca!")
            return None
        
        print(f"Znaleziono {len(reviews)} opinii")
        
        # Sortowanie opinii od najnowszych po polu 'time' (timestamp)
        reviews_sorted = sorted(reviews, key=lambda r: r.get('time', 0), reverse=True)
        
        top_reviews = reviews_sorted[:10]
        print(f"Wyświetlamy {len(top_reviews)} najnowszych opinii")
        
        return {
            'name': place_info.get('name', place_name),
            'address': place_info.get('formatted_address', ''),
            'rating': place_info.get('rating', 0),
            'total_ratings': place_info.get('user_ratings_total', 0),
            'recent_reviews': top_reviews
        }
        
    except Exception as e:
        print(f"Błąd podczas pobierania opinii:{e}")
        return None
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
    # output.append("Opinie z ostatnich 7 dni:")
    output.append("Opinie użytkowników:")
    output.append("=" * 50)
    output.append("")
    
    for review in place_data['recent_reviews']:
        # Formatowanie oceny gwiazdkami
        rating = review.get('rating', 0)
        stars = int(rating)
        
        # Informacje o autorze
        author = review.get('author_name', 'Anonimowy')
        time_desc = review.get('relative_time_description', '')
        
        # Tekst opinii
        text = review.get('text', 'Brak tekstu')
        
        # Dodawanie do wyjścia
        output.append(f"{stars}/5 {author} ({time_desc})")
        output.append(text)
        output.append("")
    
    return "\n".join(output) 