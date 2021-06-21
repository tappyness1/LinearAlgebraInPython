def addition(left, right):
    """accepts two list of list

    Parameters
    ----------
    left : [type]
        [description]
    right : [type]
        [description]
    """
    pass

def mult(left, right):
    """accepts two list of list
    prints row wise results

    Parameters
    ----------
    left : [type]
        [description]
    right : [type]
        [description]
    """
    assert len(left) == len(right[0]), "Number of rows for left must equals number of elements of all rows in right"
    mat = [[0 for i in range(len(left))] for j in range(len(right[0]))]

    length = len(left)
    for idx, row in enumerate(left):        
        for jdx, column in enumerate(right[0]):
            sum_product = 0
            for kdx, elem in enumerate(left[idx]):
                sum_product += elem * right[kdx][jdx]
                
            # print (sum_product)
            mat[idx][jdx] = sum_product
    return (mat)

if __name__=='__main__':
    left = [[1,2,3],
            [2,3,4],
            [1,1,1]]

    right = [[4,5,6],
            [7,8,9],
            [4,5,7]]

    res = mult(left, right)

    A =     [[1,1,0],
            [1,1,0],
            [0,0,1]]

    res = mult(A, A)
    for i in range(98):
        res = mult(res, A)
    print (res)

    A =     [[-2,-9],
            [1,4]]

    res = mult(A, A)
    for i in range(998):
        res = mult(res, A)
    print (res)