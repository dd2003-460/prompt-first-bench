#!/usr/bin/env python3
"""GPU 建模探针三臂分解分析 (research-agi-budget 子项⑥)。

读 A+B JSON (gpu-model-probe-<date>.json) + C JSON (gpu-model-probe-<date>_C.json),
输出三臂分解:
  A - C = harness 净贡献 (接地+计算)
  B - A = 自审 hook 净贡献 (压缩+排除错误解释)
  B - C = 总提升

判据 (相对有效, 同模型同题面):
  1. free_params  (紧凑性, 启发式上界, 只作相对比)
  2. n_negations  (否定结构数: 显式排除错误解释, B 臂预期更高)
  3. grounded_rate (search 调用中非空结果占比, 仅 A/B 臂)
  4. roofline_hit (final 是否收敛到 BW/权重 型关系, 正则粗判)
用法: python3 q9_gpu_probe_analyze.py <ab_json> <c_json>
"""
import json, re, sys

NEG = re.compile(r"❌|错了|错。|否定|排除|不是.{0,8}主导|并非|wrong|incorrect|misconception", re.I)
ROOFLINE = re.compile(r"带宽\s*[÷/]/?(?:权重|模型|参数量)|BW\s*[÷/]|tok/s\s*[≈≈]\s*B|吞吐\s*[∝≈]\s*带宽|decode.{0,20}(?:带宽|BW)", re.I)

def load(fp):
    d = json.load(open(fp))
    out = {}
    for key, arm in d.get("arms", {}).items():
        eps = arm.get("per_episode", [])
        # 公平基准: 只数 final_formula (公式行), 避免 C 臂一次性记忆倾倒 vs A/B 多轮收敛的混淆
        from q9_gpu_model_probe import count_free_params
        fps = [count_free_params(e.get("final_formula", ""))[0] for e in eps]
        negs = [sum(len(NEG.findall(e.get("final_text", ""))) for _ in [0]) for e in eps]
        # 否定数按 episode 的 final_text
        negs = [len(NEG.findall(e.get("final_text", ""))) for e in eps]
        grounded = []
        for e in eps:
            tot = sum(len(c.get("result_head", "")) and 1 for c in e.get("tool_calls", []) if c.get("name") == "search")
            nonempty = sum(1 for c in e.get("tool_calls", []) if c.get("name") == "search" and c.get("result_head", "") != "(no results)")
            grounded.append(nonempty / tot if tot else None)
        roof = [bool(ROOFLINE.search(e.get("final_formula", "") + e.get("final_text", ""))) for e in eps]
        out[key] = {
            "n": len(eps),
            "fp_mean": sum(fps) / len(fps) if fps else None,
            "fp_list": fps,
            "neg_mean": sum(negs) / len(negs) if negs else None,
            "neg_list": negs,
            "grounded_mean": (sum(g for g in grounded if g is not None) /
                              len([g for g in grounded if g is not None])) if any(g is not None for g in grounded) else None,
            "roofline_hits": sum(roof),
        }
    return out

def main():
    ab, c = load(sys.argv[1]), load(sys.argv[2])
    A = next((v for k, v in ab.items() if "raw" in k), None)
    B = next((v for k, v in ab.items() if "selfaudit" in k), None)
    C = next((v for k, v in c.items() if "noharness" in k), None)
    print(f"{'臂':<14}{'n':>3}{'fp均值':>8}{'fp列表':>14}{'否定均值':>8}{'接地率':>8}{'Roofline命中':>12}")
    for name, x in [("A 裸harness", A), ("B +自审hook", B), ("C 无harness", C)]:
        if not x:
            print(f"{name:<14}  (缺失)"); continue
        gr = f"{x['grounded_mean']:.2f}" if x["grounded_mean"] is not None else "-"
        print(f"{name:<14}{x['n']:>3}{x['fp_mean']:>8.1f}{str(x['fp_list']):>14}{x['neg_mean']:>8.1f}{gr:>8}{x['roofline_hits']:>12}")
    if A and C:
        print(f"\nA - C (harness 净贡献)  Δfp = {C['fp_mean'] - A['fp_mean']:+.1f}  (负=harness 更紧凑)")
    if A and B:
        print(f"B - A (自审 hook 净贡献) Δfp = {A['fp_mean'] - B['fp_mean']:+.1f}  Δ否定 = {B['neg_mean'] - A['neg_mean']:+.1f}")
    if B and C:
        print(f"B - C (总提升)          Δfp = {C['fp_mean'] - B['fp_mean']:+.1f}")
    print("\n注意: free_params 是启发式上界(公式行独立符号数), 只作相对比; 接地率仅 A/B 臂有意义。")

if __name__ == "__main__":
    main()
