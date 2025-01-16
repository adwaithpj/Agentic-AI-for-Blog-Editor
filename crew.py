from crewai import Crew, Process
from agents import planner, writer, editor
from tasks import plan, write, edit
from IPython.display import Markdown

##Forming the blog making crew


# Markdown(result)

# print(result)


def crew_start(topic: str):
    crew = Crew(
        agents=[planner, writer, editor],
        tasks=[plan, write, edit],
        verbose=True,
        process=Process.sequential,
    )

    result = crew.kickoff(inputs={"topic": f"{topic}"})

    return result


crew_start("messi")
