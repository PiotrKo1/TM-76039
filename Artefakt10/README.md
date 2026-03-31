Mobile Automation & Cloud-Ready Testing Suite



**Prowadzący:** mgr Mariusz Dworniczak 

**Student:** Piotr Kowalski

**Numer Albumu:** 76039



---



## 🏗️ Architektura Projektu (Marketing & Tech Stack)

Ten projekt to kompletny ekosystem testowy oparty na podejsciu **Cloud-Ready / Headless**. Zamiast polegać na ciężkich emulatorach, skupiamy się na narzędziach CLI, analizie statycznej, konteneryzacji (Docker) oraz automatyzacji procesów (Pipeline). 



**Główne technologie:**

* **Język:** Python 3.10+

* **Automatyzacja UI:** Appium 2.x (Mobile Engine)

* **Infrastruktura:** Docker & Docker Compose

* **Raportowanie:** Allure Framework

* **Analiza:** MobSF (Static Analysis) & ADB CLI



---



## 📅 PRZEBIEG LABORATORIUM (Kamienie Milowe)



### 🔹 BLOK 1: Tooling & Environment (Infrastruktura)

Przygotowanie bazy narzędziowej w modelu kontenerowym.

* **Co zrobiono:** Pobranie i konfiguracja obrazów `appium`, `android-sdk` oraz `mobsf`.

* **Wniosek:** Wykorzystałem obrazy Docker, aby zapewnić pełną izolację mojego środowiska testowego .

Dzięki temu uniknąłem problemów typu "u mnie działa", ponieważ korzystałem z dokładnie tej samej wersji serwera Appium i Android SDK bez konieczności ich żmudnej instalacji lokalnej.



### 🔹 BLOK 2: Debugowanie i Analiza Statyczna (MobSF)

Zrozumienie "wnętrza" aplikacji mobilnej przed przystąpieniem do testów.

* **Co zrobiono:** Wykorzystanie MobSF do skanowania plików APK pod kątem podatności i uprawnień.

* **Wniosek:** Dzięki analizie statycznej w narzędziu MobSF wykryłem krytyczne luki bezpieczeństwa, takie jak zahardkodowane klucze API czy niebezpieczne uprawnienia, jeszcze przed fizycznym uruchomieniem aplikacji.

Pozwoliło mi to zaoszczędzić czas i realnie wpłynęło na zwiększenie bezpieczeństwa produktu końcowego .



### 🔹 BLOK 3-4: Fundamenty Skryptowania (Python for QA)

Budowa logiki testowej w języku Python.

* **Co zrobiono:** Skupiłem się na opanowaniu fundamentów automatyzacji w Pythonie: biegłym posługiwaniu się zmiennymi, listami i słownikami w celu sprawnego zarządzania danymi testowymi. Zaimplementowałem zaawansowane konstrukcje warunkowe if/else oraz autorskie funkcje, a do komunikacji z backendem z powodzeniem wykorzystałem bibliotekę



### 🔹 BLOK 5-7: Hybrydowe Testowanie API (Requests & Pytest)

Weryfikacja warstwy backendowej aplikacji mobilnej.

* **Co zrobiono:** Testowanie endpointów REST (JSONPlaceholder), obsługa kodów HTTP i asercja danych JSON.

* **Wniosek:** Testowanie API pozwala wyłapać błędy zanim uruchomimy ciężkie testy UI.



### 🔹 BLOK 8: Appium UI Automation (Deep Dive)

Automatyzacja interakcji z interfejsem użytkownika.

* **Co zrobiono:** W moich skryptach wykorzystywałem precyzyjne lokalizatory, takie jak ID (Resource-ID), XPath oraz Accessibility ID.W pełni zautomatyzowałem kluczowe akcje użytkownika: symulowałem kliknięcia (click), wpisywanie tekstu (send_keys) oraz tworzyłem asercje, które weryfikowały poprawność wyświetlania elementów interfejsu po wykonanej akcji.
 


### 🔹 BLOK 9: Konteneryzacja Serwera (Docker Compose)

Izolacja silnika Appium od systemu operacyjnego.

* **Co zrobiono:** Stworzenie pliku `docker-compose.yml` zarządzającego serwerem Appium i sterownikami.



### 🔹 BLOK 10: MASTER PIPELINE (Capstone Project) 🏆

Finałowa automatyzacja całego procesu testowego.

* **Co zrobiono:** Stworzenie skryptu `pipeline.py`, który w jednym cyklu:

1. Rezerwuje zasoby i stawia infrastrukturę Docker.

2. Wykonuje testy hybrydowe (API + UI).

3. Generuje profesjonalny raport Allure z metadanymi.

4. Czyści środowisko po zakończonej pracy.



---



## 📊 Raportowanie Wyników (Allure)

Projekt wykorzystuje zaawansowane raportowanie Allure, które pozwala na:

* Śledzenie kroków testowych (`@allure.step`).

* Analizę błędów wraz z załącznikami (zrzuty ekranu, logi JSON).

* Dokumentowanie środowiska wykonawczego w sekcji **Environment**.