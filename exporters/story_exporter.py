# ==========================================================
# Imports
# ==========================================================

from formatters.story_formatter import StoryFormatter
from config.paths import STORIES_DIR


# ==========================================================
# Story Exporter
# ==========================================================

class StoryExporter:

    @staticmethod
    def export(story):

        filename = (
            story.title
            .replace(" ", "_")
            .replace("/", "_")
        )

        markdown_file = STORIES_DIR / f"{filename}.md"
        text_file = STORIES_DIR / f"{filename}.txt"

        markdown_file.write_text(
            StoryFormatter.to_markdown(story),
            encoding="utf-8"
        )

        text_file.write_text(
            StoryFormatter.to_text(story),
            encoding="utf-8"
        )

        print("\nStory exported successfully.")
        print(markdown_file)
        print(text_file)