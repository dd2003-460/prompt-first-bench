# R4 全因子 × 五 Judge 面板矩阵（合并版）

> origin: ai · 2026-10-31 r62m · 合并 receipt-5judge-panel-consolidated.json + matrix-v11.md
> 判官: J1-strict-v11 (主判) + J1-strict-v2 (密度参照) + v3/v4/v5 (诊断用)
> 模型: qwen3.8-27b @ :8787 · 36/36 run × 5 judge = 180 判分，0 failed

## 五 Judge Pass Rate 矩阵

| config | v11(主) | v2(密度) | v3 | v4 | v5 | v11 floors |
|---|---|---|---|---|---|---|
| A-full | **0.775** | 0.868 | 0.659 | 0.613 | 0.053 | — |
| B-nofreeze | **0.469** | 0.339 | 0.000 | 0.393 | 0.016 | low_specificity×2 |
| B-noevidence | **0.906** | 0.950 | 0.219 | 0.815 | 0.000 | — |
| B-noowner | **0.767** | 0.906 | 0.000 | 0.667 | 0.000 | — |
| B-2del-fe | **0.652** | 0.949 | 0.288 | 0.700 | 0.031 | low_specificity×1 |
| B-2del-eo | **0.606** | 0.814 | 0.250 | 0.750 | 0.031 | — |
| B-2del-fo | **0.523** | 0.944 | 0.000 | 0.768 | 0.000 | — |
| B-none | **0.657** | 0.831 | 0.179 | 0.561 | 0.000 | — |
| B-sham | **0.542** | 0.823 | 0.182 | 0.699 | 0.000 | floor+evidence_floor+low_spec |

## 各 Judge 判定

| judge | 规则 | sham 分离 | 副作用 | 可用性 |
|---|---|---|---|---|
| v11 | 特异性指纹（具体数字/型号/字段占比 <0.2 → fail） | ✓ gap -0.233 | 无 | **主判** |
| v2 | 密度审计（空转检测） | ✗ (+0.045) | 无 | 密度参照 |
| v3 | anti-template（模板句检测） | ✓ (-0.477) | 误杀 75% | 诊断用 |
| v4 | anti-spin（零 pass + 零数值断言） | ✗ (+0.087) | 无 | 失效 |
| v5 | 计划/发现二分 | ✓ (-0.053) | 全场归零 | 失效 |

## 三个稳健发现

1. **Freeze 负效应**：B-nofreeze rank 1/9 under v11/v2/v3/v4（4/4 usable judges）。最稳健结论。
2. **B-noevidence 高分系 judge-dependent**：v11/v2/v4 下 rank 1，v3 下跌 rank 6。非稳定配置属性。
3. **Sham 分离只有 v11 干净**：v3 能分但误杀 75%，v4/v5 失守或全场归零。

## 报告口径

后续所有 run 报告：**v11 主判 + v2 密度参照**。v3/v4/v5 仅诊断用，不入主表。

## 与 matrix-v11.md 的关系

本文件是 matrix-v11.md 的五 judge 扩展版。matrix-v11.md 保留 v11 单判的详细 cell 级数据（D1/a, D1/b, D2/a, D2/b + floors），本文件提供跨 judge 对比视角。两者互补，不取代。
