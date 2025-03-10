import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Cargar animaciones
lottie_coding = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_jcikwtux.json")
lottie_success = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_tutvdkg0.json")

# Configuración de la página
st.set_page_config(page_title="CV Interactivo", page_icon="📊", layout="wide")

# Encabezado con animación
st.title("📊 CV Dinámico - Antonio Salazar")
st.write("### Economista y Científico de Datos con experiencia en Machine Learning e Inteligencia Artificial")
st_lottie(lottie_success, height=200)

# Secciones con Tabs
tabs = st.tabs(["Perfil", "Experiencia", "Educación", "Habilidades", "Proyectos", "Certificaciones", "Contacto"])

with tabs[0]:  # Perfil
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/150", width=150)  # Foto de perfil
    with col2:
        st.write(
            "Economista y Matemático con experiencia en Finanzas, Econometría y Ciencia de Datos. He trabajado en \n"
            "desarrollo de modelos de Machine Learning, análisis estadístico avanzado y soluciones tecnológicas basadas en IA/ML."
        )
        st.metric(label="Años de Experiencia", value="5+")
        st_lottie(lottie_coding, height=200)

with tabs[1]:  # Experiencia
    st.subheader("Experiencia Laboral")
    with st.expander("📌 Freelancer en Machine Learning"):
        st.write("Desarrollo de modelos avanzados para soluciones de negocio.")
    with st.expander("📌 Creación de aplicaciones y plataformas tecnológicas"):
        st.write("Implementación de soluciones IA/ML en múltiples sectores.")
    st.progress(85)

with tabs[2]:  # Educación
    st.subheader("Educación")
    st.write("🎓 **Licenciatura en Economía y Matemáticas** - Universidad Nacional Autónoma de México (UNAM)")
    st.write("📚 Participación en conferencias en UNAM, Universidad Nacional de Colombia, UNESCO, ITAM, entre otras.")
    st.success("Educación continua en Ciencia de Datos y Finanzas Cuantitativas.")

with tabs[3]:  # Habilidades
    st.subheader("Lenguajes de Programación")
    st.write("Python, R, SQL")
    st.subheader("Bibliotecas y Herramientas")
    st.write("NumPy, Pandas, Matplotlib, Seaborn, TensorFlow, PyTorch, scikit-learn, PySpark")
    st.subheader("Cloud Computing")
    st.write("AWS, Azure")
    st.bar_chart({"Python": 90, "SQL": 85, "R": 75})

with tabs[4]:  # Proyectos
    st.subheader("Proyectos Destacados")
    st.write("- 🚀 Desarrollo de plataformas tecnológicas basadas en IA/ML.")
    st.write("- 📊 Creación de aplicaciones web y visualización de datos con Looker Studio.")
    st.write("- 📈 Modelos predictivos para análisis financiero y econométrico.")
    

with tabs[5]:  # Certificaciones
    st.subheader("Certificaciones")
    st.write("✅ **Certificado en Ciencia de Datos** - Microsoft")
    st.write("✅ Cursos avanzados en Machine Learning y Finanzas Cuantitativas.")
    st.balloons()

with tabs[6]:  # Contacto
    st.subheader("📬 Contacto")
    contacto = st.text_input("Deja tu correo para recibir más información")
    if st.button("Enviar"):
        with st.spinner("Enviando..."):
            time.sleep(2)
            st.success("¡Gracias por tu interés! Te contactaremos pronto.")
