class StoryFormatter:

    def to_markdown(self, story):

        return f"""# {story.title}

## Story

{story.story}

---

## Moral

{story.moral}

---

**Word Count:** {story.word_count}
"""

    def to_text(self, story):

        return f"""TITLE

{story.title}


STORY

{story.story}


MORAL

{story.moral}


WORD COUNT

{story.word_count}
"""