from py2neo import authenticate, Graph, Node, Relationship

graph = Graph()

# authenticate("localhost:7474", "neo4j", "neo4j")

alice = Node("Person", name="Alice")
bob = Node("Person", name="Bob")
alice_knows_bob = Relationship(alice, "KNOWS", bob)
graph.create(alice_knows_bob)
