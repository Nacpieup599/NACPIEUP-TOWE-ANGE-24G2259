import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import requests

# 1. CONFIGURATION DE LA PAGE
st.set_page_config(page_title="TP INF 232 - TOWE ANGE", layout="wide")

# Forçage du style pour les métriques
st.markdown("""
    <style>
    [data-testid="stMetricValue"] { font-size: 28px; color: #1f77b4; font-weight: bold; }
    .prediction-box {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        border-left: 5px solid #ff4b4b;
    }
    </style>
""", unsafe_allow_html=True)

st.title("📊 Flora Market - TOWE ANGE")
st.markdown("### *Collecte de données & Analyse Descriptive du Marché*")

# 2. RÉCUPÉRATION DES DONNÉES (API)
@st.cache_data
def charger_donnees_api():
    try:
        url = "https://fakestoreapi.com/products/category/women's clothing"
        reponse = requests.get(url, timeout=5)
        donnees = reponse.json()
        df_api = pd.DataFrame([
            {
                'Article': item['title'][:20], 
                'Qualite_X': item['rating']['rate'], 
                'Prix_Y': round(item['price'] * 650) 
            } for item in donnees
        ])
        return df_api
    except:
        return pd.DataFrame({'Article':['Article Test'], 'Qualite_X':[4.0], 'Prix_Y':[25000]})

# 3. GESTION DE LA MÉMOIRE (Session State)
if 'df_final' not in st.session_state:
    st.session_state.df_final = charger_donnees_api()

# 4. BARRE LATÉRALE (SAISIE)
with st.sidebar:
    st.header("📝 Collecte de données")
    with st.form("ajout"):
        n = st.text_input("Nom de l'article")
        q = st.slider("Note Qualité (X)", 1.0, 5.0, 3.5)
        p = st.number_input("Prix d'achat (Y)", min_value=0)
        if st.form_submit_button("Enregistrer l'article"):
            if n:
                new = pd.DataFrame({'Article':[n], 'Qualite_X':[q], 'Prix_Y':[p]})
                st.session_state.df_final = pd.concat([st.session_state.df_final, new], ignore_index=True)
                st.rerun()

df = st.session_state.df_final

# 5. CALCULS STATISTIQUES (MATHÉMATIQUES INF 232)
x, y = df['Qualite_X'], df['Prix_Y']
moy_x, moy_y = x.mean(), y.mean() 
cov_xy = ((x - moy_x) * (y - moy_y)).sum()
var_x = ((x - moy_x)**2).sum()

if var_x != 0:
    a = cov_xy / var_x
    b = moy_y - a * moy_x
else:
    a, b = 0, moy_y

r_corr = x.corr(y)
df['Prediction_Model'] = a * df['Qualite_X'] + b

# 6. INDICATEURS CLÉS
c1, c2, c3, c4 = st.columns(4)
c1.metric("Prix Minimum", f"{y.min():,.0f} FCFA")
c2.metric("Prix Maximum", f"{y.max():,.0f} FCFA")
c3.metric("Prix Moyen", f"{moy_y:,.0f} FCFA")
c4.metric("Total Articles", len(df))

st.divider()

# 7. GRAPHIQUES GRANDE TAILLE
st.subheader("📊 Graphique des prix (Analyse de TOWE-ANGE)")
df_sorted = df.sort_values('Prix_Y', ascending=False)
fig_bar = px.bar(df_sorted, x='Article', y='Prix_Y', 
                 color='Prix_Y', color_continuous_scale='Viridis',
                 text_auto='.2s', height=500)
fig_bar.update_layout(bargap=0.2, xaxis_tickangle=-45)
st.plotly_chart(fig_bar, use_container_width=True)

st.subheader("📌 Modèle de Régression Linéaire")
fig_scatter = px.scatter(df, x='Qualite_X', y='Prix_Y', text='Article',
                         labels={'Qualite_X': 'Qualité (X)', 'Prix_Y': 'Prix (Y)'},
                         height=500)
fig_scatter.add_scatter(x=df['Qualite_X'], y=df['Prediction_Model'], mode='lines', 
                        name='Droite de régression', line=dict(color='red', width=3))
fig_scatter.add_scatter(x=[moy_x], y=[moy_y], mode='markers', 
                        name='Point G (Moyen)', 
                        marker=dict(color='orange', size=15, symbol='diamond', line=dict(width=2, color='black')))
st.plotly_chart(fig_scatter, use_container_width=True)

st.divider()

# 8. MODULE DE PRÉDICTION (NOUVEAU)
st.subheader("🔮 Simulateur de Prix (Inférence Statistique)")
st.write("Utilisez le modèle mathématique pour estimer le prix d'un futur article en fonction de sa note qualité.")

col_p1, col_p2 = st.columns([1, 2])
with col_p1:
    note_test = st.number_input("Entrez une note de qualité (X)", min_value=0.0, max_value=5.0, value=4.0, step=0.1)
    prix_predit = a * note_test + b
with col_p2:
    st.markdown(f"""
    <div class="prediction-box">
        <h4>Résultat de l'estimation :</h4>
        <h2 style="color: #ff4b4b;">{max(0, prix_predit):,.0f} FCFA</h2>
        <p><i>Basé sur l'équation : Y = {a:.2f}X + {b:.2f}</i></p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# 9. DÉTAILS MATHÉMATIQUES & BASE DE DONNÉES
col_end1, col_end2 = st.columns(2)
with col_end1:
    with st.expander("📝 Détails des calculs"):
        st.write(f"*   **Moyenne Qualité (X̄) :** `{moy_x:.2f}`")
        st.write(f"*   **Coeff. de Corrélation (r) :** `{r_corr:.4f}`")
        st.latex(r"Y = " + f"{a:.2f}X + {b:.2f}")
        st.write(f"**Point G :** `({moy_x:.2f}, {moy_y:.0f})`")

with col_end2:
    with st.expander("🗂️ Consulter la base de données "):
        st.dataframe(df[['Article', 'Qualite_X', 'Prix_Y']], use_container_width=True)

st.info("💡 Travail réalisé par NACPIEUP TOWE ANGE - Projet INF 232 - 2026")
