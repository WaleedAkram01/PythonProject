# PythonProject

## Assalam o Alaikum, Faraz here so I have started to contribution your project

- Check the code if you don't understand use ChatGPT

### API FOR SEARCH

`https://api-docs.quran.com/docs/quran.com_versioned/search`

- The search pattern would be : `https://api.quran.com/api/v4/search?q=fire&language=ur`

- Here q={keyword} and language={language}

- Returns a response like :

```json
{
  "search": {
    "query": "fire",
    "total_results": 2,
    "current_page": 1,
    "total_pages": 1,
    "results": [
      {
        "verse_key": "52:13",
        "verse_id": 4748,
        "text": "يَوْمَ يُدَعُّونَ إِلَىٰ نَارِ جَهَنَّمَ دَعًّا",
        "highlighted": null,
        "words": [], // list of words
        "translations": [
          {
            "text": "Jis din unhein dhakke maar maar kar naar-e-jahannum (<em>fire</em> of hell) ki taraf le chala jayega",
            "resource_id": 831,
            "name": "Abul Ala Maududi(Roman Urdu)",
            "language_name": "urdu"
          }
        ]
      },
      {
        "verse_key": "40:47",
        "verse_id": 4180,
        "text": "وَإِذْ يَتَحَآجُّونَ فِى ٱلنَّارِ فَيَقُولُ ٱلضُّعَفَـٰٓؤُا۟ لِلَّذِينَ ٱسْتَكْبَرُوٓا۟ إِنَّا كُنَّا لَكُمْ تَبَعًا فَهَلْ أَنتُم مُّغْنُونَ عَنَّا نَصِيبًا مِّنَ ٱلنَّارِ",
        "highlighted": null,
        "words": [], /// list of words
        "translations": [
          {
            "text": "Phir zara khayal karo us waqt ka jab yeh log dozakh mein ek dusre se jhagad rahey hongey. Duniya mein jo log kamzoar thay woh badey ban-ney walon se kahenge ke “hum tumhare tabey(followers) thay, ab kya yahan tum naar-e-jahannum (hell <em>fire</em>) ki takleef ke kuch hissey se humko bacha logey",
            "resource_id": 831,
            "name": "Abul Ala Maududi(Roman Urdu)",
            "language_name": "urdu"
          }
        ]
      }
    ]
  }
}
```
