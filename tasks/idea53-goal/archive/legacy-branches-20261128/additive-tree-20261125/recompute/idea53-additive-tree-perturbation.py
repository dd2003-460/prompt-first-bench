#!/usr/bin/env python3
"""#53 加性树的微扰敏感性与级数信息增益 (2026-11-25, 第二版).

核心模型 (把 surface-vs-deep 升级为可解析的加性树):
  t_i = f_i / rate_i^alpha  =>  log t_i = log f_i - alpha log rate_i   (加性)
  树: root T=sum t_i; branch(logsumexp 聚合); leaf t_i
  微扰: log rate_k -> log rate_k + delta_k, delta ~ N(0, sigma^2)
  弹性: d log t_i / d log rate_k = -alpha [i=k]  (对角, 闭式)
  软判断: p_i = softmax(beta * log t_i)  (beta=inf 恢复硬 argmax)

三个可验证命题:
  P1 叶翻转: P(argmax 变) = Phi(-margin/(alpha*sigma*sqrt2)), 与 MC 对照
  P2 主导层面: branch-level vs within-level 的翻转概率, 解析 vs MC
  P3 级数信息增益: I(delta;D) = E_eps[D_KL(p(delta)||E p)] 的二阶
     = 0.5 (alpha*beta*sigma)^2 (1 - E sum p_i^2)   —— Fisher 信息闭式
     有效域 beta*alpha*sigma <= 0.4 (误差 ~10%); beta->inf 失效 (硬判断不可微)

第四项: 换公式结构 alpha=1 vs 2, 展示主导层面可随之改变.

纯数学闭式 + 采样验证, 无 LLM/无实测.
"""
import json
import math

import numpy as np

SEED = 0
N = 20000
COMPS = ["fp4", "fp16", "scalar", "bw"]
SPECS = {
    "5090": {"fp4": 1677.0, "fp16": 419.0, "scalar": 21760.0, "bw": 1792.0},
    "T5000": {"fp4": 1035.0, "fp16": 258.0, "scalar": 2560.0, "bw": 273.0},
    "4090": {"fp4": 57.0, "fp16": 114.0, "scalar": 16384.0, "bw": 1008.0},
    "A100": {"fp4": 156.0, "fp16": 312.0, "scalar": 6912.0, "bw": 2039.0},
}


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def softmax(logt, beta):
    z = beta * (logt - logt.max(axis=-1, keepdims=True))
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)


def logsumexp_2(logt):
    """branch 父节点: log(t_compute) = logsumexp(log t_fp4, log t_fp16)."""
    out = np.empty((logt.shape[0], 2))
    for b, idx in enumerate([[0, 1], [2, 3]]):
        sub = logt[:, idx]
        m = sub.max(axis=1, keepdims=True)
        out[:, b] = (m + np.log(np.exp(sub - m).sum(axis=1, keepdims=True))).ravel()
    return out


def make_workloads(spec, alpha, n=N, seed=SEED):
    rng = np.random.default_rng(seed)
    g = rng.gamma(1.0, 1.0, size=(n, 4))
    F = g / g.sum(axis=1, keepdims=True)
    rate = np.array([spec[c] for c in COMPS], dtype=float)
    lr = np.log(rate / rate.min())
    logt = np.log(F) - alpha * lr[None, :]
    return F, logt


def p1_leaf_flip(logt, alpha, sigma, seed=SEED):
    order = np.sort(logt, axis=1)
    margin = order[:, -1] - order[:, -2]
    sd = alpha * sigma * math.sqrt(2.0)
    ana = float(np.array([phi(-m / sd) for m in margin]).mean())
    rng = np.random.default_rng(seed + 1)
    d = rng.normal(0.0, sigma, size=logt.shape)
    mc = float(((logt - alpha * d).argmax(axis=1) != logt.argmax(axis=1)).mean())
    return {"analytic": ana, "mc": mc,
            "rel_err": float(abs(ana - mc) / max(mc, 1e-9))}


def p2_dominant_level(logt, alpha, sigma, seed=SEED):
    logB = logsumexp_2(logt)
    leaf = logt.argmax(axis=1)
    branch = logB.argmax(axis=1)
    # branch 内叶权重 w_k = exp(log t_k - logsumexp)
    within_w = np.empty_like(logt)
    for idx in [[0, 1], [2, 3]]:
        sub = logt[:, idx]
        m = sub.max(axis=1, keepdims=True)
        e = np.exp(sub - m)
        within_w[:, idx] = e / e.sum(axis=1, keepdims=True)
    varB = (alpha * sigma) ** 2 * (within_w ** 2).sum(axis=1)
    mB = np.abs(logB[:, 0] - logB[:, 1])
    ana = float(np.array([phi(-m / math.sqrt(v)) for m, v in zip(mB, varB)]).mean())
    rng = np.random.default_rng(seed + 1)
    d = rng.normal(0.0, sigma, size=logt.shape)
    leaf_p = (logt - alpha * d).argmax(axis=1)
    branch_p = logsumexp_2(logt - alpha * d).argmax(axis=1)
    return {
        "branch_analytic": ana,
        "branch_mc": float((branch_p != branch).mean()),
        "within_mc": float(((leaf_p != leaf) & (branch_p == branch)).mean()),
        "dominant": "branch" if (branch_p != branch).mean() > ((leaf_p != leaf) & (branch_p == branch)).mean() else "within",
    }


def p3_series_info_gain(logt, alpha, sigma, beta, reps=12, seed=SEED + 2):
    p0 = softmax(logt, beta)
    # 二阶 Fisher 闭式: I2 = 0.5 (alpha beta sigma)^2 (1 - E sum p_i^2)
    I2 = float(0.5 * (alpha * beta * sigma) ** 2 * (1.0 - (p0 ** 2).sum(axis=1).mean()))
    # MC 对照: I = E_eps KL(p(eps) || mean p)
    rng = np.random.default_rng(seed)
    d = rng.normal(0.0, sigma, size=(logt.shape[0], reps, 4))
    p = np.stack([softmax(logt - alpha * d[:, j, :], beta) for j in range(reps)], axis=1)
    pbar = p.mean(axis=1)
    pbar /= pbar.sum(axis=1, keepdims=True)
    KL = (p * np.log(p / pbar[:, None, :] + 1e-300)).sum(axis=2)
    Imc = float(KL.mean())
    return {"beta": beta, "alpha": alpha, "sigma": sigma,
            "beta_alpha_sigma": beta * alpha * sigma,
            "I2_closed_form": I2, "I_mc": Imc,
            "ratio_mc_over_I2": float(Imc / I2) if I2 > 0 else None}


def main():
    out = {"design": "additive tree + elasticity perturbation + series information gain",
           "seed": SEED, "n": N,
           "model": "t_i=f_i/rate_i^alpha; log t_i=log f_i - alpha log rate_i; p=softmax(beta log t)",
           "propositions": {
               "P1": "P(leaf flip)=Phi(-margin/(alpha sigma sqrt2))",
               "P2": "dominant level from branch vs within flip rates",
               "P3": "I2 = 0.5(alpha beta sigma)^2 (1 - E sum p_i^2); valid when alpha beta sigma <= 0.4",
           }}
    sigma = 0.15
    out["P1_P2_by_platform"] = {}
    for name, spec in SPECS.items():
        F, logt = make_workloads(spec, alpha=1.0)
        out["P1_P2_by_platform"][name] = {
            "P1_leaf_flip": p1_leaf_flip(logt, 1.0, sigma),
            "P2_dominant": p2_dominant_level(logt, 1.0, sigma),
        }
    # P3: 有效域扫描 (以 T5000 为例)
    F, logt = make_workloads(SPECS["T5000"], alpha=1.0)
    out["P3_series_scan"] = []
    for beta in [1, 2, 4, 8, 16, 32]:
        for sig in [0.05, 0.10, 0.15, 0.30]:
            out["P3_series_scan"].append(p3_series_info_gain(logt, 1.0, sig, beta))
    out["P3_hard_limit"] = "beta->inf (hard argmax): elasticity undefined at ties, Taylor series fails; use P1 instead"

    # 换公式结构: alpha=1 vs 2, 主导层面
    out["formula_variants"] = {}
    for name in ["T5000", "5090", "A100"]:
        out["formula_variants"][name] = {}
        for alpha in [1.0, 2.0]:
            _, logt = make_workloads(SPECS[name], alpha=alpha)
            out["formula_variants"][name]["alpha_%g" % alpha] = p2_dominant_level(logt, alpha, sigma)

    with open("idea53-additive-tree-perturbation.json", "w") as fp:
        json.dump(out, fp, ensure_ascii=False, indent=1)

    print("=== P1/P2 加性树微扰 (sigma=%.2f) ===" % sigma)
    print("%-8s %9s %9s %9s %9s %9s %8s" %
          ("平台", "叶解析", "叶MC", "br解析", "brMC", "withinMC", "主导"))
    for name, r in out["P1_P2_by_platform"].items():
        a, d = r["P1_leaf_flip"], r["P2_dominant"]
        print("%-8s %9.4f %9.4f %9.4f %9.4f %9.4f %8s" %
              (name, a["analytic"], a["mc"], d["branch_analytic"], d["branch_mc"], d["within_mc"], d["dominant"]))
    print("\n=== P3 级数有效域 (T5000) ===")
    print("%5s %6s %10s %10s %8s" % ("beta", "sigma", "I2", "Imc", "ratio"))
    for r in out["P3_series_scan"]:
        print("%5g %6.2f %10.5f %10.5f %8.3f" %
              (r["beta"], r["sigma"], r["I2_closed_form"], r["I_mc"], r["ratio_mc_over_I2"] or 0))
    print("\n=== 换公式 alpha 1->2 的主导层面 ===")
    for name, v in out["formula_variants"].items():
        print("%-8s alpha=1:%-7s alpha=2:%-7s" %
              (name, v["alpha_1"]["dominant"], v["alpha_2"]["dominant"]))


if __name__ == "__main__":
    main()
