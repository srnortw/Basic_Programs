def sort_funct(row_vector):

    mylist1=[]

    for index in range(len(row_vector)):
        mylist1.append(max(row_vector))
        row_vector.pop(row_vector.index(max(row_vector)))

    row_vector=mylist1

    return row_vector

#This row vector has to be list
row_vector=[9,5,7,.2,9.5,45,17]
row_vector=sort_funct(row_vector)
