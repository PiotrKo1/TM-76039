import xml.etree.ElementTree as ET
import glob

def run_game():
    print("=== INTERAKTYWNY KREATOR SELEKTOROW ===")
    target_id = input("1. Podaj wartosc 'id' z raportu (np. lunch): ").strip()
    target_tag = input("2. Podaj wartosc 'tag' z raportu (np. RadioButton): ").strip()
    matches = 0
    ns = '{http://schemas.android.com/apk/res/android}'
    
    for file in glob.glob("../Artefakt02/decompiled_apk/res/layout/**/*.xml", recursive=True):
        try:
            tree = ET.parse(file)
            for elem in tree.iter():
                node_id = elem.get(f'{ns}id', '')
                node_tag = elem.tag
                if target_id in node_id and target_tag == node_tag:
                    matches += 1
        except:
            continue

    print(f"\nWynik wyszukiwania: Znaleziono {matches} dopasowan.")
    if matches == 1:
        print(">>>>> STATUS: ZALICZONE! Twój selektor jest unikalny. <<<<<<")
        with open('xpath_verification.txt', 'w') as f:
            f.write(f"PROJEKT SELEKTORA:\nID: {target_id}\nTAG: {target_tag}\nSTATUS: ZALICZONE")
    else:
        print(">>> STATUS: BLAD! Musisz znalezc unikalna pare ID TAG (Wynik musi wynosic 1). <<<")

if __name__ == "__main__":
    run_game()