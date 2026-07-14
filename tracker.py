import phonenumbers
from phonenumbers import geocoder, carrier
from geopy.geocoders import Nominatim
import sys

def track_phone_number(phone_number_str):
    try:
        parsed_number = phonenumbers.parse(phone_number_str)

        if not phonenumbers.is_valid_number(parsed_number):
            print("Invalid phone number.")
            return
        print(f"Phone Number: {phone_number_str}")
        region= geocoder.description_for_number(parsed_number, 'en')
        print(f"Region: {region}")

        service_info = carrier.name_for_number(parsed_number, 'en')
        print(f"Service Provider: {service_info}")

        if region:
            search_quyery = f"{region}, {service_info}"
        else:
            search_quyery = service_info
            print(f"location search query: {search_quyery}")

        geolocator = Nominatim(user_agent="phone_tracker")
        location = geolocator.geocode(search_quyery)

        if location:
            print(f"Approximate Location: {location.address}")
            print(f"Latitude: {location.latitude}, Longitude: {location.longitude}")
            print(f"Google Maps Link: https://www.google.com/maps/search/?api=1&query={location.latitude},{location.longitude}")
        else:
            print("Unable to fetch coordinates.")

    except phonenumbers.NumberParseException as e:
        print(f"Paerse error: {e}")
    except Exception as e:
        print(f"Error parsing phone number: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python tracker.py <phone_number>")
        print("Example: python tracker.py +1234567890")
        sys.exit(1)
        
    track_phone_number(sys.argv[1])