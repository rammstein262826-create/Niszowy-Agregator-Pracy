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
    
    st.subheader("Aktualne Oferty:")
    
    # --- NOWY KOD, KTÓRY WYŚWIETLA WSZYSTKIE KOLUMNY I PRZYCISK ---
    st.dataframe(listings_df,
                column_config={
                    "Link do aplikacji": st.column_config.LinkColumn(
                        "Link do aplikacji",
                        display_text="Zacznij zarabiać (Kup Kurs)" # Wyświetlany tekst przycisku
                    ),
                    "Kategoria": st.column_config.TextColumn("Kategoria"),
                    "Stawka": st.column_config.TextColumn("Stawka")
                },
                # Wskazujemy kolejność wszystkich kolumn, w tym Link do aplikacji
                column_order=("Tytuł Oferty", "Wynagrodzenie (Potencjalne)", "Opis", "Źródło", "Kategoria", "Stawka", "Link do aplikacji"),
                hide_index=True,
                use_container_width=True)
    # --- KONIEC NOWEGO KODU ---

    st.markdown("---")
    
    st.success("Twoje linki afiliacyjne są teraz zintegrowane bezpośrednio w tabeli. Kliknij w przycisk 'Zacznij zarabiać (Kup Kurs)'.")





