import streamlit as st
import random

st.title("🎮 Sayı Tahmin Oyunu")
st.write("1 ile 100 arasında bir sayı tuttum. Tahmin edebilecek misin?")

# Oyunun başlangıç değişkenlerini hafızaya (Session State) kaydediyoruz
if 'gizli_sayi' not in st.session_state:
    st.session_state.gizli_sayi = random.randint(1, 100)
    st.session_state.tahmin_sayisi = 0
    st.session_state.oyun_bitti = False

# Değişiklik BURADA: number_input yerine slider kullanıyoruz.
# Basılı tutup sağa sola kaydırarak hızlıca sayıyı seçebilirsin.
tahmin = st.slider("Tahmininiz:", min_value=1, max_value=100, value=50, step=1)

# "Tahmin Et" butonu
if st.button("Tahmin Et") and not st.session_state.oyun_bitti:
    st.session_state.tahmin_sayisi += 1
    
    if tahmin < st.session_state.gizli_sayi:
        st.warning("⬆️ Daha BÜYÜK bir sayı söyleyin!")
    elif tahmin > st.session_state.gizli_sayi:
        st.warning("⬇️ Daha KÜÇÜK bir sayı söyleyin!")
    else:
        st.success(f"🎉 Tebrikler! Sayıyı {st.session_state.tahmin_sayisi} denemede buldunuz!")
        st.session_state.oyun_bitti = True

# Oyunu Yeniden Başlatma Butonu
if st.session_state.oyun_bitti:
    if st.button("Yeniden Oyna 🔄"):
        # Hafızayı temizleyip oyunu sıfırlıyoruz
        del st.session_state.gizli_sayi
        del st.session_state.tahmin_sayisi
        del st.session_state.oyun_bitti
        st.rerun()
