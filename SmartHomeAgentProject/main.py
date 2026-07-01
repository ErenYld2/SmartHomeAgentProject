from agent import Agent
from interpreter import interpret_input_with_gemini
import json

def load_rules_from_json(agent, path="rules.json"):
    with open(path, "r", encoding="utf-8") as file:
        rules = json.load(file)
        for condition, action in rules.items():
            agent.tell_rule(condition, action)

def main():
    agent = Agent()
    load_rules_from_json(agent)

    user_input = input("Komut girin (Akıllı Cihazlar:Klima,Isıtıcı,Perdeler,Işıklar,Kapı): ")
    fact = interpret_input_with_gemini(user_input)
    print(f"Yorumlanan gerçek: {fact}")

    agent.tell_fact(fact)
    actions = agent.infer_actions()

    if actions:
        for action in actions:
            print(f"Gerçekleştirilecek eylem: {action}")
    else:
        print("Hiçbir eylem tetiklenmedi.")

if __name__ == "__main__":
    main()
