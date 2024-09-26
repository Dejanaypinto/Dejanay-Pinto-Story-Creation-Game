#Author: Dejanay Pinto
#Date: March 1, 2024
#Purpose: Code to play game and create a story

from vertex import Vertex
def parse_line(line):
    section_split = line.split("|")
    vertex_name = section_split[0].strip()

    adjacent_vertices = section_split[1].strip().split(",")

    # add all except empty strings
    adjacent = []
    for a in adjacent_vertices:
        if a:
            adjacent.append(a.strip())

    text = section_split[2].strip()

    return vertex_name, adjacent, text


def load_story(filename):

    vertex_dict = {}

    # Read the lines in the file into a list of lines:
    file = open(filename, "r")

    for l in file:

        # if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)

            # print("vertex " + vertex_name)
            # print(" adjacent:  " + str(adjacent_vertices))
            # print(" text:  " + text)

        # YOU WRITE THIS PART
        # create a graph vertex here and add it to the dictionary
        v_obj = Vertex(vertex_name,text)
        vertex_dict[vertex_name] = v_obj  #value is object address
    file.close()

    #creating adjacent vertices list with addresses
    file = open(filename, "r")
    for l in file:

        # checks if this is a line in the correct format:
        if len(l.split("|")) == 3:
            vertex_name, adjacent_vertices, text = parse_line(l)
            story_obj= vertex_dict[vertex_name]

            # creating a list of addresses/references
            adj_list = []
            for name in adjacent_vertices:
                vertex_obj = vertex_dict[name]
                adj_list.append(vertex_obj)

            # updating obj vertices to adresses
            story_obj.adjacent_vertices= adj_list


    file.close()

    return vertex_dict

#function to play game
def game(vertices):

    #starts game at the start key
    current_vertex = vertices["START"]
    print(current_vertex.text)

    #loops as long as the current_vertex has adjacent vertices
    while current_vertex.adjacent_vertices:

        #recieves choice from user
        choice = input("Enter your choice (a, b, c): ").strip().lower()
        #convert the choice to an index (a->0, b->1, c->2, ...)
        choice_index = ord(choice) - ord('a')

        #checks if user input is valid and updates current vertex
        if 0 <= choice_index < len(current_vertex.adjacent_vertices):
            current_vertex = current_vertex.adjacent_vertices[choice_index]
        else:
            print("Invalid option. Lets go again!.")

        print(current_vertex.text)

    print("End of the story. Thanks for playing!")

story_dict = load_story("story")
game(story_dict)