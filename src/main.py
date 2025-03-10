import cmd
import os
import runpy
import inquirer
class MyCLI(cmd.Cmd):
    intro = 'Welcome to Fuefex. Type help or ? to list commands. '
    print("| __|  _ _ _ / _|_____ __  ___  | __|_ _| |_ __ _| |")
    print("| _| || | '_|  _/ -_) \ / |___| | _/ _` |  _/ _` | |")
    print("|_| \_,_|_| |_| \___/_\_\       |_|\__,_|\__\__,_|_|")
    prompt = '(Furfex...) '

    def do_modules(self, target):
      #Options = ("{options1}{{1}}, {options1}")
      #run = input("What Modules do you want to run",)
      response = ''
      while response not in {"yes", "no"}:
         print("Oki :3 Will shart running")
         response = input().lower()
      return response == "yes" ==runpy.run_module("modules hash.py") or  "no" ==print("n")
           


    
        
    #print("2")
    #print("Oki :3 Will shart running")  
     
    
    def do_info(self, line):
      print("Furfex{1}")
      runpy.run_module("info")

    def do_exit(self, line):
        print("Exiting...")
        return True
print
if __name__ == '__main__':
    MyCLI().cmdloop()
