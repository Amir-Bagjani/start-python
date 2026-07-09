from src.utils.utils import chat


def main():
    while True:
        prompt = input("\nSay somthing to your Khadang AI: ").strip()
        print(f"\n{chat(prompt)}")


if __name__ == "__main__":
    main()
