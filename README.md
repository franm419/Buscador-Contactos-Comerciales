📊 Buscador de Contactos Comerciales:
Bienvenido al proyecto Buscador de Contactos Comerciales. Esta plantilla está diseñada para ayudarte a configurar un sistema de inteligencia artificial con múltiples agentes de manera sencilla, aprovechando el poderoso y flexible framework que ofrece crewAI.

Nuestro objetivo es permitir que tus agentes colaboren eficazmente en tareas complejas, maximizando su inteligencia colectiva y capacidades.

⚙️ Instalación:
Requisitos: Asegurate de tener una versión de Python compatible (≥ 3.10 y ≤ 3.13).

Instalar uv (gestor de dependencias recomendado):

pip install uv

Instalar dependencias del proyecto:
Navegá a la raíz del proyecto y ejecutá:

uv lock
uv sync

Configurar claves API:
Asegurate de tener un archivo .env con las siguientes variables:

OPENAI_API_KEY=tu_clave_openai
SERPER_API_KEY=tu_clave_serper

🔧 Personalización:
🧠 Definí tus agentes en: src/sales_contact_finder/config/agents.yaml

🗂️ Definí tus tareas en: src/sales_contact_finder/config/tasks.yaml

⚙️ Configurá la lógica del equipo en: src/sales_contact_finder/crew.py

🧪 Modificá los inputs de prueba en: src/sales_contact_finder/main.py

🚀 Ejecución del Proyecto:
Para poner en marcha tu equipo de agentes de IA y comenzar la ejecución de tareas, corré uno de estos comandos desde la carpeta raíz:

crewai run
# o bien
uv run sales_contact_finder

Esto inicializa el equipo, ensamblando los agentes y asignándoles tareas según tu configuración.
El ejemplo sin modificar generará un archivo report.md con los resultados de una investigación sobre LLMs.

👥 Estructura del Equipo:
La aplicación está compuesta por múltiples agentes de IA, cada uno con roles, objetivos y herramientas específicas.
Estos agentes colaboran en tareas definidas en config/tasks.yaml y están configurados en config/agents.yaml.