# G1 — 大样本主实验（n=30/臂）· S0 基线节

> origin: ai · 2026-11-08 · goal-pfb-production-hardening G1
> 数据源: runs-prod/S0-{nat,soc}-r*.json（各 30 runs，v3 judge，anti-cache perturbation）
> A3/A4 臂运行中，三臂对比表待补（§3）。

## 1. S0 基线总分（本轮核心数字）

| 域 | n | mean coverage | sd | min | max |
|----|---|---------------|-----|-----|-----|
| nat（多步定量推导题） | 30 | **0.600** | 0.205 | — | — |
| soc（行为经济学叙事题） | 30 | **0.957** | 0.075 | — | — |

交叉验证：A3 pilot n=3 mean=0.611 ≈ prod S0-nat 0.600（来自 gap-to-gold-2026-11-08.md），口径一致。

## 2. 逐点命中率（gold point 级分解）

### nat（6 个 gold points）

| pt | 内容 | 命中 |
|----|------|------|
| 1 | （见 s8b_pilot.py GOLD） | 25/30 |
| 2 | | 24/30 |
| 3 | LFU aging 机制 | 11/30 |
| 4 | request-vs-byte 单位混淆 | 16/30 |
| 5 | residence-time-based stale derivation | **2/30** |
| 6 | honesty labeling | **30/30** |

gap 结构非均匀：集中在 pt5（几乎全灭）+ pt3/pt4；pt6 诚实标注满分。这个异质性本身就是可发表发现——组件贡献不均匀可视化。

### soc（7 个 gold points）

| pt | 命中 |
|----|------|
| 1 | 27/30 |
| 2 | 30/30 |
| 3 | 30/30 |
| 4 | 30/30 |
| 5 | 24/30 |
| 6 | 30/30 |
| 7 | 30/30 |

soc 只有 pt1/pt5 有漏，其余全满。

## 3. 三臂对比（待 A3/A4 完成）

| 臂 | nat mean | soc mean | Δ vs S0 (nat) | Δ vs S0 (soc) |
|----|----------|----------|---------------|---------------|
| S0 | 0.600 | 0.957 | — | — |
| A3（量纲纪律） | running | running | ? | ? |
| A4（few-shot） | running | running | ? | ? |

重点检验问题：
- A3 救不救得回 pt4（request-vs-byte 单位混淆，S0 16/30）？
- A4 拉不拉得动 pt5（stale derivation，S0 2/30）？

## 4. 解读（初步）

soc/nat 不对称（0.957 vs 0.600）指向 **reasoning-type deficit**：同一套 prompt lever，soc 域靠参数化知识就够（叙事/行为经济学），nat 域需要多步定量推导链，断点在推导中间（pt3/pt4/pt5），不是知识缺失。G5 汇总时作为独立观察项。