"""只运行已核对函数的三个小反例；不执行外部脚本的顶层代码或比赛框架。"""
import ast
import contextlib
import hashlib
import io
import json
import math
import pathlib
import random
import sys
import tempfile

root = pathlib.Path(sys.argv[1])

def load(path, blob, names):
    file = root / path
    data = file.read_bytes()
    actual = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if actual != blob:
        raise ValueError('Source changed: ' + path)
    tree = ast.parse(data.decode('utf-8'))
    selected = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name in names]
    if {n.name for n in selected} != set(names):
        raise ValueError('Missing reviewed function')
    namespace = {'math': math, 'random': random}
    exec(compile(ast.Module(body=selected, type_ignores=[]), str(file), 'exec'), namespace)
    return namespace

results = []
milad = 'MiladNooraei/Orienteering-Problem/Orienteering Problem.py'
code = load(milad, '2756cafe2f7abdce63cf168b8b76cea3a0124f2f', ['greedy_orienteering'])
points = [[0, 0, 0], [10, 0, 1000], [1, 0, 10]]
distances = [[0, 10, 1], [10, 0, 9], [1, 9, 0]]
path, distance, value = code['greedy_orienteering'](2, points, distances)
assert value == 0
results.append({'source': milad, 'case': 'highest ratio infeasible, another point fits',
                'budget': 2, 'actual_path': path, 'actual_score': value,
                'feasible_witness': [0, 2], 'witness_distance': 1, 'witness_score': 10})

with tempfile.TemporaryDirectory() as folder:
    folder = pathlib.Path(folder)
    for file, sha, function, instance, witness, witness_score in [
        ('App5_DP.py', 'ea6a458200ca0782fff2a64dbb5436781bdb6bb7', 'orienteering_problem',
         '3 1\n0 0 0\n2 0 10\n1 0 10\n3 0 0\n', [0, 2, 1, 3], 20),
        ('App8_DFS_Modifed.py', '23aad98c307fcba94e6d4301e3966169d18fe029', 'dfs_randomized',
         '3 1\n0 0 0\n1 0 10\n', [0, 1], 10),
    ]:
        source = 'aliiimaher/Algorithm-OP-Heuristic-Approaches/' + file
        methods = ['euclidean_distance', function]
        code = load(source, sha, methods)
        input_path = folder / 'input.txt'; output_path = folder / 'output.txt'
        input_path.write_text(instance)
        with contextlib.redirect_stdout(io.StringIO()):
            code[function](str(input_path), str(output_path))
        output = output_path.read_text()
        if file == 'App5_DP.py':
            actual = float(output.split('Total Profit:')[1]); assert actual == 10
        else:
            assert output == 'No valid path found.'; actual = 0
        results.append({'source': source, 'input': instance, 'actual_output': output,
                        'actual_score': actual, 'feasible_witness': witness,
                        'witness_score': witness_score})
print(json.dumps({'scope': 'Three reviewed function-level synthetic counterexamples; not full repository execution.',
                  'cases': results}, ensure_ascii=False, indent=2))
