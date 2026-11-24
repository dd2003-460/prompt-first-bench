#!/usr/bin/env python3
"""#53 非线性曲率检验 — 命中率 P(Y|depth) 的二次项 (2026-11-24).

claim 精确读法: "深层节点对瓶颈判定的信息贡献更大 (非线性模型下)".
前两步已测: ① I(L;Y) 总互信息 (极小) ② 逐层 KL 贡献分解 (浅层最大).
本步 = claim 里"非线性模型下"的直接检验: 命中率曲线 P(Y)~depth 的曲率.
  二次系数 c>0 → 命中率随深度加速 (凸) → 深层非线性贡献大 (支持 claim)
  c≈0 → 近线性; c<0 → 凹/深层减速 (非线性不集中在深层, 反驳)
  判定用相对曲率 c/b (每单位深度斜率变化/斜率, 无量纲, 避免绝对 c 量纲任意).
加权 (权重=层节点数), 纯 Python 高斯消元解 3x3 正规方程 (无 numpy 依赖).
坑 (2026-11-24 踩到): 正规方程 A[i][j]=Σ w·x^(i+j), 不能写成 row[i]*row[j]
当 row=[w,w·x,w·x²] — 那会出 w² 双重加权, 拟合值全趋 0, R² 出 -44 荒谬值.
"""
import os, importlib.util
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('b',
    os.path.join(HERE, 'idea53-supply-bottleneck-enrichment.py'))
assert spec is not None and spec.loader is not None
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)
SUPPLY, JUDGE, text_of = b.SUPPLY, b.JUDGE, b.text_of


def y1(nd):
    t = text_of(nd)
    return bool(SUPPLY.search(t) and JUDGE.search(t))


def solve3(A, rhs):
    """3x3 高斯消元 (部分主元)."""
    A = [row[:] for row in A]; rhs = rhs[:]
    for i in range(3):
        p = max(range(i, 3), key=lambda r: abs(A[r][i]))
        if abs(A[p][i]) < 1e-12:
            raise ValueError('singular')
        A[i], A[p] = A[p], A[i]; rhs[i], rhs[p] = rhs[p], rhs[i]
        for r in range(i + 1, 3):
            f = A[r][i] / A[i][i]
            for c in range(i, 3):
                A[r][c] -= f * A[i][c]
            rhs[r] -= f * rhs[i]
    x = [0.0] * 3
    for i in (2, 1, 0):
        x[i] = (rhs[i] - sum(A[i][c] * x[c] for c in range(i + 1, 3))) / A[i][i]
    return x


def lin_fit(xs, ys, ws):
    """P(Y) ~ a + b*d 加权最小二乘 (2 参数). 返回 (a, b, r2)."""
    W = sum(ws)
    mx = sum(w * x for w, x in zip(ws, xs)) / W
    my = sum(w * y for w, y in zip(ws, ys)) / W
    sxx = sum(w * (x - mx) ** 2 for w, x in zip(ws, xs))
    syy = sum(w * (y - my) ** 2 for w, y in zip(ws, ys))
    sxy = sum(w * (x - mx) * (y - my) for w, x, y in zip(ws, xs, ys))
    b = sxy / sxx if sxx > 0 else 0.0
    a = my - b * mx
    ss_res = sum(w * (y - (a + b * x)) ** 2 for w, x, y in zip(ws, xs, ys))
    r2 = 1 - ss_res / syy if syy > 0 else 0.0
    return a, b, r2


def quad_fit(xs, ys, ws):
    """P(Y) ~ a + b*d + c*d^2 加权最小二乘. 返回 (a,b,c, r2_lin, r2_quad).
    r2_lin = 独立 2 参数线性拟合的 R² (参考); r2_quad = 二次拟合 R² (同 syy, ≥ r2_lin)."""
    W = sum(ws)
    my = sum(w * y for w, y in zip(ws, ys)) / W
    syy = sum(w * (y - my) ** 2 for w, y in zip(ws, ys))
    A = [[0.0] * 3 for _ in range(3)]
    rhs = [0.0] * 3
    for w, x, y in zip(ws, xs, ys):
        # 加权正规方程: A[i][j] = Σ w·x^i·x^j, rhs[i] = Σ w·x^i·y
        # (注意: 不能写成 row[i]*row[j] 当 row=[w,w·x,w·x²] — 那会出 w² 双重加权)
        for i in range(3):
            rhs[i] += w * (x ** i) * y
            for j in range(3):
                A[i][j] += w * (x ** (i + j))
    a, bb, c = solve3(A, rhs)
    ss_quad = sum(w * (y - (a + bb * x + c * x * x)) ** 2 for w, x, y in zip(ws, xs, ys))
    r2_quad = 1 - ss_quad / syy if syy > 0 else 0.0
    _, _, r2_lin = lin_fit(xs, ys, ws)
    assert r2_quad >= r2_lin - 1e-9, (r2_quad, r2_lin)  # 二次拟合不差于最优线性
    return a, bb, c, r2_lin, r2_quad


def main():
    print('#53 非线性曲率检验: 命中率 P(Y|depth) ~ depth + depth^2 (加权)')
    print('c>0=命中率随深度加速(深层非线性贡献大, 支持claim); c≈0/<0=近线性/减速(反驳)')
    print()
    print('%-30s %8s %7s %8s %8s %9s  %s' % ('源', 'c(二次)', 'c/b', 'R2线性', 'R2二次', 'ΔR2曲率', '判定'))
    for name, nodes in b.collect_sources():
        lv = Counter(); lvy = Counter()
        for nd in nodes:
            lv[nd['level']] += 1
            if y1(nd):
                lvy[nd['level']] += 1
        levels = sorted(lv)
        depth = {x: i + 1 for i, x in enumerate(levels)}
        xs = [depth[x] for x in levels]
        ys = [lvy[x] / lv[x] for x in levels]
        ws = [lv[x] for x in levels]
        a, bb, c, r2_lin, r2_quad = quad_fit(xs, ys, ws)
        rel = c / bb if abs(bb) > 1e-9 else 0.0   # 相对曲率 = 每单位深度斜率变化/斜率
        if c > 0 and rel > 0.1:
            verdict = '支持 (凸/深层加速)'
        elif c < 0 and rel < -0.1:
            verdict = '反驳 (凹/深层减速, 非线性不集中在深层)'
        else:
            verdict = '近线性'
        print('%-30s %8.4f %7.2f %8.3f %8.3f %9.4f  [%s]' % (name, c, rel, r2_lin, r2_quad, r2_quad - r2_lin, verdict))
        print('   命中率: ' + ' '.join('%s:%.1f%%' % (x, lvy[x] / lv[x] * 100) for x in levels))


if __name__ == '__main__':
    main()
