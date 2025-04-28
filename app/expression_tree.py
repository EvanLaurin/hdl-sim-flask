class TreeNode:
  def __init__(self, value, left=None, right=None):
    self.value = value.lower()
    self.left = left
    self.right = right

  def evaluate(self, inputs):
    if self.left is None and self.right is None:
      return int(inputs.get(self.value, 0))

    left_value = self.left.evaluate(inputs) if self.left else 0
    right_value = self.right.evaluate(inputs) if self.right else 0

    if self.value == 'and':
      return left_value & right_value
    elif self.value == 'or':
      return left_value | right_value
    elif self.value == 'not':
      return (~left_value) & 1
    elif self.value == 'xor':
      return left_value ^ right_value
    elif self.value == 'nand':
      return ~(left_value & right_value) & 1
    elif self.value == 'nor':
      return ~(left_value | right_value) & 1
    elif self.value == 'xnor':
      return ~(left_value ^ right_value) & 1
    else:
      raise ValueError(f"Invalid operator: {self.value}")

  def __repr__(self):
    if self.value == 'not':
      return f"({self.value} {self.left})"
    elif self.left and self.right:
      return f"({self.left} {self.value} {self.right})"
    else:
      return self.value


def expr_to_tree(expression):
  if isinstance(expression, str):
    tokens = expression.lower().split()
  else:
    tokens = expression

  ops = ['and', 'or', 'nand', 'nor', 'xor', 'xnor']

  for op in ops:
    if op in tokens:
      idx = tokens.index(op)
      left = expr_to_tree(tokens[:idx])
      right = expr_to_tree(tokens[idx + 1:])
      return TreeNode(op, left, right)

  if 'not' in tokens:
    idx = tokens.index('not')
    operand = expr_to_tree(tokens[idx + 1:])
    return TreeNode('not', operand)

  return TreeNode(tokens[0])
  