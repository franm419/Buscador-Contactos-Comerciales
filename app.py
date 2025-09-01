import streamlit as st
import os
import io
import sys
import markdown
import pdfkit
from dotenv import load_dotenv

# ✅ Asegurarse de que src esté en el path ANTES del import
sys.path.append(os.path.abspath("src"))
from sales_contact_finder.crew import SalesContactFinderCrew

# Configuración inicial
load_dotenv()
sys.path.append(os.path.abspath("src"))
st.set_page_config(page_title="Venko Assistant", layout="centered")

# Variables de estado para mantener contenido tras descarga
if "resultado_md" not in st.session_state:
    st.session_state.resultado_md = ""
if "log_ejecucion" not in st.session_state:
    st.session_state.log_ejecucion = ""

# Estilo personalizado
st.markdown(
    """
    <style>
    body {
        background-color: #0f1117;
        color: white;
    }
    .stButton>button {
        background-color: #6246ea;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 8px 16px;
    }
    ::-webkit-scrollbar {
        width: 12px;
    }
    ::-webkit-scrollbar-thumb {
        background-color: #888;
        border-radius: 6px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background-color: #555;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar para claves API
with st.sidebar:
    st.header("🔐 API Keys")
    openai_key = st.text_input("OpenAI API Key", type="password")
    serper_key = st.text_input("Serper API Key", type="password")
    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key
    if serper_key:
        os.environ["SERPER_API_KEY"] = serper_key

# Título e inputs principales
st.title("🔎 Venko Assistant")
st.markdown("Encuentra contactos clave de una empresa objetivo y desarrolla una estrategia comercial específica para esta empresa.")

empresa_objetivo = st.text_input("🏢 Empresa objetivo", placeholder="Ej: Empresa Objetivo")
nuestro_producto = st.text_input("🚀 Producto o servicio a ofrecer", placeholder="Ej: Chatbot Inteligente")

# Función para convertir Markdown a PDF
def markdown_to_pdf(content_md: str, output_pdf_path: str):
    content_md = content_md.replace("# BuscadorContactosComerciales", "").strip()
    html = markdown.markdown(content_md)
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")
    pdfkit.from_string(html, output_pdf_path, configuration=config, options={"encoding": "UTF-8"})

# BOTÓN EJECUCIÓN PRINCIPAL
if st.button("🚀 Buscar contactos"):
    if not openai_key or not serper_key:
        st.error("⚠️ Debés ingresar ambas claves API.")
    elif not empresa_objetivo or not nuestro_producto:
        st.warning("📋 Completá el nombre de la empresa y del producto.")
    else:
        with st.spinner("Ejecutando agentes de búsqueda..."):
            inputs = {
                "empresa_objetivo": empresa_objetivo,
                "nuestro_producto": nuestro_producto
            }

            # Capturar logs
            buffer = io.StringIO()
            sys.stdout = buffer

            try:
                SalesContactFinderCrew().crew().kickoff(inputs=inputs)
            except Exception as e:
                st.error(f"❌ Error al ejecutar los agentes: {e}")
            finally:
                sys.stdout = sys.__stdout__

            # Leer el markdown generado
            if os.path.exists("buyer_contact.md"):
                with open("buyer_contact.md", "r", encoding="utf-8") as f:
                    content = f.read()
                    if content.startswith("```markdown"):
                        content = content.replace("```markdown", "", 1).strip()
                    content = content.replace("# BuscadorContactosComerciales", "").strip()
                    st.session_state.resultado_md = content
            else:
                st.warning("⚠️ El archivo buyer_contact.md no se generó o no fue encontrado.")

            # Guardar logs
            st.session_state.log_ejecucion = buffer.getvalue()

            st.success("✅ ¡Reporte generado exitosamente!")

# Mostrar resultado si existe
if st.session_state.resultado_md:
    st.markdown("### 📄 Resultado del análisis:")
    st.markdown(st.session_state.resultado_md, unsafe_allow_html=True)

    # Generar PDF y botón de descarga
    pdf_path = "reporte_comercial.pdf"
    try:
        markdown_to_pdf(st.session_state.resultado_md, pdf_path)
        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Descargar PDF del informe",
                data=f.read(),
                file_name="reporte_comercial.pdf",
                mime="application/pdf"
            )
    except Exception as e:
        st.warning(f"⚠️ No se pudo generar el PDF: {e}")

# Mostrar logs si existen
if st.session_state.log_ejecucion:
    with st.expander("🧾 Detalle de ejecución (ver más)"):
        st.code(st.session_state.log_ejecucion, language="bash")
