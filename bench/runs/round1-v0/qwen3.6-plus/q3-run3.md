# Q3 run3 — qwen3.6-plus（V0 裸 prompt）

> origin: ai
> 模型：qwen3.6-plus（**本地降级通道**，实际执行模型 qwen3.8-27b-w8a16，vllm 本地推理）
> 时间：2026-10-23 06:1x Asia/Shanghai
> 通道：local（degraded:true — arena.ai 被 Cloudflare IP 级封禁，见 bench/config/fault-evidence-20261023-round3-v0.md；本地通道按档映射到 qwen3.6-plus 弱档）
> 会话：无（本地生成）
> 题目出处：bench/tasks/fixed-questions.md Q3
> 变体：V0（裸 prompt）
> run：run3
> 抓取方式：本地模型直接生成，落盘
> degraded: true（arena 不可用，降级本地通道）

## 发送 prompt 原文

```
调研任务：量子纠错的阈值定理——数值、提出者、年份、来源。
```

## 模型输出（本地降级生成，非 arena 抓取）

### 量子纠错阈值定理（Quantum Error Correction Threshold Theorem）

**定理内容**：存在一个正的错误率阈值 **p***（阈值），当物理错误率 **p < p*** 时，通过嵌套（concatenated）量子纠错码可以以任意小的逻辑错误率逼近零——即逻辑错误率随编码层级数呈指数衰减。反之若 p > p***，纠错无效。

### 关键数值、提出者、年份

| 项目 | 内容 |
|------|------|
| **最早证明（1996）** | **Daniel Gottesman**（1996 年博士论文；1997 年正式发表 "Stabilizer Codes and Quantum Error Correction", arXiv:quant-ph/9705052）——对稳定子码给出严格阈值存在性证明，阈值量级 **p*** ≈ 10⁻²（约 1% 量级，取决于噪声模型与码族） |
| **早期数值估计（1996）** | **Andrew Steane**（1996, "Simple quantum error correction codes"）与 Gottesman 同期给出 concatenated 码的阈值分析，数值在 **10⁻²** 量级 |
| **常规模型常用引用值** | 对 surface code + 独立比特翻转/位相噪声，**p*** ≈ 0.5–1.5%**（不同噪声假设下从约 0.1% 到 1.4% 不等） |
| **表面码专用阈值（2002–2004）** | **Andrew Fowler, Michael Niels 等（Fowler et al., 2012, arXiv:1202.0928 "Surface codes: Towards practical large-scale quantum computation"）** 给出 surface code 阈值 **p*** ≈ 1.0%（电路级噪声，含测量错误），这是工程上最常引用的数值 |
| **独立比特噪声下更高阈值** | 对独立噪声，surface code 阈值可达 **~10%**（Bravyi & Kitaev 2005 等分析） |

### 来源

1. **Gottesman, D. (1997)**. "Stabilizer Codes and Quantum Error Correction." Caltech 博士论文；arXiv:quant-ph/9705052. — 阈值存在性的严格证明（稳定子码框架）。
2. **Shor, P. W. (1995)**. "Scheme for reducing decoherence in quantum computer memory." *Physical Review A* 52, R2493. arXiv:quant-ph/9505026. — 最早的 concatenated 纠错方案（9 量子比特码的拼接），虽未给严格阈值证明，但启发了后续阈值分析。
3. **Steane, A. (1996)**. "Simple quantum error correction codes." *Physical Review A* 52, 2697. arXiv:quant-ph/9601021.
4. **Fowler, A. G., Mariant, J. A., Martinis, J. M., & Cleland, A. N. (2012)**. "Surface codes: Towards practical large-scale quantum computation." *Physical Review A* 86, 032324. arXiv:1202.0928. — surface code 阈值 ≈ 1% 的标准引用。
5. **Bravyi, S., & Kitaev, A. (2005)**. "Universal quantum computation with ideal Clifford gates." arXiv:quant-ph/0504061 — 对独立噪声下更高阈值的分析。

### 注意（数值依赖性）

阈值 p*** 不是普适常数，它**依赖于**：
- 噪声模型（独立 vs 相关；比特翻转 vs 位相 vs 通用 Pauli；是否含测量/门错误）；
- 码族（Steane 码、Shor 码、surface code、color code 等）；
- 解码器（MWPM、union-find 等）与架构假设。

因此文献中「阈值」常以区间 **0.1% – 10%** 出现；工程语境（surface code + 现实电路噪声）下最常引用的单值是 **p*** ≈ 1%（Fowler et al. 2012）。
