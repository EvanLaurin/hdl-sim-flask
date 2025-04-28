signal_trees = {}  # Global or session-based storage

def simulate_hdl(inputs):
  outputs = {}
  for signal, tree in signal_trees.items():
    outputs[signal] = tree.evaluate(inputs)
  return outputs