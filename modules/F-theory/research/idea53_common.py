"""#53 共享逻辑: 词表加载 (子进程隔离) + 树加载 + 文本工具.
被 idea53-info-theoretic-contribution.py (主, 纯数学) 和 idea53-embed.py
(干净子进程, 唯一 import sentence_transformers) 共用.
"""
import json, glob, re, os, sys, pickle
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
_VOCAB_PKL = HERE + '/.idea53-vocab.pkl'


def _load_vocab():
    """子进程提取词表 (enrichment 内部 import re, 同进程 exec 会污染
    sys.modules['re'] 导致 transformers 的 import regex 循环导入)."""
    if not os.path.exists(_VOCAB_PKL):
        import subprocess
        code = (
            "import sys, os, pickle\n"
            f"sys.path.insert(0, {HERE!r})\n"
            "import importlib.util\n"
            f"p = {HERE + '/idea53-supply-bottleneck-enrichment.py'!r}\n"
            "spec = importlib.util.spec_from_file_location('enr', p)\n"
            "m = importlib.util.module_from_spec(spec)\n"
            "src = open(p).read().split(chr(39)*3 + '__main__' + chr(39)*3)[0]\n"
            "exec(compile(src, 'enr', 'exec'), m.__dict__)\n"
            "out = {'SUPPLY': m.SUPPLY, 'JUDGE': m.JUDGE, 'MICRO': m.MICRO,\n"
            "       'REPS': m.REPS, 'T53B': m.T53B, 'STAGE': m.STAGE}\n"
            f"pickle.dump(out, open({_VOCAB_PKL!r}, 'wb'))\n"
        )
        r = subprocess.run([sys.executable, '-c', code], capture_output=True,
                           text=True)
        if r.returncode != 0:
            raise RuntimeError('vocab extract failed: ' + r.stderr[-500:])
    with open(_VOCAB_PKL, 'rb') as fh:
        _v = pickle.load(fh)
    return _v


_V = _load_vocab()
SUPPLY, JUDGE, MICRO = _V['SUPPLY'], _V['JUDGE'], _V['MICRO']
REPS, T53B, STAGE = _V['REPS'], _V['T53B'], _V['STAGE']

# D 点名测得动的词 (边界)
MEASURABLE = ['内存带宽', 'occupancy/占用率', 'MFU', 'Kernel Launch']
UNMEASURABLE = ['指令吞吐', 'issue rate/发射', 'warp']


def text_of(nd):
    return ' '.join(str(nd.get(k) or '') for k in
                    ('claim', 'evidence', 'corrected_claim'))


def find_nodes(obj):
    out = []
    if isinstance(obj, dict):
        if isinstance(obj.get('level'), str) and 'claim' in obj:
            out.append(obj)
        else:
            for v in obj.values():
                out += find_nodes(v)
    elif isinstance(obj, list):
        for v in obj:
            out += find_nodes(v)
    return out


def load_trees():
    """返回 {源名: [(tree_id, root_text, [nodes]), ...]}."""
    trees = {}
    # ① rep-scan: nodes list, 无 answer → 根 = L1 claims
    t1 = []
    for f in sorted(glob.glob(REPS + 'rep-*.json')):
        if 'era-matched' in f or 'scores' in f:
            continue
        d = json.load(open(f))
        ns = [nd for nd in d.get('nodes', []) if nd.get('level') is not None]
        if not ns:
            continue
        l1 = ' '.join(text_of(nd) for nd in ns if nd.get('level') == 'L1')
        t1.append((os.path.basename(f), l1, ns))
    trees['①rep-scan(L1-L4)'] = t1
    # ② t53b: nodes + answer → 根 = answer
    t2 = []
    for f in sorted(glob.glob(T53B + 'runs*/gpu_*.json')):
        d = json.load(open(f))
        ns = find_nodes(d)
        if not ns:
            continue
        ans = (d.get('answer') or '').strip()
        root = ans if ans else ' '.join(
            text_of(nd) for nd in ns if nd.get('level') == 'L1')
        t2.append((os.path.basename(f), root, ns))
    trees['②t53b(L1-L4)'] = t2
    # ③ stage-ablation: node.json per node, 无 answer → 根 = L1 claims
    files = [f for f in glob.glob(STAGE + '**/node.json', recursive=True)
             if re.search(r'(sm-gpu|gpu-|/gpu)', f)]
    by_tree = defaultdict(list)
    for f in files:
        parts = f.split('/')
        run = next((p for p in parts if re.match(r'(sm-gpu|gpu-)', p)),
                   'unknown')
        try:
            d = json.load(open(f))
        except Exception:
            continue
        if isinstance(d, dict) and isinstance(d.get('level'), str):
            by_tree[run].append(d)
    t3 = []
    for run, ns in sorted(by_tree.items()):
        l1 = ' '.join(text_of(nd) for nd in ns if nd.get('level') == 'L1')
        t3.append((run, l1, ns))
    trees['③stage-ablation GPU域(L1-L5)'] = t3
    return trees
