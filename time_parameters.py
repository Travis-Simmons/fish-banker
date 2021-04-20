import pulp as p
import random
from functions import play_game

ships_in_deep = 0
ships_in_shallow = 0
ships_in_harbor = 0


BSTS_t1 = p.LpVariable("BSTS_t1", lowBound = 0)
BSTS_t2 = p.LpVariable("BSTS_t2", lowBound = 0)
BSTS_t3 = p.LpVariable("BSTS_t3", lowBound = 0)
BSTS_t4 = p.LpVariable("BSTS_t4", lowBound = 0)
BSTS_t5 = p.LpVariable("BSTS_t5", lowBound = 0)
BSTS_t6 = p.LpVariable("BSTS_t6", lowBound = 0)
BSTS_t7 = p.LpVariable("BSTS_t7", lowBound = 0)
BSTS_t8 = p.LpVariable("BSTS_t8", lowBound = 0)
BSTS_t9 = p.LpVariable("BSTS_t9", lowBound = 0)
BSTS_t10 = p.LpVariable("BSTS_t10", lowBound = 0)
BSTS_t11 = p.LpVariable("BSTS_t11", lowBound = 0)
BSTS_t12 = p.LpVariable("BSTS_t12", lowBound = 0)
BSTS_t13 = p.LpVariable("BSTS_t13", lowBound = 0)
BSTS_t14 = p.LpVariable("BSTS_t14", lowBound = 0)
BSTS_t15 = p.LpVariable("BSTS_t15", lowBound = 0)
BSTS_t16 = p.LpVariable("BSTS_t16", lowBound = 0)
BSTS_t17 = p.LpVariable("BSTS_t17", lowBound = 0)
BSTS_t18 = p.LpVariable("BSTS_t18", lowBound = 0)
BSTS_t19 = p.LpVariable("BSTS_t19", lowBound = 0)
BSTS_t20 = p.LpVariable("BSTS_t20", lowBound = 0)
STD_t1 = p.LpVariable("STD_t1", lowBound = 0)
STD_t2 = p.LpVariable("STD_t2", lowBound = 0)
STD_t3 = p.LpVariable("STD_t3", lowBound = 0)
STD_t4 = p.LpVariable("STD_t4", lowBound = 0)
STD_t5 = p.LpVariable("STD_t5", lowBound = 0)
STD_t6 = p.LpVariable("STD_t6", lowBound = 0)
STD_t7 = p.LpVariable("STD_t7", lowBound = 0)
STD_t8 = p.LpVariable("STD_t8", lowBound = 0)
STD_t9 = p.LpVariable("STD_t9", lowBound = 0)
STD_t10 = p.LpVariable("STD_t10", lowBound = 0)
STD_t11 = p.LpVariable("STD_t11", lowBound = 0)
STD_t12 = p.LpVariable("STD_t12", lowBound = 0)
STD_t13 = p.LpVariable("STD_t13", lowBound = 0)
STD_t14 = p.LpVariable("STD_t14", lowBound = 0)
STD_t15 = p.LpVariable("STD_t15", lowBound = 0)
STD_t16 = p.LpVariable("STD_t16", lowBound = 0)
STD_t17 = p.LpVariable("STD_t17", lowBound = 0)
STD_t18 = p.LpVariable("STD_t18", lowBound = 0)
STD_t19 = p.LpVariable("STD_t19", lowBound = 0)
STD_t20 = p.LpVariable("STD_t20", lowBound = 0)
STH_t1 = p.LpVariable("STH_t1", lowBound = 0)
STH_t2 = p.LpVariable("STH_t2", lowBound = 0)
STH_t3 = p.LpVariable("STH_t3", lowBound = 0)
STH_t4 = p.LpVariable("STH_t4", lowBound = 0)
STH_t5 = p.LpVariable("STH_t5", lowBound = 0)
STH_t6 = p.LpVariable("STH_t6", lowBound = 0)
STH_t7 = p.LpVariable("STH_t7", lowBound = 0)
STH_t8 = p.LpVariable("STH_t8", lowBound = 0)
STH_t9 = p.LpVariable("STH_t9", lowBound = 0)
STH_t10 = p.LpVariable("STH_t10", lowBound = 0)
STH_t11 = p.LpVariable("STH_t11", lowBound = 0)
STH_t12 = p.LpVariable("STH_t12", lowBound = 0)
STH_t13 = p.LpVariable("STH_t13", lowBound = 0)
STH_t14 = p.LpVariable("STH_t14", lowBound = 0)
STH_t15 = p.LpVariable("STH_t15", lowBound = 0)
STH_t16 = p.LpVariable("STH_t16", lowBound = 0)
STH_t17 = p.LpVariable("STH_t17", lowBound = 0)
STH_t18 = p.LpVariable("STH_t18", lowBound = 0)
STH_t19 = p.LpVariable("STH_t19", lowBound = 0)
STH_t20 = p.LpVariable("STH_t20", lowBound = 0)
BSTD_t1 = p.LpVariable("BSTD_t1", lowBound = 0)
BSTD_t2 = p.LpVariable("BSTD_t2", lowBound = 0)
BSTD_t3 = p.LpVariable("BSTD_t3", lowBound = 0)
BSTD_t4 = p.LpVariable("BSTD_t4", lowBound = 0)
BSTD_t5 = p.LpVariable("BSTD_t5", lowBound = 0)
BSTD_t6 = p.LpVariable("BSTD_t6", lowBound = 0)
BSTD_t7 = p.LpVariable("BSTD_t7", lowBound = 0)
BSTD_t8 = p.LpVariable("BSTD_t8", lowBound = 0)
BSTD_t9 = p.LpVariable("BSTD_t9", lowBound = 0)
BSTD_t10 = p.LpVariable("BSTD_t10", lowBound = 0)
BSTD_t11 = p.LpVariable("BSTD_t11", lowBound = 0)
BSTD_t12 = p.LpVariable("BSTD_t12", lowBound = 0)
BSTD_t13 = p.LpVariable("BSTD_t13", lowBound = 0)
BSTD_t14 = p.LpVariable("BSTD_t14", lowBound = 0)
BSTD_t15 = p.LpVariable("BSTD_t15", lowBound = 0)
BSTD_t16 = p.LpVariable("BSTD_t16", lowBound = 0)
BSTD_t17 = p.LpVariable("BSTD_t17", lowBound = 0)
BSTD_t18 = p.LpVariable("BSTD_t18", lowBound = 0)
BSTD_t19 = p.LpVariable("BSTD_t19", lowBound = 0)
BSTD_t20 = p.LpVariable("BSTD_t20", lowBound = 0)
DTS_t1 = p.LpVariable("DTS_t1", lowBound = 0)
DTS_t2 = p.LpVariable("DTS_t2", lowBound = 0)
DTS_t3 = p.LpVariable("DTS_t3", lowBound = 0)
DTS_t4 = p.LpVariable("DTS_t4", lowBound = 0)
DTS_t5 = p.LpVariable("DTS_t5", lowBound = 0)
DTS_t6 = p.LpVariable("DTS_t6", lowBound = 0)
DTS_t7 = p.LpVariable("DTS_t7", lowBound = 0)
DTS_t8 = p.LpVariable("DTS_t8", lowBound = 0)
DTS_t9 = p.LpVariable("DTS_t9", lowBound = 0)
DTS_t10 = p.LpVariable("DTS_t10", lowBound = 0)
DTS_t11 = p.LpVariable("DTS_t11", lowBound = 0)
DTS_t12 = p.LpVariable("DTS_t12", lowBound = 0)
DTS_t13 = p.LpVariable("DTS_t13", lowBound = 0)
DTS_t14 = p.LpVariable("DTS_t14", lowBound = 0)
DTS_t15 = p.LpVariable("DTS_t15", lowBound = 0)
DTS_t16 = p.LpVariable("DTS_t16", lowBound = 0)
DTS_t17 = p.LpVariable("DTS_t17", lowBound = 0)
DTS_t18 = p.LpVariable("DTS_t18", lowBound = 0)
DTS_t19 = p.LpVariable("DTS_t19", lowBound = 0)
DTS_t20 = p.LpVariable("DTS_t20", lowBound = 0)
DTH_t1 = p.LpVariable("DTH_t1", lowBound = 0)
DTH_t2 = p.LpVariable("DTH_t2", lowBound = 0)
DTH_t3 = p.LpVariable("DTH_t3", lowBound = 0)
DTH_t4 = p.LpVariable("DTH_t4", lowBound = 0)
DTH_t5 = p.LpVariable("DTH_t5", lowBound = 0)
DTH_t6 = p.LpVariable("DTH_t6", lowBound = 0)
DTH_t7 = p.LpVariable("DTH_t7", lowBound = 0)
DTH_t8 = p.LpVariable("DTH_t8", lowBound = 0)
DTH_t9 = p.LpVariable("DTH_t9", lowBound = 0)
DTH_t10 = p.LpVariable("DTH_t10", lowBound = 0)
DTH_t11 = p.LpVariable("DTH_t11", lowBound = 0)
DTH_t12 = p.LpVariable("DTH_t12", lowBound = 0)
DTH_t13 = p.LpVariable("DTH_t13", lowBound = 0)
DTH_t14 = p.LpVariable("DTH_t14", lowBound = 0)
DTH_t15 = p.LpVariable("DTH_t15", lowBound = 0)
DTH_t16 = p.LpVariable("DTH_t16", lowBound = 0)
DTH_t17 = p.LpVariable("DTH_t17", lowBound = 0)
DTH_t18 = p.LpVariable("DTH_t18", lowBound = 0)
DTH_t19 = p.LpVariable("DTH_t19", lowBound = 0)
DTH_t20 = p.LpVariable("DTH_t20", lowBound = 0)
BSTH_t1 = p.LpVariable("BSTH_t1", lowBound = 0)
BSTH_t2 = p.LpVariable("BSTH_t2", lowBound = 0)
BSTH_t3 = p.LpVariable("BSTH_t3", lowBound = 0)
BSTH_t4 = p.LpVariable("BSTH_t4", lowBound = 0)
BSTH_t5 = p.LpVariable("BSTH_t5", lowBound = 0)
BSTH_t6 = p.LpVariable("BSTH_t6", lowBound = 0)
BSTH_t7 = p.LpVariable("BSTH_t7", lowBound = 0)
BSTH_t8 = p.LpVariable("BSTH_t8", lowBound = 0)
BSTH_t9 = p.LpVariable("BSTH_t9", lowBound = 0)
BSTH_t10 = p.LpVariable("BSTH_t10", lowBound = 0)
BSTH_t11 = p.LpVariable("BSTH_t11", lowBound = 0)
BSTH_t12 = p.LpVariable("BSTH_t12", lowBound = 0)
BSTH_t13 = p.LpVariable("BSTH_t13", lowBound = 0)
BSTH_t14 = p.LpVariable("BSTH_t14", lowBound = 0)
BSTH_t15 = p.LpVariable("BSTH_t15", lowBound = 0)
BSTH_t16 = p.LpVariable("BSTH_t16", lowBound = 0)
BSTH_t17 = p.LpVariable("BSTH_t17", lowBound = 0)
BSTH_t18 = p.LpVariable("BSTH_t18", lowBound = 0)
BSTH_t19 = p.LpVariable("BSTH_t19", lowBound = 0)
BSTH_t20 = p.LpVariable("BSTH_t20", lowBound = 0)
HTS_t1 = p.LpVariable("HTS_t1", lowBound = 0)
HTS_t2 = p.LpVariable("HTS_t2", lowBound = 0)
HTS_t3 = p.LpVariable("HTS_t3", lowBound = 0)
HTS_t4 = p.LpVariable("HTS_t4", lowBound = 0)
HTS_t5 = p.LpVariable("HTS_t5", lowBound = 0)
HTS_t6 = p.LpVariable("HTS_t6", lowBound = 0)
HTS_t7 = p.LpVariable("HTS_t7", lowBound = 0)
HTS_t8 = p.LpVariable("HTS_t8", lowBound = 0)
HTS_t9 = p.LpVariable("HTS_t9", lowBound = 0)
HTS_t10 = p.LpVariable("HTS_t10", lowBound = 0)
HTS_t11 = p.LpVariable("HTS_t11", lowBound = 0)
HTS_t12 = p.LpVariable("HTS_t12", lowBound = 0)
HTS_t13 = p.LpVariable("HTS_t13", lowBound = 0)
HTS_t14 = p.LpVariable("HTS_t14", lowBound = 0)
HTS_t15 = p.LpVariable("HTS_t15", lowBound = 0)
HTS_t16 = p.LpVariable("HTS_t16", lowBound = 0)
HTS_t17 = p.LpVariable("HTS_t17", lowBound = 0)
HTS_t18 = p.LpVariable("HTS_t18", lowBound = 0)
HTS_t19 = p.LpVariable("HTS_t19", lowBound = 0)
HTS_t20 = p.LpVariable("HTS_t20", lowBound = 0)
HTD_t1 = p.LpVariable("HTD_t1", lowBound = 0)
HTD_t2 = p.LpVariable("HTD_t2", lowBound = 0)
HTD_t3 = p.LpVariable("HTD_t3", lowBound = 0)
HTD_t4 = p.LpVariable("HTD_t4", lowBound = 0)
HTD_t5 = p.LpVariable("HTD_t5", lowBound = 0)
HTD_t6 = p.LpVariable("HTD_t6", lowBound = 0)
HTD_t7 = p.LpVariable("HTD_t7", lowBound = 0)
HTD_t8 = p.LpVariable("HTD_t8", lowBound = 0)
HTD_t9 = p.LpVariable("HTD_t9", lowBound = 0)
HTD_t10 = p.LpVariable("HTD_t10", lowBound = 0)
HTD_t11 = p.LpVariable("HTD_t11", lowBound = 0)
HTD_t12 = p.LpVariable("HTD_t12", lowBound = 0)
HTD_t13 = p.LpVariable("HTD_t13", lowBound = 0)
HTD_t14 = p.LpVariable("HTD_t14", lowBound = 0)
HTD_t15 = p.LpVariable("HTD_t15", lowBound = 0)
HTD_t16 = p.LpVariable("HTD_t16", lowBound = 0)
HTD_t17 = p.LpVariable("HTD_t17", lowBound = 0)
HTD_t18 = p.LpVariable("HTD_t18", lowBound = 0)
HTD_t19 = p.LpVariable("HTD_t19", lowBound = 0)
HTD_t20 = p.LpVariable("HTD_t20", lowBound = 0)
ss_t1 = p.LpVariable("ss_t1", lowBound = 0)
ss_t2 = p.LpVariable("ss_t2", lowBound = 0)
ss_t3 = p.LpVariable("ss_t3", lowBound = 0)
ss_t4 = p.LpVariable("ss_t4", lowBound = 0)
ss_t5 = p.LpVariable("ss_t5", lowBound = 0)
ss_t6 = p.LpVariable("ss_t6", lowBound = 0)
ss_t7 = p.LpVariable("ss_t7", lowBound = 0)
ss_t8 = p.LpVariable("ss_t8", lowBound = 0)
ss_t9 = p.LpVariable("ss_t9", lowBound = 0)
ss_t10 = p.LpVariable("ss_t10", lowBound = 0)
ss_t11 = p.LpVariable("ss_t11", lowBound = 0)
ss_t12 = p.LpVariable("ss_t12", lowBound = 0)
ss_t13 = p.LpVariable("ss_t13", lowBound = 0)
ss_t14 = p.LpVariable("ss_t14", lowBound = 0)
ss_t15 = p.LpVariable("ss_t15", lowBound = 0)
ss_t16 = p.LpVariable("ss_t16", lowBound = 0)
ss_t17 = p.LpVariable("ss_t17", lowBound = 0)
ss_t18 = p.LpVariable("ss_t18", lowBound = 0)
ss_t19 = p.LpVariable("ss_t19", lowBound = 0)
ss_t20 = p.LpVariable("ss_t20", lowBound = 0)

def play_game(length_of_round):

    # build the matrix using the variable names eg: BSTS_x1, BSTS_x2...BSTS_x(length of round)
    # strategy = build_game_matrix(length_of_round)


    # Profit
    bank = 0

    # Initial Values
    shallow_population = 150
    deep_population = 300

    ships_in_deep = 0
    ships_in_shallow = 0
    ships_in_harbor = 0
    upkeep_total = 0


    # Coeficients
    upkeep_cost = 250
    ship_cost = 300
    birth_rate = 0.5
    death_rate = 0.5
    catch_value = 20
    

    # Use game rules such as money constraints and fisheries crashes
    for i in range(1,length_of_round+1):

        # Define variables in terms of turn
        parameters = ['BSTS', 'STD', 'STH', 'BSTD', 'DTS', 'DTH', 'BSTH', 'HTS', 'HTD', 'SS']

        # BSTS = variable_dict[f'BSTS_t{i}']
        # STD = variable_dict[f'STD_t{i}']
        # STH = variable_dict[f'STH_t{i}']
        # BSTD = variable_dict[f'BSTD_t{i}']
        # DTS = variable_dict[f'DTS_t{i}']
        # DTH = variable_dict[f'DTH_t{i}']
        # BSTH = variable_dict[f'BSTH_t{i}']
        # HTS = variable_dict[f'HTS_t{i}']
        # HTD = variable_dict[f'HTD_t{i}']
        # SS = variable_dict[f'ss_t{i}']


        BSTS = eval(f'BSTS_t{i}')
        STD = eval(f'STD_t{i}')
        STH = eval(f'STH_t{i}')
        BSTD = eval(f'BSTD_t{i}')
        DTS = eval(f'DTS_t{i}')
        DTH = eval(f'DTH_t{i}')
        BSTH = eval(f'BSTH_t{i}')
        HTS = eval(f'HTS_t{i}')
        HTD = eval(f'HTD_t{i}')
        SS = eval(f'ss_t{i}')
        
        # Non population or bank dependent
        expenses = ((ships_in_deep + ships_in_harbor + ships_in_shallow) * upkeep_cost)
        bank -= expenses

        if (deep_population <=0) or (shallow_population<=0):
            return bank 

        # Catch should come first
        deep_catch = random.randint(10,25)
        shallow_catch = random.randint(5,15)

        # Change population from catch
        deep_population -= deep_catch
        shallow_population -= shallow_catch

        # Add money from catch
        bank += (deep_catch + shallow_catch) * catch_value

        # Natural population change
        deep_population += deep_population*birth_rate
        deep_population -= deep_population*death_rate

        #Ship management

        ## Moving Ships
        ships_in_deep -= (DTS + DTH)
        ships_in_shallow -= (STD + STH)
        ships_in_harbor -= (HTD + HTS)

        # Ship costs
        bank -= (ships_in_deep + ships_in_harbor + ships_in_shallow) * upkeep_cost

        ## If you have enough money, buy the ships
        if bank >= ((BSTD + BSTS + BSTH)*ship_cost):
            ships_in_deep += BSTD

            ships_in_harbor += BSTS

            ships_in_shallow += BSTH


        print(bank)



    # may also want to return summary stats for the run
    return bank
 



Lp_prob = p.LpProblem('Problem', p.LpMaximize)
Lp_prob += play_game(20)
Lp_prob += STD_t1 >=  ships_in_shallow
Lp_prob += STD_t2 >=  ships_in_shallow
Lp_prob += STD_t3 >=  ships_in_shallow
Lp_prob += STD_t4 >=  ships_in_shallow
Lp_prob += STD_t5 >=  ships_in_shallow
Lp_prob += STD_t6 >=  ships_in_shallow
Lp_prob += STD_t7 >=  ships_in_shallow
Lp_prob += STD_t8 >=  ships_in_shallow
Lp_prob += STD_t9 >=  ships_in_shallow
Lp_prob += STD_t10 >=  ships_in_shallow
Lp_prob += STD_t11 >=  ships_in_shallow
Lp_prob += STD_t12 >=  ships_in_shallow
Lp_prob += STD_t13 >=  ships_in_shallow
Lp_prob += STD_t14 >=  ships_in_shallow
Lp_prob += STD_t15 >=  ships_in_shallow
Lp_prob += STD_t16 >=  ships_in_shallow
Lp_prob += STD_t17 >=  ships_in_shallow
Lp_prob += STD_t18 >=  ships_in_shallow
Lp_prob += STD_t19 >=  ships_in_shallow
Lp_prob += STD_t20 >=  ships_in_shallow
Lp_prob += STH_t1 >=  ships_in_shallow
Lp_prob += STH_t2 >=  ships_in_shallow
Lp_prob += STH_t3 >=  ships_in_shallow
Lp_prob += STH_t4 >=  ships_in_shallow
Lp_prob += STH_t5 >=  ships_in_shallow
Lp_prob += STH_t6 >=  ships_in_shallow
Lp_prob += STH_t7 >=  ships_in_shallow
Lp_prob += STH_t8 >=  ships_in_shallow
Lp_prob += STH_t9 >=  ships_in_shallow
Lp_prob += STH_t10 >=  ships_in_shallow
Lp_prob += STH_t11 >=  ships_in_shallow
Lp_prob += STH_t12 >=  ships_in_shallow
Lp_prob += STH_t13 >=  ships_in_shallow
Lp_prob += STH_t14 >=  ships_in_shallow
Lp_prob += STH_t15 >=  ships_in_shallow
Lp_prob += STH_t16 >=  ships_in_shallow
Lp_prob += STH_t17 >=  ships_in_shallow
Lp_prob += STH_t18 >=  ships_in_shallow
Lp_prob += STH_t19 >=  ships_in_shallow
Lp_prob += STH_t20 >=  ships_in_shallow
Lp_prob += DTS_t1 >=  ships_in_deep
Lp_prob += DTS_t2 >=  ships_in_deep
Lp_prob += DTS_t3 >=  ships_in_deep
Lp_prob += DTS_t4 >=  ships_in_deep
Lp_prob += DTS_t5 >=  ships_in_deep
Lp_prob += DTS_t6 >=  ships_in_deep
Lp_prob += DTS_t7 >=  ships_in_deep
Lp_prob += DTS_t8 >=  ships_in_deep
Lp_prob += DTS_t9 >=  ships_in_deep
Lp_prob += DTS_t10 >=  ships_in_deep
Lp_prob += DTS_t11 >=  ships_in_deep
Lp_prob += DTS_t12 >=  ships_in_deep
Lp_prob += DTS_t13 >=  ships_in_deep
Lp_prob += DTS_t14 >=  ships_in_deep
Lp_prob += DTS_t15 >=  ships_in_deep
Lp_prob += DTS_t16 >=  ships_in_deep
Lp_prob += DTS_t17 >=  ships_in_deep
Lp_prob += DTS_t18 >=  ships_in_deep
Lp_prob += DTS_t19 >=  ships_in_deep
Lp_prob += DTS_t20 >=  ships_in_deep
Lp_prob += DTH_t1 >=  ships_in_deep
Lp_prob += DTH_t2 >=  ships_in_deep
Lp_prob += DTH_t3 >=  ships_in_deep
Lp_prob += DTH_t4 >=  ships_in_deep
Lp_prob += DTH_t5 >=  ships_in_deep
Lp_prob += DTH_t6 >=  ships_in_deep
Lp_prob += DTH_t7 >=  ships_in_deep
Lp_prob += DTH_t8 >=  ships_in_deep
Lp_prob += DTH_t9 >=  ships_in_deep
Lp_prob += DTH_t10 >=  ships_in_deep
Lp_prob += DTH_t11 >=  ships_in_deep
Lp_prob += DTH_t12 >=  ships_in_deep
Lp_prob += DTH_t13 >=  ships_in_deep
Lp_prob += DTH_t14 >=  ships_in_deep
Lp_prob += DTH_t15 >=  ships_in_deep
Lp_prob += DTH_t16 >=  ships_in_deep
Lp_prob += DTH_t17 >=  ships_in_deep
Lp_prob += DTH_t18 >=  ships_in_deep
Lp_prob += DTH_t19 >=  ships_in_deep
Lp_prob += DTH_t20 >=  ships_in_deep
Lp_prob += HTS_t1 >=  ships_in_harbor
Lp_prob += HTS_t2 >=  ships_in_harbor
Lp_prob += HTS_t3 >=  ships_in_harbor
Lp_prob += HTS_t4 >=  ships_in_harbor
Lp_prob += HTS_t5 >=  ships_in_harbor
Lp_prob += HTS_t6 >=  ships_in_harbor
Lp_prob += HTS_t7 >=  ships_in_harbor
Lp_prob += HTS_t8 >=  ships_in_harbor
Lp_prob += HTS_t9 >=  ships_in_harbor
Lp_prob += HTS_t10 >=  ships_in_harbor
Lp_prob += HTS_t11 >=  ships_in_harbor
Lp_prob += HTS_t12 >=  ships_in_harbor
Lp_prob += HTS_t13 >=  ships_in_harbor
Lp_prob += HTS_t14 >=  ships_in_harbor
Lp_prob += HTS_t15 >=  ships_in_harbor
Lp_prob += HTS_t16 >=  ships_in_harbor
Lp_prob += HTS_t17 >=  ships_in_harbor
Lp_prob += HTS_t18 >=  ships_in_harbor
Lp_prob += HTS_t19 >=  ships_in_harbor
Lp_prob += HTS_t20 >=  ships_in_harbor
Lp_prob += HTS_t1 >=  ships_in_harbor
Lp_prob += HTS_t2 >=  ships_in_harbor
Lp_prob += HTS_t3 >=  ships_in_harbor
Lp_prob += HTS_t4 >=  ships_in_harbor
Lp_prob += HTS_t5 >=  ships_in_harbor
Lp_prob += HTS_t6 >=  ships_in_harbor
Lp_prob += HTS_t7 >=  ships_in_harbor
Lp_prob += HTS_t8 >=  ships_in_harbor
Lp_prob += HTS_t9 >=  ships_in_harbor
Lp_prob += HTS_t10 >=  ships_in_harbor
Lp_prob += HTS_t11 >=  ships_in_harbor
Lp_prob += HTS_t12 >=  ships_in_harbor
Lp_prob += HTS_t13 >=  ships_in_harbor
Lp_prob += HTS_t14 >=  ships_in_harbor
Lp_prob += HTS_t15 >=  ships_in_harbor
Lp_prob += HTS_t16 >=  ships_in_harbor
Lp_prob += HTS_t17 >=  ships_in_harbor
Lp_prob += HTS_t18 >=  ships_in_harbor
Lp_prob += HTS_t19 >=  ships_in_harbor
Lp_prob += HTS_t20 >=  ships_in_harbor
Lp_prob += SS_t1 <=  ships_in_harbor
Lp_prob += SS_t2 <=  ships_in_harbor
Lp_prob += SS_t3 <=  ships_in_harbor
Lp_prob += SS_t4 <=  ships_in_harbor
Lp_prob += SS_t5 <=  ships_in_harbor
Lp_prob += SS_t6 <=  ships_in_harbor
Lp_prob += SS_t7 <=  ships_in_harbor
Lp_prob += SS_t8 <=  ships_in_harbor
Lp_prob += SS_t9 <=  ships_in_harbor
Lp_prob += SS_t10 <=  ships_in_harbor
Lp_prob += SS_t11 <=  ships_in_harbor
Lp_prob += SS_t12 <=  ships_in_harbor
Lp_prob += SS_t13 <=  ships_in_harbor
Lp_prob += SS_t14 <=  ships_in_harbor
Lp_prob += SS_t15 <=  ships_in_harbor
Lp_prob += SS_t16 <=  ships_in_harbor
Lp_prob += SS_t17 <=  ships_in_harbor
Lp_prob += SS_t18 <=  ships_in_harbor
Lp_prob += SS_t19 <=  ships_in_harbor
Lp_prob += SS_t20 <=  ships_in_harbor
