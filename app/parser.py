import re

def remove_comments(code):
  # Remove single-line comments
  code = re.sub(r'--.*?(\r?\n|$)', '', code)

  # Remove multi-line comments
  code = re.sub(r'/\*.*?\*/', '', code, flags=re.DOTALL)

  return code

