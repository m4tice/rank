import numpy as np
import timeit


# Test made
def extract(input_file):
    print("Extract phase Started")
    data = []
    with open(input_file) as f:
        lines = f.readlines()
        for line in lines:
            match = extract_match_info(line)
            data.append(match)

    print("Extract phase Ended")
    return data


# Test made
def transform(data):
    print("Transform phase Started")
    point_table = create_table_dict(data)

    for match in data:
        _ = point_analysis(point_table, match)

    sorted_point_table = sort_point_table(point_table)
    final_table = rank_table(sorted_point_table)
    print("Transform phase Ended")

    return final_table


def load(data):
    print("Load phase Started")
    with open('./data/sample-output.txt', 'w') as f:
        for item in data:
            name, point, rank = item
            pt = 'pt' if point == 1 else 'pts'
            line = ("{}. {}, {} {}".format(rank, name, point, pt))
            f.write(line + '\n')

    print("Load phase Ended")
    

# Test made
def extract_team_info(team):
    team_name_parts, team_score = team.split()[:-1], team.split()[-1]
    team_name = ' '.join(team_name_parts)
    return [team_name, int(team_score)]


# Test made
def extract_match_info(match):
    team1, team2 = match.split(",")
    team1_name, team1_score = extract_team_info(team1)
    team2_name, team2_score = extract_team_info(team2)

    return [[team1_name, team1_score], [team2_name, team2_score]]


# Test made
def create_table_dict(data):
    data_table = np.array(data)
    team_name = list(data_table[:, 0][:, 0])
    team_name_extend = list(data_table[:, 1][:, 0])
    team_name.extend(team_name_extend)
    team_name = set(team_name)

    keys = team_name
    values = [0] * len(keys)
    table = dict(zip(keys, values))

    return table


# Test made
def point_analysis(table_dict, match):
    t1n, t1s = match[0][0], match[0][1]
    t2n, t2s = match[1][0], match[1][1]

    # Point adding conditions
    team1_win = t1s > t2s
    team2_win = t1s < t2s
    team_draw = t1s == t2s

    if team1_win:
        table_dict[t1n] += 3
    elif team2_win:
        table_dict[t2n] += 3
    elif team_draw:
        table_dict[t1n] += 1
        table_dict[t2n] += 1
    else:
        pass

    return table_dict


# Test made
def sort_point_table(dict):
    table_tuple = (sorted(dict.items(), key=lambda x: (-x[1], x[0])))
    table_list = [list(item) for item in table_tuple]

    return table_list


# Test made
def rank_table(table):
    table[0].extend([1])

    for idx, value in enumerate(table[1:], start=1):
        if value[1] == table[idx - 1][1]:
            table[idx].extend([table[idx - 1][2]])
        else:
            table[idx].extend([idx + 1])

    return table


def generate(input_file):
    matches = extract(input_file)
    final_table = transform(matches)
    load(final_table)

    print("-- RESULT -----------------------------------------")
    for item in final_table:
        name, point, rank = item
        pt = 'pt' if point == 1 else 'pts'
        print("{}. {}, {} {}".format(rank, name, point, pt))
