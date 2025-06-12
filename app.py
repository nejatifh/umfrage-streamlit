import streamlit as st
import pandas as pd
import io

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

# Initialize session state defaults
for i in range(len(rules)):
    if f"choice_{i}" not in st.session_state:
        st.session_state[f"choice_{i}"] = "Beibehalten"
    if f"comment_{i}" not in st.session_state:
        st.session_state[f"comment_{i}"] = ""

# Display questions and inputs
for i, rule in enumerate(rules):
    st.subheader(rule)

    choice = st.radio(
        "Bitte auswählen:",
        ["Beibehalten", "Abschaffen", "Anpassen"],
        index=["Beibehalten", "Abschaffen", "Anpassen"].index(st.session_state[f"choice_{i}"]),
        key=f"choice_{i}"
    )

    if choice == "Anpassen":
        comment = st.text_area("Wie soll es angepasst werden?", value=st.session_state[f"comment_{i}"], key=f"comment_{i}")
    else:
        # Clear comment if not Anpassung
        st.session_state[f"comment_{i}"] = ""

# Disabled submit button with message
if st.button("Absenden (Derzeit deaktiviert)"):
    st.info("Bitte benutzen Sie stattdessen die Download-Schaltfläche unten.")

st.write("---")

# Show download button only if participant entered
if participant.strip():
    if st.button("Antworten als CSV herunterladen"):
        responses = []
        for i, rule in enumerate(rules):
            responses.append({
                "Teilnehmer": participant,
                "Regelnummer": i + 1,
                "Regel": rule,
                "Entscheidung": st.session_state[f"choice_{i}"],
                "Kommentar": st.session_state[f"comment_{i}"] if st.session_state[f"choice_{i}"] == "Anpassen" else ""
            })

        df = pd.DataFrame(responses)
        csv_buffer = io.StringIO()
        df.to_csv(csv_buffer, index=False)
        csv_data = csv_buffer.getvalue()

        st.download_button(
            label="Download CSV",
            data=csv_data,
            file_name=f"umfrage_{participant.replace(' ', '_')}.csv",
            mime="text/csv"
        )

        st.success("Bitte laden Sie die Datei herunter und senden Sie sie per E-Mail an [Faezeh.NejatiHatamian@senfin.berlin.de].")
else:
    st.warning("Bitte geben Sie Ihren Namen ein, um die Umfrage abzuschließen.")

