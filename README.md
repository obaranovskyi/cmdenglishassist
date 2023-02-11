# cmdenglishassist

It Is your daily English learning assistance app.

## Installation
```bash
curl -s https://raw.githubusercontent.com/obaranovskyi/cmdenglishassist/main/install.sh | bash /dev/stdin
```

## Usage

To use `cmdenglishassist`:
1. Enter words in google translate and split by colon;
2. Copy the URL;
3. Use it with the current app to generate:
    - json with translations
    - mp3 with translations
    - english flashcards
    - anki flashcards

To generate the json with translations, run:
```bash
cmdenglishassist json 'https://translate.google.com/?sl=en&tl=uk&text=1.%20Enter%20words%20in%20google%20translate%20and%20split%20by%20colon%3B%0A2.%20Copy%20URL%20%0A3%20Use%20it%20with%20the%20current%20app%20to%20generate%20the%3A%0A&op=translate'
```

To generate the mp3 with translations, run:
```bash
cmdenglishassist audio 'https://translate.google.com/?sl=en&tl=uk&text=1.%20Enter%20words%20in%20google%20translate%20and%20split%20by%20colon%3B%0A2.%20Copy%20URL%20%0A3%20Use%20it%20with%20the%20current%20app%20to%20generate%20the%3A%0A&op=translate'
```

To generate the flashcards in pdf, run:
```bash
cmdenglishassist card 'https://translate.google.com/?sl=en&tl=uk&text=1.%20Enter%20words%20in%20google%20translate%20and%20split%20by%20colon%3B%0A2.%20Copy%20URL%20%0A3%20Use%20it%20with%20the%20current%20app%20to%20generate%20the%3A%0A&op=translate'
```
To generate anki flashcards, run:
```bash
cmdenglishassist anki 'https://translate.google.com/?sl=en&tl=uk&text=1.%20Enter%20words%20in%20google%20translate%20and%20split%20by%20colon%3B%0A2.%20Copy%20URL%20%0A3%20Use%20it%20with%20the%20current%20app%20to%20generate%20the%3A%0A&op=translate'
```

## Uninstall
To uninstall run the following script
```bash
curl -s https://raw.githubusercontent.com/obaranovskyi/cmdenglishassist/main/uninstall.sh | bash /dev/stdin
```
