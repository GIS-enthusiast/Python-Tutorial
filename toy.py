class Toy():
    def __init__(self, colour, age):
        self.colour = colour
        self.age = age
        self.my_dict = {
            'name':'Yoyo',
            'has_pets': False
        }

    def __call__(self): # __call__ allows you to call an object, action_figure in this case. 
        print('you called??')

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)

print(action_figure['name'])