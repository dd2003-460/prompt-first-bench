#!/usr/bin/env python3
# origin: ai
# GPU 选卡题 · 机械连续 judge（rubric_gpu_mech.md，对齐 score_m7.py 形态）
# 确定性脚本：f(输出)→连续分数，无 LLM 参与，可复现，hits 可审计
# 用法: python3 judge_gpu_mech.py <raw_outputs.json> [--arm A|B|both]
import json, re, sys, os

# ---- gold 参照集（来源声明见 rubric_gpu_mech.md）----
SKU_WHITELIST = {
    "消费级": ["4090","3090","4080","3060","4060","RTX 6000 Ada","A6000"],
    "数据中心": ["A100","H100","H200","L40S","L40","A40","A800","H800"],
    "AMD": ["MI250X","MI300X","MI300A"],
    "非典型": ["FPGA","TPU","Mac","M1 ","M2 ","M3 ","M4 ","Apple","CPU"],
}
SKU_TARGET = 12  # 饱和点

DIMENSIONS = [
    ("功耗/散热", r"功耗|散热|TDP|瓦|W\b"),
    ("显存带宽", r"显存带宽|HBM|GB/s|带宽"),
    ("PCIe/拓扑", r"PCIe|插槽|x16|拓扑"),
    ("互联带宽", r"NVLink|InfiniBand|卡间|互联"),
    ("软件栈/驱动", r"软件栈|驱动|CUDA|cuDNN|ROCm|vLLM|TensorRT"),
    ("二手/矿卡风险", r"二手|矿卡|翻新"),
    ("价格波动", r"价格波动|涨价|降价|行情|供需"),
    ("CPU/内存", r"CPU|内存|RAM|DDR"),
    ("机箱/供电", r"机箱|电源|PSU|供电|风道"),
    ("量化方法", r"GPTQ|AWQ|GGUF|量化方法|量化算法"),
]
DIM_TARGET = 10

PATTERNS = [
    ("P1容量下限", r"(32\s?K|32768).{0,60}(上下文|context|KV)"),
    ("P2精度质量论证", r"(BF16|FP8|INT8|NVFP4|W4|量化|精度).{0,120}(质量损失|可接受|困惑度|perplexity|下降|损失)"),
    ("P3单多卡TCO", r"(单卡|多卡|2\s*[×x*]).{0,120}(TCO|总成本|成本)"),
    ("P4数字溯源", r"(\[待核验\]|待核验|来源[:：]|凭记忆|刚查|已验证)"),
    ("P5条件性推荐", r"(若|如果|取决于|在.{0,10}条件下|前提|假设).{0,80}(推荐|选择|建议)"),
    ("P6非典型方案", r"(FPGA|CPU\s*\+|大内存|二手|矿卡|混合架构|非典型|TPU|Mac|Apple)"),
]

def s1_coverage(t):
    hits = []
    for cat, skus in SKU_WHITELIST.items():
        for sku in skus:
            if re.search(re.escape(sku), t):
                hits.append(f"{cat}:{sku}")
    n = len(hits)
    return min(n / SKU_TARGET, 1.0), hits, n

def s2_dimensions(t):
    hits = []
    for name, pat in DIMENSIONS:
        if re.search(pat, t, re.I):
            hits.append(name)
    return len(hits) / DIM_TARGET, hits, len(hits)

def s3_compliance(t):
    hits = []
    for name, pat in PATTERNS:
        if re.search(pat, t, re.I | re.S):
            hits.append(name)
    return len(hits) / len(PATTERNS), hits, len(hits)

def judge(text):
    s1, h1, n1 = s1_coverage(text)
    s2, h2, n2 = s2_dimensions(text)
    s3, h3, n3 = s3_compliance(text)
    overall = (s1 + s2 + s3) / 3
    return {"overall": round(overall, 4),
            "S1_sku_coverage": round(s1, 4), "S1_n": n1, "S1_hits": h1,
            "S2_dimension": round(s2, 4), "S2_n": n2, "S2_hits": h2,
            "S3_compliance": round(s3, 4), "S3_n": n3, "S3_hits": h3}

def arm_texts(d):
    """返回 {label: text}"""
    out = {}
    for i, a in enumerate(d.get("arm_a", []), 1):
        out[f"A{i}"] = a.get("content", "")
    for i, b in enumerate(d.get("arm_b", []), 1):
        st = b.get("stages", {})
        parts = [f"【阶段{s}】\n" + st.get(s, {}).get("content", "")
                 for s in ["01", "02", "02.5", "03", "04", "04.5"]]
        out[f"B{i}"] = "\n\n".join(parts)
    return out

def main():
    path = sys.argv[1]
    d = json.load(open(path))
    texts = arm_texts(d)
    results = {k: judge(v) for k, v in texts.items()}
    outpath = path.replace(".json", "_mech_scores.json")
    json.dump(results, open(outpath, "w"), ensure_ascii=False, indent=2)
    # 汇总
    for arm in ("A", "B"):
        ks = [k for k in results if k.startswith(arm)]
        if not ks: continue
        mean = sum(results[k]["overall"] for k in ks) / len(ks)
        per = " ".join(f"{k}={results[k]['overall']:.3f}" for k in sorted(ks))
        s1m = sum(results[k]["S1_sku_coverage"] for k in ks)/len(ks)
        s2m = sum(results[k]["S2_dimension"] for k in ks)/len(ks)
        s3m = sum(results[k]["S3_compliance"] for k in ks)/len(ks)
        print(f"{arm}: overall_mean={mean:.4f} (S1={s1m:.3f} S2={s2m:.3f} S3={s3m:.3f}) | {per}")
    a = [results[k]["overall"] for k in results if k.startswith("A")]
    b = [results[k]["overall"] for k in results if k.startswith("B")]
    if a and b:
        print(f"\nDelta(B-A) = {sum(b)/len(b)-sum(a)/len(a):+.4f}")
    print(f"WROTE {outpath}")

if __name__ == "__main__":
    main()
