from googletrans import Translator

def translate_text(input_text, target_language):
    translator = Translator()
    translated_text = translator.translate(input_text, dest=target_language)
    return translated_text.text

# Example usage
if __name__ == "__main__":
    input_text = input("Enter the text you want to translate: ")
    target_language = input("Enter the target language (e.g., 'en' for English, 'es' for Spanish): ")

    translated_text = translate_text(input_text, target_language)
    print("Translated text: ", translated_text)
