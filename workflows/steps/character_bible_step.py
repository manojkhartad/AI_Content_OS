from agents.agent_manager import AgentManager

from exporters.character_bible_exporter import CharacterBibleExporter

from workflows.steps.base_step import BaseStep
from workflows.workflow_context import WorkflowContext


class CharacterBibleStep(BaseStep):

    def execute(
        self,
        context: WorkflowContext
    ) -> WorkflowContext:

        print("\n========== Character Bible ==========")

        agent = AgentManager().get("character_bible")

        character_bibles = agent.generate_character_bibles(
            context.get("characters")
        )

        CharacterBibleExporter.export(
            character_bibles
        )

        context.set(
            "character_bibles",
            character_bibles
        )

        return context