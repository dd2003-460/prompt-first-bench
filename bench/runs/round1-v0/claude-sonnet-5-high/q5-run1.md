# Q5 run1 — claude-sonnet-5-high（V0 裸 prompt）

> origin: ai
> 模型：claude-sonnet-5-high（arena Direct 模式）
> 时间：2026-10-22 22:5x Asia/Shanghai
> 通道：arena.ai Direct（ego-browser 自动化）
> 会话：https://arena.ai/c/01a1640c-99e8-748e-82f8-5e7494c5a332
> 题目出处：bench/tasks/fixed-questions.md Q5（开放题，领域=信息论/编码理论）
> 发送 prompt 原文：`调研任务：信息论/编码理论领域——完整搜集里程碑工作，并选出你置信度最高的研究方向。`

## 模型输出（原文）

信息论/编码理论领域里程碑工作调研

**一、奠基性工作（1940s-1950s）**

| 年份 | 工作 | 贡献 |
|------|------|------|
| 1948 | Shannon, "A Mathematical Theory of Communication" | 信息论创立：熵、信道容量、信源编码定理、信道编码定理 |
| 1949 | Shannon, "Communication Theory of Secrecy Systems" | 信息论安全/密码学基础 |
| 1949 | Hamming, "Error Detecting and Error Correcting Codes" | 第一个实用纠错码（Hamming码） |
| 1950 | Golay码 | 完美码的早期例子 |
| 1952 | Huffman编码 | 最优前缀码，无损压缩基础 |
| 1954 | Reed-Muller码 | 代数编码早期重要构造 |

**二、代数编码理论黄金时代（1950s-1960s）**

- 1955 Elias — 卷积码（Convolutional Codes）
- 1959/1960 Hocquenghem；Bose-Chaudhuri — BCH码
- 1960 Reed-Solomon码 — 纠正突发错误，后广泛用于CD、QR码、深空通信
- 1963 Gallager — LDPC码（低密度奇偶校验码），当时因计算能力限制被埋没30余年
- 1967 Viterbi算法 — 卷积码最大似然译码，后广泛用于通信、语音识别(HMM)
- 1968 Forney — 级联码（Concatenated Codes）

**三、速率失真与多用户信息论（1960s-1980s）**

- 1959 Shannon — 率失真理论（Rate-Distortion Theory）
- 1961-1973 Slepian-Wolf — 分布式信源编码定理
- 1973 Wyner-Ziv — 边信息下的率失真理论
- 1976 Cover — 广播信道容量区域
- 1978 Csiszár-Körner — 信息论安全信道（Wiretap Channel后续发展，源自Wyner 1975）
- 1975 Wyner — 窃听信道（Wiretap Channel），信息论安全奠基

**四、实用化突破：逼近香农极限（1990s）**

- 1993 Berrou, Glavieux, Thitimajshima — Turbo码，首次以可实现复杂度逼近香农极限
- 1996 MacKay & Neal重新发现 LDPC码 并证明可逼近容量
- 1981/1998 Tanner图 — LDPC码的图模型表示基础
- 1999 Richardson-Urbanke — LDPC码密度进化分析，不规则LDPC设计理论

**五、网络信息论突破（2000s）**

- 2000 Ahlswede, Cai, Li, Yeung — 网络编码（Network Coding），提出"蝴蝶网络"，证明编码可超越路由
- 2003 Li, Yeung, Cai — 线性网络编码的充分性
- 2006 Ho et al. — 随机线性网络编码
- 2004 El Gamal及后续 — 中继信道容量理论进展

**六、容量可达构造的理论突破（2008-2010s）**

- 2009 Arıkan — 极化码（Polar Codes）：第一个被严格证明可达到任意二进制对称信道容量、且具有显式构造和低复杂度编译码（O(N log N)）的码，解决了50年未解的理论难题
- 2016 极化码被3GPP采纳为5G控制信道标准
- 2011 Guruswami-Xing — 代数几何码的列表译码容量可达构造

**七、量子信息论（1990s-至今）**

- 1995 Shor — 量子纠错码
- 1996 Calderbank-Shor-Steane (CSS码)
- 1973/1995 Holevo界 — 量子信道容量上界
- 2008 Devetak — 量子信道容量的完整刻画（私密容量、量子容量）

**八、信息论与统计/学习交叉（2000s-至今）**

- 2003 MacKay — 《Information Theory, Inference, and Learning Algorithms》系统整合
- 2015-2017 Tishby — 信息瓶颈（Information Bottleneck）理论用于深度学习解释
- 2018-2020 关于神经网络泛化的信息论界（Xu-Raginsky等互信息泛化界）

**九、现代编码理论延伸方向**

- 删除码/纠删码（Fountain Codes: LT码2002, Raptor码2006）—大规模数据分发
- 空间耦合LDPC码（Spatially-Coupled LDPC, Kudekar-Richardson-Urbanke 2011）—理论证明可普适逼近容量
- 局部可修复码（Locally Repairable Codes, ~2012）—分布式存储系统
- DNA存储编码（2017后兴起）

**置信度最高的研究方向选择**

选定方向：面向分布式存储与大规模系统的局部可修复码（LRC）及其与现代信息论工具的融合

选择理由：
1. 需求侧驱动明确、持续增长——数据中心/云存储规模指数级增长，传统RS码全局修复代价成工程瓶颈；Facebook、Microsoft Azure、Google 已在生产环境部署相关方案（如 Azure 的 LRC、Facebook 的 Xorbas）
2. 理论框架成熟且仍有空间——Gopalan et al. (2012) 建立 LRC 的 Singleton 型界；Tamo-Barg 等构造达到该界的显式码；最优构造、不同局部性参数下精确可达性仍有开放问题
3. 与其他前沿交叉潜力大——与 PIR/安全多方计算、极化构造、分布式 ML 梯度编码（Gradient Coding）结合
4. 可验证性强、研究周期合理——相比"信息论+深度学习"偏诠释性方向，LRC 有明确数学目标，结果可通过严格证明或工程实测验证

具体子方向建议：
- 多个擦除同时修复下的最优局部性-距离权衡（现有界尚不紧）
- 非线性/非MDS局部可修复码在特定拓扑（如异构可靠性节点）下的构造
- 局部可修复码与隐私保护分布式存储（结合安全网络编码思想）的统一框架

（结尾：可展开 Polar 码证明思路或 LRC Singleton 界推导的详细讲解，或给出 LRC 方向可执行研究计划。）

---

## 评分（rubric/scoring.md · 100 分制 · 评审：lead-subagent 单评，n=1 探索性）

| 维度 | 分值 | 得分 | 依据 |
|------|------|------|------|
| D1 正确性 | 40 | 33 | 里程碑主体准确：Shannon 1948/1949、Hamming 1949、Huffman 1952、BCH 1959、Reed-Solomon 1960、Gallager 1963、Viterbi 1967、Turbo 1993、Polar 2009/2016 入 5G、Ahlswede 2000 网络编码、Gopalan 2012 LRC 界都对。扣分：①Golay 码写 1950（实际 1949 论文）；②Reed-Muller 1954 正确但"代数编码早期"含糊；③Holevo 界写"1973/1995"含糊（经典 Holevo 1973 是量子容量上界，此处混在量子信息论节）；④Wyner-Ziv 1973、Slepian-Wolf 1973（1961 提出 1973 证明）表述可接受但年份口径不一；⑤"1981/1998 Tanner图"年份混乱（Tanner 1981）。总体大项无错。 |
| D2 完备性 | 25 | 22 | 题目要"完整里程碑 + 选最高置信方向"。里程碑按 9 大时代分节，覆盖 1948-2020s，含经典编码/率失真/多用户/网络/量子/交叉方向，广度好。选方向给出明确选择（LRC）+ 4 条理由 + 3 个子方向，满足"选出并论证"。小缺：未覆盖 2020s 的 qLDPC 突破（LDPC 复兴）与分布式存储中 LRC 之后的代数几何 LRC 最新进展；"完整"程度中上。 |
| D3 结构正交 | 20 | 18 | 按时代+主题双维分节，表格+列表混用清晰；"里程碑"与"方向选择"两大部分正交。小重叠：LRC 在"现代延伸"和"方向选择"各出现一次（属必要呼应，轻扣）。 |
| D4 来源/conf | 15 | 11 | 全程**无任何 URL/DOI/arXiv 号**，纯模型内化知识罗列；但模型在选方向时诚实标注了具体出处（Gopalan 2012 / Tamo-Barg / Azure Xorbas），方向论证部分有可验证性。里程碑部分可验证性弱（无引用）。 |

**总分：84 / 100 → success（≥80）**

**备注**：开放题上 V0 强模型表现稳健（84），与 Q3（88）一致——题面越有结构、越能引导枚举式作答，V0 得分越高；Q2/Q4 的模糊/工具依赖型题才是 V0 失分重灾区。n=1/3 探索性单评。
