def simulate_hdl(filepath, inputs):
    # Mock: just return inputs with a "simulated" output
    outputs = {'Y': str(int(inputs.get('A', 0)) & int(inputs.get('B', 0)))}
    return outputs