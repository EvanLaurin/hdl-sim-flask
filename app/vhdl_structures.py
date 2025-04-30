import re

class CodeBlock:
  def __init__(self, name, block_type, raw_code):
    self.name = name                # e.g., "process1"
    self.block_type = block_type    # e.g., "process", "architecture", etc.
    self.raw_code = raw_code        # The original code lines
    
  def __repr__(self):
    return f"<{self.block_type.capitalize()}Block name='{self.name}'>"
  
class vhdlBlock(CodeBlock):
  def __init__(self, name, raw_code):
    super().__init__(name, "vhdl", raw_code)
    self.entities = []              # List of entities in the VHDL code
    self.architectures = []         # List of architectures in the VHDL code

  def parse_entities(self):
    ## TODO: Implement entity parsing logic
    return []
  
  def parse_architectures(self):
    ## TODO: Implement architecture parsing logic
    return []
  

class EntityBlock(CodeBlock):
  def __init__(self, name, raw_code):
    super().__init__(name, "entity", raw_code)
    self.ports = []                # List of ports in the entity
    self.generics = []             # List of generics in the entity
  
  def parse_entity_name(self):
    match = re.search(r'entity\s+(\w+)\s+is', self.raw_code, re.IGNORECASE)
    if match:
      name =  match.group(1).strip()
    self.name = name  # Cache the result
    return name
  
  def parse_port_block(self):
    """
    Parses the VHDL entity port block from the raw VHDL code and extracts port information.
    This method identifies the port block within the VHDL entity declaration, extracts
    the port names, their directions (in/out), and caches the result for future use.
    Returns:
      list: A list of dictionaries, where each dictionary represents a port with the
          following keys:
          - 'name': The name of the port (str).
          - 'dir': The direction of the port, either 'in' or 'out' (str).
          - 'type': The data type of the port (str).
    Example:
      Given the following VHDL code:
      ```
      entity example is
        port (
          clk : in std_logic;
          rst, enable : in std_logic;
          data_out : out std_logic_vector(7 downto 0)
        );
      end example;
      ```
      The method will return:
      [
        {'name': 'clk', 'dir': 'in', 'type': 'std_logic'},
        {'name': 'rst', 'dir': 'in', 'type': 'std_logic'},
        {'name': 'enable', 'dir': 'in', 'type': 'std_logic'},
        {'name': 'data_out', 'dir': 'out', 'type': 'std_logic_vector(7 downto 0)'}
      ]
    Note:
      - If the port block is not found in the raw VHDL code, an empty list is returned.
      - Comments following port declarations (e.g., `-- comment`) are ignored.
    """
    if self.ports:  # Return cached result if already computed
      return self.ports
    
    match = re.search(r'entity\s+\w+\s+is\s+port\s*\((.*?)\)\s*;', self.raw_code, re.DOTALL | re.IGNORECASE)
    if not match:
      return []

    ports_block = match.group(1)
    ports = []

    for line in ports_block.split(';'):
      line = line.strip()
      if not line:
        continue
      m = re.match(r"([\w,\s]+)\s*:\s*(in|out)\s+([\w\s\(\)]+)(?:\s*--.*)?", line, re.IGNORECASE)
      if m:
        names, direction, type = m.groups()
        for name in names.split(','):
          ports.append({'name': name.strip(), 'dir': direction.lower(), 'type': type.strip()})
  
    self.ports = ports  # Cache the result
    return self.ports      

  def parse_generic_block(self):
    """
    Parses the generic block of the VHDL entity to extract generic parameters.

    This method searches for the generic block in the raw VHDL code of the entity,
    extracts the generic parameters (name and type), and caches the result for
    future use.

    Returns:
        list: A list of dictionaries, each containing the name and type of a generic parameter.
    """
    if self.generics is not None:  # Return cached result if already computed
      return self.generics
    
    match = re.search(r'entity\s+\w+\s+is\s+generic\s*\(\s*(.*?)\s*\)\s*;', self.raw_code, re.DOTALL | re.IGNORECASE)
    if not match:
      return [] 
    
    match_block = match.group(1)
    generics = []

    for line in match_block.split(';'):
      line = line.strip()
      if not line:
        continue
      m = re.match(r"([\w,\s]+)\s*:\s*([\w\s]+)", line, re.IGNORECASE)
      if m:
        names, type_ = m.groups()
        for name in names.split(','):
          generics.append({'name': name.strip(), 'type': type_.strip()})
    
    self.generics = generics  # Cache the result
    return self.generics

class ArchitectureBlock(CodeBlock):
  def __init__(self, name, raw_code):
    super().__init__(name, "architecture", raw_code)
    self.signals = []              # List of signals in the architecture
    self.processes = []            # List of processes in the architecture
    self.components = []           # List of components in the architecture
    self.concurent_statements = [] # List of concurrent statements in the architecture
  
  def parse_concurrent_statements(self):
    ## TODO: Implement concurrent statement parsing logic
    return []
  
  def parse_signals(self):
    ## TODO: Implement signal parsing logic
    return []
  
  def parse_processes(self):
    ## TODO: Implement process parsing logic
    return []
  
  def parse_components(self):
    ## TODO: Implement component parsing logic
    return []
    
  
class ComponentBlock(CodeBlock):
  def __init__(self, name, raw_code):
    super().__init__(name, "component", raw_code)
    self.ports = []                # List of ports in the component
    self.generic = []              # List of generics in the component

class ProcessBlock(CodeBlock):
  def __init__(self, name, raw_code):
    super().__init__(name, "process", raw_code)
    self.sensitivity_list = []      # List of signals in the sensitivity list
    self.statements = []            # List of statements in the process
    self.variables = []             # List of variables declared in the process
    