import csv
import pandas
import argparse

def print_file_content(file):
    print(open(file).read())

def write_list_to_file(output_file, lst):
    with open(output_file, 'w') as f:
        for item in lst:
            f.write("%s\n" % item)
        #rewritten
        #print(len(f))

def read_csv(input_file):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


if __name__ == '__main__':
    parser=argparse.ArgumentParser(
        description='''HOW TO USE: Exercise1.py --path --file  ''')
    parser.add_argument('--path', help='path to csv')
    parser.add_argument('--file', help='file to output')
    args=parser.parse_args()
    write_list_to_file(args.path, args.file)
    print(args.path)
    #print(args)
    #contentList = ['Column1', 'Column2', 'Column3']
    #write_list_to_file('ex1Fileoutput', contentList)
    #print_file_content('ex1Fileoutput')
    #read_csv('ex1.csv') """





    


#def read_csv(input_file):
#    print('hi')

