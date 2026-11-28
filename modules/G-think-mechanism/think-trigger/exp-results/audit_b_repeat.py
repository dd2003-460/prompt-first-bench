#!/usr/bin/env python3
# origin: ai
# T8c B 臂复读退化审计（t8c-smoke-rerun-report F2 的前置探针）
# 口径: 每 stage 的 (a) 最长连续重复 5-gram 次数 (b) 重复 5-gram 占比 = 重复token/总token
#       (c) 与前一 stage 的 5-gram 重叠率（跨阶段复读 = 流程级退化信号）
# 产出: 脚本写 t8c-b-repeat-audit.json（结构化数据走脚本落盘，不走模型输出流）
import json, os, collections

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, "raw_outputs_t8c.json")
OUT = os.path.join(BASE, "t8c-b-repeat-audit.json")
ORDER = ["01", "02", "02.5", "03", "04", "04.5"]

def ngrams(text, n=5):
    words = text.split()
    return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]

def audit_sample(sample):
    stages = {}
    prev_grams = None
    for sid in ORDER:
        st = sample.get("stages", {}).get(sid)
        if not st:
            continue
        text = (st.get("content") or "") + " " + (st.get("reasoning") or "")
        grams = ngrams(text)
        if not grams:
            continue
        cnt = collections.Counter(grams)
        dup_grams = sum(c - 1 for c in cnt.values() if c > 1)  # 超出首次出现的 gram 数
        total_words = len(text.split())
        # 最长连续重复: 找最长的 g 使得 g 连续出现 >=2 次（近似: 最大重复次数）
        max_run = max(cnt.values())
        cross = None
        if prev_grams is not None and grams:
            prev_set = set(prev_grams)
            cross = round(sum(1 for g in set(grams) if g in prev_set) / max(1, len(set(grams))), 3)
        stages[sid] = {
            "words": total_words,
            "unique5_gram_ratio": round(1 - dup_grams / max(1, len(grams)), 3),
            "max_5gram_repeat": max_run,
            "cross_stage_overlap": cross,
            "repeat5_logged": st.get("repeat5"),
            "finish": st.get("finish_reason"),
        }
        prev_grams = grams
    return stages

def main():
    data = json.load(open(RAW))
    out = {"note": "B 臂复读退化审计 (F2 前置探针); unique5_gram_ratio 低=复读重; cross_stage_overlap 高=跨阶段复读",
           "samples": {}}
    for i, s in enumerate(data.get("arm_b", []), 1):
        out["samples"][f"run{i}"] = audit_sample(s)
    # 汇总
    summary = {}
    for k, v in out["samples"].items():
        ratios = [st["unique5_gram_ratio"] for st in v.values()]
        crosses = [st["cross_stage_overlap"] for st in v.values() if st["cross_stage_overlap"] is not None]
        summary[k] = {
            "mean_unique5_gram_ratio": round(sum(ratios)/len(ratios), 3) if ratios else None,
            "min_unique5_gram_ratio": min(ratios) if ratios else None,
            "mean_cross_overlap": round(sum(crosses)/len(crosses), 3) if crosses else None,
            "stages_with_repeat5_ge5": sum(1 for st in v.values() if (st["repeat5_logged"] or 0) >= 5),
            "n_stages": len(v),
        }
    out["summary"] = summary
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=1)
    print(f"WROTE {os.path.basename(OUT)}")
    for k, v in summary.items():
        print(k, v)

if __name__ == "__main__":
    main()
