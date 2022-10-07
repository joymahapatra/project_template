import imp
import logging
import argparse
import json   


class cla_parsing():
    """for command line argument parsing"""
    def __init__(self):
        self.parser = argparse.ArgumentParser()

        # required (or positional) argument
        self.parser.add_argument("value", help="Want a value to print", type=int)

        # optional argument
        self.parser.add_argument("-v", "--verbose", help="Giving more details.", action="store_true")
        self.parser.add_argument("-f", "--family", help="Giving family name.", type=str, choices=["me", "you"])
        self.parser.add_argument("-n", "--number", help="enter a number", type=int, default=10)
        self.parser.add_argument("-e", "--echo", help="enter a string to echo", type=str)

        args = self.parser.parse_args()

        print("The verbose is : ", args.verbose)
        if args.verbose:
            print("The value is ", args.value)
            if args.family:
                print(args.family)
            print("the number (default 10) is ", args.number)
            if args.echo:
                print(args.echo) 


class do_logging():
    """for logging"""
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        fh = logging.FileHandler(filename=(name+".log"), mode="a+")
        sh = logging.StreamHandler()
        fmt = logging.Formatter("[%(asctime)s] [%(levelname)s] [in %(module)s at line %(lineno)s] :: %(message)s")
        fh.setFormatter(fmt)
        sh.setFormatter(fmt)

        self.logger.addHandler(fh)
        self.logger.addHandler(sh)

        self.logger.setLevel(logging.DEBUG) # DEBUG, INFO, WARNING, ERROR, CRITICAL
        self.logger.info("Start.")
        return self.logger

class read_config():
    
    def __init__(self, name):
        
        self.t_dict = json.load(open(name,"r"))
    
    def get_dict(self):
        return self.t_dict