#!/usr/bin/python
# Filename: objvar.py

class Robot:
    '''Represents a robot, with a name.'''

    #A class variable, counting the number of robots
    population = 0

    def __init__(self,name):
        '''Initializes the data.'''
        self.name = name
        print(f'(Initialize {self.name})')

        #When this person is created, the robot
        # adds to the population
        Robot.population += 1

    def __del__(self):
        '''I am del'''
        print(f'{self.name} is being destroyed!')

        Robot.population -= 1

        if Robot.population == 0:
            print(f'{self.name} was the last one.')
        else:
            print('There are still {0:d} robots working.'.format(Robot.population))

    def sayHi(self):
        '''Greeting by the robot.

        Yeah, they can do that.'''
        print(f'Greetings, my master call me {self.name}.')
        
    def howMany():
        '''Prints the current population.'''
        print('We have {0:d} robots.'.format(Robot.population))
    howMany = staticmethod(howMany)

def main():
    droid1 = Robot('R2-D2')
    droid1.sayHi()
    Robot.howMany()

    droid2 = Robot('C-3P0')
    droid2.sayHi()
    Robot.howMany()

    print("\nRobots can do some work here.\n")

    print("Robots have finished their work. So let's destroy them.")

    del droid1
    del droid2

    Robot.howMany()

if __name__ == '__main__':
    main()
else:
    print("objvar.py was imported!")




















        
