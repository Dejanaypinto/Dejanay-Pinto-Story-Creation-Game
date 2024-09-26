#Author: Dejanay Pinto
# Date: March 1, 2024
#Purpose: Vertex class to create a story

class Vertex:
    def __init__(self, vertex_name, text):
        self.vertex_name= vertex_name
        self.adjacent_vertices= []
        self.text= text
