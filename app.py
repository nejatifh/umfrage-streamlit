import streamlit as st
import pandas as pd
import io

st.title("Teamregeln – Umfrage")

# Name input
participant = st.text_input("Ihr Name (oder Initialen):")

rules = [
    "Regel 1: Meetings starten pünktlich.",
    "Regel 2: Jede Meinung wird respektiert.",
    "Regel 3: Aufgaben werden termingerecht erledigt.",
    "Regel 4: Feedback wird regelmäßig gegeben.",
    "Regel 5: Kamera an bei Videocalls.",
    "Regel 6: Slack wird täglich gelesen.",
    "Regel 7: Urlaube werden frühzeitig eingetragen.",
    "Regel 8: Jeder ist für seine Aufgaben verantwortlich."
]

responses = []

for i, rule in enumerate(rules):
    st.subheader(rule)

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
        "Regelnummer": i + 1,
        "Regel": rule,
        "Entscheidung": choice,
        "Kommentar": comment
    })

# Disabled Absenden button with message
if st.button("Absenden (Derzeit deaktiviert)"):
    st.info("Bitte benutzen Sie stattdessen die Download-Schaltfläche unten.")

st.write("---")

if participant.strip():
    df = pd.DataFrame(responses)

    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    csv_data = csv_buffer.getvalue()

    st.download_button(
        label="Antworten als CSV herunterladen",
        data=csv_data,
        file_name=f"umfrage_{participant.replace(' ', '_')}.csv",
        mime="text/csv"
    )

    st.info("Bitte laden Sie Ihre Antworten als CSV herunter und senden Sie diese per E-Mail an [Faezeh.NejatiHatamian@senfin.berlin.de].")
else:
    st.warning("Bitte geben Sie Ihren Namen ein, um die Umfrage abzuschließen.")
