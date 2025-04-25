import re

def parse_entity_ports(file_path):
    with open(file_path, 'r') as f:
        code = f.read()

    match = re.search(r'entity\s+\w+\s+is\s+port\s*\((.*?)\);', code, re.DOTALL | re.IGNORECASE)
    if not match:
        return []

    ports_block = match.group(1)
    ports = []

    for line in ports_block.split(';'):
        line = line.strip()
        if not line:
            continue
        m = re.match(r"([\w,\s]+)\s*:\s*(in|out)\s+\w+", line, re.IGNORECASE)
        if m:
            names, direction = m.groups()
            for name in names.split(','):
                ports.append({'name': name.strip(), 'dir': direction.lower()})
    return ports