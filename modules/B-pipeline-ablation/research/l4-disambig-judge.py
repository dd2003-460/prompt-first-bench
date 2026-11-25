#!/usr/bin/env python3
"""L4-disambig 消歧义实验判读（2026-11-25，预注册口径 tasks/l4-disambig-prereg-20261125.md）

判别 H1 残留机制：候选生成缺口 vs 推理能力缺口。
题面消歧三处（64K 定值/候选固定 5 类/c_pass 口径），卡数留自由变量（1-8）。

判读（预注册冻结，不许事后改）：
  A: 结论区出现 4 卡配置（任意卡型×4）→ 候选生成缺口坐实，H1 关闭
  B: 结论区仍是 1-2 卡 → 更深机制（H1-lite 复活）
  C: 出现 4 卡但非 3090 → 部分 A（卡型选择偏差）
  D: run 失败/无结论区 → 无效

口径要点（2026-11-25 教训）：
  - 结论区 = synth 文件 answer 最后 2000 字符（非 synth 版 answer 字段恒空，
    见 l4-zero-convergence.py 同日修复；读错文件 = 空串假阳性）
  - 4 卡 regex 泛化到 5 类候选卡型（3090/V100/M2Ultra/L40S/A100），
    基础口径同 tjudge1_formula.l4_check（卡型号×N / N×卡型号 / 四张）
  - 机械判定，无 LLM，bias-immune

用法: python3 l4-disambig-judge.py [run_dir]
  run_dir 默认 experiments/stage-ablation（找 runs-s5-sm-l4-disambig-synth.json）
"""
import json, glob, os, re, sys

CARD_TYPES = ["RTX 3090", "3090", "V100", "M2 Ultra", "M2Ultra", "L40S", "A100"]

def combo4_regex(card):
    """单卡型的 4 卡组合 regex（基础口径同 l4_check，N=4，紧邻形式，无 gap）。

    覆盖 5 种自然写法：card×4 / ×4 card / 4× card / 四张 card / 4 张 card。
    注意: rf-string 里字面花括号须写成 {{}}，这里刻意不用 {0,N} gap（越界 l4_check
    口径且有误报风险），全用紧邻匹配。
    """
    c = re.escape(card)
    return re.compile(
        rf"{c}\s*(?:\(二手\)|\(全新\)|\(used\)|\(new\))?\s*[×xX*]\s*4(?!\d)"  # card×4
        rf"|[×xX*]\s*4\s*[×xX*]?\s*{c}"                                       # ×4 card
        rf"|\b4\s*[×xX*]\s*{c}"                                               # 4× card
        rf"|四张\s*{c}|{c}\s*四张"                                             # 四张 card / card 四张
        rf"|\b4\s*张\s*{c}|{c}\s*4\s*张"                                       # 4 张 card / card 4 张
    )

def judge(synth_path, tree_path):
    out = {"synth": os.path.basename(synth_path)}
    d = json.load(open(synth_path))
    a = (d.get("answer") or "").strip()
    out["answer_len"] = len(a)
    if not a:
        # 回退: synth 无 answer 时看非 synth 版（可能 run 失败）
        out["verdict"] = "D"
        out["reason"] = "synth answer 为空（run 失败/无结论区）"
        return out
    tail = a[-2000:]
    # 主判读: 结论区 4 卡组合
    hits4 = {}
    for card in CARD_TYPES:
        m = combo4_regex(card).findall(tail)
        if m:
            hits4[card] = m
    # 结论区 1-2 卡组合（B 判据）
    hits12 = {}
    for card in CARD_TYPES:
        c = re.escape(card)
        m = re.findall(rf"{c}\s*[×xX*]\s*[12](?!\d)|[×xX*]\s*[12]\s*{c}", tail)
        if m:
            hits12[card] = m
    if hits4:
        cards4 = list(hits4.keys())
        is_3090 = any("3090" in c for c in cards4)
        out["verdict"] = "A" if is_3090 else "C"
        out["reason"] = "结论区 4 卡: %s" % cards4
    elif hits12:
        out["verdict"] = "B"
        out["reason"] = "结论区 1-2 卡: %s" % list(hits12.keys())
    else:
        # 结论区既无 4 卡也无 1-2 卡显式组合 → 提取含推荐/结论的行供人工核对
        concl = [l.strip() for l in tail.split("\n")
                 if re.search(r"(推荐|最优|最终|结论|性价比)", l)][:6]
        out["verdict"] = "B?"
        out["reason"] = "结论区无显式 N×卡型组合，需人工核对结论行"
        out["concl_lines"] = concl
    # 次级观测
    out["tail_4card_hits"] = hits4
    out["tail_12card_hits"] = hits12
    # 64K 锚
    out["ctx64k_mentioned"] = bool(re.search(r"64\s*K|64K|65536", a))
    out["ctx32k_mentioned"] = bool(re.search(r"32\s*K|32K|32768", a))
    # c_pass 口径
    out["c_per_task_mentioned"] = bool(re.search(r"[¢$]\s*/\s*(task|req)|c_pass|cost.?per", a, re.I))
    # 树内 4 卡候选节点数
    if tree_path and os.path.exists(tree_path):
        td = json.load(open(tree_path))
        claims = " ".join((nd.get("claim") or "") + " " + (nd.get("evidence") or "")
                          for nd in td.get("nodes", []))
        n4 = sum(len(combo4_regex(c).findall(claims)) for c in CARD_TYPES)
        out["tree_4card_mentions"] = n4
        out["n_nodes"] = len(td.get("nodes", []))
        out["final_state"] = td.get("final_state")
    return out

def main():
    run_dir = sys.argv[1] if len(sys.argv) > 1 else "experiments/stage-ablation"
    cands = sorted(glob.glob(os.path.join(run_dir, "runs-s5-sm-l4-disambig-synth.json")))
    if not cands:
        print("未找到 runs-s5-sm-l4-disambig-synth.json（run 未完成？）")
        sys.exit(1)
    synth = cands[-1]
    tree = synth.replace("-synth.json", ".json")
    r = judge(synth, tree)
    print(json.dumps(r, ensure_ascii=False, indent=2))
    v = r["verdict"]
    print("\n=== 判读: %s ===" % v)
    print(r["reason"])
    if v == "A":
        print("→ 候选生成缺口坐实: 给足候选+口径后模型能到 4 卡。L4 0/21 主因 = 原题面框架 prime ≤2 卡 + 候选自搜。H1 关闭。")
    elif v == "C":
        print("→ 部分 A: 候选生成 OK、卡型选择仍有偏差（口径/规格细节问题），比 A 弱一档。")
    elif v == "B":
        print("→ 更深机制: 消歧后仍不到 4 卡。缺口不止候选生成，还有口径内推理/权衡（H1-lite 复活）。下一步 oracle-parent (O2)。")
    elif v == "B?":
        print("→ 结论区无显式组合，人工核对 concl_lines 后定 A/B/C。")
    elif v == "D":
        print("→ 无效: 重跑一次（换 seed 或 budget 150），仍失败则记 artifact 不判读。")

if __name__ == "__main__":
    main()
