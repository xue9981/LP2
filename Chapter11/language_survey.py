from survey import AnonyousSurvey

# define a question, and create an AnonymousSurvey object
question = "What language did you first learn to speak?"
my_survey = AnonyousSurvey(question)

# display the question and save response
my_survey.show_question()
print("Enter 'q' at any time to quit")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# display all results
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()

