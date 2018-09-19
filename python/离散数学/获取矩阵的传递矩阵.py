# 获取矩阵的关系矩阵具体来说有如下两个步骤
# 1. 获取到矩阵本身的复合矩阵
#   因为对于最终的传递矩阵来说，一定是包含矩阵本身的复合矩阵的
# 2. 在原有矩阵的基础上加上求出来的复合矩阵
#   因为，如果一个矩阵它不是传递矩阵，那么他所欠缺的传递的部分一定会在它自身的复合矩阵中
#   因此，把这两个结果进行相加，最终的结果就是最后的矩阵的传递矩阵了
#
# 因此求传递矩阵的函数如下：

def get_transmit_matrix(matrix):
    print(matrix)
    import numpy as np
    if type(matrix) is list:
        print("type is list")
        matrix = np.array(matrix)
    elif type(matrix) is np.array:
        print("type is np.array")
        matrix = matrix
    else:
        raise RuntimeError("Not Match Type Of Param 'matrix'")
    sp = np.shape(matrix)
    print(sp)
    i_dim_1 = sp[0]
    for i_dim in sp:
        if i_dim != i_dim_1:
            raise RuntimeError("Param 'matrix' must be a Square Matrix")
    return np.where(np.dot(matrix, matrix)+matrix>=1, 1, 0)

if __name__ == "__main__":
    a = [[1, 1, 0],[0, 1, 0],[0, 0, 1]]
    print(get_transmit_matrix(a))
