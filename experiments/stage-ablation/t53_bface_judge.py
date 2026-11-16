#!/usr/bin/env python3
"""T53-B12 B-face 判分：核心数字 0.5 + 口径 0.5，qwen2.5-7b @1234，n=3 median。
口径来源：tasks/B-pipeline-ablation/TASK-B12-t53-deepresearch-bench-spec.md 验收标准 2/3
（异族 judge B-face 7b 打分 0-1，数字正确 0.5 + 对比/单位正确 0.5，n=3 median）。
gold 要点：questions/T53-B12-new3-gold.md（判分用，不进 prompt）。
用法：python3 t53_bface_judge.py <qid> <answer_file> [N]
"""
import json, os, re, sys, time, urllib.request, statistics

HERE = os.path.dirname(os.path.abspath(__file__))
JUDGE_URL = "http://localhost:1234/v1/chat/completions"
JUDGE_MODEL = "qwen2.5-7b-original"
GOLD_FILE = os.path.join(HERE, "questions/T53-B12-new3-gold.md")


def bface_call(prompt, max_tokens=3000):
    payload = json.dumps({
        "model": JUDGE_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0,
        "max_tokens": max_tokens,
    }).encode()
    req = urllib.request.Request(JUDGE_URL, data=payload, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = json.loads(resp.read())
    return data["choices"][0]["message"]["content"]


def load_gold_points(qid):
    """从 T53-B12-new3-gold.md 解析指定 qid 的 gold 要点行。"""
    text = open(GOLD_FILE).read()
    # 定位 "## Q* `<qid>` —" 小节，取到下一个 "## " 或 "## L1" 为止
    m = re.search(rf"^## [^\n]*`{qid}`[^\n]*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    if not m:
        raise ValueError(f"qid {qid!r} not found in {GOLD_FILE}")
    section = m.group(1)
    points = [ln.strip()[2:] for ln in section.splitlines() if ln.strip().startswith("- ")]
    if not points:
        raise ValueError(f"no gold points parsed for {qid}")
    return points


def judge_t53(qid, answer, gold_points):
    """单次 B-face 判分。返回 (total 0/0.5/1.0 或 None, detail dict)。"""
    pts = "\n".join(f"{i+1}. {p}" for i, p in enumerate(gold_points))
    prompt = f"""你是研究质量评审。任务：对【候选回答】按两个维度打分，满分 1.0。

维度1 核心数字（0 或 0.5 分）：
- 对照 gold 要点逐条检查：候选回答中的核心数字是否正确（允许 ±5% 误差，或同源不同年份并列给出）
- 所有核心数字正确 → 0.5 分；任一核心数字明显错误 → 0 分

维度2 对比/单位/口径（0 或 0.5 分）：
- 分母口径是否明确（产量 vs 销量 / 营收分母 / 财年截止日）
- 来源是否可溯（用了哪个来源、为什么选它）
- 来源不一致时是否说明口径差异（如中汽协 vs 海关）
- 全部满足 → 0.5 分；任一缺失 → 0 分

只输出 JSON：{{"core_numbers": 0|0.5, "caliber": 0|0.5, "total": 0|0.5|1.0, "core_reason": "一句话", "caliber_reason": "一句话", "evidence": ["候选回答中的关键数字与口径原文片段"]}}

【Gold 要点】
{pts}

【候选回答】
{answer[:12000]}"""
    try:
        raw = bface_call(prompt)
        m = re.search(r"\{.*\}", raw, re.DOTALL)
        if m:
            d = json.loads(m.group(0))
            total = d.get("total")
            if total is None:
                total = (d.get("core_numbers") or 0) + (d.get("caliber") or 0)
            return float(total), d
        return None, {"parse_error": raw[:300]}
    except Exception as e:
        return None, {"error": f"{type(e).__name__}: {e}"}


def main():
    qid = sys.argv[1]
    answer_file = sys.argv[2]
    N = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    answer = open(answer_file).read()
    if answer.startswith("{"):
        d = json.loads(answer)
        answer = d.get("answer") or d.get("output_text") or answer
    gold_points = load_gold_points(qid)
    print(f"B-face judge: {qid} N={N} gold_points={len(gold_points)}", flush=True)
    scores, details = [], []
    t0 = time.time()
    for i in range(N):
        sc, det = judge_t53(qid, answer, gold_points)
        scores.append(sc)
        details.append(det)
        print(f"run {i+1}/{N}: bface={sc} | core={det.get('core_reason','')[:50]} | caliber={det.get('caliber_reason','')[:50]} ({time.time()-t0:.0f}s)", flush=True)
        time.sleep(1)
    valid = [s for s in scores if s is not None]
    med = statistics.median(valid) if valid else None
    print(f"\n=== RESULT ({qid}) ===")
    print(f"scores = {scores}")
    print(f"median = {med} (valid {len(valid)}/{N})")
    out = {
        "qid": qid, "n": N, "scores": scores, "median": med,
        "details": details, "wall_s": round(time.time() - t0, 1),
        "judge": f"{JUDGE_MODEL} @1234",
    }
    out_path = f"runs-s5-sm-{qid}-bface.json"
    json.dump(out, open(out_path, "w"), ensure_ascii=False, indent=2)
    print(f"saved → {out_path}")


if __name__ == "__main__":
    main()