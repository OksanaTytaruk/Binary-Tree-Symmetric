class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root):
    if root is None:
        return True

    def isMirror(left, right):
        # Якщо обидва вузли відсутні,
        # ця частина дерева симетрична
        if left is None and right is None:
            return True

        # Якщо один вузол відсутній,
        # а інший існує — дерева не симетричні
        if left is None or right is None:
            return False

        # Значення дзеркальних вузлів повинні бути однаковими
        if left.val != right.val:
            return False

        # Ліве піддерево повинно відповідати
        # правому піддереву
        return (
            isMirror(left.left, right.right)
            and isMirror(left.right, right.left)
        )

    return isMirror(root.left, root.right)


# ==========================================
# ТЕСТУВАННЯ
# ==========================================

# Приклад 1:
# root = [1,2,2,3,4,4,3]
# Очікуваний результат: True

root1 = TreeNode(1)

root1.left = TreeNode(2)
root1.right = TreeNode(2)

root1.left.left = TreeNode(3)
root1.left.right = TreeNode(4)

root1.right.left = TreeNode(4)
root1.right.right = TreeNode(3)

print("Приклад 1:", isSymmetric(root1))


# Приклад 2:
# root = [1,2,2,null,3,null,3]
# Очікуваний результат: False

root2 = TreeNode(1)

root2.left = TreeNode(2)
root2.right = TreeNode(2)

root2.left.right = TreeNode(3)
root2.right.right = TreeNode(3)

print("Приклад 2:", isSymmetric(root2))


# Приклад 3:
# p = [1,2,1]
# q = [1,1,2]
# Очікуваний результат: False

# Для перевірки симетрії створюємо дерево:
# root = [1,2,1]

root3 = TreeNode(1)

root3.left = TreeNode(2)
root3.right = TreeNode(1)

print("Приклад 3:", isSymmetric(root3))