class Agent:
    def __init__(self):
        self.facts = set()
        self.rules = {}

    def tell_fact(self, fact):
        self.facts.add(fact)

    def tell_rule(self, condition, action):
        self.rules[condition] = action

    def infer_actions(self):
        actions = []
        for condition, action in self.rules.items():
            if condition in self.facts:
                actions.append(action)
        return actions
