from bs4 import BeautifulSoup
import requests
import sys
import subprocess
import os
from colorama import Fore

contest_name = sys.argv[1]

url = 'https://codeforces.com/contest/'
url += contest_name

def download_testcases(url):

    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml') # print(soup)

    # testcases_data = soup.find('div', {'class':'sample-tests'})
    testcases_data = soup.find_all('pre')

    arr = []
    for element in range(len(testcases_data)):
        arr += testcases_data[element]

    final = []
    for i in arr:
        final.append(i)

    no_of_testcases = len(final) // 2

    # for tc in range(len(final)):
    #     print(final[tc])

    # initialising URL as elements into an array list
    pb_arr = []
    for i in url:
        pb_arr.append(i)
    # print(pb_arr)

    pb_char = pb_arr[len(pb_arr) - 1] # initialising character
    if pb_char == '1' or pb_char == '2':
        pb_char = pb_arr[len(pb_arr) - 2] + pb_arr[len(pb_arr) - 1]

    print("Testcases found for problem", pb_char + ": " + f'{Fore.GREEN}',str(no_of_testcases), f'{Fore.WHITE}')
    print()


    CF_Path = "/Users/abhijayrajvansh/Desktop/codeforces/" + contest_name

    try : 
        os.mkdir(CF_Path)
    except FileExistsError:
        print(end="")

    curr_prob_path = CF_Path + '/' + pb_char

    print("Problem Path:" + curr_prob_path)
    print()
    try : 
        os.mkdir(curr_prob_path)
    except FileExistsError:
        print(end="")

    if no_of_testcases == 1:
        sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
        sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")
        
        #solution file:-
        solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
        solution_file = open(solution_file_path, "w")
        # subprocess.run(["code", solution_file_path])

        array_file = [sample_input_1, sample_output_1]

    if no_of_testcases == 2:
        sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
        sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")
        sample_input_2 = open(curr_prob_path + "/sample_input_2.txt", "w")
        sample_output_2 = open(curr_prob_path + "/sample_output_2.txt", "w")

        #solution file:-
        solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
        solution_file = open(solution_file_path, "w")
        # subprocess.run(["code", solution_file_path])

        array_file = [sample_input_1, sample_output_1, sample_input_2, sample_output_2]


    if no_of_testcases == 3:
        sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
        sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")
        sample_input_2 = open(curr_prob_path + "/sample_input_2.txt", "w")
        sample_output_2 = open(curr_prob_path + "/sample_output_2.txt", "w")
        sample_input_3 = open(curr_prob_path + "/sample_input_3.txt", "w")
        sample_output_3 = open(curr_prob_path + "/sample_output_3.txt", "w")

        #solution file:-
        solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
        solution_file = open(solution_file_path, "w")
        # subprocess.run(["code", solution_file_path])

        array_file = [sample_input_1, sample_output_1, sample_input_2, sample_output_2, sample_input_3, sample_output_3]

    if no_of_testcases == 3:
        sample_input_1 = open(curr_prob_path + "/sample_input_1.txt", "w")
        sample_output_1 = open(curr_prob_path + "/sample_output_1.txt", "w")
        sample_input_2 = open(curr_prob_path + "/sample_input_2.txt", "w")
        sample_output_2 = open(curr_prob_path + "/sample_output_2.txt", "w")
        sample_input_3 = open(curr_prob_path + "/sample_input_3.txt", "w")
        sample_output_3 = open(curr_prob_path + "/sample_output_3.txt", "w")
        sample_input_4 = open(curr_prob_path + "/sample_input_4.txt", "w")
        sample_output_4 = open(curr_prob_path + "/sample_output_4.txt", "w")

        #solution file:-
        solution_file_path = curr_prob_path + "/" + pb_char + ".cpp"
        solution_file = open(solution_file_path, "w")
        # subprocess.run(["code", solution_file_path])

        array_file = [sample_input_1, sample_output_1, sample_input_2, sample_output_2, sample_input_3, sample_output_3, sample_input_4, sample_output_4]

    n = len(final)
    for all_tc in range(n):

        temp_tc = final[all_tc];
        counter = 0
        final_tc = ""

        for i in temp_tc:
            if i == '\n' and counter == 0:
                counter += 1
            else:
                final_tc += i
        
        final[all_tc] = final_tc

    for i in range(n):
        array_file[i].write(final[i])

def checkurl(check):
     
    try:
       
        response = requests.head(check)
         
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.ConnectionError as e:
        return e
 

def problem(problem_name):
    current_problem_url = url + "/problem/" + problem_name
    
    # print("Checking Problem Link: ", current_problem_url)

    if checkurl(current_problem_url) == True:
        download_testcases(current_problem_url)


all_problems_set = ['A', 'A1', 'A2', 'B', 'B1', 'B2', 'C', 'C1', 'C2', 'D', 'D1', 'D2', 'E', 'E1', 'E2', 'F', 'F1', 'F2','G', 'G1' ,'G2', 'H', 'H1', 'H2']

for i in all_problems_set:
    problem(i)



