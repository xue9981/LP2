def print_models(unprinted_designs, completed_models):
    """
    simulate to print all designs
    after print everything, copy the result in completed_models
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        #create print progress
        print("Printing mode: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    # print completed design
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)

