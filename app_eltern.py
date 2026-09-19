import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="BTV Nachwuchs- & Eltern-Kompass",
    page_icon="🎾",
    layout="wide"
)

# Custom Styling (BTV CI)
st.markdown("""
    <style>
    :root {
        --btv-blue: #235D7A;
        --btv-green: #B3CA38;
        --btv-light-bg: #F4F7F9;
        --btv-card-bg: #FFFFFF;
    }
    
    .stApp {
        background-color: var(--btv-light-bg);
    }
    
    .btv-header {
        background-color: var(--btv-blue);
        color: white;
        padding: 25px;
        border-radius: 10px;
        margin-bottom: 25px;
        text-align: center;
    }
    .btv-header h1 {
        color: #FFFFFF !important;
        font-weight: 700;
        margin-bottom: 5px;
    }
    .btv-header p {
        color: var(--btv-green);
        font-size: 1.1rem;
        margin: 0;
    }

    .btv-card {
        background-color: var(--btv-card-bg);
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid var(--btv-blue);
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    
    .btv-metric-box {
        background-color: var(--btv-blue);
        color: white;
        padding: 15px;
        border-radius: 8px;
        text-align: center;
    }
    .btv-metric-number {
        font-size: 2rem;
        font-weight: bold;
        color: var(--btv-green);
    }

    .stButton>button {
        background-color: var(--btv-green) !important;
        color: #235D7A !important;
        font-weight: bold !important;
        border-radius: 6px !important;
        border: none !important;
    }

    .section-title {
        color: var(--btv-blue);
        border-bottom: 2px solid var(--btv-green);
        padding-bottom: 5px;
        margin-top: 15px;
        margin-bottom: 15px;
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# BTV Banner Header
st.markdown("""
    <div class="btv-header">
        <h1>BTV NACHWUCHS- & ELTERN-KOMPASS</h1>
        <p>Orientierung für Eltern & Junior-Spieler im BTV-Leistungssportsystem</p>
    </div>
""", unsafe_allow_html=True)

# Tabs
tab_profile, tab_roadmap, tab_budget = st.tabs([
    "👦 1. PROFIL DES KINDES", 
    "🎯 2. BTV-SOLL-ABGLEICH & PFAD", 
    "💶 3. ZEIT- & BUDGET-RECHNER"
])

# --- TAB 1: PROFIL DES KINDES ---
with tab_profile:
    st.markdown("<h3 class='section-title'>Stammdaten & Altersklasse</h3>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    
    with col1:
        altersklasse = st.selectbox(
            "Altersklasse des Kindes:",
            ["U7 / U8", "U9 / U10", "U11 / U12", "U13 / U14", "U15 / U16", "U17 / U18"],
            index=1
        )
        geschlecht = st.radio("Geschlecht:", ["Junioren (männlich)", "Juniorinnen (weiblich)"], horizontal=True)
        
    with col2:
        kader_status = st.selectbox(
            "Aktueller BTV-Kaderstatus:",
            [
                "Kein Kader / Vereinsspieler",
                "BTV-Talentsichtung absolviert",
                "Förderstufe 1: Regionalkader",
                "Förderstufe 1: Überregionalkader (Top 15-20)",
                "Förderstufe 2: BTV-Talent-Pool",
                "Förderstufe 3: BTV-Kader (U13-U16)",
                "Förderstufe 4: BTV-Kader (U17-U18)"
            ],
            index=0
        )

    st.markdown("<h3 class='section-title'>Aktueller Trainings- & Turnierumfang</h3>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    
    with c1:
        einzel_std = st.number_input("Einzeltraining (Std./Woche):", min_value=0.0, max_value=20.0, value=1.0, step=0.5)
        gruppen_std = st.number_input("Gruppentraining Club (Std./Woche):", min_value=0.0, max_value=20.0, value=3.0, step=0.5)
    with c2:
        btv_gruppen_std = st.number_input("BTV-Verbandstraining (Std./Woche):", min_value=0.0, max_value=20.0, value=0.0, step=0.5)
        athletik_std = st.number_input("Athletiktraining (Std./Woche):", min_value=0.0, max_value=20.0, value=1.0, step=0.5)
    with c3:
        matches_jahr = st.number_input("Gespielte Matches pro Jahr:", min_value=0, max_value=150, value=25)
        dtb_rangliste = st.number_input("DTB-Ranglistenposition (0 = keine):", min_value=0, max_value=500, value=0)

# --- TAB 2: SOLL-ABGLEICH ---
with tab_roadmap:
    st.markdown("<h3 class='section-title'>BTV-Anforderungen & Empfehlungen im Abgleich</h3>", unsafe_allow_html=True)
    
    # BTV Reference Data Setup
    if altersklasse in ["U7 / U8", "U9 / U10"]:
        foerderstufe_name = "Förderstufe 1 (U7–U10) | BTV-Kids-Pool"
        soll_tennis = "3–5 Std. (U8) bzw. 5–7 Std. (U10)"
        soll_matches = "10–25 (U8) bzw. 30–40 (U10)"
        tage_platz = "2–4 Tage"
        fokus = "Allgemeinsportliches Talent, BTV-Kids-Race Turniere, Sichtung"
    elif altersklasse == "U11 / U12":
        foerderstufe_name = "Förderstufe 2 (U11–U12) | BTV-Talent-Pool"
        soll_tennis = "6–8 Std. pro Woche"
        soll_matches = "40–60 Matches pro Jahr"
        tage_platz = "3–4 Tage"
        fokus = "Einstieg DTB-Ranglistenturniere (mind. 10 Siege für Rangliste peilen)"
    elif altersklasse in ["U13 / U14", "U15 / U16"]:
        foerderstufe_name = "Förderstufe 3 (U13–U16) | BTV-Kader"
        soll_tennis = "8–12 Std. (U14) bzw. 10–14 Std. (U16)"
        soll_matches = "50–70 (U14) bzw. 60–80 (U16)"
        tage_platz = "4–5 Tage"
        fokus = "DTB-Ranglistenplatzierung, TE-/ITF-Turniere, Athletik"
    else:
        foerderstufe_name = "Förderstufe 4 (U17–U18) | BTV-Kader"
        soll_tennis = "12–18 Std. Tennis & Athletik"
        soll_matches = "70–90 Matches pro Jahr"
        tage_platz = "5–6 Tage"
        fokus = "ITF-Jugend, nationale Damen/Herren, profiorientiert"

    st.info(f"📍 **Ziel-Ebene für {altersklasse}:** {foerderstufe_name}")

    col_r1, col_r2 = st.columns(2)
    
    total_tennis_ist = einzel_std + gruppen_std + btv_gruppen_std
    
    with col_r1:
        st.subheader("📊 Ist vs. BTV-Empfehlung")
        st.write(f"• **Tennistraining:** Aktuell **{total_tennis_ist:.1f} Std./Woche** (BTV-Empfehlung: {soll_tennis})")
        st.write(f"• **Athletik:** Aktuell **{athletik_std:.1f} Std./Woche**")
        st.write(f"• **Match-Anzahl:** Aktuell **{matches_jahr} Matches/Jahr** (BTV-Empfehlung: {soll_matches})")
        st.write(f"• **Trainingstage:** Empfohlen werden ca. **{tage_platz} pro Woche**")

    with col_r2:
        st.subheader("🚀 Konkrete Empfehlungen für Eltern")
        if altersklasse in ["U7 / U8", "U9 / U10"]:
            st.markdown("""
                * **Sichtung:** Teilnahme an der jährlichen BTV-Talentsichtung einplanen.
                * **Kids Race:** Teilnahme an BTV Kids-Race Turnieren (Kat. 3 für Regionalkader, Kat. 1-2 für Überregionalkader).
                * **BTV-Training:** Überregionalkader erhält 1x wöchentlich BTV-Verbandstraining (Vierergruppe).
            """)
        elif altersklasse == "U11 / U12":
            st.markdown("""
                * **Ranglisteneintrag:** Mindestens **10 Siege bei DTB-Turnieren** erzielen, um automatisch auf der Rangliste geführt zu werden.
                * **BTV-Zuschuss:** Die Top 20 Spieler erhalten ca. **500 € Trainingskostenzuschuss** pro Jahr vom BTV.
            """)
        else:
            st.markdown("""
                * **Turnierfokus:** Ausgewogene Periodisierung aus DTB-, TE- und ITF-Turnieren sowie Regenerationsphasen.
                * **Kader-Kriterien:** Ranglistenplatzierung im eigenen Jahrgang maßgeblich für Sonder- oder Grundförderung.
            """)

# --- TAB 3: BUDGET & ZEIT ---
with tab_budget:
    st.markdown("<h3 class='section-title'>Jahresbudget & Zeitaufwand Kalkulator</h3>", unsafe_allow_html=True)
    
    b1, b2 = st.columns(2)
    with b1:
        st.subheader("⚙️ Kostensätze anpassen")
        cost_einzel = st.slider("Stundensatz Einzeltraining (€/Std.):", 40, 90, 60)
        cost_gruppe = st.slider("Stundensatz Club-Gruppentraining (€/Std. pro Kind):", 10, 30, 15)
        cost_btv_gruppe = st.slider("Stundensatz BTV-Verbandstraining (4er-Gruppe, €/Std. pro Kind):", 10, 30, 15)
        cost_hallenumlage = st.slider("Zusätzliche Hallenplatzmiete im Winter (€/Std. anteilig):", 5, 25, 12)
        turniere_anzahl = st.slider("Geplante Turniere pro Jahr:", 5, 30, 15)
        cost_turnier = st.slider("Durchschnittliches Nenngeld pro Turnier (€):", 20, 60, 35)

    # Calculation (25 Weeks Summer, 22 Weeks Winter)
    weeks_summer = 25
    weeks_winter = 22
    
    # Base Training Costs
    cost_einzel_year = einzel_std * cost_einzel * (weeks_summer + weeks_winter)
    cost_gruppe_year = gruppen_std * cost_gruppe * (weeks_summer + weeks_winter)
    cost_btv_year = btv_gruppen_std * cost_btv_gruppe * (weeks_summer + weeks_winter)
    cost_athletik_year = athletik_std * 12 * (weeks_summer + weeks_winter)
    
    # Hallen Zusatzkosten im Winter (für Einzel + Gruppe + BTV)
    cost_halle_winter = (einzel_std + gruppen_std + btv_gruppen_std) * cost_hallenumlage * weeks_winter
    
    # Turniere
    cost_turniere_year = turniere_anzahl * cost_turnier
    
    # Total Expenses
    total_costs = cost_einzel_year + cost_gruppe_year + cost_btv_year + cost_athletik_year + cost_halle_winter + cost_turniere_year
    
    # BTV Subsidies / Zuschüsse
    zuschuss = 0
    if "Förderstufe 2" in kader_status:
        zuschuss = 500
    elif "Förderstufe 3" in kader_status or "Förderstufe 4" in kader_status:
        zuschuss = 800

    netto_costs = total_costs - zuschuss

    with b2:
        st.subheader("📊 Geschätzte Jahresausgaben")
        st.markdown(f"""
            <div class='btv-card'>
                <h4>Gesamtkosten Training & Turniere:</h4>
                <div style='font-size:1.5rem; color:#FF8A8A; font-weight:bold;'>~ {total_costs:,.0f} € / Jahr</div>
                <hr style='border-color:rgba(255,255,255,0.2);'>
                <p>• <b>Einzeltraining:</b> {cost_einzel_year:,.0f} €</p>
                <p>• <b>Gruppentraining (Club & BTV):</b> {cost_gruppe_year + cost_btv_year:,.0f} €</p>
                <p>• <b>Hallenkosten-Zuschlag (Winter):</b> {cost_halle_winter:,.0f} €</p>
                <p>• <b>Turnier-Nenngelder:</b> {cost_turniere_year:,.0f} €</p>
                <p>• <b>Athletiktraining:</b> {cost_athletik_year:,.0f} €</p>
                <hr style='border-color:rgba(255,255,255,0.2);'>
                <h4>BTV-Förderung / Zuschuss:</h4>
                <div style='font-size:1.3rem; color:var(--btv-green); font-weight:bold;'>- {zuschuss:,.0f} €</div>
                <h3>Netto-Aufwand für Eltern:</h3>
                <div class='btv-metric-number'>~ {netto_costs:,.0f} €</div>
            </div>
        """, unsafe_allow_html=True)
