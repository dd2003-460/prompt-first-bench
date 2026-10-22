# Q1 run2 — claude-sonnet-5-high（V0 裸 prompt）

> origin: ai
> 模型：claude-sonnet-5-high（arena Direct 模式模型选择器原样可选，未回退）
> 时间：2026-10-23 03:35 Asia/Shanghai
> 通道：arena.ai Direct（ego-browser 自动化）
> 会话：https://arena.ai/c/01a1651b-85ba-759c-9df0-531e0773fce3
> 题目出处：bench/tasks/fixed-questions.md Q1（V0 节裸 prompt）
> 发送 prompt 原文：`调研任务：Shannon 1948 原文的核心贡献，精确陈述并给出来源。`

## 模型输出（原文）

**Shannon 1948 原文核心贡献**

**文献来源**：Claude E. Shannon, "A Mathematical Theory of Communication," The Bell System Technical Journal, Vol. 27, pp. 379–423, 623–656, July, October, 1948.

**核心贡献精确陈述**

**1. 通信系统的一般模型**

Shannon 提出了通信系统的抽象模型，包含五个基本要素：信源（information source）、发射器（transmitter）、信道（channel）、接收器（receiver）、信宿（destination）。这一框架将通信问题从具体的物理实现中抽象出来，成为后续全部理论的基础。

**2. 信息的统计度量——熵（Entropy）**

对于离散信源，Shannon 定义了信息熵：

H = −∑ pᵢ log pᵢ

其中 pᵢ 为第 i 个符号出现的概率。当 log 取底 2 时，单位为 bit（二进制数字）。

原文论证：Shannon 通过三条公理（对 pᵢ 连续、等概率时随 n 单调增、可分解可加性）推导出满足这些条件的唯一函数形式（相差一常数因子）必为上述对数形式。这一结果出现在原文第 6 节 "The Discussion of the Statistical Theory" 附近（§6，原文 pp. 393–398 区间）。

**3. 无噪编码定理（Noiseless Coding Theorem / 第一定理）**

若信源熵为 H（bit/symbol），则存在编码方式，使每个符号平均码长任意接近 H（但不小于 H）。即：

H ≤ L̄ < H + 1/n（n 为编码块长度，随 n→∞ 趋近 H）

原文中该定理为 Theorem 9（§9 "The Noiseless Coding Theorem"）。Shannon 同时给出了构造性编码方法（Shannon-Fano 编码，原文中描述为按概率排序并二分划分）。

**4. 信道容量（Channel Capacity）**

定义信道容量为：

C = max I(X; Y)（对输入分布 X 最大化互信息）

即单位时间内通过信道可靠传输的最大信息量。原文第 12 节 "The Capacity of a Discrete Memoryless Channel" 给出定义与若干特例（含二元对称信道等）。

**5. 噪声信道编码定理（Noisy Channel Coding Theorem / 第二定理）**

若传输速率 R < C，则存在编码方案使任意小误差概率成为可能（随编码长度增加可任意压低错误概率）；若 R > C，则不可能任意压低错误概率。

原文中该定理为 Theorem 11（§11 "The Noisy Channel Coding Theorem"）。该证明是存在性证明（基于典型序列/随机编码），未给出显式可实现的码。

**6. 连续输入高斯信道容量**

对带宽 W、信号功率 P、加性高斯白噪声功率谱密度 N/2 的连续信道，容量为：

C = W log₂(1 + P/N) bits/sec

其中 W 为带宽，P 为信号功率，N 为噪声功率。该结果出现在原文第 24 节 "The Capacity of a Channel with a Continuous Range of Inputs"，是后世通信工程中应用最广泛的公式之一。

**7. 率失真的雏形**

原文第 27 节初步讨论了在允许一定失真度下对连续信源进行编码的问题，为后来 1959 年 Shannon 正式提出的率失真理论埋下伏笔。

**总结：原文贡献的核心精髓**

Shannon 1948 年论文的根本性贡献在于：将"信息"从语义/物理属性中剥离，定义为纯粹的统计/概率量，并证明通信的可靠性与效率之间存在一个由信道容量刻画的清晰边界——低于此边界可实现任意可靠通信，高于此边界则不可能。这一工作奠定了信息论（Information Theory）作为独立学科的基础。

---

（以下为本 run 元数据，非模型输出）
- 提取方式：ego-browser 打开会话 URL，取页面 `<ol>` innerText（会话页消息列表）。
- 本会话共 1 条用户消息（Q1）+ 1 条 assistant 回复，无后续轮次。
- 无 conf 数值标注（V0 裸 prompt，未要求置信度）。
