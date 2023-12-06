from googlesearch import search

def get_search_rankings(query, num_results=10):
    try:
        search_results = search(query, num_results=num_results, stop=num_results, pause=2)
        rankings = {link: rank + 1 for rank, link in enumerate(search_results)}
        return rankings
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":
    keywords = input("Enter the keyword(s) to search: ")
    rankings = get_search_rankings(keywords)

    if rankings:
        print("Search Rankings:")
        for link, rank in rankings.items():
            print(f"Rank {rank}: {link}")
    else:
        print("Failed to retrieve search rankings.")
