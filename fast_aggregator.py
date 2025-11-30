import streamlit as st
import random
import time

# --- Ustawienia Aplikacji ---
st.set_page_config(page_title="Viral Forecast: Generator Trendów AI", page_icon="🔮")
st.title("🔮 Viral Forecast: Generator Trendów AI")

st.markdown("""
Jesteś gotów na sławę? Wpisz dowolne słowo, a nasza sieć neuronowa przewidzi Twój viralowy trend na TikToku / YT Shorts!
""")

# --- Stałe Wartości i Link ---
LINK_AFILIACYJNY = "https://strefakursow.pl/?ref=371976" # Twój Link Afiliacyjny

# --- Sekcja Wprowadzania Danych ---
st.header("1. Wprowadź swój temat")

with st.form("viral_generator_form"):
    temat = st.text_input(
        "Wpisz dowolne słowo lub frazę (np. Mój pies, szkoła, nowa praca):",
        value="mój nowy outfit"
    )

    submitted = st.form_submit_button("Analizuj Trend i Generuj Viral!")

# --- Sekcja Wyników i Monetyzacji ---

if submitted:
    st.markdown("---")
    st.header(f"2. Analiza AI dla: **{temat.upper()}**")

    # Symulacja ładowania
    with st.spinner('Analizowanie sieci neuronowych... Proszę czekać na werdykt...'):
        time.sleep(2) 
    
    # Generowanie absurdalnych wyników
    wspolczynnik_hype = round(random.uniform(70, 99.9), 1)
    liczba_przewidywanych_wyswietlen = random.randint(100, 900) * 1000
    przewidywany_zarobek = round(random.randint(10, 50) * 1000, -2) # np. 10000, 25000 PLN

    # Generowanie absurdalnego hashtagu
    slowa_kluczowe = temat.split() + ['szybko', 'viral', 'hype', '2025', 'mega']
    hashtag_viral = "#" + "_".join(random.sample(slowa_kluczowe, k=random.randint(2, 4)))

    
    # Wyświetlanie Wyników
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="🔥 Współczynnik HYPE:",
            value=f"{wspolczynnik_hype}%"
        )
    with col2:
        st.metric(
            label="📈 Potencjalne Wyświetlenia:",
            value=f"{liczba_przewidywanych_wyswietlen:,} 🚀"
        )
    with col3:
        st.metric(
            label="💰 Przewidywany Zarobek:",
            value=f"**{przewidywany_zarobek:,} PLN**"
        )

    st.markdown("---")
    
    st.success(f"**Twój VIRALOWY HASHTAG:** `{hashtag_viral}`")

    # 🗣️ Wezwanie do udostępniania
    st.subheader("🔥 Zrób Screenshota i Udostępnij na TikToku/IG! 🔥")
    st.markdown("Pokaż znajomym, że wiesz, co się zaraz stanie viralem! 👇")

    # 💰 MIEJSCE NA MONETYZACJĘ!
    st.warning("Psst! Prawdziwe pieniądze wymagają profesjonalizmu. Zdobądź umiejętności, by zamienić wyświetlenia na REALNY ZYSK:")

    # Przycisk Monetyzacyjny
    st.markdown(f'<a href="{LINK_AFILIACYJNY}" target="_blank" style="text-decoration: none;">'
                f'<button style="background-color:#FF0077; color: white; padding: 15px 25px; border: none; border-radius: 8px; font-size: 18px; cursor: pointer;">'
                f'Zdobądź Umiejętności Wideo/Montażu (Zacznij Zarabiać Poważnie) 🎬'
                f'</button>'
                f'</a>', unsafe_allow_html=True)
