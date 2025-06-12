import streamlit as st
import pandas as pd
import os
from filelock import FileLock

st.title("Teamregeln – Umfrage")

# Name input
participant = st.text_input("Ihr Name (oder Initialen):")

rules = [
    "Regel 1: Wir beschriften unsere Lebensmittel mit dem Nachnamen.",
    "Regel 2: Wir entsorgen unsere offenen Lebensmittel im Kühlschrank regelmäßig in eigener Verantwortung spätestens jeden Freitag – zum Dienstschluss.",
    "Regel 3: Wir räumen unser benutztes Geschirr umgehend in den Geschirrspüler bzw. waschen es ab, falls dieser gerade läuft.",
    "Regel 4: Wir übernehmen alle Verantwortung für das Befüllen, Anstellen und Ausräumen des Geschirrspülers.",
    "Regel 5: Wir halten uns an das Verbot des Entsorgens von Essensresten in Spüle oder Toiletten.",
    "Regel 6: Klimaschutz geht uns alle an, wir beteiligen uns u.a. durch das ordnungsgemäße Trennen unserer Abfälle.",
    "Regel 7: Alle übernehmen die Verantwortung für die regelmäßige Reinigung der bereitgestellten Gegenstände (Kaffeemaschinen, Kühlschränke, Spülmaschinen etc.), mind. einmal im Quartal.",
    "Regel 8: Die Entsorgung abgelaufener Lebensmittel erfolgt in eigener Verantwortung, spätestens bei der Quartalsreinigung."
]

responses = []

for i, rule in enumerate(rules):
    st.subheader(f"{i+1}. {rule}")

    choice = st.radio(
        "Bitte auswählen:",
        ["Beibehalten", "Abschaffen", "Anpassen"],
        key=f"choice_{i}"
    )

    comment = ""
    if choice == "Anpassen":
        comment = st.text_area("Wie soll es angepasst werden?", key=f"comment_{i}")

    responses.append({
        "Teilnehmer": participant,
        "Regelnummer": i+1,
        "Regel": rule,
        "Entscheidung": choice,
        "Kommentar": comment
    })

if st.button("Absenden"):
    if not participant.strip():
        st.warning("Bitte geben Sie Ihren Namen ein.")
    else:
        df = pd.DataFrame(responses)

        csv_file = "umfrage_ergebnisse.csv"
        lock_file = "umfrage_ergebnisse.csv.lock"

        # Use file lock to prevent write collisions
        with FileLock(lock_file):
            if os.path.exists(csv_file):
                df.to_csv(csv_file, mode='a', header=False, index=False)
            else:
                df.to_csv(csv_file, index=False)

        st.success("Vielen Dank für Ihre Teilnahme!")
        st.write("Ihre Antworten wurden gespeichert.")
