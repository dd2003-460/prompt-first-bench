#!/usr/bin/env python3
"""#53 相关扰动玩具 (2026-11-26, G8 泛化探针 v3 = Probe #2).

Probe #1 (nondiag) 测公式结构轴 (弹性非对角); 本探针测噪声结构轴 (扰动协方差非对角).
模型 (基线, 对角弹性): log t_i = log f_i - alpha*log rate_i
扰动: log rate_k += d_k, d ~ N(0, Sigma), Sigma 非对角.

关键推导 (闭式存在性 = 泛化判据):
  margin 差 d_i - d_j ~ N(0, 2*sigma^2*(1-rho_ij))  对任意协方差结构精确 (高斯).
  => P(top2 flip | M) = Phi(-M / (alpha*sigma*sqrt(2(1-rho_ij)))), 闭式存活.
  公共因子特例 d_k = gamma_k*g + sqrt(1-gamma_k^2)*eps_k:
    d_i - d_j = (gamma_i-gamma_j)*g + sqrt(1-gamma_i^2)*eps_i - sqrt(1-gamma_j^2)*eps_j
    => Var = 2*sigma^2*(1 - gamma_i*gamma_j); gamma_i=gamma_j 时公共冲击 g 精确抵消 (共模不可见).
  信息增益二阶项推广: I2_corr = (alpha*beta*sigma)^2 * sum_ij p_i p_j (1-rho_ij)
    (rho=0 时退化为基线 0.5*(alpha*beta*sigma)^2*(1-sum p^2)... 注: sum_ij p_i p_j = 1-sum p^2, 系数一致).

三重对照 (与 Probe #1 同构):
  A 闭式(精确 Sigma) vs MC      -> 推导正确性
  B iid 近似(rho=0) vs 精确     -> 适用域边界: iid 假设漏掉/高估多少
  C 信息增益: I_mc / I2_iid     -> iid 假设的信息偏差方向

预声明判据 (先于跑数, 是假设不是期望):
  H1: 闭式 vs MC 相对误差 <2% (所有 Sigma)  —— 高斯 margin 差对任意协方差精确
  H2: 正公共因子 gamma 下 iid 高估翻转; gamma=0.9 时相对误差 >=50%
  H3: gamma=0.99 时翻转 <0.5% (共模抵消, 即使小 margin)
  H4: 负相关 AR1(rho=-0.6) 时 iid 低估翻转 (方向反转, 幅度可比)
  若 H1 被证伪 -> 非高斯/非线性才是闭式死亡边界, 本探针范围内闭式普适.
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


def flip_prob(M, sd):
    if sd < 1e-12:
        return 0.0 if M > 0 else 1.0
    return phi(-M / sd) if M > 0 else 1.0 - phi(M / sd)


def make_workloads(spec, n=N, seed=SEED):
    rng = np.random.default_rng(seed)
    g = rng.gamma(1.0, 1.0, size=(n, 4))
    F = g / g.sum(axis=1, keepdims=True)
    rate = np.array([spec[c] for c in COMPS], dtype=float)
    return np.log(F), np.log(rate / rate.min())[None, :]


# ---------- 噪声生成器 ----------

def noise_factor(rng, n, gamma, sigma, seed):
    """公共因子: d_k = gamma_k*g + sqrt(1-gamma_k^2)*eps_k, g/eps ~ N(0, sigma^2)."""
    g = rng.normal(0.0, sigma, size=n)
    eps = rng.normal(0.0, sigma, size=(n, 4))
    gv = np.asarray(gamma, dtype=float)
    return gv[None, :] * g[:, None] + np.sqrt(np.maximum(1.0 - gv ** 2, 0.0))[None, :] * eps


def noise_ar1(rng, n, rho, sigma, seed):
    """AR(1) 沿分量轴: d_0=e_0, d_k = rho*d_{k-1} + sqrt(1-rho^2)*e_k. rho_ij = rho^|i-j|."""
    e = rng.normal(0.0, sigma, size=(n, 4))
    d = np.empty_like(e)
    d[:, 0] = e[:, 0]
    s = math.sqrt(max(1.0 - rho * rho, 0.0))
    for k in range(1, 4):
        d[:, k] = rho * d[:, k - 1] + s * e[:, k]
    return d


def rho_matrix(kind, param):
    """返回 4x4 相关系数矩阵 (对角=1)."""
    if kind.startswith("factor"):
        gv = np.asarray(param, dtype=float)
        R = np.outer(gv, gv)
        np.fill_diagonal(R, 1.0)  # Var 归一: 对角必须是 1
    elif kind == "ar1":
        r = param
        R = np.array([[r ** abs(i - j) for j in range(4)] for i in range(4)])
    else:
        R = np.eye(4)
    return R


# ---------- 指标 ----------

def top2_closed_vs_iid(logt, R, alpha, sigma):
    """top-2 翻转: 精确闭式 (按对取 rho_ij) vs iid 近似 (rho=0)."""
    order = np.argsort(logt, axis=1)
    j2, j1 = order[:, -2], order[:, -1]
    M = logt[np.arange(N), j1] - logt[np.arange(N), j2]
    rho_ij = np.array([R[a, b] for a, b in zip(j1, j2)])
    sd_exact = alpha * sigma * np.sqrt(np.clip(2.0 * (1.0 - rho_ij), 0.0, None))
    sd_iid = alpha * sigma * math.sqrt(2.0)
    exact = np.array([flip_prob(m, s) for m, s in zip(M, sd_exact)])
    iid = np.array([flip_prob(m, sd_iid) for m in M])
    return float(exact.mean()), float(iid.mean())


def mc_top2_flip(logt, d, alpha):
    """MC 真值: winner 变了 或 top-2 顺序颠倒 (与 Probe #1 同口径)."""
    pert = logt - alpha * d
    o0, o1 = np.argsort(logt, axis=1), np.argsort(pert, axis=1)
    w0, w1, r0, r1 = o0[:, -1], o1[:, -1], o0[:, -2], o1[:, -2]
    return float(((w0 != w1) | ((w0 == r1) & (w1 == r0))).mean())


def mc_caliber_matched(logt, d, alpha):
    """口径匹配诊断. 闭式事件 A = {t_j' > t_i'} (原 winner 跌到原 runner-up 之下, 含第三方上位).
    A = swap(B: 新winner=原runner-up) ∪ (C: 第三方上位 且 i 仍在 j 下).
    返回 (A_mc, swap, third). 推导正确 <=> closed ≈ A_mc."""
    pert = logt - alpha * d
    o0, o1 = np.argsort(logt, axis=1), np.argsort(pert, axis=1)
    w0, w1, r0 = o0[:, -1], o1[:, -1], o0[:, -2]
    rows = np.arange(N)
    a_mc = float((pert[rows, r0] > pert[rows, w0]).mean())
    swap = float((w1 == r0).mean())
    third = float((~((w1 == w0) | (w1 == r0))).mean())
    return a_mc, swap, third


def mc_argmax_flip(logt, d, alpha):
    return float(((logt - alpha * d).argmax(axis=1) != logt.argmax(axis=1)).mean())


def info_gain(logt, R, alpha, beta, sigma, kind, param, rng, reps=12):
    """I2_iid vs I2_corr 闭式 vs MC. I2_corr = (a*b*s)^2 * sum_ij p_i p_j (1-rho_ij)."""
    z = beta * (logt - logt.max(axis=1, keepdims=True))
    p0 = np.exp(z)
    p0 /= p0.sum(axis=1, keepdims=True)
    I2_iid = 0.5 * (alpha * beta * sigma) ** 2 * (1.0 - (p0 ** 2).sum(axis=1).mean())
    # 严格二阶: I = 0.5 beta^2 sum_i p_i E[(eta_i - mu)^2], eta=-alpha d ~ N(0, a^2 s^2 R)
    #   E[(eta_i-mu)^2] = a^2 s^2 [1 - 2(Rp)_i + p^T R p]
    #   sum_i p_i (...) = a^2 s^2 (1 - p^T R p)   [p 归一]
    # R=I 时退化 0.5 c^2 (1 - sum p^2) = I2_iid;  rho->1 共模时 I->0 (合理)
    Rp = np.einsum("ni,ij,nj->n", p0, R, p0)
    I2_corr = float((0.5 * (alpha * beta * sigma) ** 2 * (1.0 - Rp)).mean())
    ds = []
    for _ in range(reps):
        ds.append(noise_factor(rng, N, param, sigma, 0) if kind.startswith("factor")
                  else noise_ar1(rng, N, param, sigma, 0))
    ps = []
    for d in ds:
        lt = logt - alpha * d
        zz = beta * (lt - lt.max(axis=1, keepdims=True))
        ee = np.exp(zz)
        ps.append(ee / ee.sum(axis=1, keepdims=True))
    p = np.stack(ps, axis=1)
    pbar = p.mean(axis=1)
    pbar /= pbar.sum(axis=1, keepdims=True)
    KL = (p * np.log(p / pbar[:, None, :] + 1e-300)).sum(axis=2)
    Imc = float(KL.mean())
    return {"I2_iid": float(I2_iid), "I2_corr": I2_corr, "I_mc": Imc,
            "mc_over_iid": float(Imc / I2_iid) if I2_iid > 0 else None,
            "mc_over_corr": float(Imc / I2_corr) if I2_corr > 0 else None}


def run_config(name, kind, param, alpha, sigma, logt, with_info=False):
    R = rho_matrix(kind, param)
    ex, ii = top2_closed_vs_iid(logt, R, alpha, sigma)
    rng = np.random.default_rng(SEED + 11)
    d1 = noise_factor(rng, N, param, sigma, 0) if kind.startswith("factor") else noise_ar1(rng, N, param, sigma, 0)
    mct = mc_top2_flip(logt, d1, alpha)
    a_mc, swap, third = mc_caliber_matched(logt, d1, alpha)
    d2 = noise_factor(rng, N, param, sigma, 1) if kind.startswith("factor") else noise_ar1(rng, N, param, sigma, 1)
    mca = mc_argmax_flip(logt, d2, alpha)
    row = {"platform": name, "kind": kind, "param": param,
           "top2_closed": ex, "top2_iid": ii, "top2_mc": mct,
           "mc_eventA": a_mc, "mc_swap_only": swap, "mc_third_party": third,
           "closed_vs_eventA_relerr": abs(ex - a_mc) / max(a_mc, 1e-9),
           "iid_vs_exact_relerr": abs(ii - ex) / max(ex, 1e-9),
           "argmax_mc": mca}
    if with_info:
        row["info_b4"] = info_gain(logt, R, alpha, 4.0, sigma, kind, param, rng)
        row["info_b16"] = info_gain(logt, R, alpha, 16.0, sigma, kind, param, rng)
    return row


def main():
    alpha, sigma = 1.0, 0.15
    gammas = [0.0, 0.3, 0.5, 0.7, 0.9, 0.99]
    ar1s = [-0.6, -0.3, 0.3, 0.6]
    asym = [0.9, 0.9, 0.1, 0.1]  # 组内强共模, 组间弱
    out = {"design": "correlated-noise toy v3 (G8 Probe #2): additive tree + non-iid perturbation",
           "model": "log t_i = log f_i - alpha log rate_i; d ~ N(0,Sigma) non-diagonal",
           "closed_form": "sd_ij = alpha*sigma*sqrt(2(1-rho_ij)); factor: rho_ij=gamma_i*gamma_j; ar1: rho^|i-j|",
           "common_mode_cancellation": "gamma_i=gamma_j => (gamma_i-gamma_j)*g = 0, ranking 对公共冲击不变",
           "hypotheses_predeclared": {
               "H1": "闭式 vs MC 相对误差 <2% (所有 Sigma)",
               "H2": "正公共因子下 iid 高估翻转; gamma=0.9 相对误差>=50%",
               "H3": "gamma=0.99 翻转 <0.5% (共模抵消)",
               "H4": "AR1 rho=-0.6 时 iid 低估翻转"},
           "alpha": alpha, "sigma": sigma, "n": N, "seed": SEED}
    out["scan"] = []
    for name, spec in SPECS.items():
        logf, lr = make_workloads(spec)
        logt = logf - alpha * lr
        for g in gammas:
            out["scan"].append(run_config(name, "factor", [g] * 4, alpha, sigma, logt,
                                          with_info=(name == "T5000")))
        for r in ar1s:
            out["scan"].append(run_config(name, "ar1", r, alpha, sigma, logt,
                                          with_info=(name == "T5000")))
        if name == "T5000":
            out["scan"].append(run_config(name, "factor_asym", asym, alpha, sigma, logt,
                                          with_info=True))
    with open("idea53-corrnoise-toy.json", "w") as fp:
        json.dump(out, fp, ensure_ascii=False, indent=1, default=str)
    print("=== 相关扰动 v3: 噪声结构扫描 (alpha=1, sigma=%.2f) ===" % sigma)
    print("%-8s %-12s %8s %9s %9s %9s %9s" %
          ("平台", "噪声", "gamma/rho", "闭式", "iid", "MC", "iid误%"))
    for r in out["scan"]:
        if r["platform"] != "T5000":
            continue
        p = r["param"]
        pl = ("g=%.2f" % p[0]) if isinstance(p, list) and len(p) == 4 and len(set(map(str, p))) == 1 \
            else ("asym" if r["kind"] == "factor_asym" else "ar1=%.1f" % p)
        print("%-8s %-12s %8s %9.4f %9.4f %9.4f %8.2f%%" %
              (r["platform"], r["kind"], pl, r["top2_closed"], r["top2_iid"], r["top2_mc"],
               100 * r["iid_vs_exact_relerr"]))
    print("\n=== 闭式 vs MC 全配置 (H1: 点估计闭式 vs MC事件A, 应 <2%) ===")
    print("%-8s %-12s %8s %9s %9s %9s" %
          ("平台", "噪声", "参数", "闭式", "MC事件A", "闭vsA%"))
    bad = []
    for r in out["scan"]:
        flag = " <--FAIL" if r["closed_vs_eventA_relerr"] > 0.02 else ""
        if r["closed_vs_eventA_relerr"] > 0.02:
            bad.append(r)
        print("%-8s %-12s %8s %9.4f %9.4f %8.3f%%%s" %
              (r["platform"], r["kind"],
               ("g=%.2f" % r["param"][0]) if isinstance(r["param"], list) and len(set(map(str, r["param"]))) == 1
               else ("asym" if r["kind"] == "factor_asym" else "ar1=%.1f" % r["param"]),
               r["top2_closed"], r["mc_eventA"],
               100 * r["closed_vs_eventA_relerr"], flag))
    print("H1 FAIL 数: %d / %d" % (len(bad), len(out["scan"])))
    print("\n=== 信息增益比 (T5000, I_mc/I2_iid vs I_mc/I2_corr) ===")
    for r in out["scan"]:
        if r["platform"] != "T5000" or "info_b4" not in r:
            continue
        for bkey in ["info_b4", "info_b16"]:
            i = r[bkey]
            print("%-12s %8s  %s: mc/iid=%.3f mc/corr=%.3f" %
                  (r["kind"],
                   ("g=%.2f" % r["param"][0]) if isinstance(r["param"], list) and len(set(map(str, r["param"]))) == 1
                   else ("asym" if r["kind"] == "factor_asym" else "ar1=%.1f" % r["param"]),
                   bkey[-1], i["mc_over_iid"] or 0, i["mc_over_corr"] or 0))


if __name__ == "__main__":
    main()
