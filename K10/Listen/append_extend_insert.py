#how to increase the number of items in a 

animals = ['Dog', 'Cat', 'Pig', 'Rat', 'Tiger', 'Lion', 'Snake', 'Worm']
animals.append('Eagle')                 #Adds the item at the end of the list.
animals.append('Hawk')
animals.extend(["Frog", "Spider"])      # Extend the list using another list.([Double brackets are needed])
animals.insert(3, 'Ant')                # After the 3rd Item, insert Ant
                                        # The First 1st item in a list is always counted as 0. Eg. the item in the 3rd spot is 2nd in the list.

  for i in animals:
    print (i)  # prints each item in the list one after the other.

print (animals) # prints the complete list together
