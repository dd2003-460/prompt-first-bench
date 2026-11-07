#!/usr/bin/env python3
"""B-face: cross-family O6 judge using qwen2.5-7b (LM Studio @1234).
Re-scores S8 n=3 + S5 baseline O6 with a different model family.
Output: /tmp/bface-o6.json
"""
import json, os, re, sys, urllib.request, time

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from score import extract_contradictions, _smart_truncate
from ablation_harness import QUESTIONS

JUDGE_URL = "http://localhost:1234/v1/chat/completions"
JUDGE_MODEL = "qwen2.5-7b-original"

def bface_judge(prompt, max_tokens=4000):
    """Call qwen2.5-7b as judge."""
    payload = json.dumps({
        "model": JUDGE_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": max_tokens,
    }).encode()
    req = urllib.request.Request(JUDGE_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"]


def judge_o6_bface(output_text, gold_items, gold_section):
    """Same logic as score.judge_o6 but uses qwen2.5-7b."""
    if not gold_items:
        return 0, 0, "gold has no contradiction section (N/A)"
    prompt = f"""你是研究质量评审。任务：判断【模型输出】是否发现了【Gold 隐藏矛盾】中列出的每一条矛盾/误读。

对 Gold 中的每条矛盾，按以下三档判定模型输出的命中程度：
- 0 = 没发现（输出中完全没触及该矛盾点）
- 1 = 发现了但没转化（指出了矛盾或相关数字差异，但没有推出它影响哪个结论、涉及什么变量）
- 2 = 转化为具体新发现（明确指出矛盾双方 + 涉及的变量/条件 + 对原结论的具体影响）

规则：
- 语义命中即可，不要求措辞一致
- 模型自己额外发现的矛盾（不在 gold 列表里）不计入本分，单独记录在 extra_findings
- 最后给 JSON: {{"hits": [{{"gold_item": <编号>, "tier": 0|1|2, "evidence": "输出中的对应原文片段"}}], "extra_findings": ["..."], "score": <总命中分>}}
其中 score = sum(tier)，满分 = 2 × gold 条数。

【Gold 隐藏矛盾】
{gold_section}

【模型输出】
{_smart_truncate(output_text)}"""
    try:
        raw = bface_judge(prompt)
        m = re.search(r'\{.*\}', raw, re.DOTALL)
        if m:
            d = json.loads(m.group())
            hits = d.get("hits", [])
            tier_sum = sum(h.get("tier", 0) for h in hits)
            norm = tier_sum / max(2 * len(gold_items), 1)
            detail = "; ".join(f"#{h.get('gold_item')}:{h.get('tier')}" for h in hits)
            extras = d.get("extra_findings", [])
            note = f"[O6-bface] tiers={detail} score={tier_sum}/{2*len(gold_items)}"
            if extras:
                note += f" extra={extras[:2]}"
            return min(norm, 1.0), 1, note
        return 0, 1, f"no JSON in response: {raw[:100]}"
    except Exception as e:
        return 0, 1, f"judge failed: {e}"


def main():
    results = {}
    
    # S8 n=3: Q1-Q5 × r1-r3
    for qid in ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']:
        gold_path = QUESTIONS[qid]['gold_file']
        gold_text = open(gold_path).read()
        items, section = extract_contradictions(gold_text)
        if not items:
            print(f"{qid}: no gold contradiction section, skip")
            continue
        for r in range(1, 4):
            fpath = f"runs/S8-{qid}-r{r}.json"
            if not os.path.exists(fpath):
                print(f"{fpath}: missing")
                continue
            d = json.load(open(fpath))
            output_text = d.get('output_text', '')
            t0 = time.time()
            score, _, note = judge_o6_bface(output_text, items, section)
            elapsed = round(time.time() - t0, 1)
            key = f"S8-{qid}-r{r}"
            results[key] = {'o6': score, 'note': note, 'elapsed_s': elapsed}
            print(f"{key}: O6={score:.3f} ({elapsed}s) {note[:80]}")
            time.sleep(1)  # be nice to LM Studio
    
    # S5 baseline: runs-r293/S5-Q{n}-r{rep}.json (n=3 per question)
    for qid in ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']:
        gold_path = QUESTIONS[qid]['gold_file']
        gold_text = open(gold_path).read()
        items, section = extract_contradictions(gold_text)
        if not items:
            print(f"S5 {qid}: no gold contradiction section, skip")
            continue
        for r in range(1, 4):
            fpath = f"runs-r293/S5-{qid}-r{r}.json"
            if not os.path.exists(fpath):
                print(f"{fpath}: missing")
                continue
            d = json.load(open(fpath))
            output_text = d.get('output_text', '')
            t0 = time.time()
            score, _, note = judge_o6_bface(output_text, items, section)
            elapsed = round(time.time() - t0, 1)
            key = f"S5-{qid}-r{r}"
            results[key] = {'o6': score, 'note': note, 'elapsed_s': elapsed}
            print(f"{key}: O6={score:.3f} ({elapsed}s) {note[:80]}")
            time.sleep(1)
    
    json.dump(results, open('/tmp/bface-o6.json', 'w'), ensure_ascii=False, indent=1)
    print(f"\nTotal scored: {len(results)}")
    print("Saved to /tmp/bface-o6.json")


if __name__ == '__main__':
    main()