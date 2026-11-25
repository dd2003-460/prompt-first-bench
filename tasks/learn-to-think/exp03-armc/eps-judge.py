#!/usr/bin/env python3
# origin: ai · 2026-11-25 · armC' ε_pred 终审判官（机械筛查 HIT 时的语义确认）
# 定位: 两级判读的第二级。第一级 = armc-eps-screen.py 机械筛查（信息论轴 pattern 命中）；
#   机械 0 命中 → 直接判未对齐（不调本判官）；机械 HIT → 本判官确认"结构对齐"而非撞词/鹦鹉学舌。
# 判据来源（预注册, 非事后）:
#   - lossless-criterion-operationalization.md L54: "命中 = 预言与 gold 中某步结构对齐"
#   - 同文件 L42: 结构对齐 = 信息流角色（机制层），非逐字/非表层措辞
#   - preregistration.md L16 gold 原文 + L61 预言判例: "若先验信息量大则优化更易/先验近似0有效则…"
# gold 结构（给判官的比对基准, 2 轴）:
#   轴1 机制层: 优化难 ← 随机 landscape = 非凸优化（为什么难）
#   轴2 信息论层: 难易由信息量决定 ← 先验信息量大/先验近似有效 → 差不多算出来（什么决定难易）
# 判官模型: 27b (8787 唯一 LLM)。自偏风险缓解: ①机械筛查已挡掉 0 命中;
#   ②prompt 显式定义"鹦鹉学舌不算对齐"(复述轴名无可检验结构 = 0); ③D 人工终核保留
#   (lossless L69 双标注者协议: AI 判官先行, D 复核)。
# 用法: python3 eps-judge.py <raw_outputs.json>
#   只对机械筛查 HIT 的样本调 LLM (先跑 armc-eps-screen.py 看哪些 HIT)。
# 鉴别力预注册: 已知正例(构造的真信息论预言)必须 aligned=1; 已知负例(armC run2 几何层预言)必须 0。
import json, sys, time, urllib.request

BASE = "http://127.0.0.1:8787/v1/chat/completions"
MODEL = "qwen3.8-27b-mtp"

GOLD = """D 的后半段 gold（held-out, 判据参照）:
"但是感觉这块优化和信息量有关，差不多算出来（先验近似0有效/先验信息量大）感觉也可以?"
gold 结构拆解:
  轴1 机制层: 优化难 ← 随机 landscape = 非凸优化（回答"为什么难"）
  轴2 信息论层: 难易由信息量决定 ← 先验信息量大 / 先验近似有效 → 差不多算出来（回答"什么决定难易"）"""

JUDGE_PROMPT = """你是严格的实验判官。任务: 判断下面"模型预言"是否与 gold 结构对齐。

{gold}

【对齐的充要条件】(同时满足才 aligned=1):
1. 预言含可检验的"如果X则Y"结构（有明确条件X和可观察结论Y, 不是空泛断言）
2. 其因果机制落在 gold 轴2（信息量/先验决定难易）——即预言的X或Y涉及"先验信息量大小/先验近似是否有效/问题自带信息多少"如何影响"好不好算/要多少计算"
3. 是真推导不是鹦鹉学舌: 只复述"与信息量有关/先验信息量大"而没有可检验结构或条件边界 → aligned=0

【不算对齐的情形】(即使出现"信息量/先验"字样):
- 几何层预言（条件数/曲率/batch噪声/强凸性决定难易）——这是 gold 轴1 之下的子层, 不是轴2
- 混沌/动力学域（李雅普诺夫/吸引子/相空间）
- 空泛复述: "难易与信息量有关" 但没有"如果X则Y"的可检验形式

【模型预言】
{pred}

只回答 JSON: {{"aligned": true/false, "prediction_structure": true/false, "axis": "轴1/轴2/无", "reason": "一句话判据依据"}}"""


def call_judge(pred_text):
    payload = json.dumps({
        "model": MODEL,
        "messages": [{"role": "user", "content": JUDGE_PROMPT.format(gold=GOLD, pred=pred_text[:3000])}],
        "temperature": 0.0,
        "max_tokens": 2000,  # 2026-11-25 21:43 修: 300→2000, 27b 思考模型 CoT 超 300 截断致 JSON 丢失 (discrim-test 2/2 parse_error)
    }).encode("utf-8")
    for attempt in range(1, 4):
        try:
            req = urllib.request.Request(BASE, data=payload, headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=300) as r:
                d = json.loads(r.read().decode("utf-8"))
            txt = d["choices"][0]["message"].get("content", "").strip()
            # 提取 JSON (容忍 markdown 围栏 + CoT 前缀): 取最后一个能 parse 且含 aligned 的扁平 JSON
            # (原贪婪 \{.*\} 从 CoT 首个 { 起匹配, 若 CoT 含花括号则 json.loads 失败)
            import re
            cand = None
            for m in re.finditer(r"\{[^{}]*\}", txt):
                try:
                    c = json.loads(m.group(0))
                    if isinstance(c, dict) and "aligned" in c:
                        cand = c
                except Exception:
                    pass
            return cand if cand is not None else {"raw": txt, "parse_error": True}
        except Exception as e:
            print(f"[judge] attempt {attempt}: {repr(e)}", flush=True)
            time.sleep(attempt * 5)
    return {"error": "all attempts failed"}


def main():
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    d = json.load(open(sys.argv[1]))
    samples = d["samples"] if isinstance(d, dict) and "samples" in d else d
    out = []
    for s in samples:
        pred = (s.get("content") or "") + "\n[reasoning]\n" + (s.get("reasoning") or "")
        verdict = call_judge(pred)
        out.append({"arm": s.get("arm"), "run": s.get("run"), "verdict": verdict})
        print(f"{s.get('arm')}{s.get('run')}: aligned={verdict.get('aligned')} "
              f"structure={verdict.get('prediction_structure')} axis={verdict.get('axis')} "
              f"| {verdict.get('reason', verdict.get('raw', ''))[:100]}", flush=True)
    result = {"model": MODEL, "temperature": 0.0, "criterion": "lossless L54 结构对齐 + prereg L61 判例",
              "n_aligned": sum(1 for o in out if o["verdict"].get("aligned")),
              "verdicts": out,
              "judged_at": time.strftime("%Y-%m-%d %H:%M:%S %z")}
    dest = sys.argv[1].replace(".json", "_judge.json")
    with open(dest, "w") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\n[saved] {dest} | n_aligned={result['n_aligned']}/{len(out)}")


if __name__ == "__main__":
    main()
