# Q3 run1 — claude-sonnet-5-high（V0 裸 prompt）

> origin: ai
> 模型：claude-sonnet-5-high（arena Direct 模式）
> 时间：2026-10-22 22:2x Asia/Shanghai
> 通道：arena.ai Direct（ego-browser 自动化）
> 会话：https://arena.ai/c/01a163fc-6f91-7204-96ce-4bc4298e359e
> 题目出处：bench/tasks/fixed-questions.md Q3
> 发送 prompt 原文：`调研任务：量子纠错的阈值定理——数值、提出者、年份、来源。`

## 模型输出（原文）

**量子纠错阈值定理（Quantum Threshold Theorem）调研**

**核心内容**

阈值定理指出：只要物理错误率低于某个临界阈值，就可以通过级联/容错的量子纠错编码，将逻辑错误率任意压低，从而实现任意长时间的可靠量子计算（只需适度增加资源开销）。

**提出者与年份**

阈值定理并非单一论文一次性提出，而是由多个研究组在1996-1998年间几乎同时独立证明：

| 提出者 | 年份 | 备注 |
|--------|------|------|
| Peter Shor | 1996 | 最早给出容错量子计算的构造性证明思路 |
| Dorit Aharonov & Michael Ben-Or | 1996-1997 | 独立给出严格阈值证明 |
| Emanuel Knill, Raymond Laflamme & Wojciech Zurek | 1996-1998 | 独立证明，给出早期阈值估计 |
| John Preskill | 1997-1998 | 对阈值定理做了系统性综述与改进证明 |

**关键原始文献来源**

- P. W. Shor, "Fault-tolerant quantum computation," Proceedings of the 37th Annual Symposium on Foundations of Computer Science (FOCS), 1996, pp. 56–65. arXiv: quant-ph/9605011
- D. Aharonov, M. Ben-Or, "Fault-Tolerant Quantum Computation with Constant Error Rate," SIAM Journal on Computing, 2008（会议版本1997/STOC）。arXiv: quant-ph/9906129
- E. Knill, R. Laflamme, W. H. Zurek, "Resilient Quantum Computation," Science, 279 (5349), 342–345, 1998. arXiv: quant-ph/9702058
- J. Preskill, "Reliable quantum computers," Proceedings of the Royal Society A, 454, 385–410, 1998. arXiv: quant-ph/9705031

**阈值数值**

阈值数值取决于具体的纠错码、错误模型（去极化、测量误差等）和容错方案设计，没有统一的"唯一值"，随研究进展不断被刷新：

| 年代 | 典型阈值估计 | 来源/方案 |
|------|-------------|-----------|
| 1996-1998 | ~10⁻⁶ | 早期理论估计（Knill-Laflamme-Zurek等），非常保守 |
| 2002 | ~10⁻⁴ | Aharonov-Ben-Or、Preskill 改进估计 |
| Surface Code（表面码），2006年后 | ~1%（10⁻²量级） | A. G. Fowler, A. M. Stephens, P. Groszkowski 等；Dennis, Kitaev, Landahl, Preskill (2002) |
| 实用化阈值（考虑测量/门误差具体模型） | 0.5%~1.1% 左右 | 多篇表面码容错研究，如 Fowler et al. 2012 |

**关于表面码阈值的重要文献**

- E. Dennis, A. Kitaev, A. Landahl, J. Preskill, "Topological quantum memory," Journal of Mathematical Physics, 43, 4452 (2002). arXiv: quant-ph/0110143（给出表面码容错阈值约为 1.1% 的估计）
- A. G. Fowler, M. Mariantoni, J. M. Martinis, A. N. Cleland, "Surface codes: Towards practical large-scale quantum computation," Physical Review A, 86, 032324 (2012). arXiv: 1208.0928（综述，约 1% 阈值）

**总结图谱**

```
理论奠基（1996-1998）
├── Shor (1996) — 首次构造性提出
├── Aharonov-Ben-Or (1996/97) — 严格证明，阈值~10⁻⁶级别
├── Knill-Laflamme-Zurek (1998) — 独立证明 "Resilient Quantum Computation"
└── Preskill (1998) — 综述与改进

阈值数值提升（2000s至今）
├── Dennis-Kitaev-Landahl-Preskill (2002) — 表面码，阈值≈1.1%
└── Fowler et al. (2012) — 实用化表面码，阈值≈1%
```

**备注**

"阈值定理"本身是一个存在性定理，证明只要错误率低于某临界值 p_th，容错计算即可无限延展；具体数值高度依赖错误模型假设、码的选择（级联码、表面码、LDPC码等）及解码算法；近年（2020s）qLDPC codes 等新方案也在不断刷新实用阈值。

建议：如果需要用于学术引用，请核实最新的 arXiv 版本号及期刊出版信息。

---

## 评分（rubric/scoring.md · 100 分制 · 评审：lead-subagent 单评，n=1 探索性）

| 维度 | 分值 | 得分 | 依据 |
|------|------|------|------|
| D1 正确性 | 40 | 35 | 主体正确：1996-1998 多组独立证明（Shor/Aharonov-Ben-Or/KLZ/Preskill）、表面码 ~1% 阈值、Dennis 2002 1.1% 估计都对。扣分：①Shor 1996 论文标题 "Fault-tolerant quantum computation" 正确，但 Shor 本人并未给阈值数值（他的贡献是 FTQC 框架），表中"最早构造性证明"表述略松；②Aharonov-Ben-Or 的 arXiv 号 quant-ph/9906129 存疑（实际是 1996/1997 年的工作，9906129 是 1999 的另一篇——编号可能张冠李戴）；③"2002 ~10⁻⁴"一行归属含糊。核心事实（多组独立、~1% 表面码、1996-1998 时间窗）无误。 |
| D2 完备性 | 25 | 23 | 题目要"数值+提出者+年份+来源"，四项全给：数值有演进表（10⁻⁶→10⁻⁴→1%→0.5-1.1%），提出者 4 组，年份明确，来源 6 条含 arXiv 号。还主动解释了"为什么没有唯一值"（码/噪声模型/解码依赖）——超出题面要求。小缺：未提 qLDPC 2020s 具体数值（只一句带过）。 |
| D3 结构正交 | 20 | 18 | 分节清晰（核心→提出者→来源→数值→表面码→图谱→备注），表格+ASCII 图谱双重呈现；"来源"节与"数值"节有轻微重复（同一文献出现两次），正交性略降。 |
| D4 来源/conf | 15 | 12 | 6 条文献含 arXiv 号（可证伪细节给足了），但**无检索痕迹/URL**，纯模型内化知识；末尾"建议核实 arXiv 号"诚实但等于承认未验证——按 rubric D4"来源可验证性"标准，可验证性中等。 |

**总分：88 / 100 → success（≥80）**

**备注**：对比 Q2（73 partial）——题目要素越具体（Q3 明确要"数值/提出者/年份/来源"四要素），V0 裸 prompt 表现越好；模糊题（Q2 "分工关系"）强模型倾向反问消歧而失分。n=1/3 探索性单评。
