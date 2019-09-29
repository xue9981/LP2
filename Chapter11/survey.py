class AnonyousSurvey():
    """collect survey without name"""

    def __init__(self, question):
        """save an question, and be ready to save responses"""
        self.question = question
        self.responses = []

    def show_question(self):
        """show survey"""
        print(self.question)

    def store_response(self, new_response):
        """save an response"""
        self.responses.append(new_response)

    def show_results(self):
        """show all results"""
        print("Survey results:")
        for response in self.responses:
            print("- " + response)
        
