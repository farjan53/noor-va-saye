import streamlit as st
from pathlib import Path
import base64

st.set_page_config(page_title="نور و سایه", layout="centered")

def play_audio(file_path):
    audio_file = open(file_path, 'rb')
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')

def main():
    st.markdown("<h1 style='text-align: center;'>برنامه نور و سایه</h1>", unsafe_allow_html=True)
    st.markdown("---")
    st.write("به دنیای نور و سایه خوش آمدید.")

    st.markdown("هر آن‌چه نور بود پدیدار شد، و آن‌چه نتوانست، به صورت سایه پدیدار شد.")

    with st.expander("🔦 مشاهده منطق نور و سایه"):
        st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/Light_dispersion_of_a_mercury-vapor_lamp_with_a_prism.jpg/640px-Light_dispersion_of_a_mercury-vapor_lamp_with_a_prism.jpg",
                 caption="تجزیه نور توسط منشور")
        st.markdown("این تصویر نشان می‌دهد چگونه نور سفید به رنگ‌های مختلف شکسته می‌شود، اما تاریکی تجزیه‌ناپذیر است.")

    st.markdown("---")
    st.info("✨ این نسخه ابتدایی برنامه است. به زودی امکانات بیشتری اضافه خواهد شد.")

    st.markdown("**تهیه‌کننده: فرجان احسانی**")

if __name__ == "__main__":
    audio_path = Path("assets/startup_music.mp3")
    if audio_path.exists():
        play_audio(audio_path)
    main()