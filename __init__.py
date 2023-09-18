import boiga

map_tbl_src = ["str", "int"]
map_tbl_desk = ["STRING", "NUMBER"]

def can_do_type_checks(val):
  try:
    map_tbl_src.index(val)
    return True
  except ValueError:
    return False

class GeneratedExpression(boiga.core.Expression):
  def __init__(self, id, block_type, opcode, rebuilt_args):
    if block_type == "BOOLEAN":
      self.type = "bool"

    self.op = f"{id}_{opcode}"
    self.args = rebuilt_args

class ExtensionBlockStructure():
  def __init__(self, dict, suppress_type_errors = False):
    self.dict = dict
    self.suppress_type_errors = suppress_type_errors

  def do_data_proc(self, opcode, **args):
    block_opcode_list = [x for x in self.dict["blocks"] if x["opcode"] == opcode]
    if len(block_opcode_list) == 0:
      raise ValueError("Opcode specified does not exist")
    
    block_op = block_opcode_list[0]

    # Validate arguments to make sure they're valid, then reconstruct & parse
    if len(args) != len(block_op["arguments"]):
      raise ValueError("Invalid number of arguments")
    
    rebuilt_args = {}
    
    for arg in args:
      if arg not in block_op["arguments"]:
        raise ValueError(f"Argument '{arg}' not found in block")

      type_search = type(args[arg]).__name__
      if can_do_type_checks(type_search):
        map_index = map_tbl_src.index(type_search)
        actual_val = map_tbl_desk[map_index]

        # Test the types
        if actual_val != block_op["arguments"][arg]["type"]:
          raise ValueError("Type of argument does not match")
      else:
        if not self.suppress_type_errors: print("Type checks skipped (passed currently uncheckable yet probably correct input through)")

      rebuilt_args[arg] = boiga.ensure_expression(args[arg])

    return (rebuilt_args, block_op)

  def statement(self, opcode, **args):
    id = self.dict["id"]

    (rebuilt_args, block_op) = self.do_data_proc(opcode, **args)
    statement = boiga.core.Statement(f"{id}_{opcode}", **rebuilt_args)
    
    return statement
  
  def expression(self, opcode, **args):
    id = self.dict["id"]
    (rebuilt_args, block_op) = self.do_data_proc(opcode, **args)
    
    return GeneratedExpression(id, block_op["blockType"], opcode, rebuilt_args)