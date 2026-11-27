# 审稿复算脚本（纯 Python3 标准库，无 numpy/scipy）

所有脚本用 `python3 <file>` 直接跑，无外部依赖。用于支撑 `review-strict-20261127-tmlr-v1.md` 的每条数字主张。

| 脚本 | 支撑的审稿结论 |
|---|---|
| `reproduce.py` | R1：主表 flip/shift/H(D|S) 独立复现（N=40000，Dirichlet(1,1,1,1)） |
| `candidates.py` | R1：shift 五种候选定义对照，确认稿件 0.200/0.166/0.231/0.218 的精确口径 |
| `hds_probe.py` | R2：H(D|S) 在不同条件化口径下的取值 |
| `hds_same_sampler.py` | R2（**核心**）：用作者自己的采样器（`random.Random(42)`, `gammavariate`, N=40000）复算 H(D|S)，证明表中 T5000/4090 两行互换 |
| `closed_form_check.py` | R5：`P(Exp(λ_i) 为最大)` 的精确有理式，证明 H(D) 可闭式，稿件未做 |
| `final_checks.py` | R3/R4：CRN 置换检验、H(D|S) 的 MC 噪声、错误节点得分更高 |
| `perm_theory_check.py` | **R4（关键，推翻审稿人初判）**：24 置换的不变性是**总体恒真**（Dirichlet(1,1,1,1) 坐标可交换），N↑ 时 range 单调收缩；作者的 "narrow MC band" 说法正确 |
| `nullmodel_check.py` | R6：chance 基线（branch=0.5, within=0.25），归一化**不**改变 dominant 判定（审稿人撤回该批评） |
| `trace_hds.py` | R2：穷举可能产生 0.76/0.71/0.77/0.74 的口径，确认无一口径命中 |
| `verify_sec5_and_scoring.py` | R6/R7：§5 四格表重建 + anti-bottleneck 控制 |
| `split_sensitivity.py` | R6（**核心**）："dominant dimension" 随剖分而变 |
| `prior_sensitivity.py` | R8：先验敏感性，§5 结构结论在 fp16-heavy 先验下翻转 |
| `unit_sensitivity.py` | R9：量纲敏感性，scalar 速率 ×10/×0.1 使 flip 变化 |
| `consolidate.py` | R10/R11：shift 定义污染、H(D|S) 与 flip 秩相关 −0.80、噪声节点 H(D|S)=2.0 |

关键复现结果（正文引用）：

```
                 flip    shift    H(D|S) recomputed    H(D|S) in paper
RTX 5090        0.5266   0.2004       0.7667               0.76    ✓
Thor T5000      0.4344   0.1655       0.7639               0.71    ✗ (属 4090)
RTX 4090        0.5627   0.2307       0.7128               0.77    ✗ (属 T5000)
A100            0.5559   0.2183       0.7464               0.74    ≈
```

作者自己的 `idea53-theory-flip.py`（commit 718394ece）输出 `flip=0.527/0.434/0.563/0.556`、`shift=0.2004/0.1655/0.2307/0.2183`，与稿件完全一致；
但该 JSON **不含** `H(D|S)` 字段，`H(D|S)` 列在仓库中无任何持久化产物可追溯。
