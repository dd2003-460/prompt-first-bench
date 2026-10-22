# Q1 run1 — claude-sonnet-5-high（V0 裸 prompt）

> origin: ai
> 模型：claude-sonnet-5-high（arena Direct 模式）
> 时间：2026-10-22 21:5x Asia/Shanghai
> 通道：arena.ai Direct（ego-browser 自动化）
> 会话：https://arena.ai/c/01a163e8-623e-760f-a7b4-44ac455fa73c
> 题目出处：bench/tasks/fixed-questions.md Q1
> 发送 prompt 原文：`调研任务：Shannon 1948 原文的核心贡献，精确陈述并给出来源。`

## 模型输出（原文）

**Shannon 1948 原文核心贡献：精确陈述与来源**

**文献来源**

Shannon, C. E. (1948). "A Mathematical Theory of Communication." The Bell System Technical Journal, Vol. 27, pp. 379–423（第一部分，7月）, pp. 623–656（第二部分，10月）。

次年（1949年）与 Warren Weaver 合作以书籍形式再版：The Mathematical Theory of Communication, University of Illinois Press。

**核心贡献精确陈述**

**1. 通信系统的一般数学模型**

Shannon 在论文开篇提出了通信系统的示意框架，包含五个基本部分：

"信息源（Information Source）→ 发射器（Transmitter）→ 信道（Channel）→ 接收器（Receiver）→ 信宿（Destination）"

并引入"噪声源（Noise Source）"作用于信道，这一模型成为此后信息与通信工程的标准范式。

**2. 信息的数学定义——熵（Entropy）**

Shannon 将信息量与概率分布的不确定性联系起来，定义离散信源的熵为：H = −Σ pᵢ log pᵢ（页面内为渲染乱码，公式按上下文还原）

原文第 11 节（"The Discrete Source"）精确表述：

"Quantities of the form H = −Σ pᵢ log pᵢ … play a central role in information theory as measures of information, choice and uncertainty."

他证明了 H 满足三个公理化条件（连续性、单调性、可加性分解性质），并证明满足这些条件的函数必为上述形式（唯一性定理，见原文 Appendix 2）。

**3. 信源编码定理（无噪声编码定理）**

原文定理（Theorem 9）：

"设信源的熵为 H（每符号比特数），信道容量为 C。则可以将信源编码到信道上，使得平均每个信源符号在信道上所需的符号数任意接近 H/C，但不可能小于此。"

这奠定了数据压缩的理论极限——即信源的熵是无损压缩所能达到的理论下界。

**4. 信道容量的定义**

Shannon 定义了离散无记忆信道的信道容量：C = lim_{T→∞} (1/T) log N(T)

对于连续信道（带宽 W，加性高斯白噪声功率 N，信号功率 P），他给出了著名的香农公式（原文第 25 节，Theorem 17）：

C = W log₂(1 + P/N) bits/sec

**5. 噪声信道编码定理（Shannon第二定理）**

这是全文最具革命性的结果。原文 Theorem 11（离散情形）精确陈述：

"设一个离散信道的容量为 C，一个离散信源的熵率为 H。若 H ≤ C，则存在一种编码系统，使得信源的输出能以任意小的差错率通过信道传输。若 H > C，则无法使差错率任意小。"

这一定理首次证明：只要传输速率不超过信道容量，就存在编码方案使错误率趋于零——这与当时工程界普遍认为"噪声必然导致错误率随距离/时间累积"的直觉完全相反，是信息论最深刻的洞见。

**6. 连续信源与率失真的雏形**

论文第四部分（"连续信息的速率"）讨论了连续信源的熵（微分熵）及其在有噪声信道下的处理，为后来的率失真理论（Rate-Distortion Theory，1959年由Shannon本人正式提出）埋下伏笔。

**总结：五大核心贡献一览**

| 贡献 | 原文位置 | 意义 |
|------|---------|------|
| 通信系统五元模型 | 引言部分 | 奠定工程分析框架 |
| 熵的数学定义与公理化 | §6, §11, Appendix 2 | 信息的可计算度量 |
| 信源编码定理 | Theorem 9 | 数据压缩的理论极限 |
| 信道容量定义与高斯信道公式 | §9, §25, Theorem 17 | C = W log₂(1+S/N) |
| 噪声信道编码定理 | Theorem 11 | 可靠通信的存在性证明 |

这篇论文被公认为信息论的奠基之作，首次将"信息"严格数学化，并证明了在噪声存在下实现任意低错误率可靠通信的可能性，深刻影响了通信工程、计算机科学、统计学乃至物理学（如统计力学中熵概念的联系）。

---

## 评分（rubric/scoring.md · 100 分制 · 评审：lead-subagent 单评，n=1 探索性）

| 维度 | 分值 | 得分 | 依据 |
|------|------|------|------|
| D1 正确性 | 40 | 38 | 五大贡献全部命中（五元模型/熵/信源编码定理/信道容量+香农公式/噪声编码定理），文献定位准确（Bell System Tech Journal Vol.27 两部分页码、1949 年 Illinois Press 书版）。两处小瑕疵：①把"信源编码定理"引为 Theorem 9、"噪声信道编码定理"引为 Theorem 11——1948 原文定理编号实际为 Part I Theorem 9（无噪声）/ Part II Theorem 13 等，Theorem 11 归属需核对（-2）；②§6 率失真"1959 年 Shannon 本人正式提出"正确，但说 1948 论文第四部分"埋下伏笔"略宽（-0，可接受）。核心事实无误。 |
| D2 完备性 | 25 | 23 | 问"核心贡献"，答出五大贡献+总结表，覆盖全面；缺"对后续领域影响的具体例证"（仅末段泛泛一句）；缺交叉引用（如与 Kolmogorov/统计力学的关系仅在末句一笔带过）。 |
| D3 结构正交 | 20 | 18 | 六点分节+表格总结，结构清晰无重叠；小扣分：第 2 节与第 3/4 节对熵的重复提及，总结表与前文重复（正交性略降）。 |
| D4 来源/conf | 15 | 12 | 给出主文献完整书目+原文节/定理编号，但**无 URL**（arena 环境未联网搜索，仅凭模型知识作答）；对定理编号未标 conf，存在可证伪细节（Theorem 9/11）未做不确定性声明。 |

**总分：91 / 100 → success（≥80）**

**备注**：本次为 V0 裸 prompt 单 run（n=1/3），分数为探索性单评；盲评要求（双评审）在 3 runs 齐后按匿名编号执行。
