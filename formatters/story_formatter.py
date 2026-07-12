class StoryFormatter:

    @staticmethod
    def print_review(review):

        print("\n==============================")
        print("Story Review")
        print("==============================")

        print(f"Score : {review.score}/100")
        print(f"Passed : {'Yes' if review.passed else 'No'}")

        print("\nFeedback:")
        print(review.feedback)

    @staticmethod
    def print_story(story):

        print("\n==============================")
        print("Story Generated Successfully")
        print("==============================")

        print(f"\nTitle:\n{story.title}")

        print(f"\nStory:\n{story.story}")

        print(f"\nMoral:\n{story.moral}")

        print(f"\nWord Count:\n{story.word_count}")

    @staticmethod
    def to_markdown(story):

        return f"""# {story.title}

## Story

{story.story}

---

## Moral

{story.moral}

---

**Word Count:** {story.word_count}
"""

    @staticmethod
    def to_text(story):

        return f"""TITLE

{story.title}


STORY

{story.story}


MORAL

{story.moral}


WORD COUNT

{story.word_count}
"""