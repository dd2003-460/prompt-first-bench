#!/usr/bin/env python3
# T53 综合脚本：SM 节点树 → 分段综合 → merge → 存 answer。
# 不走 s8b_pilot.judge（新题 qid 不在 GOLD 字典里，会 KeyError）；
# 判分用 t53_bface_judge.py（B-face qwen2.5-7b，核心数字 0.5 + 口径 0.5，n=3 median）。
# 综合逻辑照抄 s5_state_machine.synthesize_answer（含 2026-11-16 新 merge prompt 限制因素规则）。
# 用法：python3 t53_synth.py <qid>
import json, sys, time, random
from collections import defaultdict
sys.path.insert(0, '/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation')
from ablation_harness import call_llm

def _perturb():
    return "".join(random.choice(["\u200b", "\u200c", " ", "\u200d"]) for _ in range(4))

base = '/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation'
qid = sys.argv[1]
d = json.load(open(f'{base}/runs-s5-sm-{qid}.json'))
nodes = d['nodes']
question = d['question']
print(f'load {len(nodes)} nodes, question {len(question)} chars', flush=True)

by_lv = defaultdict(list)
for n in nodes:
    by_lv[n.get('level', '?')].append(n)
parts = []
for lv in sorted(by_lv, key=lambda x: str(x).lstrip('L')):
    seg = "\n".join(
        f"{n['id']} ({lv}): {n.get('corrected_claim') or n['claim']}  "
        f"[status={n['status']}; evidence: {(n.get('evidence') or '')[:80]}]"
        for n in by_lv[lv])
    p = (f"你是研究员。基于下面第 {lv} 层的已核验事实，回答原问题中该层涉及的部分。"
         f"只写结论+数值/公式，每条标来源条目 id，不要重复其他层的内容。\n\n"
         f"【问题】\n{question}\n\n【第 {lv} 层事实】\n{seg}") + _perturb()
    t0 = time.time()
    out_l, _ = call_llm(p, max_tokens=4000, temperature=0.7, top_p=0.95, retries=3) or ("", {})
    parts.append(f"=== 第 {lv} 层 ===\n{out_l or '(空)'}")
    print(f'  {lv}: {len(by_lv[lv])} 节点, out={len(out_l or "")}c, {time.time()-t0:.0f}s', flush=True)

merge_p = (f"你是研究员。下面是同一道问题按目录树分层得到的各层结论摘要。"
           f"请把它们合并成一份完整最终答案：覆盖问题全部子问，保留所有具体数值/公式/排序，"
           f"消除层间重复，最后给一个明确的推荐结论。"
           f"规则：问题问「最多/上限/提升多少/打几折」时，必须显式列出限制因素并给出其定量影响，"
           f"不能只讲优势不讲上限；涉及对比/口径的，明确分母、单位、来源、财年；"
           f"来源不一致时说明口径差异并给出选用理由。\n\n【问题】\n{question}\n\n"
           + "\n\n".join(parts)) + _perturb()
t0 = time.time()
answer, _ = call_llm(merge_p, max_tokens=8000, temperature=0.7, top_p=0.95, retries=3) or ("", {})
print(f'merge: out={len(answer or "")}c, {time.time()-t0:.0f}s', flush=True)

out = {
    'qid': qid,
    'ts': time.strftime('%Y-%m-%dT%H:%M:%S%z'),
    'source': f'runs-s5-sm-{qid}.json (SM 终盘)',
    'n_nodes': len(nodes),
    'answer': answer,
}
out_path = f'{base}/runs-s5-sm-{qid}-synth.json'
with open(out_path, 'w') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)
print(f'DONE → {out_path} | answer={len(answer or "")}c', flush=True)