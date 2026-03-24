# 🛡️ AUDYT BEZPIECZEŃSTWA: MANIFEST SCANNER
**Status:** Wykonano automatyczną ekstrakcję ryzyka.

### 📝 1. Zawartość RiskyPermission.xml
Zidentyfikowano następujące wpisy krytyczne:
- **Debuggable:** `true` (⚠️ WYSOKIE RYZYKO - Aplikacja podatna na inżynierię wsteczną w czasie rzeczywistym).
- **Permissions:** Wykryto uprawnienia dające dostęp do sieci (`INTERNET`) oraz pamięci zewnętrznej.

### 🧠 2. Interpretacja Inżynierska
Z punktu widzenia bezpieczeństwa, najpoważniejszym problemem jest flaga `debuggable`. Pozwala ona na użycie komendy `adb jdwp` do śledzenia procesów aplikacji przez osoby niepowołane. Dodatkowo, nadmierna liczba żądanych uprawnień niepotrzebnie poszerza powierzchnię ataku (tzw. Attack Surface).

### 🛠️ 3. Akcja korygująca
Zaleca się wdrożenie skryptu do procesu CI/CD (np. w Jenkins/GitHub Actions), który będzie automatycznie blokował buildy, jeśli `RiskyPermission.xml` wykaże flagę `debuggable="true"`. Należy również przeprowadzić przegląd manifestu i usunąć z niego wszystkie uprawnienia, które nie są absolutnie niezbędne do działania programu.

####  Raport wykonany przez:
**Podpis:** Piotr Kowalski 76039
**Data:** 24-03-2026