import requests

def get_search_rankings(query, api_key, cx, num_results=10):
    base_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": api_key,
        "cx": cx,
        "q": query,
        "num": num_results
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()
        items = data.get("items", [])
        rankings = {item["link"]: rank + 1 for rank, item in enumerate(items)}
        return rankings
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    api_key = "YOUR_API_KEY"  # Replace with your actual API key
    cx = "YOUR_CUSTOM_SEARCH_ENGINE_ID"  # Replace with your actual Custom Search Engine ID
    keywords = input("Enter the keyword(s) to search: ")
    rankings = get_search_rankings(keywords, api_key, cx)

    if rankings:
        print("Search Rankings:")
        for link, rank in rankings.items():
            print(f"Rank {rank}: {link}")
    else:
        print("Failed to retrieve search rankings.")
