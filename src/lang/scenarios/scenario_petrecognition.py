from lang.scenario import Scenario


class ScenarioPetRecognition(Scenario):

    def respond(self, inp: str):
        possible_responses = ['it', 'ty']
        if inp in possible_responses:
            self.cast_dope()