import requests
import json
# %%
def get_exchange_rates():
    """Fetch exchange rates from the API and return the conversion rates"""
    url = "https://v6.exchangerate-api.com/v6/c11a2331b51cc2e55732b236/latest/USD"
    response = requests.get(url)
      
    if response.status_code == 200:
        data = response.json()
        print("API Response Structure:")
        print(json.dumps(data, indent=2))
        
        if 'conversion_rates' in data:
            print("Available keys in the response:", list(data.keys()))
            return data['conversion_rates']

        else:
            print("Expected 'conversion_rates' key not found in the API response.")
            print("Available keys in the response:", list(data.keys()))
            raise KeyError("'conversion_rates' key not found in API response")
    else:
        print(f"Failed to fetch exchange rates. Status code: {response.status_code}")
        print("Response content:", response.text)
        raise Exception("Failed to fetch exchange rates")
# %%
get_exchange_rates()