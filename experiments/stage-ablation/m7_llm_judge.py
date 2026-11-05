"""M7 LLM judge: 二次判定 Q3/Q4 全零是真实还是正则 miss。

对每个产物，让 27B 回答：模型是否"裁决"了以下矛盾点（不是提到，而是给出否定/限定/条件化判断）？
输出 JSON: {qid, arm, rep, adjudications: [{point, verdict: yes/no/partial, evidence}]}
"""
import json, os, time, urllib.request

VLLM = "http://localhost:8787/v1/chat/completions"

# 每题的矛盾裁决点（自然语言描述，给 LLM judge 用）
POINTS = {
    'Q3': [
        "SLO（TTFT/TPOT/并发）应作为可行域约束处理，而不是成本项——不达 SLO 的框架无论多快都应直接排除",
        "厂商标称的延迟/吞吐值与实测有显著差距（2-3倍），不能直接当设计依据",
        "框架不支持目标硬件时应一票否决，先过可行域再比性能",
    ],
    'Q4': [
        "标称 128K 上下文不等于 128K token 都有效——长上下文中段定位能力显著衰减（U型/首尾偏差），这是长上下文方案最常被高估的能力",
        "只比较边际成本（每次问答的 token 费）会无条件偏向 RAG，漏掉 RAG 的一次性索引/调参建设成本；只看建设成本会无条件偏向长上下文",
        "RAG 检索到'相关但不够'的片段时模型会强行作答产生幻觉；长上下文因信息完整幻觉更低但受定位衰减影响——两方案幻觉率无先验公式，必须实测",
    ],
}

JUDGE_PROMPT_HEAD = """你是一个严格的评审。下面是一个 AI 系统对技术选型问题的回答。

你的任务：判断该回答是否对以下每个"矛盾裁决点"做出了**裁决**（明确否定某个常见误读、或给出限定/条件化判断），而不仅仅是**提到**相关概念或把它列为待查缺口。

判定标准：
- **yes** = 回答明确指出某说法是错的/被高估的/有条件的，并给出理由
- **partial** = 暗示了裁决但没有明确说出来
- **no** = 只提到概念、或列为待研究缺口、或完全没涉及

对每个点输出一个对象: point_id(编号), verdict(yes/partial/no), evidence(引用回答中的原文片段,不超过50字)

---
问题背景: __QID_CONTEXT__

待判定的矛盾裁决点:
__POINTS_LIST__

---
AI 系统的回答:
__OUTPUT_TEXT__

---
只输出 JSON 数组，不要其他文字。"""

def call_vllm(prompt, max_tokens=2000):
    payload = json.dumps({
        "model": "qwen3.8-27b",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.0,
        "max_tokens": max_tokens,
    }).encode()
    req = urllib.request.Request(VLLM, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        d = json.loads(resp.read())
    return d["choices"][0]["message"]["content"]

def parse_json_array(text):
    # strip code fences if present
    t = text.strip()
    if t.startswith("```"):
        t = t.split("\n", 1)[1] if "\n" in t else ""
        if t.endswith("```"):
            t = t[:-3]
    # find first [ ... ]
    start = t.find("[")
    end = t.rfind("]")
    if start >= 0 and end > start:
        return json.loads(t[start:end+1])
    return None

def main():
    results = []
    for qid in ['Q3', 'Q4']:
        context = {
            'Q3': "为固定 GPU (RTX 3090×4) + 27B 模型选推理服务框架 (vLLM/TGI/transformers/SGLang)，使每千输出 token 成本最低且满足在线 SLO。",
            'Q4': "企业知识库问答 (500万 token 文档)，选数据处理方案 (纯RAG/纯长上下文/混合)，使每千次正确回答成本最低且答案可引用出处。",
        }[qid]
        points_list = "\n".join(f"{i+1}. {p}" for i, p in enumerate(POINTS[qid]))
        
        for arm in ['S0','S1','S2','S3','S4','S5']:
            for rep in [1,2,3]:
                path = f'runs/{arm}-{qid}-r{rep}.json'
                if not os.path.exists(path):
                    continue
                run = json.load(open(path))
                text = run.get('output_text', '')
                prompt = JUDGE_PROMPT_HEAD.replace("__QID_CONTEXT__", context).replace("__POINTS_LIST__", points_list).replace("__OUTPUT_TEXT__", text[:12000])
                
                try:
                    raw = call_vllm(prompt)
                    parsed = parse_json_array(raw)
                    if parsed is None:
                        print(f"WARN {arm}-{qid}-r{rep}: unparseable, raw={raw[:100]}")
                        results.append({"arm": arm, "qid": qid, "rep": rep, "error": "unparseable", "raw": raw[:500]})
                        continue
                    # score: yes=1, partial=0.5, no=0
                    scores = []
                    for item in parsed:
                        v = item.get('verdict', 'no').lower()
                        scores.append({'point_id': item.get('point_id'), 'verdict': v, 
                                       'evidence': item.get('evidence','')[:80],
                                       'score': {'yes':1.0,'partial':0.5,'no':0.0}.get(v,0.0)})
                    m7_llm = sum(s['score'] for s in scores)/len(scores) if scores else 0.0
                    results.append({"arm": arm, "qid": qid, "rep": rep, "M7_llm": round(m7_llm,3), "adjudications": scores})
                    print(f"{arm}-{qid}-r{rep}: M7_llm={m7_llm:.2f} {[s['verdict'][0] for s in scores]}")
                except Exception as e:
                    print(f"ERR {arm}-{qid}-r{rep}: {e}")
                    results.append({"arm": arm, "qid": qid, "rep": rep, "error": str(e)})
                time.sleep(0.5)
    
    with open('/tmp/m7-llm-judge-results.json', 'w') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Summary
    print("\n=== M7 LLM judge per-arm (Q3+Q4) ===")
    for arm in ['S0','S1','S2','S3','S4','S5']:
        arm_r = [r for r in results if r['arm']==arm and 'M7_llm' in r]
        if arm_r:
            mean = sum(r['M7_llm'] for r in arm_r)/len(arm_r)
            q3 = [r['M7_llm'] for r in arm_r if r['qid']=='Q3']
            q4 = [r['M7_llm'] for r in arm_r if r['qid']=='Q4']
            print(f"{arm}: mean={mean:.3f}  Q3={sum(q3)/len(q3):.2f}  Q4={sum(q4)/len(q4):.2f}")
    print("\nSaved to /tmp/m7-llm-judge-results.json")

if __name__ == '__main__':
    main()
