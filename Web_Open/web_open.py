import importlib.util
import subprocess
import sys
import webbrowser
import time

def install_package(package):
    """Attempt to install a package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    except Exception as e:
        print(f"Failed to install {package}: {e}")
        sys.exit(1)

# Check if the 'googlesearch' module (provided by googlesearch-python) is installed.
if importlib.util.find_spec("googlesearch") is None:
    print("googlesearch module not found. Installing googlesearch-python...")
    install_package("googlesearch-python")
else:
    print("googlesearch module found.")

from googlesearch import search

def google_search(query, num_results=5):
    """
    Performs a Google search for the given query and returns a list of top URLs.
    Since unsupported keyword arguments like pause or stop may cause errors,
    we manually iterate over the generator and collect the desired number of results.
    """
    results = []
    try:
        for url in search(query):
            results.append(url)
            if len(results) >= num_results:
                break
    except Exception as e:
        print(f"Error during search for '{query}': {e}")
    return results

def open_urls(urls):
    """
    Opens each URL in the default web browser with a small delay.
    """
    for url in urls:
        print("Opening:", url)
        webbrowser.open(url)
        time.sleep(2)  # Pause so they don't all open at once.

def main():
    # Prompt the user for search terms.
    user_input = input("Enter search terms separated by commas (e.g., youtube, instagram, facebook): ")
    # Split the input into a list of terms, stripping whitespace.
    terms = [term.strip() for term in user_input.split(",") if term.strip()]

    # Append ".com" to each term if it's not already present.
    processed_terms = []
    for term in terms:
        if not term.endswith(".com"):
            term = term + ".com"
        processed_terms.append(term)

    # For each processed term, search and open the top URLs.
    for term in processed_terms:
        print(f"\nSearching for: {term}")
        urls = google_search(term, num_results=5)
        if urls:
            print("Found URLs:")
            for url in urls:
                print(url)
            open_urls(urls)
        else:
            print(f"No results found for: {term}")

if __name__ == "__main__":
    main()