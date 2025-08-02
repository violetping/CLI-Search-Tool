from googlesearch import search

def run(query, num=5):
    print(f"🔍 Google Search Results for: {query}\n")
    try:
        results = search(query, num_results=num)
        for i, url in enumerate(results, 1):
            print(f"{i}. {url}")
    except Exception as e:
        print(f"Error during search: {e}")