def U_listToDictionary(key_list,val_list):
    op = dict(zip(key_list,val_list))
    return op


#This is the square function will print the square of a given number.
def U_sqare(num):
    sq = num**2
    return sq


def student_Data_Function(firstname,lastname):
    Bio_data = firstname +" " + lastname
    return Bio_data


def plot_equation(m,x,c):    
    y = (m*x)+c
    return y
    
    