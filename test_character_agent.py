from agents.character_agent import CharacterAgent
from agents.research_agent import ResearchAgent


def main():

    topic = "Lion and Rabbit"

    research_agent = ResearchAgent()
    research_agent.start()

    report = research_agent.research(topic)

    print()

    character_agent = CharacterAgent()
    character_agent.start()

    characters = character_agent.generate_characters(report)

    print("\n==============================")
    print("Generated Characters")
    print("==============================\n")

    for character in characters:
        print(character)
        print()


if __name__ == "__main__":
    main()