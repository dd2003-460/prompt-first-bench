"""M7 建模/矛盾推理维度 — 纯规则判分（不需 LLM judge）

判分逻辑：检测模型是否"正确裁决"了 gold 中的隐藏矛盾/常见误读。
不是检测"是否提到概念"（太弱），而是检测"提到 + 否定/限定/条件化上下文"。

用法: python3 score_m7.py → 输出 /tmp/score-m7-results.json
"""
import json, os, re, sys

# 每题的矛盾裁决模式：(正则, 描述)
# 正则要求：概念 X 附近出现裁决词（错/误/不是/取决于/才/先/划掉/不能直接...）
M7_PATTERNS = {
    'Q1': [
        (r'(14\s*倍|900.*64|卡间互联).{0,100}(错|误|不对|不是.*吞吐|互联带宽|与吞吐无关)', "识别 14x 是互联带宽比非吞吐比"),
        (r'(decode|解码).{0,80}(memory.?bound|带宽瓶颈|3\.35.*2\.0|1\.68|显存带宽)', "decode 瓶颈是带宽非算力"),
        (r'(prefill|长\s*prompt|长上下文输入).{0,80}(compute.?bound|算力|计算密集)', "prefill 才是 compute-bound"),
        (r'(NVLink|卡间互联|900\s*GB).{0,100}(多卡|TP|张量并行|才.*重要|才有意义|单机.*无)', "NVLink 只在多卡时重要"),
    ],
    'Q2': [
        (r'(benchmark|HumanEval|榜单|基准分).{0,120}(不能直接|≠|不等于|gap|衰减|55%|黑盒|内部.*代码库)', "benchmark 分≠实际任务可用率"),
        (r'(许可|license|LICENSE).{0,80}(一票否决|直接划掉|先行|不进排名|非商用)', "许可证一票否决先行"),
        (r'(参数量大|参数多).{0,60}(≠|不等于|不代表|不能.*能力|反噬|漏掉)', "参数量大≠能力强"),
    ],
    'Q3': [
        (r'(SLO|TTFT|TPOT|延迟).{0,80}(约束|不是成本|划掉|无论多快|feasible)', "SLO 是约束非成本项"),
        (r'(厂商标称|标称值|官方.*延迟).{0,80}(实测|差\s*2|差\s*3|2–3|2-3|差距|不可信)', "厂商标称 vs 实测差 2-3 倍"),
        (r'(不支持|硬件支持|CI 支持).{0,60}(直接划掉|一票否决|可行域)', "硬件不支持直接划掉"),
    ],
    'Q4': [
        (r'(128K|长上下文).{0,120}(≠|不等于|都有效|衰减|U型|首尾|中段|高估)', "标称 128K≠128K 都有效（定位衰减）"),
        (r'(只看边际|只算边际|仅看 token).{0,80}(漏|RAG|upfront|建设|索引)', "只看边际成本会漏 RAG upfront"),
        (r'(检索.*不够|相关但不够|强行作答).{0,60}(幻觉|halluc)', "检索到不够片段时强行作答产生幻觉"),
    ],
    'Q5': [
        (r'(制度约束|监管|期刊|α 显著|alpha).{0,80}(feasible|约束|不是损失|划掉|一票否决|直接)', "制度约束是 feasible 约束非损失项"),
        (r'(p 值|p-value|显著性).{0,80}(滥用|≠|不等于|效应量|误读|misuse)', "p 值滥用（显著性≠效应量）"),
        (r'(后验|贝叶斯).{0,80}(小众|直观|可解释|沟通)', "后验直观但小众（沟通代价）"),
    ],
}

def score_m7(output_text, qid):
    """返回 (score 0-1, hits list, total patterns)"""
    patterns = M7_PATTERNS.get(qid, [])
    if not patterns:
        return None, [], 0
    hits = []
    for pattern, desc in patterns:
        if re.search(pattern, output_text, re.I | re.S):
            hits.append(desc)
    score = len(hits) / len(patterns)
    return score, hits, len(patterns)

def main():
    results = []
    for arm in ['S0','S1','S2','S3','S4','S5']:
        for qid in ['Q1','Q2','Q3','Q4','Q5']:
            for rep in [1,2,3]:
                path = f'runs/{arm}-{qid}-r{rep}.json'
                if not os.path.exists(path):
                    continue
                run = json.load(open(path))
                text = run.get('output_text', '')
                m7_score, hits, total = score_m7(text, qid)
                if m7_score is None:
                    continue
                results.append({
                    'arm': arm, 'qid': qid, 'rep': rep,
                    'M7': round(m7_score, 4),
                    'hits': hits, 'total_patterns': total,
                })
    
    with open('/tmp/score-m7-results.json', 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Per-arm summary
    print(f"{'Arm':<5} {'M7_mean':>8} {'per-rep detail'}")
    for arm in ['S0','S1','S2','S3','S4','S5']:
        arm_r = [r for r in results if r['arm']==arm]
        if not arm_r: continue
        mean = sum(r['M7'] for r in arm_r)/len(arm_r)
        per_q = {}
        for r in arm_r:
            per_q.setdefault(r['qid'], []).append(r['M7'])
        detail = " ".join(f"{q}={sum(v)/len(v):.2f}" for q,v in sorted(per_q.items()))
        print(f"{arm:<5} {mean:>8.3f}  {detail}")
    
    # H4 check: S5 vs S1 on M7
    s1 = sum(r['M7'] for r in results if r['arm']=='S1')/15
    s5 = sum(r['M7'] for r in results if r['arm']=='S5')/15
    s0 = sum(r['M7'] for r in results if r['arm']=='S0')/15
    print(f"\nH4 (S5-S1 on M7): {s5-s1:+.4f}")
    print(f"S0 baseline: {s0:.4f}, S1: {s1:.4f}, S5: {s5:.4f}")
    print("Saved to /tmp/score-m7-results.json")

if __name__ == '__main__':
    main()
