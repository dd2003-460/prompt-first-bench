# Q3 × qwen3.6-plus run1

- **题面**: 调研任务：量子纠错阈值定理（threshold theorem）的提出者、年份和关键数值，精确陈述并给出来源。
- **V 等级**: V0（裸 prompt，无 loop 结构）
- **模型**: qwen3.6-plus
- **run**: 1
- **会话 URL**: https://arena.ai/c/01a164ee-a422-7a1d-bb09-2f969d111a9a
- **抓取时间**: 2026-10-23 02:55 +08:00
- **抓取方式**: ego-browser v2 API, body.innerText, 右界="Battle ModeBattle 2 anonymous models"
- **特殊**: 答案含完整思维链（Thought for 20 seconds），落盘时保留

## 答案（完整）

### 一、提出者与年份

该定理并非由单一学者提出，而是1996–1998年间由多个研究团队在量子纠错码基础上独立完成的里程碑成果。核心贡献者及时间线如下：

| 贡献者 | 年份 | 贡献 |
|---|---|---|
| Peter Shor | 1995 | 首次构造出可纠正任意单量子比特错误的量子纠错码（9-qubit码） |
| Andrew Steane | 1996 | 构造 7-qubit CSS 码，为容错计算奠定编码基础 |
| Dorit Aharonov & Michael Ben-Or | 1997 | 首次严格证明存在常数阈值，使容错量子计算在多项式开销下可实现任意精度 |
| Alexei Kitaev | 1997 | 独立给出基于拓扑与稳定子框架的容错阈值证明 |
| John Preskill | 1998 | 进一步完善错误模型、容错门构造与阈值估计 |
| Emanuel Knill, Raymond Laflamme & Wojciech Zurek | 1998 | 完善错误模型与容错协议 |

**学术界通常将该定理称为 Aharonov–Ben-Or–Kitaev–Preskill 定理**，以反映其多源贡献属性。

### 二、精确陈述

**定理（量子容错阈值定理）**：
存在一个严格大于零的常数阈值 p_th > 0，使得当量子计算系统中所有基本物理操作（包括单/双量子比特门、测量、态制备及空闲退相干）的独立错误率均低于 p_th 时，通过量子纠错码与容错量子计算协议，可实现任意长度、任意精度的量子计算。此时，将逻辑错误率压制至 ε 所需的物理资源（量子比特数与门操作数）仅随逻辑电路规模 L 和 log(1/ε) 呈多对数增长，即开销为 polylog(L, 1/ε)。

**⚠️ 注**：该定理为存在性定理，仅证明 p_th > 0 的存在性，不给出唯一数值。具体阈值高度依赖错误模型、纠错码结构、容错协议与硬件架构。

### 三、关键数值（典型模型下的估计）

| 错误模型/架构 | 阈值估计 p_th | 说明 |
|---|---|---|
| 早期通用独立错误模型 | 10⁻⁶ ~ 10⁻⁴ | Aharonov & Ben-Or (1997) 保守界；Preskill (1998) 优化后界 |
| 二维表面码（Surface Code）+ 独立去极化噪声 | 0.75% ~ 1.03% | 当前最接近工程实现的方案（Fowler et al., 2012） |
| 偏置噪声（Dephasing-dominated） | ~3% 以上 | 利用噪声不对称性可显著提升阈值（Tuckett et al., 2020） |
| 离子阱/超导平台实测等效阈值 | 0.5% ~ 1.5% | 依赖具体门保真度与串扰抑制（Arute et al., 2019; Google/IBM 技术报告） |

**重要澄清**：阈值定理本身不指定具体数值。上述数值均来自后续对特定纠错码与噪声模型的数值模拟或解析估计，非定理原始内容。

### 四、权威来源文献

1. Aharonov, D., & Ben-Or, M. (1997). Fault-tolerant quantum computation with constant error rate. STOC '97, 176–188. DOI: 10.1145/258533.258579（完整版见 SIAM J. Comput. 38(4), 2008）
2. Kitaev, A. Y. (1997). Quantum computations: algorithms and error correction. Russian Math. Surveys, 52(6), 1191–1249. DOI: 10.1070/RM1997v052n06ABEH002155
3. Preskill, J. (1998). Reliable quantum computers. Proc. R. Soc. Lond. A, 454, 385–410. DOI: 10.1098/rspa.1998.0167
4. Knill, E., Laflamme, R., & Zurek, W. H. (1998). Resilient quantum computation. Science, 279, 342–345. DOI: 10.1126/science.279.5349.342
5. Fowler, A. G., et al. (2012). Surface codes: Towards practical large-scale quantum computation. Phys. Rev. A, 86, 032324. DOI: 10.1103/PhysRevA.86.032324（表面码阈值基准）
6. Terhal, B. M. (2015). Quantum error correction for quantum memories. Rev. Mod. Phys., 87, 307. DOI: 10.1103/RevModPhys.87.307（现代综述，含阈值依赖性与工程进展）

### 五、补充说明

- 阈值定理是量子计算**可扩展性（Scalability）**的理论基石，表明只要物理错误率低于临界值，量子优势即可通过纠错协议无限延伸。
- 当前主流量子硬件（超导、离子阱、中性原子）的单/双门保真度已突破 99%（错误率 ~1%），正逼近表面码阈值，进入容错量子计算工程验证阶段。
- 实际系统中需考虑空间/时间关联错误、测量延迟、串扰与校准漂移，这些会使有效阈值低于理想模型估计，需通过定制化容错协议（如 lattice surgery, flag qubits）补偿。

## 评分

| 维度 | 满分 | 得分 | 说明 |
|------|------|------|------|
| D1 正确性 | 40 | 38 | 提出者/年份/关键数值/精确陈述全部正确：Shor 1995/Steane 1996/A-B 1997/Kitaev 1997/Preskill 1998/KLZ 1998，阈值 10⁻⁶~10⁻⁴/0.75%~1.03%/~3%，定理陈述严谨（存在性/polylog 开销）。扣分：① 未提 Dennis 2002 的 1.1% 阈值（表面码早期精确值）；② 未提 Tuckett 2018 的 XZZZ 码（只提了 2020 的 Tuckett）；③ "Arute et al., 2019" 引用略模糊（应给具体论文名）。 |
| D2 完备性 | 25 | 23 | 覆盖题面"提出者/年份/关键数值/来源"，五节结构完整（提出者/精确陈述/关键数值/来源/补充说明）。扣分：① 未提阈值定理的"独立证明"历史细节（如 A-B 与 Kitaev 的独立性）；② 未提"阈值定理"在不同错误模型下的变体（如 correlated noise）；③ 未提"阈值定理"与"量子纠错码"的关系（只说"奠定编码基础"）。 |
| D3 结构正交 | 20 | 18 | 五节结构清晰，表格便于扫描，"关键数值"与"补充说明"正交。扣分：① 思维链混在正文前（干扰阅读）；② "补充说明"节可并入"关键数值"节（都是工程实现相关的补充）；③ 未用"时间线"表格统一呈现提出者/年份（只列在"提出者与年份"节）。 |
| D4 来源 conf | 15 | 13 | 6 条文献全给 DOI（Aharonov&Ben-Or/Kitaev/Preskill/KLZ/Fowler/Terhal），具体到卷/期/页码。扣分：① 未标注置信度（conf 高/中）；② "Google/IBM 技术报告"未给具体 URL/标题；③ 未给 arXiv 编号（只给 DOI）。 |
| **总分** | **100** | **92** | **success** |

## 与其他模型对比

- Q3 × claude (88)：四组独立证明+阈值演进表，Shor 未给阈值数值表述略松。
- Q3 × gemini (94)：四阶段阈值演进表+6 条文献含 arXiv 号，来源标注最完整。
- Q3 × qwen (92)：六节结构+6 条文献全给 DOI，思维链可见。

**结论**：qwen 在 Q3 上略低于 gemini（92 vs 94），略高于 claude（92 vs 88）。主要胜在来源标注的精确度（全给 DOI）和"存在性定理 vs 数值估计"的区分，败在未提 Dennis 2002 的 1.1% 阈值和 Tuckett 2018 的 XZZZ 码。
