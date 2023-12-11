"""
二叉排序树:
    1. 左子树节点值 < 根结点节点值 < 右子树结点值
    2. 在二叉排序树中不允许存在两个结点key相同的情况
    3. 中序遍历得到一个递增序列
"""


class BSTNode:
    def __init__(self, key, LChild, RChild):
        self.key = key
        self.LChild = LChild
        self.RChild = RChild


# 普通形式
def bst_search_A(T, key):
    while T is not None and key != T.key:
        if key < T.key:
            T = T.LChild
        else:
            T = T.RChild

    return T


# 递归形式查询
def bst_search_B(T, key):
    # 空结点查找失败
    if T is None:
        return None
    # 找到就返回
    if T.key == key:
        return T
    # 当前结点的key小于要查找的key, 到当前结点的右子树查找
    if T.key < key:
        bst_search_B(T.RChild, key)
    # 当前结点的key大于要查找的key, 到当前结点的左子树查找
    if T.key > key:
        bst_search_B(T.LChild, key)


# 二叉排序树插入操作
def BST_Insert(T, k):
    if T is None:
        # 创建一个新结点
        NT = BSTNode(k, None, None)
        return True
    # 如果要插入的元素key已经存在,直接返回失败
    elif k == T.key:
        return False
    # 要插入的元素比当前结点的key小，则插入到当前结点的左子树中
    elif k < T.key:
        BSTNode(T.LChild, k)
    # 要插入的元素比当前结点的key大，则插入到当前结点的右子树中
    else:
        BST_Insert(T.RChild, k)
