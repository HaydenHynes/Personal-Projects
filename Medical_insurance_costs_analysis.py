import csv

def load_data():
    with open("insurance.csv", newline='') as insurance_csv:
        return list(csv.DictReader(insurance_csv))

def charges_by_gender(data):
    female_total_charge = 0
    male_total_charge = 0
    number_of_women = 0
    number_of_men = 0
    for dictionary in data:
        if dictionary['sex'] == "female":
            female_total_charge += float(dictionary['charges'])
            number_of_women += 1
        elif dictionary['sex'] == 'male':
            male_total_charge += float(dictionary['charges'])
            number_of_men += 1
    avg_female_charge = female_total_charge/number_of_women
    avg_male_charge = male_total_charge/number_of_men

    print(f'Women in total are charged ${female_total_charge:,.2f} and on average are charged '
          f'${avg_female_charge:,.2f}\nMen in total are charged ${male_total_charge:,.2f} and on average are '
          f'charged ${avg_male_charge:,.2f}')

def charges_by_region(data):
    southwest = 0
    southeast = 0
    northwest = 0
    northeast = 0

    for dictionary in data:
        if dictionary['region'] == 'southwest':
            southwest += float(dictionary['charges'])
        elif dictionary['region'] == 'southeast':
            southeast += float(dictionary['charges'])
        elif dictionary['region'] == 'northwest':
            northwest += float(dictionary['charges'])
        elif dictionary['region'] == 'northeast':
            northeast += float(dictionary['charges'])

    print(f'Total Charges Southwest: ${southwest:,.2f}\n'
          f'Total Charges Southeast: ${southeast:,.2f}\n'
          f'Total Charges Northwest: ${northwest:,.2f}\n'
          f'Total Charges Northeast: ${northeast:,.2f}')

def number_of_smokers(data):
    smokers_southeast = {'Smokers': 0, "Non-Smokers": 0}
    smokers_southwest = {'Smokers': 0, "Non-Smokers": 0}
    smokers_northeast = {'Smokers': 0, "Non-Smokers": 0}
    smokers_northwest = {'Smokers': 0, "Non-Smokers": 0}

    for dictionary in data:
        if dictionary['smoker'] == 'yes':
            if dictionary['region'] == 'southeast':
                smokers_southeast['Smokers'] += 1
            elif dictionary['region'] == 'southwest':
                smokers_southwest['Smokers'] += 1
            elif dictionary['region'] == 'northeast':
                smokers_northeast['Smokers'] += 1
            elif dictionary['region'] == 'northwest':
                smokers_northwest['Smokers'] += 1
        elif dictionary['smoker'] == 'no':
            if dictionary['region'] == 'southeast':
                smokers_southeast['Non-Smokers'] += 1
            elif dictionary['region'] == 'southwest':
                smokers_southwest['Non-Smokers'] += 1
            elif dictionary['region'] == 'northeast':
                smokers_northeast['Non-Smokers'] += 1
            elif dictionary['region'] == 'northwest':
                smokers_northwest['Non-Smokers'] += 1

    print(f'There are {smokers_southeast['Smokers']} smokers and {smokers_southeast['Non-Smokers']} non-smokers in the '
          f'southeast regions.\n'
          f'There are {smokers_southwest['Smokers']} smokers and {smokers_southwest['Non-Smokers']} non-smokers in the '
          f'southwest regions.\n'
          f'There are {smokers_northeast['Smokers']} smokers and {smokers_northeast['Non-Smokers']} non-smokers in the '
          f'northeast regions.\n'
          f'There are {smokers_northwest['Smokers']} smokers and {smokers_northwest['Non-Smokers']} non-smokers in the '
          f'northwest regions.')

def average_age_of_patients(data):
    total_age = 0
    number_of_patients = 0
    for patient in data:
        total_age += int(patient['age'])
        number_of_patients += 1
    avg_age = total_age / number_of_patients
    return f'The average age across all patients is roughly {round(avg_age)} years old'

def most_populated_region(data):
    population_by_region = {'southeast': 0, 'southwest': 0, 'northeast': 0, 'northwest': 0}
    for dictionary in data:
        if dictionary['region'] == 'southeast':
            population_by_region['southeast'] += 1
        elif dictionary['region'] == 'southwest':
            population_by_region['southwest'] += 1
        elif dictionary['region'] == 'northeast':
            population_by_region['northeast'] += 1
        elif dictionary['region'] == 'northwest':
            population_by_region['northwest'] += 1

    largest_population = max(population_by_region, key=population_by_region.get)
    print(f'The most populated region is the {largest_population} region which has '
          f'{population_by_region[largest_population]} people')

def different_costs(data):
    number_of_smokers = 0
    smokers_total_costs = 0
    number_of_non_smokers = 0
    non_smokers_total_costs = 0

    for dictionary in data:
        if dictionary['smoker'] == 'yes':
            number_of_smokers += 1
            smokers_total_costs += float(dictionary['charges'])
        elif dictionary['smoker'] == 'no':
            number_of_non_smokers += 1
            non_smokers_total_costs += float(dictionary['charges'])
        else:
            continue

    avg_smoker_cost = smokers_total_costs/number_of_smokers
    avg_non_smoker_cost = non_smokers_total_costs/number_of_non_smokers
    avg_difference = avg_smoker_cost - avg_non_smoker_cost

    print(f'\nThere are {number_of_smokers} smokers and {number_of_non_smokers:,.0f} non-smokers.\nSmokers altogether '
          f'are charged ${smokers_total_costs:,.2f} and non-smokers are charged ${non_smokers_total_costs:,.2f}.'
          f'\nThus, on average smokers are charged ${avg_smoker_cost:,.2f} per smoker whereas non-smokers are charged '
          f'on average ${avg_non_smoker_cost:,.2f}.\nThat is a ${avg_difference:,.2f} average cost difference!')

def average_age_with_at_least_one_child(data):
    total_ages = 0
    number_of_people = 0

    for dictionary in data:
        if dictionary['children'] != '0':
            total_ages += int(dictionary['age'])
            number_of_people += 1

    average_age = total_ages / number_of_people

    return f'Average Age: {average_age:.0f}'



data = load_data()
charges_by_gender(data)
charges_by_region(data)
number_of_smokers(data)
print(average_age_of_patients(data))
most_populated_region(data)
different_costs(data)
print(average_age_with_at_least_one_child(data))
