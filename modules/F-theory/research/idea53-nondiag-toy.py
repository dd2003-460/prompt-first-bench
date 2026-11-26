#!/usr/bin/env python3
"""#53 非对角玩具: 加性树 + 同branch耦合 (2026-11-26, G8 泛化探针 v2).

模型 (基线 idea53-additive-tree-perturbation.py 的耦合扩展):
  log t_i = log f_i - alpha*(log rate_i + rho*log rate_sibling(i))
  扰动: log rate_k += d_k, d ~ N(0, sigma^2) iid
  => log t_i 的有效扰动 = -alpha*(d_i + rho*d_sibling(i))  (叶间相关)

关键推导 (闭式存在性 = 泛化判据):
  对 (i,j) margin M_ij = logt_i - logt_j, 扰动差:
    sibling 对 (0,1)/(2,3): alpha*(1-rho)*(d_i-d_j) ~ N(0, 2*alpha^2*sigma^2*(1-rho)^2)
    非 sibling 对:          alpha*(d_i+rho d_si - d_j-rho d_sj) ~ N(0, 2*alpha^2*sigma^2*(1+rho^2))
  => P(pair flip | M) = Phi(-M/sd_ij), sd 随对类型变化. 闭式存活.
  对角近似 (基线公式) = 假设 sd 恒为 alpha*sigma*sqrt2 (忽略耦合).

三重对照:
  A 闭式(耦合精确) vs MC      -> 推导正确性 (应 ~1e-4)
  B 对角近似 vs 精确           -> 失效曲线 = 适用域边界
  C 信息增益: I_mc(耦合) / I2(基线对角公式) -> 对角假设漏掉多少信息

预声明判据 (先于跑数, 是假设不是期望):
  H1: |rho|<=0.3 时对角翻转相对误差 <5%  (弱耦合=对角一阶近似够用)
  H2: rho->1 时 sibling 对 sd->0, 翻转趋于确定性 (完美耦合抵消扰动)
  若 H1 被证伪 -> 适用域边界比 0.3 更紧, 边界值本身进论文 limitation.
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
PAIRS = {(0, 1), (2, 3)}  # sibling 对


def phi(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def flip_prob(M, sd):
    """P(sign 翻转) = Phi(-M/sd) if M>0 else 1-Phi(M/sd); sd->0 时趋于 0/1."""
    if sd < 1e-12:
        return 0.0 if M > 0 else 1.0
    return phi(-M / sd) if M > 0 else 1.0 - phi(M / sd)


def sibling_of(i):
    return {0: 1, 1: 0, 2: 3, 3: 2}[i]


def make_workloads(spec, n=N, seed=SEED):
    rng = np.random.default_rng(seed)
    g = rng.gamma(1.0, 1.0, size=(n, 4))
    F = g / g.sum(axis=1, keepdims=True)
    rate = np.array([spec[c] for c in COMPS], dtype=float)
    return np.log(F), np.log(rate / rate.min())[None, :]


def logt_coupled(logf, lr, alpha, rho):
    out = np.empty(logf.shape)
    for i in range(4):
        out[:, i] = logf[:, i] - alpha * (lr[:, i] + rho * lr[:, sibling_of(i)])
    return out


def top2_closed_vs_diag(logt, alpha, rho, sigma):
    """top-2 (winner, runner-up) 对的翻转概率: 精确闭式 vs 对角近似, 逐样本按对类型取 sd."""
    order = np.argsort(logt, axis=1)
    j2 = order[:, -2]  # runner-up
    j1 = order[:, -1]  # winner
    M = logt[np.arange(N), j1] - logt[np.arange(N), j2]
    is_sib = np.array([(a, b) in PAIRS or (b, a) in PAIRS for a, b in zip(j1, j2)])
    sd_exact = np.where(is_sib,
                        alpha * sigma * math.sqrt(2.0) * abs(1.0 - rho),
                        alpha * sigma * math.sqrt(2.0 * (1.0 + rho ** 2)))
    sd_diag = alpha * sigma * math.sqrt(2.0)
    exact = np.array([flip_prob(m, s) for m, s in zip(M, sd_exact)])
    diag = np.array([flip_prob(m, sd_diag) for m in M])
    return float(exact.mean()), float(diag.mean())


def mc_top2_flip(logt, alpha, rho, sigma, seed=SEED + 1):
    """top-2 翻转 MC 真值: winner 与 runner-up 的顺序是否颠倒 (含第三方上位)."""
    n = logt.shape[0]
    rng = np.random.default_rng(seed)
    d = rng.normal(0.0, sigma, size=(n, 4))
    dc = d + rho * np.stack([d[:, sibling_of(i)] for i in range(4)], axis=1)
    pert = logt - alpha * dc
    order0 = np.argsort(logt, axis=1)
    order1 = np.argsort(pert, axis=1)
    top2_0 = {tuple(sorted((a, b))) for a, b in zip(order0[:, -2], order0[:, -1])}
    # 逐样本: 原 top-2 集合 == 新 top-2 集合 且 顺序不变 => 未翻转; 简化口径: winner 变了或 top2 顺序颠倒
    w0, w1 = order0[:, -1], order1[:, -1]
    r0, r1 = order0[:, -2], order1[:, -2]
    flipped = (w0 != w1) | ((w0 == r1) & (w1 == r0))
    return float(flipped.mean())


def mc_argmax_flip(logt, alpha, rho, sigma, seed=SEED + 2):
    n = logt.shape[0]
    rng = np.random.default_rng(seed)
    d = rng.normal(0.0, sigma, size=(n, 4))
    dc = d + rho * np.stack([d[:, sibling_of(i)] for i in range(4)], axis=1)
    pert = logt - alpha * dc
    return float((pert.argmax(axis=1) != logt.argmax(axis=1)).mean())


def info_gain_ratio(logt, alpha, rho, beta, sigma, reps=16, seed=SEED + 3):
    """I_mc(耦合扰动) / I2(基线对角公式 0.5*(alpha*beta*sigma)^2*(1-E sum p^2))."""
    z = beta * (logt - logt.max(axis=1, keepdims=True))
    e = np.exp(z)
    p0 = e / e.sum(axis=1, keepdims=True)
    I2_diag = 0.5 * (alpha * beta * sigma) ** 2 * (1.0 - (p0 ** 2).sum(axis=1).mean())
    n = logt.shape[0]
    rng = np.random.default_rng(seed)
    d = rng.normal(0.0, sigma, size=(n, reps, 4))
    dc = d + rho * np.stack([d[:, :, sibling_of(i)] for i in range(4)], axis=2)
    ps = []
    for r in range(reps):
        lt = logt - alpha * dc[:, r, :]
        z = beta * (lt - lt.max(axis=1, keepdims=True))
        ee = np.exp(z)
        ps.append(ee / ee.sum(axis=1, keepdims=True))
    p = np.stack(ps, axis=1)
    pbar = p.mean(axis=1)
    pbar /= pbar.sum(axis=1, keepdims=True)
    KL = (p * np.log(p / pbar[:, None, :] + 1e-300)).sum(axis=2)
    Imc = float(KL.mean())
    return {"I2_diag": float(I2_diag), "I_mc_coupled": Imc,
            "ratio": float(Imc / I2_diag) if I2_diag > 0 else None}


def main():
    alpha, sigma = 1.0, 0.15
    rhos = [-0.9, -0.6, -0.3, -0.1, 0.0, 0.1, 0.3, 0.6, 0.9]
    out = {"design": "non-diagonal toy v2: additive tree + intra-branch coupling rho",
           "model": "log t_i = log f_i - alpha*(log rate_i + rho*log rate_sib); d~N(0,sig^2) iid",
           "closed_form": "sibling: sd=alpha*sig*sqrt2*|1-rho|; non-sib: sd=alpha*sig*sqrt(2(1+rho^2))",
           "hypotheses_predeclared": {
               "H1": "|rho|<=0.3 对角翻转相对误差<5% (弱耦合一阶近似)",
               "H2": "rho->1 sibling 对翻转趋于确定性 (sd->0)"},
           "alpha": alpha, "sigma": sigma, "n": N, "seed": SEED}
    out["scan"] = []
    for name, spec in SPECS.items():
        logf, lr = make_workloads(spec)
        for rho in rhos:
            lt = logt_coupled(logf, lr, alpha, rho)
            ex, dg = top2_closed_vs_diag(lt, alpha, rho, sigma)
            mct = mc_top2_flip(lt, alpha, rho, sigma)
            mca = mc_argmax_flip(lt, alpha, rho, sigma)
            out["scan"].append({
                "platform": name, "rho": rho,
                "top2_closed": ex, "top2_diag": dg,
                "top2_mc": mct,
                "closed_vs_mc_relerr": abs(ex - mct) / max(mct, 1e-9),
                "diag_vs_exact_relerr": abs(dg - ex) / max(ex, 1e-9),
                "argmax_mc": mca,
            })
    out["info_T5000"] = []
    logf, lr = make_workloads(SPECS["T5000"])
    for rho in [0.0, 0.3, 0.6, 0.9]:
        lt = logt_coupled(logf, lr, alpha, rho)
        for beta in [4, 16]:
            out["info_T5000"].append({"rho": rho, "beta": beta,
                                      **info_gain_ratio(lt, alpha, rho, beta, sigma)})
    with open("idea53-nondiag-toy.json", "w") as fp:
        json.dump(out, fp, ensure_ascii=False, indent=1)
    print("=== 非对角玩具 v2: 耦合 rho 扫描 (alpha=1, sigma=%.2f) ===" % sigma)
    print("%-8s %6s %9s %9s %9s %9s %9s" %
          ("平台", "rho", "闭式", "对角", "MC", "闭vsMC%", "对角误%"))
    for r in out["scan"]:
        if r["platform"] == "T5000":
            print("%-8s %6.1f %9.4f %9.4f %9.4f %8.2f%% %8.2f%%" % (
                r["platform"], r["rho"], r["top2_closed"], r["top2_diag"], r["top2_mc"],
                100 * r["closed_vs_mc_relerr"], 100 * r["diag_vs_exact_relerr"]))
    print("\n=== argmax 整体翻转 (MC) ===")
    for name in SPECS:
        row = [r for r in out["scan"] if r["platform"] == name]
        print("%-8s " % name + " ".join("%.3f@%+.1f" % (r["argmax_mc"], r["rho"]) for r in row))
    print("\n=== 信息增益比 I_mc(耦合)/I2(对角) (T5000) ===")
    for r in out["info_T5000"]:
        print("rho=%4.1f beta=%3d  ratio=%.4f" % (r["rho"], r["beta"], r["ratio"] or 0))


if __name__ == "__main__":
    main()
