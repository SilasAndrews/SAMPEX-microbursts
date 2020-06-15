""" Main code for isolating microbursts in State 1 and State 4 """

import os
import pandas as pd
import math
from tqdm import tqdm


original_folder = os.getcwd()


def eval_state1():
    """Plan : create smaller dataframe w/ needed columns. Will need to have
        a different process for state 1 and state 4. Evaluate each row w/
        O'Brien formula."""

    data_folder = "..\DATA\State1"

    os.chdir(data_folder)

    # Isolate files with relevant data
    iterate_list = []
    for item in os.listdir():
        if item[0] == 'h':
            " Remaining fragment from download programs "
            iterate_list.append(item)

    # Analyze each file, record significant results
    with open("..\Burst Parameter\TimeResultState1.txt", "w") as generate_txt:
        generate_txt.write("Time Rate4 Avg_local_background")

    #pbar1 = tqdm(total=len(iterate_list))

    """ tqdm not compatible with IDLE yet """

    with open("..\Burst Parameter\TimeResultState1.txt", "a") as result:

        for item in iterate_list:

            data_set = pd.read_table(item, sep=' ', header=0)

            for i in range(2, len(data_set) - 3):
                # OBrein
                N100 = data_set["Rate4"][i]
                mini_frame = data_set[i - 2:i + 3]
                A500 = mini_frame["Rate4"].mean()

                """ be sure to include the date as well, otherwise the times
                will just overlap """

                OBrien = (N100 - A500) / math.sqrt(100 + A500)

                if OBrien > 10:
                    time_stamp = item[4:-4] + "_" + str(data_set["Time"][i])
                    background = (int(data_set["Rate4"][i - 2]) + int(data_set["Rate4"][i - 1]) +
                                  int(data_set["Rate4"][i + 1]) + int(data_set["Rate4"][i + 2])) / 4
                    result.write('\n' + time_stamp + " " + str(data_set["Rate4"][i])
                                 + " " + str(background))

            #pbar1.update(1)
            print("Evaluated", item)
        #pbar1.close()
    os.chdir(original_folder)


def eval_state4():

    data_folder = "..\DATA\State4"
    os.chdir(data_folder)

    # Isolate files with relevant data
    iterate_list = []
    for item in os.listdir():
        if item[0] == 'h':
            iterate_list.append(item)

    # Analyze each file, record significant results
    with open("..\Burst Parameter\TimeResultState4.txt", "w") as generate_txt:
        generate_txt.write("Time Rate5 Avg_local_background")

    with open("..\Burst Parameter\TimeResultState4.txt", "a") as result:
        #pbar4 = tqdm(total=len(iterate_list))

        """ tqdm not compatible with IDLE yet """

        for item in iterate_list:

            data_set = pd.read_table(item, sep='\\s+', header=0)

            for i in range(2, len(data_set)-3):     # 2, len(data_set)-3
                # OBrein
                N100 = data_set["Rate5"][i]
                mini_frame = data_set[i - 2:i + 3]
                A500 = mini_frame["Rate5"].mean()

                """ be sure to include the date as well, otherwise the times
                will just overlap """

                OBrien = (N100 - A500) / math.sqrt(100 + A500)

                if OBrien > 10:
                    time_stamp = item[4:-4] + "_" + str(data_set["Time"][i])
                    background = (int(data_set["Rate5"][i - 2]) + int(data_set["Rate5"][i - 1]) +
                                  int(data_set["Rate5"][i + 1]) + int(data_set["Rate5"][i + 2])) / 4
                    result.write('\n' + time_stamp + " " + str(data_set["Rate5"][i])
                                 + " " + str(background))
                # pbar4.update(1)
            print("Evaluated", item)   # Remember to fix this line later
        # pbar4.close()
    os.chdir(original_folder)


eval_state4()


print("End of program.")

