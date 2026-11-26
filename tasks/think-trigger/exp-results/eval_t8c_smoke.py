#!/usr/bin/env python3
# origin: ai
# T8c smoke 评估（预注册 §4 Stage 0 机械检查 + 分流判定，判据先 commit 再跑数据）
# 用法: python3 eval_t8c_smoke.py [raw_outputs_t8c.json]
# 口径全部来自 t8c-preregistration.md (commit 8c168c2a4)：
#   - 主指标 s = 1[indeterminate] + 0[A1/A2/A3]（J1 判别器 judge_text，无 LLM）
#   - 断点深度 d: A1=1, A2=2, A3=3, indeterminate=4
#   - 截断样本（任一臂 finish_reason=length）→ 主指标判 indeterminate(截断)，单独计数，
#     不进三型分布比较（预注册 §1 截断处理）
#   - B 臂打分文本 = 全部 stage content 按 01→02→02.5→03→04→04.5 拼接（T8b 报告 L18 口径）
#   - 复读警告 = repeat5>=5（T8b 报告 §4 口径，只报告不判死）
#   - 分流（预注册 §4，pre-commit 不许事后改）：
#       分离迹象 s_B'≥2/3 且 s_A'≤1/3 → 扩 n=9/臂（执行 W1+W2+W3）
#       无分离（两臂 s 均≤1/3 或 B'≤A'）→ 停止，如实报告
#       边界：B' 断点样本全 A3（方向正但 W3 负）→ 结构进步非赢，停止
# 注（pre-data 逻辑澄清，非 post-hoc 修订）：预注册 §4 边界情形原文「s_B'=2/3 且 B' 全是 A3」
#   自相矛盾（全 A3 ⇒ s_B'=0，与 s_B'=2/3 不可共存）。本脚本按唯一自洽解释实现：
#   分离迹象触发时，B' 的**断点样本**（s=0 者）全为 A3（无 A1/A2）→ 判「结构进步非赢」停止。
#   主判据 W1/W2/W3、n=9、power 均不受影响；如需改解释须重新冻结预注册（跑数前）。
# 实现注（2026-11-27 修复）：截断样本 s=0（原实现 s=1 与头部口径矛盾，n=3 截断=0 未暴露；n=9 前修复，冻结判据未动——本修复是口径对齐非判据变更）
import json, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "../../../modules/B-pipeline-ablation/research"))
from correctness_layer_v0 import judge_text

DEPTH = {"A1": 1, "A2": 2, "A3": 3, "indeterminate": 4}
ORDER = ["01", "02", "02.5", "03", "04", "04.5"]

def load(path):
    return json.load(open(path))

def sample_text(sample):
    """A 臂: content+reasoning; B 臂: 全 stage 拼接（T8b 口径）"""
    if sample["arm"] == "A_direct":
        return (sample.get("content") or "") + "\n" + (sample.get("reasoning") or "")
    parts = []
    for sid in ORDER:
        st = sample["stages"].get(sid)
        if not st:
            continue
        txt = (st.get("content") or st.get("reasoning") or "").strip()
        if txt:
            parts.append(f"【阶段{sid}】\n{txt}")
    return "\n\n".join(parts)

def is_truncated(sample):
    if sample["arm"] == "A_direct":
        return sample.get("finish_reason") == "length"
    return any(st.get("finish_reason") == "length" for st in sample["stages"].values())

def evaluate(data):
    rows = []
    for arm_key, arm_name in [("arm_a", "A'"), ("arm_b", "B'")]:
        for s in data.get(arm_key, []):
            text = sample_text(s)
            trunc = is_truncated(s)
            if trunc:
                label, score = "indeterminate(截断)", 0
                depth = None
                note = "截断样本: 主指标判 indeterminate(截断), s=0 排除在三型分布比较外, 单独计数（预注册 §1）"
            else:
                j = judge_text(text)
                label = j["verdict"]
                score = 1 if label == "indeterminate" else 0
                depth = DEPTH[label]
                note = ""
            rows.append({
                "arm": arm_name, "run": s.get("run"),
                "label": label, "s": score, "depth": depth,
                "truncated": trunc, "note": note,
                "completion_tokens": s.get("total_completion_tokens")
                                      or s.get("completion_tokens"),
                "finish": s.get("finish_reason") if s["arm"] == "A_direct"
                          else [st.get("finish_reason") for st in s["stages"].values()],
                "repeat5_max": max([s.get("repeat5", 0)] if s["arm"] == "A_direct"
                                    else [st.get("repeat5", 0) for st in s["stages"].values()]),
            })
    return rows

def decide(rows):
    """预注册 §4 Stage 0 分流（机械执行）"""
    def agg(arm):
        rs = [r for r in rows if r["arm"] == arm]
        # 截断样本单独计数, 不进三型分布比较
        valid = [r for r in rs if not r["truncated"]]
        s_valid = sum(r["s"] for r in valid)
        n_valid = len(valid)
        frac = s_valid / n_valid if n_valid else 0.0
        labels = [r["label"] for r in valid]
        depths = [r["depth"] for r in valid if r["depth"] is not None]
        return {"n_total": len(rs), "n_valid": n_valid,
                "s_frac": frac, "labels": labels,
                "d_mean": sum(depths) / len(depths) if depths else None,
                "n_trunc": sum(1 for r in rs if r["truncated"])}
    a, b = agg("A'"), agg("B'")
    # 机械检查 1: 截断率 ≤50%/臂
    ca = a["n_trunc"] / a["n_total"] <= 0.5 if a["n_total"] else True
    cb = b["n_trunc"] / b["n_total"] <= 0.5 if b["n_total"] else True
    trunc_ok = ca and cb
    # 机械检查 2: judge 全出标签
    judge_ok = all(r["label"] for r in rows)
    # 分流
    if not (a["n_valid"] and b["n_valid"]):
        decision = "不可判（有效样本不足）"
    elif a["s_frac"] <= 1/3 and b["s_frac"] <= 1/3:
        decision = "停止：无分离（两臂 s 均 ≤1/3），效应低于可测下限"
    elif b["s_frac"] >= 2/3 and a["s_frac"] <= 1/3:
        bp_labels = [l for l in b["labels"] if l != "indeterminate"]
        if bp_labels and set(bp_labels) == {"A3"}:
            decision = "停止：边界情形（B' 断点样本全 A3，断点后移但未选对，结构进步非赢）"
        else:
            decision = "扩样 n=9/臂：分离迹象（s_B'≥2/3 且 s_A'≤1/3），执行 W1+W2+W3"
    else:
        decision = "停止：无分离（方向反或不足）"
    return {"A": a, "B": b, "trunc_ok": trunc_ok, "judge_ok": judge_ok,
            "decision": decision}

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else \
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw_outputs_t8c.json")
    # 可选第 2 参 = 输出路径（默认 t8c-smoke-eval.json；B-Rerun 等复用须显式传，防覆盖 smoke 四件套）
    outpath = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.join(os.path.dirname(path), "t8c-smoke-eval.json")
    data = load(path)
    rows = evaluate(data)
    dec = decide(rows)
    out = {"input": path, "rows": rows, "decision": dec,
           "prereg": "t8c-preregistration.md (8c168c2a4) §4 Stage 0"}
    json.dump(out, open(outpath, "w"), ensure_ascii=False, indent=2)
    print(f"{'臂':<3}{'run':<5}{'label':<18}{'s':<3}{'d':<4}{'tok':<7}{'repeat5max':<11}finish")
    for r in rows:
        fin = str(r["finish"])[:40]
        print(f"{r['arm']:<3}{r['run']:<5}{r['label']:<18}{r['s']:<3}"
              f"{str(r['depth']):<4}{str(r['completion_tokens']):<7}"
              f"{r['repeat5_max']:<11}{fin}")
    a, b = dec["A"], dec["B"]
    print(f"\nA': s={a['s_frac']:.3f} ({a['n_valid']} valid/{a['n_total']}, trunc={a['n_trunc']}) "
          f"d_mean={a['d_mean']} labels={a['labels']}")
    print(f"B': s={b['s_frac']:.3f} ({b['n_valid']} valid/{b['n_total']}, trunc={b['n_trunc']}) "
          f"d_mean={b['d_mean']} labels={b['labels']}")
    print(f"机械检查: 截断率≤50%={dec['trunc_ok']}  judge全出标签={dec['judge_ok']}")
    print(f"分流判定: {dec['decision']}")
    ok = dec["trunc_ok"] and dec["judge_ok"]
    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
