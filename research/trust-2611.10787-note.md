# TRUST 论文精读 Note（arXiv:2611.10787）

> origin: ai · 2026-11-22 · 触发：D 指令"2611 的 trust 论文很好，下载下来完整读一遍，做成准确讲解且有引用原文关键索引的 note"
> 材料：`research/trust-2611.10787.pdf`（44 页）→ `research/trust-full.txt`（pdftotext 提取，2820 行）。行号索引指向 trust-full.txt。
> 置信度：所有引文为 PDF 原文逐字摘录（来源①）。论文自报数字未独立复现。

## 0. 元数据

- **标题**：Trustworthy Recursive Self-Improvement with Statistical Guarantees
- **作者**：Zihe Gao（浙江大学）、Zhengling Qi（乔治华盛顿大学）、Yifan Cui（浙江大学）
- **arXiv**：2611.10787v1 [stat.ML]，2026-11-07，44 页含附录
- **投稿状态**：arXiv comment 仅"44 pages, including appendix"，**无 journal_ref**（截至 2026-11-22 查证）。投稿类别 stat.ML（统计机器学习），非 cs.AI——说明定位是统计保证论文，不是 agent 系统论文。

## 1. 一句话

**RSI（递归自我改进）里"接受哪个 harness 改动"的门控问题，本质是在线多重假设检验问题；用 e-value + 错误预算分配 + 非劣性检验 + 重叠校正，把"被接受的劣化更新比例"（FER）控制在预算 q 以内，同时证明真正改进的接受率（TER）随验证样本量趋于 1。**

## 2. 问题设定

- harness H_t = (R_t, P_t, M_t, W_t)：reasoning/routing/memory/workflow 四组件 20 个算子（L446-448）
- 每轮 t：proposer 生成候选 harness Θ_t，在验证池 V_N（N 个任务）上抽 n 个评估，与现任（incumbent）Θ_{t-1} 比较
- **门控问题**：分数高就接受（greedy gate）会把噪声当进步 → 性能退化（degeneration）
- 原文（L18-24）："A greedy gate that accepts updates based solely on higher validation scores can mistake an observed gain for genuine progress and lead to performance degeneration, whereas overly conservative statistical gates may reject beneficial updates and hinder performance improvement."

**两个失败模式**：贪心 → 假进化（false evolution）；过保守 → 错过真改进。TRUST 要同时压住两头。

## 3. 核心概念：FER（False Evolution Rate，假进化率）

定义（L182-199，公式 3）：
- 分数差 Δ_t = J(Θ_t) − J(Θ_{t-1})（总体分数差）
- 容忍度 ε：Δ_t ≤ −ε 判为"不可接受的劣化"；−ε < Δ_t ≤ 0 容忍但不改进；Δ_t > 0 改进
- **FER_ε(T) = E[ F_T^ε / (R_T ∨ 1) ]**，其中 F_T^ε = Σ 1{Δ_t ≤ −ε}·A_t（被接受且劣化超 ε 的轮数），R_T = Σ A_t（总接受轮数）

原文（L194-199）："FER is the expected proportion of unacceptably inferior updates among accepted updates, and ε specifies the tolerated loss... Our goal is to ensure that FER_ε(T) ≤ q for a prespecified FER budget q, thereby providing a statistical safety guarantee for the entire self-improvement process."

**类比**：FER 是 RSI 版的 FDR（错误发现率，Benjamini & Hochberg 1995）——FDR 控制"被发现的假阳性比例"，FER 控制"被接受的假进化比例"。动机原文（L106-111）："Motivated by false discovery rate (FDR) control... we define the false evolution rate (FER) as a safety criterion for recursive self-improvement."

对照指标：
- **TER（True Evolution Rate，真进化率）**（L394-398）：被接受的改进候选比例，E[S_T/(U_T∨1)]。FER 压低 + TER 拉高 = 好 gate。
- **MDD（Maximum Drawdown，最大回撤）**：过程中性能最大跌幅。
- **G(T)（最终增益）**：E[J(Θ_T) − J(Θ_0)]。

## 4. 四个定理（统计保证）

### Theorem 1（e-value 条件有效性，L369-380）
原文（L369-373）："Fix any round t. Under Assumption 1, for any m = 1,...,n, the statistic M^{(β)}_{t,m} satisfies E[M^{(β)}_{t,m} | F^pre_t] ≤ 1, if H^t_0 is true."
- 人话：检验统计量在"候选确实不比现任好"（零假设）下期望 ≤1，是合法的 e-value（e-值：一种可以连续累积证据、任意时刻停止检验的统计量）
- 关键推论（L374）：对**任意停止时间** τ_t 也成立 → 允许"证据够了就提前接受"（sequential testing），不用固定样本量
- Assumption 1（L356-357）：e-value 构造的条件均值被 p_ε + β 控制，**β = 验证数据跨轮复用带来的乐观偏差校正强度**（L359-363，引 adaptive data analysis 文献 Dwork et al. 2015）

### Theorem 2（FER 控制，L382-392）
原文（L382-384）："Fix a horizon T ≥ 1 and an FER budget q ∈ (0,1). Under Assumption 1, the false evolution rate of Algorithm 1 satisfies FER_ε(T) ≤ q."
- 人话：整个 T 轮自我改进过程中，被接受的更新里劣化超 ε 的比例，期望上 ≤ 预算 q
- 两个重要性质（L386-392）：
  1. 对任意基于自我改进历史的停止时间也成立（可以"看情况提前停"不破坏保证）
  2. **FER 保证不依赖 LLM 正确识别好候选**（L390-392）："The FER guarantee does not rely on the LLM correctly identifying beneficial candidates. The LLM uses context to allocate more FER budget to promising candidates and less to unpromising ones, safely improving the detection of beneficial updates."——LLM 只做预算分配（把检验资源倾斜给有希望的候选），分错了也不破坏安全性，只影响效率

### Theorem 3（TER 下界 → 功效一致性，L412-420）
原文（L412-415）："Under Assumption 2, there exists a constant κ > 0 such that for sufficiently large N and n, TER(T) ≥ 1 − r_{N,n} − T·e^{−κn}. Hence, TER(T) → 1 as N, n → ∞."
- 人话：验证样本 n 够大时，真正改进的候选几乎必然被接受（漏检率以 e^{−κn} 指数衰减）
- Assumption 2（L403-406）：(a) proposer 能提出改进的概率随历史反馈增长而趋于 1；(b) n/N → 0（跨轮重叠足够小）；(c) 下注分数（betting fraction，e-value 构造里的步长参数）η 在 (0, 2ε/(1+ε)) 内
- **非劣性的理论角色**（L418-420）："when ε = 0, the upper bound 2ε/(1+ε) in Assumption 2 is zero, then no positive betting fraction satisfies the condition. Under this argument, a positive ε is needed to obtain TER(T) → 1."——**必须允许一点容忍损失（ε>0）才能同时拿到 FER 控制和 TER→1**。ε=0（零容忍）时检验退化为不可能有功效。这是"非劣性检验"（临床试验里"证明新药不比旧药差"的检验）在 RSI 里的理论必要性

### Theorem 4（最终增益下界，L424-429）
原文（L424-429）："Under Assumptions 1 and 2, there exists a constant κ > 0 such that for sufficiently large N and n, G(T) ≥ (1 − e^{−κn})·P_T − Σ_t E[A_t·min{(−Δ_t)^+, ε} + α_t·(−Δ_t−ε)^+]."
- 人话：最终增益 ≥ (1−漏检率)×候选的总期望正效应 − 接受劣化更新造成的损失项。安全（FER 控制）和收益（增益下界）在同一个框架里给出

## 5. 算法组件（Figure 2 的四件套 + LLM 分配器）

1. **e-process 检验**：逐样本累积证据，达阈值即接受（任意停止时间有效，Thm 1）
2. **错误预算分配（error budget allocation）**：总 FER 预算 q 分到 T 轮，每轮阈值 α_t；**LLM 分析历史上下文，给有希望的候选分配更宽松的检验水平**（L112-113："we also use an LLM to analyze historical context and help the error budget allocator assign less restrictive testing levels to promising candidates"）
3. **非劣性检验（noninferiority）**：允许容忍损失 ε（Blackwelder 1982 的临床检验思路），提高功效
4. **重叠校正（overlap correction）**：验证池跨轮复用引入乐观偏差，用 β 校正（Dwork et al. 2015 adaptive data analysis）

## 6. 实验（30 轮 × 5 seeds）

**设置**（L453-467）：HotpotQA / DROP / APPS 三个 benchmark；Qwen-3.8-Flash 和 DeepSeek-V4-Flash（**与我们 27b 同族**）；验证集 200 例 + 测试集 300 例；TRUST 默认参数 **q=0.30, ε=0.10, β=0.01**。

**基线**（L463-466）：Greedy（分数高就接受）/ PACE（单轮 e-process，Shawn 2026）/ SGM-B、SGM-H（Bernstein/Hoeffding 检验 + FWER 控制，Wu et al. 2025）。

**主结果**（Table 1，L474-489，均值±标准误）：

| 设置 | Gate | Gain(pp) | FER₀(%) | TER(%) | MDD(pp) |
|---|---|---|---|---|---|
| HotpotQA/DeepSeek | Greedy | 7.87±0.55 | **64.67±3.28** | 40.03±5.06 | 4.96±0.93 |
| | PACE | 10.15±0.75 | 0.00 | 12.63±3.65 | 0.00 |
| | **TRUST** | **11.58±1.30** | 10.00±10.00 | 18.11±8.39 | 0.02 |
| DROP/DeepSeek | Greedy | 36.24±2.19 | 35.28±1.68 | 60.12±7.77 | 5.38±1.58 |
| | **TRUST** | **31.47±1.42** | 0.00 | 11.93±1.29 | 0.00 |
| APPS/DeepSeek | Greedy | 33.89±2.71 | 41.08±4.31 | 50.83±2.89 | 8.48±2.23 |
| | **TRUST** | **34.55±1.04** | 0.00 | 11.64±3.53 | 0.00 |
| HotpotQA/Qwen-3.8 | Greedy | 20.66±2.45 | 44.67±5.23 | 58.40±9.39 | 4.01±0.49 |
| | **TRUST** | **27.72±0.81** | 0.00 | 20.82±3.69 | 0.00 |
| DROP/Qwen-3.8 | Greedy | 15.15±2.22 | 37.38±6.04 | 56.33±5.65 | 3.37±1.03 |
| | **TRUST** | **17.22±1.49** | 0.00 | 10.76±2.82 | 0.00 |
| APPS/Qwen-3.8 | Greedy | 28.03±0.32 | 50.44±4.85 | 38.02±4.36 | 3.59±0.68 |
| | **TRUST** | **26.53±0.11** | 6.67±6.67 | 12.52±3.42 | 0.27 |

**关键数字**（摘要 L33-35 + 贡献 L125-128）：
- 平均：TRUST 最终增益 **24.84pp**（六设置中四个最高）
- 平均 FER₀：Greedy **45.59%** → TRUST **2.78%**
- 平均最大回撤：Greedy **4.963pp** → TRUST **0.047pp**（两个数量级）
- SGM-B/SGM-H 几乎从不接受更新（"never accepts" / "only three updates across all runs"，L497-498）→ 跨轮 FWER 控制在实践中过保守
- **FER₀ 是比 FER_ε 更严的经验诊断**（L458-459）：把所有被接受的非改进更新都算进去（ε=0 口径）
- 案例研究（L495-496, L444-445）：Greedy 有"验证集分数涨但测试集分数跌"的实例——**验证分数高 ≠ 测试性能好**，这是贪心 gate 失败的直接证据

**消融**（Figure 5-6，L569-599）：
- q↑、ε↑ → 更激进（TER↑ 但 FER₀↑）；β↑ → 更保守（FER₀ 从 23.33%@β=0 降到 0%@β=0.03）
- 增益先升后降/持平；β 在 0.01 时增益峰值 11.58pp（无校正 10.97pp）→ 适当的重叠校正有实际收益
- **LLM 分配器消融**（Figure 6，L593-599）：去掉 LLM 分配（w_t≡1），最终分数 44.91±1.36% → 43.78±1.18%。LLM 上下文引导的预算分配有 ~1.1pp 收益，但**去掉也不破坏安全保证**（与 Thm 2 性质 2 一致）

## 7. 局限性（作者自述，L609-615）

原文："The present study does not address how to identify an exact value of overlap correction strength from data or how to optimally tune other parameters. The noninferiority margin provides an interpretable tolerance for loss, but the theoretical guarantee can be conservative and only partly explains practical behavior. The LLM allocator can occasionally make mistakes when judging candidate updates, which may lead to poor choices of LLM multipliers."

即：β 怎么从数据定（没解决）/ 参数最优调法（没解决）/ 理论保证偏保守（承认）/ LLM 分配器会判断错（承认，但安全保证不依赖它）。

## 8. 与我们工作的映射

| TRUST 概念 | 我们的对应物 | 含义 |
|---|---|---|
| harness 四组件 20 算子 | pfb 的 prompts.py + hooks + SM 参数 | 同构：都是"不改权重改 harness"的 RSI |
| 验证分数 | pfb bench 分数（depth/cov） | **单次分数涨 ≠ 真改进**（其案例研究直接证明） |
| greedy gate | 我们目前"分数涨了就接受改动"的默认习惯 | **45.59% 的接受是劣化**——这是对我们 harness 自我改进流程的直接警告 |
| FER 预算 q | 我们缺的东西 | 自我改进 SOP 应加：每轮改动需多次重跑 + 显著性检验，不是单次分数 |
| ε 容忍度 | 我们 judge 噪声 ~0.1 | ε 应该 ≥ judge 噪声，否则 ε=0 时检验无功效（Thm 3 的理论结果） |
| β 重叠校正 | 我们跨轮复用同一验证集（同一批 checkpoint 树） | 我们的验证池跨轮复用 → 有同样的乐观偏差，需要校正或换验证集 |
| LLM 分配器 | 我们 Lead 判断"哪个改动值得多花验证预算" | 有 ~1pp 收益，安全保证不依赖它 → 可以后加 |

**直接行动项**：
1. pfb harness 自我改进（prompt 改动/SM 参数改动）接受前，必须 ≥3 次重跑 + 显著性检验（对标 TRUST 的 5 seeds）；单次分数涨不验收
2. ε 取 judge 噪声量级（~0.1）
3. 验证集跨轮复用的乐观偏差：要么每轮换新验证题，要么接受 β 校正（β 取值无数据驱动方法，[待标定]）
4. 这条写进 harness 自我改进 SOP（unattended-longrun-framework 的验收器组件）

## 9. 原文关键引用索引（→ trust-full.txt 行号）

| 内容 | 行号 |
|---|---|
| 摘要（45.59%→2.78% 数字） | L18-38 |
| 贪心 gate 失败模式定义 | L18-24 |
| FER 动机（FDR 类比） | L106-111 |
| 三贡献（24.84pp / 4.963→0.047pp MDD） | L118-128 |
| G(T) 最终增益定义（公式 2） | L180-181 |
| FER 形式化定义（公式 3） | L182-199 |
| 验证池复用机制 | L200-210 |
| Assumption 1（β 校正） | L356-363 |
| Theorem 1（e-value 有效性 + 停止时间） | L369-380 |
| Theorem 2（FER≤q + 不依赖 LLM 正确性） | L382-392 |
| TER 定义（公式 14） | L394-398 |
| Assumption 2（三条件） | L403-411 |
| Theorem 3（TER→1 + ε>0 必要性） | L412-420 |
| Theorem 4（增益下界，公式 16） | L424-429 |
| 实验设置（数据集/模型/参数） | L441-467 |
| Table 1 主结果 | L470-489 |
| 验证分数≠测试性能案例 | L444-445, L495-496 |
| SGM 过保守 | L497-498 |
| 消融（q/ε/β） | L569-592 |
| LLM 分配器消融（44.91 vs 43.78） | L593-599 |
| 局限性 | L609-615 |
| 附录证明（Lemma 1-3, Corollary 1, Prop 1） | L895-1753+ |

## 10. 投稿级别核查（2026-11-22）

- arXiv 元数据（本轮 API 查询，来源①）：comment="44 pages, including appendix"，**无 journal_ref**
- 类别 stat.ML（统计方法定位）
- **OpenReview 查询（本轮 API，来源①）：TRUST 已投 ICLR 2027（Conference Submission，在审未接收）**
- 同方向 6 篇（2505.21399 / 2408.05568 / 1312.6764 / 2609.33886 / 2602.18806）全部无 journal_ref
- **同方向 ICLR 2027 在审还有 3 篇**（OpenReview 同轮查询）：
  - Compositional Recursive Self-Improvement
  - RSIE: Recursive Self-Improvement through Interaction with Expert Environments
  - Why Is Recursive Self-Improvement Hard to Verify?
- **结论（修正）：该方向（harness RSI + 统计保证）截至 2026-11-22 无顶刊/顶会接收记录，但 ICLR 2027 在审已有 ≥4 篇（含 TRUST）——方向正在向顶会聚集，竞争窗口在收窄**。"Why Is RSI Hard to Verify?" 标题与我们 judge 客观性问题直接相关，值得跟进。[接收结果待 ICLR 2027 出分]
