import nbformat
import ast

def extract_code_from_notebook(notebook_path):
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    code = ""
    for cell in nb.cells:
        if cell.cell_type == "code":
            code += cell.source + "\n"
    return code

def test_function_a():
    notebook_path = "MelBandRoformer_UserFriendly_Colab.ipynb"
    code = extract_code_from_notebook(notebook_path)

    # We will parse the AST to extract only the _C assignment and def _a
    tree = ast.parse(code)

    relevant_nodes = []

    for node in tree.body:
        # Match `_C = {}`
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "_C":
                    if isinstance(node.value, ast.Dict) and len(node.value.keys) == 0:
                        relevant_nodes.append(node)

        # Match `def _a(...)`
        elif isinstance(node, ast.FunctionDef) and node.name == "_a":
            relevant_nodes.append(node)

    # Unparse back to code
    executable_code = ast.unparse(ast.Module(body=relevant_nodes, type_ignores=[]))

    env = {}
    exec(executable_code, env, env)

    _a = env["_a"]
    _C = env["_C"]

    assert len(_C) == 0

    _a("category1", "name1", "url1", "profile1", 100, "desc1")
    assert "category1" in _C
    assert len(_C["category1"]) == 1
    assert _C["category1"][0] == ("name1", "url1", "profile1", 100, "desc1")

    _a("category1", "name2", "url2", "profile2", 200, "desc2")
    assert len(_C["category1"]) == 2
    assert _C["category1"][1] == ("name2", "url2", "profile2", 200, "desc2")

    _a("category2", "name3", "url3", "profile3", 300, "desc3")
    assert "category2" in _C
    assert len(_C["category2"]) == 1
    assert _C["category2"][0] == ("name3", "url3", "profile3", 300, "desc3")
