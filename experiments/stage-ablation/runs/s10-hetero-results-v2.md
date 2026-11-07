# S10 异族 Judge R2 报告（Rubric v2）

> origin: ai · 2026-11-07 · arena.ai Battle mode · conversation 01a1b46a-0aff-7c56-95bc-645e556e9d29

## 一句话结论

Rubric-v2 把异族 judge 一致性从 R1 的 κ=0.396 拉到 r=0.835（Pearson total），gate 通过。

## 实验设置

- 15 个匿名样本（5 臂 × Q1-r1/r2/r3，含 1 个 withTools pilot）
- 2 个匿名 LLM judge（arena Battle，Web Search 开启）
- 评分标准：rubric-v2 五维度（M1 0.40 / M2 0.20 / M3 0.20 / M4 0.10 / M5 0.10）
- 参考答案：gold-facts.md（H100 PCIe vs SXM）

## 一致性指标

| 指标 | R1 (rubric-v1) | R2 (rubric-v2) | 变化 |
|------|---------------|----------------|------|
| 总分 Pearson r | 0.396 | **0.835** | +0.439 |
| 总分 Spearman ρ | — | 0.796 | — |
| Mean \|A−B\| | — | 0.053 | — |
| M1 r | 1.0 | 0.546 | (R1 样本不同) |
| M2 r | 1.0 | 0.472 | |
| M3 r | ~0.5 | 0.640 | +0.14 |
| M4 r | -0.087 | 0.578 | +0.665 |
| M5 r | 0.04 | 1.000 | +0.96 |

**Gate: r=0.835 ≥ 0.6 ✅ PASS**

## 臂级均值对比

| Arm | Judge A | Judge B | Local V2 | A-B diff |
|-----|---------|---------|----------|----------|
| A (朴素) | 0.312 | 0.369 | 0.336 | 0.057 |
| B (先查后拆) | 0.638 | 0.667 | 0.540 | 0.029 |
| C (分解+检查) | 0.608 | 0.574 | 0.466 | 0.034 |
| D (人话reviewer) | 0.587 | 0.563 | 0.278 | 0.024 |
| E (混合) | 0.654 | 0.652 | 0.487 | 0.002 |

两 judge 臂排序一致：B ≈ E > C > D > A。B 稳定第一。

## 关键发现

1. **Judge B 主动识别系统性错误**：指出 RC3/RE2/RC2/RC1/RB3/RA3/RD1/RB1/RB2/RA2 均犯"HBM 带宽相同"错误（声称 PCIe 也是 3.35 TB/s），由此推出"单卡 <5-10%"与 gold 的 1.68x 严重偏离。这说明 rubric-v2 的 gold 锚点有效引导了 judge 注意力。

2. **withTools pilot (RE1) 被两个 judge 都给最高分**：A=0.682, B=0.886。B 特别指出它"唯一正确给出 PCIe HBM 2.0 TB/s、明确纠正 14 倍误读、逐条标注来源、≥3 处具体缺口"。

3. **M4 改善最大**（-0.087 → 0.578）：rubric-v2 的 gap 声明定义（0/0.5/1.0 三档 + 具体对象要求）消除了 R1 中 judge 对"什么算 gap 声明"的理解分歧。

4. **M2 仍是最弱维度**（r=0.472）：知识主干覆盖需要 judge 理解领域结构，不同模型对"核心节点"的界定仍有差异。后续可考虑把 gold 的 depth≤2 节点显式列成 checklist。

## 与 R1 的差异解释

R1 用 rubric-v1（四维度，无 gold 锚点，judge 自由裁量）→ κ=0.396。
R2 用 rubric-v2（五维度 + gold 锚点 + 显式公式 + M4 三档定义）→ r=0.835。

核心改进：把"judge 自己判断什么是好的"变成"judge 按 checklist 对照打分"，裁量空间缩小 → 一致性上升。

## 文件

- 原始分数: `s10-hetero-scores-v2-raw.json`
- 盲打材料包: `s10-blind-packet-v2.json`
- Battle prompt: `s10-battle-prompt-v2.txt`
