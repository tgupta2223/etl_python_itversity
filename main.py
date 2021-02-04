import sys
from config import DB_DETAILS

def main(env):
    """Program takes at least 1 argument"""
    #env = sys.argv[1]
    db_details = DB_DETAILS[env]
    print(db_details)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main('dev')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
