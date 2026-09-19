import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="BTV Tennisschul-Planer & Gap-Analyse",
    page_icon="🎾",
    layout="wide"
)

# Custom Styling (BTV Corporate Identity)
st.markdown("""
    <style>
    /* BTV Hauptfarben */
    :root {
        --btv-blue: #235D7A;
        --btv-green: #B3CA38;
        --btv-light-bg: #F4F7F9;
        --btv-card-bg: #FFFFFF;
    }
    
    /* Haupt-Hintergrund */
    .stApp {
        background-color: var(--btv-light-bg);
    }
    
    /* Header Container */
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

    /* Cards / Container */
    .btv-card {
        background-color: var(--btv-card-bg);
        padding: 20px;
        border-radius: 8px;
        border-left: 5px solid var(--btv-blue);
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
        margin-bottom: 15px;
    }
    
    /* Metrics Highlight Card */
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

    /* Buttons */
    .stButton>button {
        background-color: var(--btv-green) !important;
        color: #235D7A !important;
        font-weight: bold !important;
        border-radius: 6px !important;
        border: none !important;
        padding: 10px 24px !important;
    }

    /* Form Section Headers */
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
        <h1>BTV TENNISSCHUL-ANALYSE & GRAND PRIX PLANER</h1>
        <p>Entscheidungs- und Standort-Tool für bayerische Tennisschulen & Vereine</p>
    </div>
""", unsafe_allow_html=True)

# Navigation / Steps Header
col_s1, col_s2, col_s3 = st.columns(3)
with col_s1:
    st.markdown("<div style='text-align:center; padding:10px; background-color:#235D7A; color:#B3CA38; border-radius:5px; font-weight:bold;'>1. Status Quo Erfassung</div>", unsafe_allow_html=True)
with col_s2:
    st.markdown("<div style='text-align:center; padding:10px; background-color:#235D7A; color:#FFFFFF; border-radius:5px;'>2. FITP-Ziel & Gap-Analyse</div>", unsafe_allow_html=True)
with col_s3:
    st.markdown("<div style='text-align:center; padding:10px; background-color:#235D7A; color:#FFFFFF; border-radius:5px;'>3. BTV Grand Prix Simulator</div>", unsafe_allow_html=True)

st.write("")

# TAB STRUCTURE
tab_status, tab_gap, tab_grandprix = st.tabs(["📋 1. IST-ZUSTAND EINGEBEN", "🎯 2. GAP-ANALYSE & KOSTEN", "🏆 3. BTV GRAND PRIX SIMULATOR"])

# --- TAB 1: IST-ZUSTAND ---
with tab_status:
    st.markdown("<h3 class='section-title'>Personal & Trainerstruktur (DTB-Standards)</h3>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        tech_leiter = st.selectbox(
            "Technischer Leiter / Cheftrainer (Höchste Lizenz):",
            [
                "Hilfstrainer / Assistant (ohne Lizenz)",
                "C-Trainer",
                "Staatlich geprüfter Tennislehrer",
                "B-Trainer Breitensport",
                "B-Trainer Leistungssport",
                "A-Trainer"
            ],
            index=3
        )
        athletik_trainer = st.selectbox(
            "Athletiktrainer:",
            ["Keiner", "Athletiktrainer Level 1", "Athletiktrainer Level 2 (Sportwiss. Abschluss)"],
            index=0
        )
    with c2:
        mental_trainer = st.selectbox(
            "Mentaltrainer / Ernährungsberatung:",
            ["Keine", "Mentaltrainer Stufe 1", "Mentaltrainer Stufe 2 & Ernährungsberater"],
            index=0
        )
        clubmanager = st.selectbox(
            "Clubmanager / Vereinsmanagement:",
            ["Keiner / Nicht besetzt", "3 Ehrenamtliche (Vorstand/Jugendwarte)", "Hauptamtlich Stufe 1", "Hauptamtlich Stufe 2"],
            index=1
        )

    st.markdown("<h3 class='section-title'>Infrastruktur & Anlage</h3>", unsafe_allow_html=True)
    i1, i2, i3, i4 = st.columns(4)
    with i1:
        multi_belag = st.checkbox("Mehrere Platzbeläge vorhanden", value=False)
    with i2:
        hallenplaetze = st.checkbox("Hallenplätze (Winter) verfügbar", value=True)
    with i3:
        fitness_bereich = st.checkbox("Eigenes Fitness-Areal", value=False)
    with i4:
        unterkunft = st.checkbox("Unterkunft für Spieler", value=False)

    st.markdown("<h3 class='section-title'>Jugendsport & BTV-Verbandskennzahlen</h3>", unsafe_allow_html=True)
    j1, j2, j3 = st.columns(3)
    with j1:
        anzahl_spieler = st.number_input("Anzahl aktive Kinder/Jugendliche im Training:", min_value=0, value=15)
        jugend_teams = st.number_input("Gemeldete Jugendmannschaften (U10-U18):", min_value=0, value=2)
        maedchen_quote = st.slider("Mädchenanteil im Jugendtraining (%):", 0, 100, 30)
    with j2:
        btv_sichtung = st.number_input("Kinder zur BTV-Talentsichtung entsendet:", min_value=0, value=1)
        kader_u9_u10 = st.number_input("Anzahl U9/U10 Spieler in BTV-Förderung:", min_value=0, value=0)
        kader_u11_u18 = st.number_input("Anzahl U11-U18 Spieler in BTV-Förderung:", min_value=0, value=0)
    with j3:
        kids_turniere = st.number_input("Veranstalte Kids-Turniere pro Jahr:", min_value=0, value=1)
        dtb_turnier = st.checkbox("Veranstaltung eines DTB-Jugend-Ranglistenturniers", value=False)
        btv_partnertrainer = st.checkbox("BTV-Partnertrainer im Verein gebunden", value=False)
        ranglisten_spieler = st.number_input("Spieler mit DTB/BTV Ranglistenposition:", min_value=0, value=0)
        kids_race = st.number_input("Kinder im BTV KidsRace aktiv:", min_value=0, value=5)

# FITP Requirements Definition Matrix
fitp_levels = {
    "Club school *": {
        "teams": 1, "spieler": 8, "leiter": ["C-Trainer", "Staatlich geprüfter Tennislehrer", "B-Trainer Breitensport", "B-Trainer Leistungssport", "A-Trainer"],
        "athletik": ["Athletiktrainer Level 1", "Athletiktrainer Level 2 (Sportwiss. Abschluss)"], "mental": ["Mentaltrainer Stufe 1", "Mentaltrainer Stufe 2 & Ernährungsberater"],
        "manager": ["3 Ehrenamtliche (Vorstand/Jugendwarte)", "Hauptamtlich Stufe 1", "Hauptamtlich Stufe 2"], "halle": False, "fitness": False, "belag": False
    },
    "Basic school **": {
        "teams": 2, "spieler": 12, "leiter": ["Staatlich geprüfter Tennislehrer", "B-Trainer Breitensport", "B-Trainer Leistungssport", "A-Trainer"],
        "athletik": ["Athletiktrainer Level 1", "Athletiktrainer Level 2 (Sportwiss. Abschluss)"], "mental": [],
        "manager": ["3 Ehrenamtliche (Vorstand/Jugendwarte)", "Hauptamtlich Stufe 1", "Hauptamtlich Stufe 2"], "halle": False, "fitness": False, "belag": False
    },
    "Standard school ***": {
        "teams": 3, "spieler": 16, "leiter": ["A-Trainer"],
        "athletik": ["Athletiktrainer Level 1", "Athletiktrainer Level 2 (Sportwiss. Abschluss)"], "mental": ["Mentaltrainer Stufe 1", "Mentaltrainer Stufe 2 & Ernährungsberater"],
        "manager": ["Hauptamtlich Stufe 2"], "halle": True, "fitness": True, "belag": True
    },
    "Super school ****": {
        "teams": 4, "spieler": 19, "leiter": ["A-Trainer"],
        "athletik": ["Athletiktrainer Level 2 (Sportwiss. Abschluss)"], "mental": ["Mentaltrainer Stufe 2 & Ernährungsberater"],
        "manager": ["Hauptamtlich Stufe 2"], "halle": True, "fitness": True, "belag": True
    },
    "Top school *****": {
        "teams": 5, "spieler": 19, "leiter": ["A-Trainer"],
        "athletik": ["Athletiktrainer Level 2 (Sportwiss. Abschluss)"], "mental": ["Mentaltrainer Stufe 2 & Ernährungsberater"],
        "manager": ["Hauptamtlich Stufe 2"], "halle": True, "fitness": True, "belag": True
    }
}

# --- TAB 2: GAP ANALYSE ---
with tab_gap:
    st.markdown("<h3 class='section-title'>Anforderungsprofil & Ziel-Klassifizierung</h3>", unsafe_allow_html=True)
    target_level = st.selectbox(
        "Wähle die angestrebte FITP-Klassifizierungsstufe:",
        ["Club school *", "Basic school **", "Standard school ***", "Super school ****", "Top school *****"],
        index=2
    )

    reqs = fitp_levels[target_level]
    gaps = []
    costs_one_time = 0
    costs_yearly = 0
    earnings_yearly = 0

    # Checks
    if tech_leiter not in reqs["leiter"]:
        gaps.append(f"<b>Technischer Leiter:</b> Erforderlich ist mind. {reqs['leiter'][0]}. (Aktuell: {tech_leiter})")
        costs_yearly += 4000  # Gehaltssprung / Honoraranpassung

    if reqs["athletik"] and athletik_trainer not in reqs["athletik"]:
        gaps.append(f"<b>Athletiktrainer:</b> Erforderlich: {reqs['athletik'][0]}.")
        costs_yearly += 2000

    if reqs["mental"] and mental_trainer not in reqs["mental"]:
        gaps.append(f"<b>Spezialist:</b> Mentaltrainer / Ernährungsberater fehlt.")
        costs_yearly += 1500

    if reqs["manager"] and clubmanager not in reqs["manager"]:
        gaps.append("<b>Management:</b> Clubmanager Stufe 2 bzw. 3 engagierte Ehrenamtliche erforderlich.")

    if jugend_teams < reqs["teams"]:
        missing_teams = reqs["teams"] - jugend_teams
        gaps.append(f"<b>Jugendmannschaften:</b> Es fehlen {missing_teams} gemeldete Mannschaft(en) (Soll: {reqs['teams']}).")
        costs_yearly += missing_teams * 500

    if anzahl_spieler < reqs["spieler"]:
        gaps.append(f"<b>Mindestspielerzahl:</b> Es fehlen {reqs['spieler'] - anzahl_spieler} aktive Kinder im Training.")

    if reqs["halle"] and not hallenplaetze:
        gaps.append("<b>Infrastruktur:</b> Hallenplätze für Wintersaison zwingend erforderlich.")
        costs_yearly += 3000

    if reqs["fitness"] and not fitness_bereich:
        gaps.append("<b>Infrastruktur:</b> Fitnessbereich / Athletik-Equipment fehlt.")
        costs_one_time += 2000

    if reqs["belag"] and not multi_belag:
        gaps.append("<b>Infrastruktur:</b> Plätze mit unterschiedlichen Belägen erforderlich.")

    # Calculate Tournament Earnings
    earnings_yearly += kids_turniere * 1000
    if dtb_turnier:
        earnings_yearly += 3000

    col_g1, col_g2 = st.columns([3, 2])
    with col_g1:
        st.subheader(f"Status & Lücken für '{target_level}'")
        if not gaps:
            st.success("🎉 Alle Kriterien für diese Stufe werden aktuell erfüllt!")
        else:
            for g in gaps:
                st.markdown(f"<div style='padding:10px; background-color:#FFF3CD; border-left:4px solid #FFC107; margin-bottom:8px; border-radius:4px;'>⚠️ {g}</div>", unsafe_allow_html=True)

    with col_g2:
        st.subheader("💰 Wirtschaftliche Bilanz")
        net_yearly = earnings_yearly - costs_yearly
        
        st.markdown(f"""
            <div class='btv-card'>
                <h4>Einmalige Investition:</h4>
                <div class='btv-metric-number'>- {costs_one_time:,} €</div>
                <hr style='border-color:rgba(255,255,255,0.2);'>
                <h4>Laufende Zusatzkosten / Jahr:</h4>
                <div style='font-size:1.4rem; color:#FF8A8A;'>- {costs_yearly:,} €</div>
                <h4>Laufende Turnierträge / Jahr:</h4>
                <div style='font-size:1.4rem; color:var(--btv-green);'>+ {earnings_yearly:,} €</div>
                <hr style='border-color:rgba(255,255,255,0.2);'>
                <h3>Jährliches Netto-Ergebnis:</h3>
                <div class='btv-metric-number' style='color:{"#B3CA38" if net_yearly >= 0 else "#FF8A8A"};'>{net_yearly:+,} €</div>
            </div>
        """, unsafe_allow_html=True)

# --- TAB 3: GRAND PRIX SIMULATOR ---
with tab_grandprix:
    st.markdown("<h3 class='section-title'>BTV & Grand Prix Ranking-Punkte Simulator</h3>", unsafe_allow_html=True)
    
    # Calculate Points
    pts_teams = jugend_teams * 50
    pts_sichtung = btv_sichtung * 50
    pts_kader = (kader_u9_u10 * 150) + (kader_u11_u18 * 200)
    pts_kids_turniere = kids_turniere * 150
    pts_dtb_turnier = 300 if dtb_turnier else 0
    pts_partnertrainer = 200 if btv_partnertrainer else 0
    pts_rangliste = ranglisten_spieler * 100
    pts_kids_race = kids_race * 20
    pts_maedchen = 100 if maedchen_quote >= 35 else 0

    total_points = (
        pts_teams + pts_sichtung + pts_kader + pts_kids_turniere + 
        pts_dtb_turnier + pts_partnertrainer + pts_rangliste + pts_kids_race + pts_maedchen
    )

    m1, m2 = st.columns([1, 2])
    with m1:
        st.markdown(f"""
            <div class='btv-card' style='text-align:center;'>
                <h3>GESAMT-PUNKTESTAND</h3>
                <div class='btv-metric-number' style='font-size:3.5rem;'>{total_points}</div>
                <p>BTV Grand Prix Punkte</p>
            </div>
        """, unsafe_allow_html=True)

    with m2:
        st.subheader("Punktesammlung nach Kategorien")
        st.write(f"• **Jugendmannschaften ({jugend_teams} Teams):** {pts_teams} Pkt.")
        st.write(f"• **BTV-Kader & Sichtung ({btv_sichtung} Sichtung / {kader_u9_u10 + kader_u11_u18} Kader):** {pts_sichtung + pts_kader} Pkt.")
        st.write(f"• **Turnierausrichtung (Kids: {kids_turniere} / DTB: {'Ja' if dtb_turnier else 'Nein'}):** {pts_kids_turniere + pts_dtb_turnier} Pkt.")
        st.write(f"• **BTV-Partnertrainer Status:** {pts_partnertrainer} Pkt.")
        st.write(f"• **Ranglistenspieler & KidsRace ({ranglisten_spieler} RL / {kids_race} KidsRace):** {pts_rangliste + pts_kids_race} Pkt.")
        st.write(f"• **Mädchenförderungs-Bonus (>35%):** {pts_maedchen} Pkt.")

    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("💡 Empfohlene Maßnahmen zur Punktesteigerung")
    
    rec_col1, rec_col2 = st.columns(2)
    with rec_col1:
        if not dtb_turnier:
            st.info("➕ **DTB-Jugendturnier veranstalten:** Bringt **+300 Punkte** und ca. **3.000 € Überschuss** für den Verein.")
        if not btv_partnertrainer:
            st.info("➕ **BTV-Partnertrainer einbinden:** Bringt sofort **+200 Punkte** im Ranking.")
    with rec_col2:
        if maedchen_quote < 35:
            st.info("➕ **Mädchenanteil auf über 35% steigern:** Aktiviert den BTV-Förderbonus von **+100 Punkten**.")
        if btv_sichtung == 0:
            st.info("➕ **Nachwuchskinder zur BTV-Sichtung schicken:** Bringt **+50 Punkte** pro teilnehmendem Kind.")
