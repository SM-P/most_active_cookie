import csv
import argparse
import datetime
def get_parser():
    parser = argparse.ArgumentParser(description="Demo of argparse")
    parser.add_argument('log_dir', type = str)
    parser.add_argument('-d', '--query_date', type = datetime.date.fromisoformat)
    return parser

def most_frequent(List):
    curr_max = 0
    ans = []
    for i in set(List):
        curr_freq = List.count(i)
        if(curr_freq > curr_max):
            curr_max = curr_freq
            ans = [i]
        elif(curr_freq == curr_max):
            ans.append(i)
    return ans 
    
if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    cookie_dict = {}
    with open(args.log_dir, 'r') as file:
        reader = csv.reader(file, delimiter=',')
        next(reader)
        for row in reader:
            row[1] = datetime.datetime.strptime(row[1].split('T')[0],"%Y-%m-%d").date()
            if row[1] not in cookie_dict:
                cookie_dict[row[1]] = [row[0]]
            else:
                cookie_dict[row[1]].append(row[0])
    date = args.query_date
    ans = most_frequent(cookie_dict[date])

    for i in ans:
        print(i)
