# 🔎 Sales Contact Finder

This project is **Venko Assistant**, an AI-powered tool built with **CrewAI** and **Streamlit**.  
It automates company research, identifies key decision-makers, and generates tailored sales strategies with an interactive web interface.

---

## 🚀 Features
- **Multi-agent system (CrewAI):**  
  - Company Research Agent  
  - Organizational Structure Analyst  
  - Key Contact Finder  
  - Sales Strategist  
- **Custom workflows:** Orchestrated using CrewAI with YAML-based configuration for agents and tasks.  
- **Streamlit Frontend:** User-friendly web app to input target company and product, run agents, and visualize results.  
- **Automated outputs:**  
  - Generates **Markdown reports** of findings.  
  - Converts reports into **PDF** files for easy sharing.  
- **Secure API management:** Keys are handled through `.env` variables, never exposed in the codebase.  

---

## ⚙️ Tech Stack
- [Python 3.12](https://www.python.org/)  
- [CrewAI](https://github.com/joaomdmoura/crewAI) – Multi-agent orchestration  
- [Streamlit](https://streamlit.io/) – Interactive frontend  
- [OpenAI API](https://platform.openai.com/) – LLM for research & text generation  
- [Serper API](https://serper.dev/) – Web search integration  
- [pdfkit](https://pypi.org/project/pdfkit/) – Export reports as PDF  

---

## 📂 Project Structure
```
├── src/
│   └── sales_contact_finder/
│       ├── crew.py
│       ├── agents.yaml
│       ├── tasks.yaml
├── app.py              # Streamlit frontend
├── pyproject.toml      # Dependencies and scripts
├── README.md           # Project documentation
├── .env                # API Keys (excluded in .gitignore)
└── .gitignore
```

---

## 🔐 Environment Variables
Create a `.env` file in the project root:

```ini
OPENAI_API_KEY=your_openai_key_here
SERPER_API_KEY=your_serper_key_here
```

⚠️ The `.env` file is excluded from GitHub via `.gitignore`.

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/franm419/Buscador-Contactos-Comerciales.git
   cd Buscador-Contactos-Comerciales
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate    # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open your browser at:
   - Local: [http://localhost:8501](http://localhost:8501)  
   - Network: `http://<your-ip>:8501`

---

## 📊 Example Output
- `buyer_contact.md` → Detailed report in Markdown.  
- `reporte_comercial.pdf` → Exported PDF report with company insights, contacts, and sales strategy.  

---

## 👨‍💻 Author
Francisco Moyano Escalera  
Specialist in Data, AI & Automation  
📧 frannmmm419@gmail.com  
🌐 GitHub: [franm419](https://github.com/franm419)


