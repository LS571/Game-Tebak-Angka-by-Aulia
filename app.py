import streamlit as st
import random

st.title("🎯 Game Tebak Angka")
st.write("Pilih mode, lalu tebak angka dari **1 sampai 20**")

# ===============================
# PILIH MODE
# ===============================
mode = st.selectbox(
    "Pilih Mode Game:",
    ("Cupu 😌", "GG Gaming 😎", "Hengkertzy ☠️")
)

# Set kesempatan berdasarkan mode
if mode == "Cupu 😌":
    max_attempts = 10
elif mode == "GG Gaming 😎":
    max_attempts = 7
else:
    max_attempts = 4

# ===============================
# INIT SESSION STATE
# ===============================
if "angka_rahasia" not in st.session_state:
    st.session_state.angka_rahasia = random.randint(1, 20)
    st.session_state.attempts = 0
    st.session_state.selesai = False
    st.session_state.mode = mode

# Reset jika mode diganti
if st.session_state.mode != mode:
    st.session_state.angka_rahasia = random.randint(1, 20)
    st.session_state.attempts = 0
    st.session_state.selesai = False
    st.session_state.mode = mode

# ===============================
# INPUT USER
# ===============================
tebakan = st.number_input(
    "Masukkan tebakan kamu:",
    min_value=1,
    max_value=20,
    step=1
)

st.write(f"Kesempatan: {max_attempts - st.session_state.attempts} kali")

# ===============================
# LOGIC GAME
# ===============================
if st.button("Cek Jawaban") and not st.session_state.selesai:
    st.session_state.attempts += 1
    selisih = abs(tebakan - st.session_state.angka_rahasia)

    if tebakan == st.session_state.angka_rahasia:
        st.success("🎉 BENAR! LU JAGO 🔥")
        st.session_state.selesai = True

    elif selisih <= 2:
        st.warning("🔥🔥 WOOO DIKIT LAGII!!!")

    elif selisih <= 4:
        st.info("⚡ Hampir benar!")

    else:
        st.error("❄️ Masih jauh brooo")

    if st.session_state.attempts >= max_attempts and not st.session_state.selesai:
        st.error(
            f"💀 GAME OVER! Angka yang benar adalah **{st.session_state.angka_rahasia}**"
        )
        st.session_state.selesai = True

# ===============================
# RESTART BUTTON
# ===============================
if st.button("🔄 Restart Game"):
    st.session_state.angka_rahasia = random.randint(1, 20)
    st.session_state.attempts = 0
    st.session_state.selesai = False
    st.rerun()
