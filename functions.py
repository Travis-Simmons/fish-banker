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