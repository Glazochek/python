"""
Задание 2.

Доработайте пример структуры "дерево", рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения

Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде.
"""

from termcolor import colored


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.root)

    def insert_left(self, new_node):
        if new_node <= self.root:
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        else:
            print(colored('ERROR', 'red'))

    def insert_right(self, new_node):
        if new_node >= self.root:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        else:
            print(colored('ERROR', 'red'))

    def get_right_child(self):
        try:
            return self.right_child
        except AttributeError:
            print(colored('AttributeError', 'red'))

    def get_left_child(self):
        try:
            return self.left_child
        except AttributeError:
            print(colored('AttributeError', 'red'))

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        try:
            return self.root
        except AttributeError:
            print(colored('AttributeError', 'red'))


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
r.insert_left(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
