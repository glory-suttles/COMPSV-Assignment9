class Person:
    def __init__(self,name):
        self.name = name
        self.friends = []
        self.friend_count = 0
    def add_friend(self, friend):
        if friend not in self.friends:
           self.friends.append(friend)

class SocialNetwork:
    def __init__(self):
        self.people = {}
    def add_person(self,name):
        if name not in self.people:
            self.people [name] = Person(name)
    def add_friendship(self, person1_name, person2_name):
        missing = []
        if person1_name not in self.people:
            missing.append(person1_name)
        if person2_name not in self.people:
            missing.append(person2_name)
        if missing: 
            print(f"{', '.join(missing)} does not exist!")
            return
        person1 = self.people[person1_name]
        person2= self.people[person2_name]
        person1.add_friend(person2)
        person2.add_friend(person1)
        

    def print_network(self):
        for name, people in self.people.items():
            friends_name = [friend.name for friend in people.friends]
            print(f"{name} is friends with: {', '.join(friends_name) if friends_name else 'None'}")


    
network = SocialNetwork()


network.add_person("Barbie")
network.add_person("Ken") 
network.add_person("Raquel")
network.add_person("Skipper")
network.add_person("Chelsea")
network.add_person("Summer")


network.add_friendship("Barbie", "Ken")
network.add_friendship("Chelsea", "Skipper")
network.add_friendship("Summer", "Barbie")
network.add_friendship("Skipper", "Ken") 
network.add_friendship("Barbie", "Raquel")
network.add_friendship("Summer", "Barbie")
network.add_friendship("Skipper", "Summer")
network.add_friendship("Ken", "Chelsea")
network.add_friendship("Barbie", "Nickie")
network.add_friendship("Raquel", "Skipper")

network.print_network()


"""
Why is a graph the right structure to represent a social network?
A graph is the right structure to represent a social network because a graph is able to create complex relationships that are interconnected 
in ways that Trees or List are not able to do . A graph can create bidirectional relationships and allows for more flexibility in the 
relationships that are present. For a social network people have a number of different friends and with that these friendships are able to show 
for each individual, creating bidirectional relationships. 
Why wouldn't a list or tree work as well for this?
A tree creates a root to the entire relationship and while some connections do not interconnect they all go back to the same root. A graph is
able to create some separation between relationships and they do not have to be connected with a root. With a list it creates all of the 
relationships in a sequence and that limits the ability for there to be complex relationships. The code can get to be very long, and can become
a lot more time consuming, and messy with lists so that is where a graph is able to come into play. 
What performance or structural trade-offs did you notice when adding friends or printing the network?
When adding friends it can create a long code of instructions that is like a run-on sentence. This takes up a lot of time and space in the code 
and isn't as complex as it could be. When printing the network while it is fairly organized, the overall structure of the output seems a bit 
clustered and sometimes hard to read. As a result of there being a lot of separate networks it displays a lot of information solely because of 
this and then comes the relationships which expands even more and add more data that's being displayed. 



"""
