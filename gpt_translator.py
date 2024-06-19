import openai
import time

def translate_text(text, prompt_language):
    openai.api_key = '[open_ai_api_key]'

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a translator. Your task is to provide direct translations without any additional information or formatting."},
            {"role": "user", "content": f"Translate this to {prompt_language}: {text}"}
        ]
    )
    return response['choices'][0]['message']['content']

def process_file(file_path, languages):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        for language in languages:
            output_file = f'response_for_{language}.txt'
            with open(output_file, 'w', encoding='utf-8') as f:
                for line in lines:
                    translated_text = translate_text(line.strip(), language)
                    f.write(translated_text + '\n')
                    print(f"{line.strip()} -> {translated_text}")
                    time.sleep(1)
                print(f"Çeviri tamamlandı ve {output_file} dosyasına kaydedildi.")

    except FileNotFoundError:
        print("Dosya bulunamadı.")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

languages = ["Turkish"]

file_path = 'word_list.txt'

process_file(file_path, languages)
