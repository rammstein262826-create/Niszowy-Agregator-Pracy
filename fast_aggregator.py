import streamlit as st
import pandas as pd
import os

# Wskazujemy na Twój lokalny plik niszowy
LOCAL_DATA_FILE = "oferty_dla_rodzicow.csv" 

st.set_page_config(page_title="Niszowy Agregator Danych", page_icon="💰")
st.title("💰 Agregator Pracy Zdalnej dla Rodziców (Niska Konkurencja)")

st.markdown("""
Aplikacja wyświetla wyselekcjonowane oferty pracy z elastycznymi godzinami.
""")

def load_data(file_path): 
    """Ładuje dane z lokalnego pliku CSV za pomocą pandas."""
    try:
        # Używamy pandas do odczytu lokalnego pliku CSV
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        st.error(f"Błąd: Nie znaleziono pliku danych: {file_path}. Sprawdź, czy plik jest w tym samym folderze.")
        return pd.DataFrame()

# --- Główny Panel Użytkownika ---

# Ładujemy dane z Twojego niszowego pliku CSV
listings_df = load_data(LOCAL_DATA_FILE) 

if not listings_df.empty:
    st.success(f"Załadowano {len(listings_df)} unikalnych wpisów pasujących do Twojej niszy.")
    
    # Wyświetlanie wyników
    # Wyświetlamy tylko kolumny z Tytułem, Wynagrodzeniem i Źródłem
    st.subheader("Aktualne Oferty:")
    st.dataframe(listings_df[['Tytuł Oferty', 'Wynagrodzenie (Potencjalne)', 'Źródło']], use_container_width=True)

    st.markdown("---")
    
    # 💰 MIEJSCE NA MONETYZACJĘ!
    st.markdown("### Reklama Partnera: Nowe Kursy dla Rodziców 👨‍👩‍👧‍👦")
    st.markdown("""
    **Zdobądź nowe umiejętności i podnieś stawkę godzinową!**
    
    Polecamy kurs **Excel lub Copywriting**, idealny do szybkiego startu w pracy zdalnej.
    
    👉 **[Zacznij kurs od 49 PLN!]** *(Twój Link Afiliacyjny do Edukacji)*
    """)
    st.caption("Pamiętaj: Zastąp ten link swoim prawdziwym linkiem afiliacyjnym.")
    
else:
    st.warning("Nie udało się załadować żadnych danych. Sprawdź nazwę pliku CSV.")