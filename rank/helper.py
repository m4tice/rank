import numpy as np


def extract(input_file):
    '''
    Extract phase: extract data from input text file
    '''
    print("- Extract phase Started")
    data = []
    with open(input_file) as f:
        lines = f.readlines()

        for line in lines:
            # Extract match information from each line
            match = extract_match_info(line)
            data.append(match)

    print("- Extract phase Ended")

    return data


def transform(data):
    '''
    Transform phase: transform data to the required format
    '''
    print("- Transform phase Started")

    # Create point table dictionary
    point_table = create_table_dict(data)  

    # Add points to team based on matches' result
    for match in data:
        _ = point_analysis(point_table, match)

    # Sort table base on points, alphabetically
    sorted_point_table = sort_point_table(point_table)

    # Add ranks to team base on points
    final_table = rank_table(sorted_point_table)

    print("- Transform phase Ended")

    return final_table
    

def load(data):
    '''
    Load phase: export data to the output text file
    '''
    print("- Load phase Started")

    with open('./data/generated-output.txt', 'w') as f:
        for item in data:
            name, point, rank = item

            # Decision for 'pts' or 'pt'
            pt = 'pt' if point == 1 else 'pts'

            # Forming line's content
            line = ("{}. {}, {} {}".format(rank, name, point, pt))
            f.write(line + '\n')

    print("- Load phase Ended")
    

def extract_team_info(team):
    '''
    Extract team name and score from the input information
    '''
    # Split the words to get the score and name parts
    team_name_parts = team.split()[:-1]
    team_score = team.split()[-1]
    
    # Join the name parts to get team name
    team_name = ' '.join(team_name_parts)

    return [team_name, int(team_score)]


def extract_match_info(match):
    '''
    Extract teams' names and scores from the input match
    '''
    team1, team2 = match.split(",")
    team1_name, team1_score = extract_team_info(team1)
    team2_name, team2_score = extract_team_info(team2)

    return [[team1_name, team1_score], [team2_name, team2_score]]


def create_table_dict(data):
    data_table = np.array(data)

    # Get all the teams' names appeared on the right side
    team_name = list(data_table[:, 0][:, 0])

    # Get all the teams' names appeared on the left side
    team_name_extend = list(data_table[:, 1][:, 0])

    # Join the two lists
    team_name.extend(team_name_extend)

    # Get all the unique teams' names
    team_name = set(team_name)

    # Create point table dictionary based on existing teams
    keys = team_name
    values = [0] * len(keys)
    table = dict(zip(keys, values))

    return table


def point_analysis(table_dict, match):
    '''
    Calculate points to be assigned to each team for the input match
    '''
    t1n, t1s = match[0][0], match[0][1]  # team 1 name & score 
    t2n, t2s = match[1][0], match[1][1]  # team 2 name & score 

    # Point adding conditions
    team1_win = t1s > t2s
    team2_win = t1s < t2s
    team_draw = t1s == t2s

    if team1_win:
        # if team 1 wins
        table_dict[t1n] += 3

    elif team2_win:
        # if team 2 wins
        table_dict[t2n] += 3

    elif team_draw:
        # if 2 teams draw
        table_dict[t1n] += 1
        table_dict[t2n] += 1
    else:
        pass

    return table_dict


def sort_point_table(dict):
    '''
    Sort the point table based on points (high to low), alphabetically
    '''
    table_tuple = (sorted(dict.items(), key=lambda x: (-x[1], x[0])))
    table_list = [list(item) for item in table_tuple]

    return table_list


def rank_table(table):
    '''
    Add rank to teams based on their points
    '''

    # Add rank to first team
    table[0].extend([1])

    # Add ranks to other teams
    for idx, value in enumerate(table[1:], start=1):
        if value[1] == table[idx - 1][1]:
            # if the point of the current team equal to the previous team's, assign the same rank
            table[idx].extend([table[idx - 1][2]])
        else:
            table[idx].extend([idx + 1])

    return table


def generate(input_file):
    try:
        # Extract
        matches = extract(input_file)

        # Transform
        final_table = transform(matches)

        # Load
        load(final_table)

    except ValueError as value_err:
        print("- Error: wrong data format.")

    except IndexError as index_err:
        print("- Error: wrong data format.")
    
    except FileNotFoundError as fnf_err:
        print("- Error: file not found.")

    except Exception as e:
        print("- Error: unknown error.")
    
    
