from agents.research_agent import ResearchAgent
from agents.character_agent import CharacterAgent
from agents.character_bible_agent import CharacterBibleAgent


def main():

    topic = "Lion and Rabbit"

    # Research

    research_agent = ResearchAgent()
    research_agent.start()

    report = research_agent.research(topic)

    # Character Profiles

    character_agent = CharacterAgent()
    character_agent.start()

    characters = character_agent.generate_characters(report)

    # Character Bible

    bible_agent = CharacterBibleAgent()
    bible_agent.start()

    print("\n==============================")
    print("Character Bible")
    print("==============================")

    for character in characters:

        bible = bible_agent.generate_character_bible(character)

        print("\n========================================")
        print(bible.name)
        print("========================================")

        print("Character ID:")
        print(bible.character_id)

        print("\nSpecies:")
        print(bible.species)

        print("\nRole:")
        print(bible.role)

        print("\nAppearance:")
        print(bible.appearance)

        print("\nClothing:")
        print(bible.clothing)

        print("\nAccessories:")
        print(bible.accessories)

        print("\nColor Palette:")
        print(bible.color_palette)

        print("\nPersonality:")
        print(bible.personality)

        print("\nStrengths:")
        print(bible.strengths)

        print("\nWeaknesses:")
        print(bible.weaknesses)

        print("\nGoals:")
        print(bible.goals)

        print("\nDefault Expression:")
        print(bible.default_expression)

        print("\nDefault Pose:")
        print(bible.default_pose)

        print("\nMovement Style:")
        print(bible.movement_style)

        print("\nGestures:")
        print(bible.gestures)

        print("\nVoice Style:")
        print(bible.voice_style)

        print("\nCatch Phrase:")
        print(bible.catch_phrase)

        print("\nImage Prompt:")
        print(bible.image_prompt)

        print("\nNegative Prompt:")
        print(bible.negative_prompt)


if __name__ == "__main__":
    main()