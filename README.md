Kantor Tracking

Projekt Kantor Tracking to aplikacja napisana w języku Python, wykorzystująca REST API oraz baze danych MongoDB. 
Głównym celem aplikacji jest umożliwienie użytkownikowi - pracownikowi kantoru śledzenie wykonywanych w kantorze transakcji, 
między innymi dodawanie transakcji do bazy danych, usuwanie transakcji z bazy danych oraz aktualizowanie danych transakcji. Dodatkowo użytkownik ma możliwość sprawdzenia aktualnych kursów walut przedstawionych na dany dzień przez NBP. 

*Wykorzystane technologie*:
* Język programowania: Python
* REST API: Wykorzystanie API Narodowego Banku Polskiego, własne API
* baza danych MongoDB

*Instalacja i uruchomienie*:
1. Sklonuj repozytorium.
2. Zainstaluj niezbędne zależności
3. Uruchom aplikację za pomocą komendy uvicorn app:app --reload
