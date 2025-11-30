import streamlit as st
import random
import time

# --- Ustawienia Aplikacji ---
st.set_page_config(page_title="Digital Persona Generator: Jaka jest Twoja Cyfrowa Osobowość?", page_icon="✨")
st.title("✨ Digital Persona Generator: Jaka jest Twoja Cyfrowa Osobowość?")

st.markdown("""
Jesteś gotów, by poznać swoje przeznaczenie w Internecie? Wpisz swój ulubiony kolor i dowolne słowo, a nasz algorytm wygeneruje Twój unikalny pseudonim i Współczynnik FAME!
""")

# --- Sekcja Wprowadzania Danych ---
st.header("1. Wprowadź informacje do analizy")

with st.form("persona_generator_form"):
    ulubiony_kolor = st.selectbox(
        "Wybierz swój ulubiony kolor:",
        ['Czerwony', 'Niebieski', 'Zielony', 'Żółty', 'Fioletowy', 'Czarny', 'Biały', 'Inny']
    )
    
    ulubione_slowo = st.text_input(
        "Wpisz dowolne, ulubione słowo (np. pizza, gaming, kot):",
        value="gaming"
    )

    submitted = st.form_submit_button("Generuj Moją Cyfrową Personę!")

# --- Sekcja Wyników (Generowanie i Symulacja) ---

if submitted:
    st.markdown("---")
    st.header("2. Twoja Cyfrowa Osobowość Gotowa!")

    # Symulacja ładowania
    with st.spinner('Analizowanie Twojego stylu i preferencji...'):
        time.sleep(2) 
    
    # 1. Generowanie Pseudonimu
    prefixy = ["Cyber", "Mega", "Shadow", "Trend", "Alpha", "Pixel", "Mistrz", "Wielki"]
    suffixy = ["Guru", "Fantom", "Włamywacz", "Zabójca", "Ekspert", "Kreator", "Wizjoner", "Legend"]
    
    # Prosty algorytm generujący unikalny pseudonim
    random.seed(ulubiony_kolor + ulubione_slowo) # Seed zapewni, że wynik jest taki sam dla tego samego inputu
    
    pseudonim = f"{random.choice(prefixy)}{ulubione_slowo.capitalize()}{random.choice(suffixy)}"
    
    # 2. Generowanie Symulowanych Wyników FAME
    wspolczynnik_fame = round(random.uniform(70, 99.9), 1)
    przewidywany_subskrybentow = random.randint(10, 200) * 1000 

    
    # Wyświetlanie Wyników
    st.success(f"Twój unikalny pseudonim to: **{pseudonim}**")

    st.markdown("---")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(
            label="✨ Współczynnik FAME (Potencjał Sławy):",
            value=f"{wspolczynnik_fame}%"
        )
    with col2:
        st.metric(
            label="📈 Przewidywani Subskrybenci (w 6 miesięcy):",
            value=f"{przewidywany_subskrybentow:,} 🧑‍🤝‍🧑"
        )
    
    st.markdown("---")

    # 🗣️ Wezwanie do udostępniania (Klucz do Viral)
    st.subheader("📸 Zrób Screenshota i Oznacz Znajomych! 🔥")
    st.markdown("Pokaż, kto jest prawdziwą cyfrową legendą!")
    
    # Brak monetyzacji na tym etapie!
