# =====================================================
# UNIVERSAL OPERATION VALIDATOR
# =====================================================

class OperationValidator:

    def __init__(self):

        self.rules = []


    def add_rule(self, rule):

        self.rules.append(rule)


    def clear_rules(self):

        self.rules.clear()


    def validate(self):

        for rule in self.rules:

            if not rule():

                return False

        return True