import sys

class Shape():
    def __init__(self):
        self.shapes = ['square','rectangle','triangle','circle']

def main():
    print("--------WELCOME TO AREA CALCULATOR--------")
    print("\nSelect one of the following shapes to begin:")

    pos = 1 #variable to indicate position of iterated values in Shape list
    for s in shape.shapes: # loop through Shape list
        
        print(pos,".", s.capitalize()) #print out the shapes in the Shape list and capitalize each word
        pos += 1 

    choice = input("Enter choice: ")
    if choice == '1':
        square()
    elif choice == '2':
        rectangle()
    elif choice == '3':
        triangle()
    elif choice == '4':
        circle()
    elif choice in ['q', 'Q']:
        end()
    else:
        print("I didn\'t understand that choice")

def square(): #function to calculate area of square
    print("\n=======================================")
    print("----------------SQUARE-----------------")
    print("=======================================")
    try:
        side = int(input("\nEnter length of side of square: ")) #square has 4 equal sides
    except ValueError:
        print("I didn\'t understand that.")
    area_of_square = side**2 #you are familiar with this
    print("Area of square = ",area_of_square)

def rectangle(): #function to calculate area of rectangle
    print("\n======================================")
    print("--------------RECTANGLE---------------")
    print("======================================")
    try:
        length = int(input("\nEnter length of rectangle: ")) #A rectangle has 2 lengths.....
        width = int(input("\nEnter width of rectangle: ")) #....and two heights. Only one of each is used
    except ValueError:
        print("I didn\'t understand that.")

    area_of_rectangle = length * width #feel old yet?
    print("Area of rectangle = ",area_of_rectangle)

def triangle(): #function to calculate area of triangle
    print("\n=======================================")
    print("---------------TRIANGLE----------------")
    print("=======================================")
    try:
        base = int(input("\nEnter length of base of triangle: ")) #Area of triangle is given by a half of base....
        height = int(input("\nEnter height of rectangle: ")) #.....multiplied by the triangle's height           
    except ValueError:
        print("I didn\'t understand that.")

    area_of_triangle = (base * height) / 2
    print("Area of triangle = ",area_of_triangle)

def circle(): #function to calculate area of circle
    print("\n=======================================")
    print("----------------CIRCLE-----------------")
    print("=======================================")
    try:
        radius = int(input("\nEnter length of radius of circle: ")) #area of circle is given by pie mulitplied to the radius exponent 2                   
    except ValueError:
        print("I didn\'t understand that.")                     
    
    area_of_circle = 3.147 * (radius**2)
    print("Area of circle = ",area_of_circle)

def end(): #end function
    print("\n========================================")
    print("----------------GOODBYE!----------------")
    print("========================================")
    print("-----THANKS FOR USING THIS PROGRAM-----")
    print("-----------By Chris Wachira------------")
    sys.exit()











if __name__ == "__main__":
    shape = Shape()
    main()





    
