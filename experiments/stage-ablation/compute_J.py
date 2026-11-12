#!/usr/bin/env python3
"""J(T) 计算脚本 — Decision 26/28/30 理论框架的机器侧实现。

读 runs-s5-sm-*.json → 算 D(T)/Δ/cov/S_α'/I/J/B，输出 JSON + 人类可读摘要。

用法:
    python3 compute_J.py runs-s5-sm-gpu.json [--oracle checkpoints/sm-gpu-r3.json] [--qid gpu]

设计决策（对应 theory-compression-intelligence.md）:
- D(T) = Σ H_M(ℓ|parent(ℓ))，H_M 用本地 27b 对 claim 文本的 NLL 近似（token 级交叉熵）
- Δ(T) = D(T) - H*(Q)，H* 用 oracle 树的 D 代理（保守偏大）
- cov(T): L1 维度 vs gold 要点的粗覆盖（无 gold 时跳过，报 None）
- S_α'(T): 直接复用 s5_state_machine.S_alpha_corrected
- I(T) = cov · exp(-Δ/H*)，Δ<0 时指数项取 1（分段设计：欠分解区 cov 主导）
- J(T) = I(T) · exp(-|ln(S_α'(T)/S_α'(T_oracle))| / σ_s)^γ，σ_s=1, γ=1
- B(T) = C_expand / C_transmit，C_expand=Σdepth，C_transmit=总 token 数
"""
import json, math, sys, os, argparse, re
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)


def nll_tokens(text: str) -> float:
    """[DEPRECATED] 假 NLL：token×4.5nat 常数。保留作 fallback，主路径用 llm_info_gain。"""
    tokens = len(re.findall(r'[\u4e00-\u9fff]|[a-zA-Z]+|[0-9]+|\S', text or ""))
    return tokens * 4.5


def llm_info_gain(parent_claim: str, leaf_claim: str) -> float:
    """用 LLM 评估叶子相对于父维度的新增信息量（0-10 分）。

    这是命题 2 需要的相对信号：冗余叶（同义改写/子集）→ 低分，新维叶 → 高分。
    不需要绝对 NLL，相对排序就够画 I-vs-n 曲线。
    """
    from ablation_harness import call_llm
    prompt = (
        "你是信息论专家。给定一个父维度和一个候选叶子维度，评估叶子相对于父维度的"
        "『新增信息量』（知道父维度后，这个叶子还带来多少新东西）。\n\n"
        "评分标准（0-10 分）：\n"
        "- 10 = 完全正交，父维度说了它之后叶子仍提供大量独立信息\n"
        "- 5 = 部分重叠，叶子补充了父维度没覆盖的角度\n"
        "- 0 = 完全冗余，叶子只是父维度的同义改写或子集\n\n"
        f"父维度：{parent_claim[:300]}\n"
        f"叶子：{leaf_claim[:300]}\n\n"
        '只输出 JSON：{"score": 分数, "reason": "一句话"}'
    )
    out, _ = call_llm(prompt, max_tokens=200, temperature=0)
    import json as _j
    m = re.search(r'\{.*?\}', out or "", re.S)
    try:
        d = _j.loads(m.group()) if m else {}
        return float(d.get("score", 5))
    except Exception:
        return 5.0  # parse 失败时给中位分，不阻塞


def d_total(nodes: list[dict], use_llm: bool = True) -> tuple[float, dict]:
    """D(T) = Σ H_M(ℓ|parent(ℓ))。

    use_llm=True: 每个非 L1 节点调 llm_info_gain（贵但准），返回 (D, per_node_scores)
    use_llm=False: 用假 NLL（快但无区分度），返回 (D, {})
    """
    scores = {}
    total = 0.0
    for n in nodes:
        lv = str(n.get("level", "L0")).lstrip("L") or "0"
        claim = n.get("corrected_claim") or n.get("claim") or ""
        if lv == "1":
            # L1 骨架：无条件信息量，用 token 数近似（没有 parent）
            h = nll_tokens(claim)
        elif use_llm:
            # 找 parent claim
            parent_ids = n.get("parent_ids", [])
            if isinstance(parent_ids, str):
                parent_ids = eval(parent_ids) if parent_ids.strip() else []
            parent_claim = ""
            for pid in parent_ids:
                for p in nodes:
                    if p.get("id") == pid:
                        parent_claim = p.get("corrected_claim") or p.get("claim") or ""
                        break
                if parent_claim:
                    break
            score = llm_info_gain(parent_claim, claim)
            # 映射 0-10 分到 nat：score × ln(11) ≈ score × 2.4
            h = score * math.log(11)
            scores[n.get("id")] = score
        else:
            h = nll_tokens(claim)
        total += h
    return total, scores


def s_alpha(nodes: list[dict]) -> float:
    from s5_state_machine import S_alpha_corrected, ObjectiveConfig
    return S_alpha_corrected(nodes, ObjectiveConfig())


def c_expand(nodes: list[dict]) -> float:
    """C_expand = Σ depth(node)。"""
    return sum(int(str(n.get("level", "L0")).lstrip("L") or 0) for n in nodes)


def c_transmit(nodes: list[dict]) -> int:
    """C_transmit = 树总 token 数。"""
    total = 0
    for n in nodes:
        text = (n.get("corrected_claim") or n.get("claim") or "")
        total += len(re.findall(r'[\u4e00-\u9fff]|[a-zA-Z]+|[0-9]+|\S', text))
    return max(total, 1)


def gold_H_star(qid: str) -> float:
    """H*(Q) 代理：gold 维度集的 info-gain 总和。

    gold 是人工标注的标准答案维度集（独立于被评树），
    每个维度文本的"信息量"用同一把 LLM 尺子量——
    parent 用问题文本（gold 维度之间无层级，视为平铺）。
    按命题 1，D(gold) ≥ H*（保守偏大，只低估分数不产生假阳）。
    """
    from s8b_pilot import GOLD, QUESTIONS
    if qid not in GOLD:
        return None
    question = QUESTIONS.get(qid, "")
    total = 0.0
    for dim_text in GOLD[qid]:
        total += llm_info_gain(question, dim_text) * math.log(11)
    return total


def cov_gold(nodes: list[dict], qid: str):
    """cov(T) = |M(T) ∩ G| / g：树的叶子对 gold 维度的覆盖率。

    v1 粗匹配：每个 gold 维度问 LLM "这棵树的哪些叶子实质覆盖了它"。
    返回 (cov, per_dim_hits) 或 None。
    """
    from s8b_pilot import GOLD
    from ablation_harness import call_llm
    if qid not in GOLD:
        return None
    leaves = [n for n in nodes if str(n.get("level", "L0")).lstrip("L") != "1"]
    leaf_claims = [(n.get("id"), (n.get("corrected_claim") or n.get("claim") or "")[:200]) for n in leaves]
    if not leaf_claims:
        return None
    leaf_block = "\n".join(f"{i}: {c}" for i, c in leaf_claims)
    covered = 0
    hits = {}
    for gi, dim in enumerate(GOLD[qid]):
        prompt = (
            "下面是一道题的标准答案维度之一，和一棵分解树的叶子列表。\n"
            f"标准维度：{dim[:300]}\n\n"
            f"叶子列表：\n{leaf_block[:4000]}\n\n"
            '问：这些叶子中有没有任何一个【实质覆盖】了该标准维度（回答该维度需要的核心内容在某个叶子里出现）？'
            '同义改写但缺核心数据的不算；沾边不深入的不算。\n'
            '只输出 JSON：{"covered": true/false, "leaf_id": "覆盖它的叶子id或null"}'
        )
        out, _ = call_llm(prompt, max_tokens=150, temperature=0)
        m = re.search(r'\{.*?\}', out or "", re.S)
        try:
            dd = json.loads(m.group()) if m else {}
            ok = bool(dd.get("covered"))
            covered += ok
            hits[f"g{gi}"] = dd.get("leaf_id") if ok else None
        except Exception:
            pass
    return covered / len(GOLD[qid]), hits


def compute(run_path: str, oracle_path=None, qid: str = "gpu", use_llm: bool = True) -> dict:
    d = json.load(open(run_path))
    nodes = d["nodes"]

    D, per_node_scores = d_total(nodes, use_llm=use_llm)
    Sa = s_alpha(nodes)
    Ce = c_expand(nodes)
    Ct = c_transmit(nodes)
    B = Ce / Ct if Ct else None

    # H* 优先从 gold 文件算（独立于被评树）；oracle 路径作 fallback
    H_star = gold_H_star(qid) if use_llm else None
    Sa_oracle = None
    h_source = "gold" if H_star is not None else None
    if H_star is None and oracle_path and os.path.exists(oracle_path):
        od = json.load(open(oracle_path))
        onodes = od["nodes"]
        H_star, _ = d_total(onodes, use_llm=use_llm)
        Sa_oracle = s_alpha(onodes)
        h_source = "oracle-tree"

    # Δ 和 I
    delta = (D - H_star) if H_star else None
    # cov: gold 维度集对照
    cov_result = cov_gold(nodes, qid) if use_llm else None
    cov, cov_hits = (cov_result if isinstance(cov_result, tuple) else (None, None))

    I = None
    J = None
    if delta is not None and H_star is not None and H_star > 0:
        # 分段：Δ<0（欠分解）→ 指数项=1，cov 线性主导
        exp_term = 1.0 if delta < 0 else math.exp(-delta / H_star)
        I = (cov * exp_term) if cov is not None else exp_term  # cov=None 时只报压缩项
        if Sa_oracle and Sa_oracle > 0 and Sa > 0:
            sigma_s, gamma = 1.0, 1.0
            expansion_prior = math.exp(-abs(math.log(Sa / Sa_oracle)) / sigma_s) ** gamma
            J = I * expansion_prior

    result = {
        "run": os.path.basename(run_path),
        "qid": qid,
        "n_nodes": len(nodes),
        "status_dist": dict(Counter(n.get("status") for n in nodes)),
        "D_T_nat": round(D, 1),
        "S_alpha_prime": round(Sa, 3),
        "C_expand": Ce,
        "C_transmit_tokens": Ct,
        "B_ratio": round(B, 3) if B else None,
        "B_in_band": (0.9 <= B <= 1.1) if B else None,
        "H_star_nat": round(H_star, 1) if H_star is not None else None,
        "H_star_source": h_source,
        "delta_nat": round(delta, 1) if delta is not None else None,
        "delta_over_Hstar": round(delta / H_star, 4) if (delta is not None and H_star) else None,
        "cov": cov,
        "cov_hits": cov_hits,
        "I": round(I, 6) if I is not None else None,
        "J": round(J, 6) if J is not None else None,
        "per_node_info_gain": per_node_scores if use_llm else None,
        "note": f"use_llm={use_llm}; H* source={h_source}; cov={'gold' if cov is not None else 'n/a'}",
    }
    return result


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("run", help="runs-s5-sm-*.json")
    ap.add_argument("--oracle", default=None, help="oracle 树 json（用于 H* 和 S_α' 基准）")
    ap.add_argument("--qid", default="gpu")
    ap.add_argument("--no-llm", action="store_true", help="跳过 LLM info-gain，用假 NLL（快但无区分度）")
    args = ap.parse_args()

    r = compute(args.run, args.oracle, args.qid, use_llm=not args.no_llm)
    out = os.path.join(HERE, f"J-{os.path.basename(args.run).replace('runs-s5-sm-','').replace('.json','')}.json")
    json.dump(r, open(out, "w"), ensure_ascii=False, indent=2)
    print(json.dumps(r, ensure_ascii=False, indent=2))
    print(f"\nsaved → {out}")