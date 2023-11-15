# ADD YOUR load_matching_data AND save_summary IMPLEMENTATIONS HERE
import json

def load_matching_data(min_score, min_stories, min_units):
    list_of_directories = []

    with open('apartment_building_evaluation.csv', 'r') as file:
        for line in file:
            newList = [(file.readline()).split(',')]

            number_of_stories = newList[2]
            number_of_units = newList[3]
            overall_score = newList[24]
            address = newList[26]

            if overall_score == min_score and number_of_stories == min_stories and number_of_units == min_units:
                dictionary = {
                    'address': address,
                    'score': overall_score,
                    'num_stories': num_stories,
                    'num_units': num_units
                }

                list_of_directories.append(dictionary)

    return list_of_directories

def save_summary(list_of_directories):
    with open('apartment_summary.json', 'w') as apartment_summary:
        json.dump(list_of_directories, apartment_summary)