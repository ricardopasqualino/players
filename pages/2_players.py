import streamlit as st

# Define as caracteristicas da pagina
st.set_page_config (
    page_title = "Jogadores",
    page_icon="🏃🏻‍♀️",
    layout="wide"
)

df_data = st.session_state['data']

# Trazer todos os clubes
clubes = df_data["Club"].value_counts().index
club = st.sidebar.selectbox("Clubes", clubes)

# Pegar apenas o jogador da variavel club
df_players = df_data[df_data["Club"] == club ]

players = df_players["Name"].value_counts().index
player = st.sidebar.selectbox("Jogadores", players)

player_stats = df_data[df_data["Name"] == player].iloc[0]

st.sidebar.image(player_stats["Photo"])
st.sidebar.image(player_stats["Flag"])

st.title(f"{player_stats['Name']}")
st.image(player_stats["Club Logo"])

col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {player_stats['Age']}")
col2.markdown(f"**Altura:** {player_stats['Height(cm.)']}")
col3.markdown(f"**Peso:** {player_stats['Weight(lbs.)'] * 0.453:.2f}")
col4.markdown(f"**Posição:** {player_stats['Position']} ")

st.divider()

st.subheader(f"Overall, {player_stats['Overall']}")
st.progress(int(player_stats['Overall']))

col1, col2, col3, col4 = st.columns(4)
col1.metric(label="Valor de mercado", value=f"£ {player_stats['Value(£)']}")
col2.metric(label="Remuneração Semanal", value=f"£ {player_stats['Wage(£)']}")
col3.metric(label="Clausula de recisão", value=f"£ {player_stats['Release Clause(£)']}")
