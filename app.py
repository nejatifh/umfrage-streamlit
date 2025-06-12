import streamlit as st

st.title("Umfrage: Regeln bewerten")

rules = [
    "Regel 1: Lorem ipsum dolor sit amet.",
    "Regel 2: Beispieltext für Regel zwei.",
    "Regel 3: Eine weitere Regel zum Bewerten.",
    "Regel 4: Noch eine Regel.",
    "Regel 5: Und noch eine.",
    "Regel 6: Die sechste Regel.",
    "Regel 7: Fast geschafft.",
    "Regel 8: Letzte Regel!"
]

options = ["Beibehalten", "Abschaffen", "Anpassen"]

responses = {}

for i, rule in enumerate(rules):
    st.subheader(f"{i+1}. {rule}")
    choice = st.radio("Wähle eine Option:", options, key=f"choice_{i}")
    responses[f"rule_{i}"] = choice

    if choice == "Anpassen":
        text = st.text_area("Ideen zur Anpassung:", key=f"text_{i}")
        responses[f"adjustment_{i}"] = text
    st.markdown("---")

st.button("Absenden")
