import argparse
import pandas as pd

def parse_args():
    # setup arg parser
    parser = argparse.ArgumentParser()

    # add arguments
    parser.add_argument("--dataset", type=str)

    # parse args
    args = parser.parse_args()

    # return args
    return args

def main(args):
    df = pd.read_csv(args.dataset)

    print(df.head(10))

# run script
if __name__ == "__main__":
    # parse args
    args = parse_args()

    # run main function
    main(args)