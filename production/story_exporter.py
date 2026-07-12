from pathlib import Path

from formatters.story_formatter import StoryFormatter


class StoryExporter:

    def export(self, story):

        formatter = StoryFormatter()

        production_folder = Path("production")
        production_folder.mkdir(exist_ok=True)

        filename = story.title.replace(" ", "_")

        markdown_file = production_folder / f"{filename}.md"
        text_file = production_folder / f"{filename}.txt"

        markdown_file.write_text(
            formatter.to_markdown(story),
            encoding="utf-8"
        )

        text_file.write_text(
            formatter.to_text(story),
            encoding="utf-8"
        )

        print("\nStory exported successfully.")

        print(markdown_file)

        print(text_file)