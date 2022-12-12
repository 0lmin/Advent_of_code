# Import deepcopy
from copy import deepcopy

# Set file to use as input
filename: str = 'input.txt'

# Set the number of step to compute for part 1 and 2
nb_step_p1: int = 20
nb_step_p2: int = 10_000

# Create a class to represent monkey
class Monkey:
    
    def __init__(self, monkey_definition: 'list(str)') -> None:
        """ 
        @Description:
            Constructor of the Monkey class.

        @Input:
            monkey_definition: list(str) = Full description of the monkey that
                                           will be parse to create its behavior

        @Output:
            None
        """
        
        # Initialize number of observations
        self.nb_observations: int = 0
        
        # Initialize objects list if the monkey doesn't have any
        self.objects_list: 'list(int)' = []
        
        # Get monkey number
        self.number: int = int(monkey_definition[0].split(' ')[-1].replace(':', ''))
        
        # Iterate through all lines of the monkey definition
        for iterate_line, line in enumerate(monkey_definition):
            
            match line.split(': '):                    
                case ["  Starting items", values]: # Get the starting list of items the moneys have
                    
                    # Populate object list
                    self.objects_list = list(map(int, values.split(', ')))
                    
                case ["  Operation", operation]: # Get operation on the worry level
                    
                    # Create worry level update function
                    self.update_worry_level: 'function' = lambda old: eval(operation.replace("new = ", ""))
        
                case ["  Test", condition]: # Get throwing condition
                    
                    # Get division condition
                    self.division_condition: int = int(condition.replace("divisible by ", ""))
                    
                    # Get list of monkey that can receive items
                    self.monkey_target_list: 'list(int)' = [int(monkey_definition[iterate_line + 1].split(' ')[-1]),
                                                            int(monkey_definition[iterate_line + 2].split(' ')[-1])]
                    
                    # Get monkey true and monkey false
                    if "true" in monkey_definition[iterate_line + 1]:
                        monkey_true: int = self.monkey_target_list[0]
                        monkey_false: int = self.monkey_target_list[1]
                    else:
                        monkey_false: int = self.monkey_target_list[1]
                        monkey_true: int = self.monkey_target_list[0]
                    
                    # Create function returning the monkey to which throwing the item
                    self.get_target_monkey: 'function' = lambda value: monkey_true if ((value % self.division_condition) == 0) else monkey_false
                
                case _: # Default
                    pass

    def update_objects_list(self, added_object: 'list(int)') -> None:
        """ 
        @Description:
            Public method to update the object list of the monkey instance

        @Input:
            added_object: list(int) = List of object to add

        @Output:
            None
        """
        
        # Update object list
        self.objects_list.extend(added_object)

    def run_round_once_p1(self) -> dict:
        """ 
        @Description:
            Public method that observe all the object the items possess and return
            a dictionary to update other monkeys for part 1.

        @Input:
            None

        @Output:
            targeted_monkey_dict: dict = Dictionary representing the thrown object to update
                                         the other monkeys.
        """
        
        # Initialize the dictionary to update the other monkey
        targeted_monkey_dict: dict = {key: [] for key in self.monkey_target_list}
        
        # Iterate through the object list
        for item in self.objects_list:
            
            # Update number of observation
            self.nb_observations += 1
            
            # Compute it's new worry level
            worry_level = self.update_worry_level(item) // 3
            
            # Get monkey to which the item is thrown and update dictionary
            targeted_monkey_dict[self.get_target_monkey(worry_level)].append(worry_level)
        
        # Empty the object list after thrown
        self.objects_list = []
        
        return targeted_monkey_dict

    def run_round_once_p2(self, ring_size: int) -> dict:
        """ 
        @Description:
            Public method that observe all the object the items possess and return
            a dictionary to update other monkeys for part 2

        @Input:
            ring_size: int = Size of the mathematical ring on which all computation are made

        @Output:
            targeted_monkey_dict: dict = Dictionary representing the thrown object to update
                                         the other monkeys.
        """
        
        # Initialize the dictionary to update the other monkey
        targeted_monkey_dict: dict = {key: [] for key in self.monkey_target_list}
        
        # Iterate through the object list
        for item in self.objects_list:
            
            # Update number of observation
            self.nb_observations += 1
            
            # Compute it's new worry level
            worry_level = self.update_worry_level(item) % ring_size
            
            # Get monkey to which the item is thrown and update dictionary
            targeted_monkey_dict[self.get_target_monkey(worry_level)].append(worry_level)
        
        # Empty the object list after thrown
        self.objects_list = []
        
        return targeted_monkey_dict

    def get_target_monkey(self, value: 'int') -> int:
        """ 
        @Description:
            Public method returning the number of the monkey to which the items will be thrown.
            This method will be declared in the init function

        @Input:
            value: int = Value to check to decide the monkey number to return

        @Output:
            _: int = Monkey number to which the item is thrown
        """
        pass
    
    def update_worry_level(self, old: 'int') -> int:
        """ 
        @Description:
            Public method returning the updated worry level of the given object
            This method will be declared in the init function.

        @Input:
            old: int = Worry level of the current object that will be updated

        @Output:
            _: int = Updated worry level of the object
        """
        pass

# Get file content
with open(filename) as f:
    lines_list: 'list(str)' = [line.rstrip() for line in f]
    
    # Initialize results sum
    result_p1: int = 0
    result_p2: int = 0
                       
    # Create all monkey and add it in a specific list
    monkeys_list: 'list(Monkey)' = []    
    
    # Initialize monkey definition start
    definition_start: int = 0
    
    # Iterate through all lines
    for iterate_line, line in enumerate(lines_list):
        if line == '':
            
            # Create and add current Monkey in the list
            monkeys_list.append(Monkey(monkey_definition = lines_list[definition_start: iterate_line]))
            
            # Update definition start index
            definition_start = iterate_line + 1
            
    # Create last monkey and add it to the list
    monkeys_list.append(Monkey(monkey_definition = lines_list[definition_start:]))
    
    # Store initial monkey list
    monkeys_list_start: 'list(Monkey)' = deepcopy(monkeys_list)
    
    # Part 1
    # Step nb_step times monkey round (for each monkey)
    for _ in range(nb_step_p1):
        for monkey in monkeys_list:
            
            # Run one round for current monkey and get update dictionary
            update_dictionary: dict = monkey.run_round_once_p1()
            
            # Update object list for each target monkey
            for key, item in update_dictionary.items():
                monkeys_list[key].update_objects_list(item)

    # Compute number of observation after nb_step steps for each monkeys
    nb_observations_list = sorted([monkey.nb_observations for monkey in monkeys_list])
                            
    # Compute monkey business
    result_p1 = nb_observations_list[-1] * nb_observations_list[-2]
        
    # Part 2
    # Reset monkey list
    monkeys_list = deepcopy(monkeys_list_start)
    
    # Compute ring size
    ring_size: int = 1
    [ring_size := ring_size * monkey.division_condition for monkey in monkeys_list]
    
    # Step nb_step times monkey round (for each monkey)
    for _ in range(nb_step_p2):
        for monkey in monkeys_list:
            
            # Run one round for current monkey and get update dictionary
            update_dictionary: dict = monkey.run_round_once_p2(ring_size = ring_size)
            
            # Update object list for each target monkey
            for key, item in update_dictionary.items():
                monkeys_list[key].update_objects_list(item)

    # Compute number of observation after nb_step steps for each monkeys
    nb_observations_list = sorted([monkey.nb_observations for monkey in monkeys_list])
                            
    # Compute monkey business
    result_p2 = nb_observations_list[-1] * nb_observations_list[-2]
        
# Print results
print(f"{result_p1 = }")
print(f"{result_p2 = }")