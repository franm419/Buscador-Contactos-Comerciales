from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task


@CrewBase
class SalesContactFinderCrew:
    """Equipo de trabajo para encontrar contactos comerciales"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def investigador_empresa(self) -> Agent:
        return Agent(
            config=self.agents_config["investigador_empresa"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def analista_estructura_organizacional(self) -> Agent:
        return Agent(
            config=self.agents_config["analista_estructura_organizacional"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def buscador_contactos(self) -> Agent:
        return Agent(
            config=self.agents_config["buscador_contactos"],
            tools=[SerperDevTool(), ScrapeWebsiteTool()],
            allow_delegation=False,
            verbose=True,
        )

    @agent
    def estratega_ventas(self) -> Agent:
        return Agent(
            config=self.agents_config["estratega_ventas"],
            tools=[],
            allow_delegation=False,
            verbose=True,
        )

    @task
    def tarea_investigacion_empresa(self) -> Task:
        return Task(
            config=self.tasks_config["tarea_investigacion_empresa"],
            agent=self.investigador_empresa(),
        )

    @task
    def tarea_analisis_estructura_organizacional(self) -> Task:
        return Task(
            config=self.tasks_config["tarea_analisis_estructura_organizacional"],
            agent=self.analista_estructura_organizacional(),
        )

    @task
    def tarea_busqueda_contactos(self) -> Task:
        return Task(
            config=self.tasks_config["tarea_busqueda_contactos"],
            agent=self.buscador_contactos(),
        )

    @task
    def tarea_estrategia_ventas(self) -> Task:
        return Task(
            config=self.tasks_config["tarea_estrategia_ventas"],
            agent=self.estratega_ventas(),
            output_file="estrategia_comercial.md",
        )

    @crew
    def crew(self) -> Crew:
        """Crea el equipo SalesContactFinder"""
        return Crew(
            agents=self.agents,  # Creado automáticamente por el decorador @agent
            tasks=self.tasks,    # Creado automáticamente por el decorador @task
            process=Process.sequential,  # También podés usar Process.hierarchical
            verbose=True,
        )
