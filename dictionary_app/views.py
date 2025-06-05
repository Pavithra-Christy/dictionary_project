import requests
from django.shortcuts import render
from .models import SearchLog  # Import the SearchLog model

def word_search(request):
    word_data = {}
    error = None

    # Check if a word was submitted in the query string
    if 'word' in request.GET:
        word = request.GET['word'].strip()

        if word:
            url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    data = response.json()[0]
                    word_data = {
                        'word': data.get('word', ''),
                        'phonetics': data.get('phonetics', []),
                        'meanings': data.get('meanings', [])
                    }

                    # ✅ Save the successful search to the database
                    SearchLog.objects.create(word=word)

                else:
                    error = f"No results found for '{word}'."
            except requests.exceptions.RequestException:
                error = "There was a problem connecting to the dictionary API."
            except (KeyError, IndexError, ValueError):
                error = "The API response format was not as expected."
        else:
            error = "Please enter a valid word."

    return render(request, 'search.html', {
        'word_data': word_data,
        'error': error
    })
