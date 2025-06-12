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

# Display questions and input widgets
for i, rule in enumerate(rules):
    st.subheader(rule)

    st.radio(
        "Bitte auswählen:",
        ["Beibehalten", "Abschaffen", "Anpassen"],
        key=f"choice_{i}"
    )

    if st.session_state.get(f"choice_{i}") == "Anpassen":
        st.text_area("Wie soll es angepasst werden?", key=f"comment_{i}")

# Collect responses after rendering all inputs
responses = []
for i, rule in enumerate(rules):
    choice = st.session_state.get(f"choice_{i}", "Beibehalten")
    comment = ""
    if choice == "Anpassen":
        comment = st.session_state.get(f"comment_{i}", "")
    responses.append({
        "Teilnehmer": participant,
        "Regelnummer": i + 1,
        "Regel": rule,
        "Entscheidung": choice,
        "Kommentar": comment
    })

# Disabled Absenden button with info
if st.button("Absenden (Derzeit deaktiviert)"):
    st.info("Bitte benutzen Sie stattdessen die Download-Schaltfläche unten.")

st.write("---")

# Show download button only if name is entered
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
