import argparse


#Передача параметров
def parse_arguments():
    parser = argparse.ArgumentParser(description='Covert channel emulation', formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-f', '--filename', help='data to tranfer via covert channel', required=True, dest='filename', type=str, default='test')
    return parser.parse_args()

def main():
    args = parse_arguments()
    fname = args.filename


if __name__ == "__main__": main()