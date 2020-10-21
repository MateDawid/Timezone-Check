from datetime import datetime
import pytz

def start_page():
    while True:
        command = int(input("Podaj numer polecenia z listy:\n\n1. Podaj strefę czasową.\n2. Pokaż dostępne strefy czasowe.\n0. Wyjdź z programu.\n--> "))
        if command == 1:
            zone = input("Strefa czasowa: ")
            time_zone(zone)
            break
        elif command == 2:
            all_timezones()
            break
        elif command == 0:
            print("Do zobaczenia!")
            break
        else:
            print("Podano nieprawidłowy numer komendy.")

def all_timezones():
    try:
        with open(r"E:\[PROGRAMOWANIE]\Python\Projects\Timezones\timezones.txt","r") as t:
            for n,timezone in enumerate(t):
                print(f"{n+1}. {timezone.strip()}")
        print("")
        start_page()
    except:
        print("Błędna ścieżka pliku!")
def time_zone(zone):
    try:
        tz = pytz.timezone(zone)
        time_in_zone = datetime.now(tz)
        print(f"{zone}: {time_in_zone.strftime('%d-%m-%Y, %H:%M:%S')}\n")
        while True:
            command = int(input("Podaj numer polecenia z listy:\n\n1. Wróć do strony startowej.\n0. Wyjdź z programu.\n--> "))
            if command == 1:
                start_page()
                break
            elif command == 0:
                print("Do zobaczenia!")
                break
            else:
                print("Podano nieprawidłowy numer komendy.")
    except:
        print("Podano nieprawidłową strefę czasową!")
        start_page()

start_page()