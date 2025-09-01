import sys
from dotenv import load_dotenv
from sales_contact_finder.crew import SalesContactFinderCrew

# Carga las variables de entorno desde el archivo .env
load_dotenv()

def run():
    """
    Ejecuta el equipo de agentes.
    """
    inputs = {
        "empresa_objetivo": "Empresa Modelo",
        "nuestro_producto": "Chatbot para whatsapp",
    }
    SalesContactFinderCrew().crew().kickoff(inputs=inputs)

def train():
    """
    Entrena el equipo durante un número específico de iteraciones.
    """
    inputs = {"tema": "IA"}
    try:
        SalesContactFinderCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"Ocurrió un error durante el entrenamiento del equipo: {e}")

def replay():
    """
    Reproduce la ejecución del equipo desde una tarea específica.
    """
    try:
        SalesContactFinderCrew().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"Ocurrió un error al reproducir la ejecución del equipo: {e}")

def test():
    """
    Prueba la ejecución del equipo y devuelve los resultados.
    """
    inputs = {"tema": "IA"}
    try:
        SalesContactFinderCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            openai_model_name=sys.argv[2],
            inputs=inputs
        )
    except Exception as e:
        raise Exception(f"Ocurrió un error al probar la ejecución del equipo: {e}")
