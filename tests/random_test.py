import unittest
import rank.helper as h


input_1 = [['Astralis', 2], ['Ninjas in Pyjamas', 1]]
input_2 = [['Navi', 2], ['G2 Esports', 0]]
input_3 = [['G2 Esports', 2], ['Vitality', 1]]
input_4 = [['Ninjas in Pyjamas', 1], ['Vitality', 1]]
input_5 = [['Astralis', 1], ['Navi', 1]]
input_6 = [['Vitality', 2], ['Astralis', 0]]

dict_1 = {'Astralis': 0, 'Navi': 0, 'G2 Esports': 0, 'Ninjas in Pyjamas': 0, 'Vitality': 0}
dict_2 = {'Astralis': 3, 'Navi': 6, 'G2 Esports': 5, 'Ninjas in Pyjamas': 4, 'Vitality': 1}

expected_1 = {'Astralis': 3, 'Navi': 0, 'G2 Esports': 0, 'Ninjas in Pyjamas': 0, 'Vitality': 0}
expected_2 = {'Astralis': 0, 'Navi': 3, 'G2 Esports': 0, 'Ninjas in Pyjamas': 0, 'Vitality': 0}
expected_3 = {'Astralis': 0, 'Navi': 0, 'G2 Esports': 3, 'Ninjas in Pyjamas': 0, 'Vitality': 0}
expected_4 = {'Astralis': 3, 'Navi': 6, 'G2 Esports': 5, 'Ninjas in Pyjamas': 5, 'Vitality': 2}
expected_5 = {'Astralis': 4, 'Navi': 7, 'G2 Esports': 5, 'Ninjas in Pyjamas': 4, 'Vitality': 1}
expected_6 = {'Astralis': 3, 'Navi': 6, 'G2 Esports': 5, 'Ninjas in Pyjamas': 4, 'Vitality': 3}


result = h.point_analysis(dict_1, input_1)
print(result)
print(expected_1)