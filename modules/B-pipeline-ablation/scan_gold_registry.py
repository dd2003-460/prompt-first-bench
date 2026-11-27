#!/usr/bin/env python3
"""scan_gold_registry.py — 题面/gold/units/机制版本三维登记册（Q9REG, D 2026-11-27 15:00 指令"完整彻底整理好"）。

为什么脚本不是人肉: 登记册的价值=可重复生成（文件变了重跑即更新），人肉整理一次就过期。
设计（压缩优先）: 一个确定性扫描器, 三个维度共用同一份文件清单:
  ① 问题维度: qid × {题面路径+版本, gold 路径+版本, units 路径+canonical}
  ② 版本维度: 文件名版本标记（v0/v1/v2/-pure/-research）+ 题面-gold 绑定
  ③ 机制维度: runs-* 目录 + scoring*.md + judge canonical 声明
冲突检测（不修复, 只标记）: qid 撞号 / units 分叉(哈希不同) / 孤儿副本(无代码引用) / 完全副本(哈希相同)
边界: 只读+生成 registry.json+conflicts.md, 不移动/不删除/不修改任何现有文件。
用法: /usr/bin/python3 scan_gold_registry.py
输出: data/registry/registry.json + data/registry/conflicts.md
"""
import hashlib, json, os, re, subprocess, sys
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
PFB = os.path.join(HERE, '..', '..')
OUT_DIR = os.path.join(HERE, 'data', 'registry')

# ---- 扫描范围（相对 PFB 根）----
GLOB_DIRS = [
    'experiments/stage-ablation/questions', 'experiments/stage-ablation/gold',
    'bench/questions', 'bench/rubric-v3/ablation',
    'modules/B-pipeline-ablation', 'modules/B-pipeline-ablation/data',
    'demo/gold', 'repro/gold',
]
RUNS_DIR = 'experiments/stage-ablation'
SCORING_GLOB = 'experiments/stage-ablation/scoring*.md'

QID_RE = re.compile(r'[Qq](\d+)')
VER_RE = re.compile(r'(?:-|_)(v\d+|pure|research)(?:\.|$|-)')

def sha1(p):
    h = hashlib.sha1()
    with open(p, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()[:12]

def rel(p):
    return os.path.relpath(p, PFB)

def qid_of(name):
    m = QID_RE.search(os.path.basename(name))
    return 'Q'+m.group(1) if m else None

def version_of(name):
    """文件名版本标记: Q9-v1.md→v1, Q9-agi-pure.txt→pure, Q9-agi-research.md→research, 无→base"""
    m = VER_RE.search(os.path.basename(name))
    return m.group(1) if m else 'base'

def main():
    files = []
    for d in GLOB_DIRS:
        dp = os.path.join(PFB, d)
        if not os.path.isdir(dp):
            continue
        for fn in sorted(os.listdir(dp)):
            fp = os.path.join(dp, fn)
            if os.path.isfile(fp):
                files.append(fp)

    registry = {'generated_at': datetime.now().astimezone().isoformat(timespec='seconds'),
                'generator': 'scan_gold_registry.py', 'entries': {}, 'conflicts': []}
    entries = registry['entries']

    def add(qid, kind, path, **kw):
        e = entries.setdefault(qid, {})
        lst = e.setdefault(kind, [])
        item = {'path': rel(path), 'sha1': sha1(path), 'version': version_of(path)}
        item.update(kw)
        lst.append(item)

    for fp in files:
        fn = os.path.basename(fp)
        d = os.path.basename(os.path.dirname(fp))
        qid = qid_of(fn)
        # units: 文件名含 gold+units 的 json；无 Q 编号时用域名词做 qid（如 gpu → Q6/Q7 共用）
        if fn.endswith('.json') and 'units' in fn and 'gold' in fn:
            if not qid:
                dm = re.search(r'gold-([a-z0-9]+)-units', fn)
                qid = dm.group(1) if dm else 'unknown'
            add(qid, 'units', fp)
            continue
        if not qid:
            continue
        # gold: gold-*.md（bench/rubric-v3/ablation）或 gold/ 目录下 Q*.md / Q*-v*.md（排除回执/台账类）
        if fn.endswith('.md') and (fn.startswith('gold-') or d == 'gold') and 'receipt' not in fn:
            add(qid, 'gold', fp)
        # question: questions/ 目录下，或文件名含 pure/research
        elif d == 'questions' or 'pure' in fn or 'research' in fn:
            add(qid, 'question', fp)

    # 题面 v1 特殊: 藏在 tasks/q9-agi-question-v0.md 的「## 题面 v1」段
    v1_doc = os.path.join(PFB, 'experiments/stage-ablation/tasks/q9-agi-question-v0.md')
    if os.path.isfile(v1_doc):
        txt = open(v1_doc).read()
        if '## 题面 v1' in txt:
            add('Q9', 'question', v1_doc, version='v1-in-doc',
                note='题面 v1 段落（D 2026-11-26 20:10 冻结）；纯题面文件=questions/Q9-agi-pure.txt(v0)')

    # ---- 冲突检测 ----
    conf = registry['conflicts']
    # 1) units 分叉: 同 qid 多份 units 哈希不同
    for qid, e in entries.items():
        us = e.get('units', [])
        if len(us) > 1:
            hashes = {u['sha1'] for u in us}
            if len(hashes) > 1:
                conf.append({'type': 'units-fork', 'qid': qid, 'paths': [u['path'] for u in us],
                             'detail': f'{len(us)} 份 units 内容分叉'})
            else:
                conf.append({'type': 'units-copy', 'qid': qid, 'paths': [u['path'] for u in us],
                             'detail': '内容相同的副本'})
    # 2) units 孤儿: 无代码引用（grep 文件名）
    for qid, e in entries.items():
        for u in e.get('units', []):
            fn = os.path.basename(u['path'])
            r = subprocess.run(['grep', '-rln', fn, '--include=*.py', '--include=*.sh', PFB],
                               capture_output=True, text=True, timeout=60)
            refs = [l for l in r.stdout.splitlines() if not l.endswith(fn)]
            u['code_refs'] = len(refs)
            if not refs:
                conf.append({'type': 'units-orphan', 'qid': qid, 'path': u['path'],
                             'detail': '无代码引用（孤儿副本风险）'})
    # 3) qid 撞号: 同 qid 的 gold 来自不同顶层目录（bench vs stage-ablation = 不同域）
    #    排除完全副本（哈希全同 = 副本问题, 已由 gold-copy 报告, 不重复报冲突）
    for qid, e in entries.items():
        gs = e.get('gold', [])
        tops = {g['path'].split('/')[0] for g in gs}
        if len(tops) > 1 and len({g['sha1'] for g in gs}) > 1:
            conf.append({'type': 'qid-collision', 'qid': qid, 'topics': sorted(tops),
                         'paths': [g['path'] for g in gs],
                         'detail': '同 qid 的 gold 来自不同目录且内容不同（编号撞车, 不同题）'})
    # 4) 完全副本: gold md 哈希相同但路径不同
    all_gold = [(q, g) for q, e in entries.items() for g in e.get('gold', [])]
    seen = {}
    for qid, g in all_gold:
        seen.setdefault(g['sha1'], []).append(g['path'])
    for h, paths in seen.items():
        if len(paths) > 1:
            conf.append({'type': 'gold-copy', 'paths': paths, 'detail': '内容相同的 gold 副本'})

    # ---- 题面↔gold 绑定（文件名推不出, 带证据的人工标注; 证据=git 考古 2026-11-27）----
    BINDINGS = {
        'Q1': {'bound': True, 'note': '题面 questions/Q1-gpu-h100.md ↔ gold/Q1.md 同期同目录（T17 时代）'},
        'Q2': {'bound': True, 'note': '同上（T17 时代）'},
        'Q3': {'bound': True, 'note': '同上（T17 时代）'},
        'Q4': {'bound': True, 'note': '同上; Q4 曾修题面-gold 缺陷（version-matrix 声明 j=Q4-fixed）'},
        'Q5': {'bound': True, 'note': '同上（T17 时代）'},
        'Q6': {'bound': True, 'note': '题面 bench/questions/Q6-network-arch.txt ↔ gold bench/rubric-v3/ablation/gold-Q6.md ↔ units data/gold-q6-units.json（B1 解析）'},
        'Q7': {'bound': True, 'note': '题面 bench/questions/Q7-storage-arch.txt ↔ gold gold-Q7.md ↔ units data/gold-q7-units.json; Q6/Q7 共用 gold-gpu-units.json（judge 跨域口径）'},
        'Q8': {'bound': True, 'note': '题面 bench/questions/Q8-eval-benchmark.txt ↔ gold bench/rubric-v3/ablation/gold-Q8.md（11-07 T50 批）'},
        'Q10': {'bound': True, 'note': '题面 bench/questions/Q10-rlhf-align.txt ↔ gold gold-Q10.md（11-07 T50 批）'},
        'Q9': {'bound': False,
               'note': '编号撞车: bench 下 Q9-vlm-arch.txt+gold-Q9.md=旧 Q9(VLM 架构, 11-07 T50 批); stage-ablation 下 Q9-agi=新 Q9(AGI, 11-22 起)。新 Q9 内部: 题面 v0(Q9-agi-pure.txt, 11-27 11:34 纯题面) ↔ gold v0(Q9.md 判定点段, 已废弃)→v1(Q9-v1.md, arena 11-24 交付 d33b5e271)→v2(Q9-v2.md, 11-24 交叉核验修正 885debea5, 当前 scan 用); 题面 v1(tasks/q9-agi-question-v0.md 段落, D 11-26 20:10 冻结) ↔ gold 未交付(Q9G-V1 追查中)',
               'current_pair': {'question': 'experiments/stage-ablation/questions/Q9-agi-pure.txt (v0)',
                                'gold': 'experiments/stage-ablation/gold/Q9-v2.md (v2, scan 在用)'}},
        'gpu': {'bound': True, 'note': 'gold-gpu-units.json 为 Q6/Q7 共用 units; canonical=modules 根(36 units, judge_v1.py L34 默认引用), data/ 副本(37 units)无代码引用=孤儿'},
    }
    for qid, b in BINDINGS.items():
        if qid in entries:
            entries[qid]['binding'] = b

    # ---- 机制维度: runs-* 目录 + scoring 文件 ----
    mech: dict = {'runs_dirs': [], 'scoring_files': []}
    rd = os.path.join(PFB, RUNS_DIR)
    if os.path.isdir(rd):
        for fn in sorted(os.listdir(rd)):
            if fn.startswith('runs-') and os.path.isdir(os.path.join(rd, fn)):
                mech['runs_dirs'].append(fn)
    for fp in sorted(__import__('glob').glob(os.path.join(PFB, SCORING_GLOB))):
        mech['scoring_files'].append(rel(fp))
    # judge canonical 声明来源（快照文档, 会过期 → 标记 staleness）
    vm = os.path.join(PFB, RUNS_DIR, 'version-matrix-20261126.md')
    mech['judge_canonical_source'] = {'path': rel(vm) if os.path.isfile(vm) else None,
                                      'note': 'canonical=j=v3 声明在此快照文档内（2026-11-26 生成, 可能过期）'}
    registry['mechanism'] = mech

    # ---- 落盘 ----
    os.makedirs(OUT_DIR, exist_ok=True)
    reg_path = os.path.join(OUT_DIR, 'registry.json')
    json.dump(registry, open(reg_path, 'w'), ensure_ascii=False, indent=1)

    lines = ['# 冲突清单（scan_gold_registry.py 生成, 勿手改）',
             f'生成: {registry["generated_at"]}', '']
    for c in conf:
        lines.append(f"- **{c['type']}** {c.get('qid','')}: {c['detail']}")
        for p in c.get('paths', []):
            lines.append(f'  - `{p}`')
        if c.get('path'):
            lines.append(f'  - `{c["path"]}`')
    md_path = os.path.join(OUT_DIR, 'conflicts.md')
    open(md_path, 'w').write('\n'.join(lines) + '\n')

    print(f'[registry] entries={len(entries)} qids={sorted(entries)} conflicts={len(conf)}')
    print(f'[registry] → {rel(reg_path)}')
    print(f'[registry] → {rel(md_path)}')
    for c in conf:
        print(f"  ! {c['type']} {c.get('qid','')}: {c['detail']}")

if __name__ == '__main__':
    main()
