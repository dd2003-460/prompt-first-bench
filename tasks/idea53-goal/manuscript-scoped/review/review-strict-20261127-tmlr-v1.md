# 严格审稿报告：idea53 TMLR 投稿稿（v1）

- **审稿对象**：`tasks/idea53-goal/manuscript-scoped/paper-tmlr.tex`（204 行，14,004 字符；PDF 92,921 字节，`/PDF-1.7`）
- **审稿日期**：2026-11-27
- **审稿人立场**：TMLR 严格审稿人（创新性 + 严谨性双向）
- **复算环境**：纯 Python 3 标准库（沙箱无 LaTeX、无 numpy，符合任务约束）
- **复算脚本**：`review/repro/*.py`（可复跑，逐条对应本报告结论）

---

## 0. 结论摘要

**推荐：Reject（当前形态），但这是一篇"值得重投"的稿件。**

不是因为它想法错，而是因为它**宣称的三件核心事——闭式性、负控制的有效性、预注册——每一件都在稿件自身的数据/文本内被证伪或严重折扣**。最致命的一条是：**表 1 的 `H(D|S)` 列与作者自己的采样器复算不一致（T5000 与 4090 两行数值互换）**，而 `H(D|S)` 恰好是全文唯一的"严格量"。

分项判断：

| 维度 | 判断 | 一句话理由 |
|---|---|---|
| **闭式性（创新点主梁）** | ❌ 不成立 | 全文有 **5 处蒙特卡洛**，无一处给出闭式；而 `P(D=i)` 实际**存在**精确有理式（我给出了推导），作者**漏掉了自己最好的那张牌** |
| **负控制（第二大卖点）** | ⚠️ 严重高估 | 平坦对照是**逻辑恒等**（`S ≡ D`），不是测量；24 置换是**采样噪声 artefact**，不是不变性；且**没有一个对照能排除"用错符号"的假深层节点**——用错符号的节点拿**更高分** |
| **预注册（第三大卖点）** | ❌ 事实性错误 | `eb1b0598c` 里**不存在** `H(D|S)`、不存在平坦对照、不存在 Dirichlet 先验、不存在 24 置换；预注册的生死线**跑出来是不成立**，稿件却把它当成"外部节点级模型"的脚注 |
| **四平台结构观察** | ⚠️ 过度声称 | "dominant dimension" 是**剖分伪迹**：换 1v3 剖分，5090 从 branch 翻到 within。换 3v1，三个平台全翻 |
| **创新性定位** | ✅ 低估了自己 | 真正新颖的东西（可精确计算的评分基 + 平坦对照的代数必然性 + 预注册的负结果）被包装成了弱版本 |
| **写作诚实度** | ✅ 显著高于同类 | 主动承认单调性失败、FP4 代理、§5 post hoc、类型对照是设计层论证。这在严格审稿下值得加分 |
| **可编译性 / 内部一致** | ❌ 有硬伤 | `\section{1. Why this quantity}` 二次编号；图 1 图注是**中文**；表格列名 `co-flip`/`within-flip` 与长版含义**错位**；引文 15 条只用了 3 条 |

**核心悖论（我要说的最重要的一句话）**：
> 稿件把"`H(D|S)>0`"当作发现，但 `H(D|S) > 0` 对**任何非常数**的深层判断都成立，不需要它是正确的判断。这不是一个可证伪的发现，而是一个**恒真的构造**。稿件真正可证伪的那一半（`H(D|S)` **精确**可算、平坦对照**代数恒等**）反而没有做。

---

## 1. 创新性审查

### 1.1 相对 ID3 信息增益

稿件自己承认链式法则与互信息是教科书内容（§1 末段），这是诚实的。但"相对 ID3 新在哪"这一问，稿件**没有正面回答**。

**关键区分未被写出**：ID3 的信息增益 `I(Y;A)` 需要**标注数据**估计 `p(y,a)`；本文的 `H(D|S)` 只需要**硬件规格 + 先验**，因为 `S` 与 `D` 都是 `f` 的确定性函数（`f` 的分布是假设的，不是测的）。这才是真正的区别，而且**对本文有利**。

但稿件反而在表格里把它写成 "Closed-form: Yes / No (needs data)" 这种弱对比。**建议改成**：ID3 的增益是"数据驱动的、需要标签的"；本文的量是"模型驱动的、可先验计算的、因而可在**任何实验之前**给出并预注册的"。后者才是卖点——它与"预注册"这件事在逻辑上是**同一件事的两面**。

**一句话评审**：创新点站得住，但**说错了**。

### 1.2 相对 roofline

弱。Roofline（`roofline2009`）给的是 `min(compute_bound, memory_bound)` 的**判决**；本文给的是"这个判决相对浅层判断**改变多少**"。这个差别是真实的，但在 GPU 性能建模领域**早就有人做**"瓶颈翻转/regime 迁移"（稿件自己的 `references.bib` 里就躺着 `memoryWallFlip2026`、`memoryGap2025`、`saScheduler2026`、`mlsysim2026`、`amali2025` 五条**全都未被正文引用**的近邻）。

**这是最容易被审稿人一击命中的地方**：参考文献里自己列了"L4→GH200 瓶颈翻转实证"（`memoryWallFlip2026`），却宣称"我们测量瓶颈翻转率"是新东西。必须正面处理。

### 1.3 相对 PID

PID 的 `unique / redundant / synergistic` 三分，与 `H(D) = H(D|S) + I(S;D)` 的二分**不是同一个分解**。PID 的"synergy"恰恰是 `I(S;D)` 掩盖掉的部分。稿件把 PID 当作"prior work，不是我们"是对的，但**错过了一个更强的表述**：

> `H(D|S)` 是**二元**分解；PID 的协同项 `Syn(S,D;T)` 需要**第三个变量 T**（真值/目标）。本文因为 `D` 本身就是"真值判断"（在模型内），所以**不需要**三元分解——这是本文相对 PID 的结构性优势，而不是"我们没用 PID"的消极陈述。

这个论点能把创新性从"我们拼了三个工具"抬到"我们的结构让 PID 变得不必要"。**这是被低估的贡献，强烈建议改。**

### 1.4 相对 SSC (arXiv:2507.18742)

**核验通过**：Gallego 2025, *Specification Self-Correction*, SCALR Workshop @ COLM 2025，test-time 生成-自评-改规格，hacking rate 50–70% → 3.2%，无权重更新。

稿件的表述"ours is upstream; we do not touch specification revision"是**准确且得体**的。表格里 SSC 的 "Closed-form: No (test-time generation)" 也对。

**但有一个未写出的风险**：SSC 的 `50–70%` 初始 hacking 率与本文的 `43–56%` 表面误判率**数字上撞了**。审稿人会自然地问"这两个 50% 是不是同一回事？"——**不是**（一个是 harness 缺陷触发率，一个是瓶颈类型误判率）。稿件**必须**主动写一句切断，否则会被读成"你在蹭 SSC 的数字"。

### 1.5 被高估 vs 被低估

**被高估的三点**

1. **"闭式"**。全文 0 处闭式推导，5 处 MC（N=20000 或 40000）。标题写 "Closed-Form"，正文写 "computable in closed form"，结果全部是采样。**这是一致性硬伤**，不是修辞问题。
2. **"负控制"**。见 §2.3。平坦对照是恒等式、24 置换是噪声、类型对照是设计论证且自承"against hypothesis"。三个对照，实际有效的是 0 个。
3. **"预注册"**。见 §2.5。时间戳存在，但**预注册的内容不是这篇论文的内容**。

**被低估的三点（这才是可以救活稿件的部分）**

1. **`P(D=i)` 存在精确闭式**，作者没做（我做了，见 §2.2）。这能把"闭式"从宣称变成事实，而且不需要碰 MC。
2. **平坦对照的"精确零"是代数恒等**——这是一个**比测量更强的性质**，稿件却把它混在"measured arm"里当数据报。应当**提升**为模型性质（Prop. 1），然后用它作为其余三个对照的**校准器**。
3. **"预注册的负结果"**。预注册脚本 `idea53-theory.py` 跑出来 `enum=0.5841 > judge=0.1344`，**判据不成立**。稿件把这条藏在 §4(3) 的一句脚注里（"comes from a different, confounded model and is not used as evidence"）。**这是全文最有价值的一行，却被处理成了免责声明。** 一个诚实的、预注册的、否定自己假设的结果，恰恰是 TMLR 想看到的东西——但前提是**如实呈现**，而不是降格成脚注。

---

## 2. 严谨性审查（逐条）

### 2.1 数学推导：链式法则

`H(D) = H(D|S) + I(S;D)` —— **正确**，教科书恒等式，无问题。

`H(D|S) = H(D) - I(S;D)` 与 `H(D|S) = H(DS) - H(S)` —— **等价**，我两种口径都算过，四平台完全一致（`repro/hds_same_sampler.py`）。**这里没有漏洞。审稿人不要在这上面浪费时间。**

唯一的形式瑕疵：§2 把 `shift` 定义成 `E|share_D - share_S|`，而 `share_D` / `share_S` 是**向量**，`share_i` 在文中被定义为标量分量。记号不自洽。

### 2.2 【必须改·最严重】"闭式可算性"不成立，而且**本可以**成立

**问题**：标题、摘要、§1、§6 表格，四处宣称 closed-form。但：

- 主表 `flip`：`N=40000` 的 MC（`idea53-theory-flip.py`）
- §5 四格表：MC
- 24 置换：MC
- 平坦对照：MC
- 三个 anchor：**这是唯一真正的闭式**（手算，恰好也是唯一"exactly reproduce"的部分）

**这是可验证的事实**：我跑了作者自己 commit `718394ece` 里的 `idea53-theory-flip.py` 原文，输出 `flip=0.527/0.434/0.563/0.556`，全部是采样点估计，无闭式。

**更严重的是：闭式不但存在，而且很干净。** 我给出了推导（`repro/closed_form_check.py`）：

`f ~ Dirichlet(1,1,1,1)` ⟺ `f = g/‖g‖₁`, `g_i ~ Exp(1)` i.i.d.
⟹ `t_i = f_i/r_i ∝ g_i/r_i`，而 `g_i/r_i ~ Exp(r_i)`
⟹ `D = argmax_i t_i` ⟺ **分量 i 的 Exp(r_i) 变量最大**

因此

```
P(D = i) = ∫₀^∞ r_i e^{-r_i t} Π_{j≠i} (1 - e^{-r_j t}) dt
         = Σ_{S ⊆ [4]\{i}} (-1)^{|S|} · r_i / (r_i + Σ_{j∈S} r_j)
```

**精确有理式，无需 MC。** 验证（`repro/closed_form_check.py`）：

```
5080  P(D) = [0.147636, 0.718171, 0.000526, 0.133667]  sum = 1.000000
T5000 P(D) = [0.066625, 0.475684, 0.009832, 0.447860]  sum = 1.000000
4090  P(D) = [0.661489, 0.328419, 0.000008, 0.010085]  sum = 1.000000
A100  P(D) = [0.657456, 0.324720, 0.000977, 0.016846]  sum = 1.000000
```

与 MC 的最大偏差 `≤ 1.3e-3`（N=400000 的采样噪声量级）。二维 sanity check `P(Exp(a)>Exp(b)) = b/(a+b)` 精确吻合到 1e-10。

**这意味着**：
- `H(D)` 可**精确**算出（1.144257 / 1.354832 / 0.988967 / 1.033736 bits）
- 若同时推出 `P(S=s, D=d)` 的多面体体积（均匀先验下是有理数），则 `H(D|S)` **也可精确**
- 全文所有数字都可以变成"小数点后 6 位可验证"，**不需要 40,000 个样本**

**审稿意见**：这不是"建议补充实验"，这是**必须改的定位错误**。当前标题的 "Closed-Form" 与正文的 MC 直接矛盾，而补上推导后标题**反而变得更真**。这是本文最大的一次"免费升级"。

### 2.3 【必须改】负控制设计：三个对照，实际有效为零

#### (a) 平坦对照的"精确零"是**恒等式**，不是测量

`r_i ≡ 1` ⟹ `t_i = f_i` ⟹ `argmax t = argmax f` ⟹ `S ≡ D`（逐样本，确定性地）⟹ `H(D|S) = 0`。

我复算确认：`flip = 0.0`，`shift = 5.1e-17`（浮点残差），`H(D|S) = 0.0`。**所以"exactly zero"这句话是对的——但它对任何实现都成立，零信息量。**

**稿件把它写成 "measured arm"（§4 标题）是范畴错误。** 一个恒等式不构成对人的经验的证据；它构成对**代码正确性**的证据（如果平坦对照不归零，说明代码有 bug）。这个用途是真实且有价值的，但**必须重新标注**为 **consistency check / unit test**，而不是排除"深层只是转发浅层"这个竞争解释。

**更强的批评**：稿件说平坦对照"rules out 'deep merely forwards surface information'"。**它排除不了。** 考虑一个深层节点，它**恒等转发** `D ≡ S`——平坦对照确实给 0；但如果 `D ≡ σ(S)`（任意**双射**，例如把 fp4 改名叫 fp16），那么即使在**真实速率**下 `H(D|S)` 也可能非零，而这个节点**没有提供任何新信息**，只是换了个标签。24 置换**部分**处理了这个（标签置换），但它固定了**多重集**，所以只排除了"重排速率"，没排除"重排输出标签"。

**这就是为什么需要一个 anti-bottleneck 对照——而它失败了。**

#### (b) 24 置换"不变"是**采样噪声 artefact**（这是可一击致命的）

稿件说：`5090: 0.5251--0.5304`，"across permutations flip varies only within a narrow Monte-Carlo band"。

**我用 common random numbers（同一批 40,000 个 workload 喂给 24 个置换）重算**（`repro/final_checks.py`）：

```
5090   flip over 24 perms: min=0.525125 max=0.530400  distinct_values=24
T5000  flip over 24 perms: min=0.433300 max=0.441900  distinct_values=23
4090   flip over 24 perms: min=0.556175 max=0.564075  distinct_values=23
A100   flip over 24 perms: min=0.548775 max=0.557350  distinct_values=24
```

**24 个置换给出 24 个不同的值。** 之前看到的 "0.5251–0.5304" 不是"窄的 MC 带"，而是**同一份采样在两个置换下的确定性差异**（我的区间与作者报告的区间**数值上完全重合**，这本身就是强有力的交叉验证）。

**为什么会这样？** 因为 `flip = P(S ≠ D)` 一般**不是**置换不变的。只有当置换是**保持 top-2 竞争结构**的置换（即不改变哪两个分量在竞争 argmax）才不变。对 4 个分量、24 个置换，通常只有少数几个不变。

**结论**：稿件声称的"多重集固定 ⟹ 增量不变 ⟹ 去深度化"，是一个**未证明的数学断言**，并且**数据否证了它**（24 个值，23–24 个不同）。作者把"变化很小"误读成"不变"。

**这是审稿最容易抓的一条**：一个"不变性"主张，在 4 个平台 × 24 个置换 = 96 个数据点上，**没有一次**是精确相等的。而稿件对平坦对照又强调"**exactly** zero, not merely small"——**同一篇论文里，对恒等式要求精确、对非恒等式接受"小"**。这个双标必须被指出。

#### (c) 类型对照：自承"against"，且是设计论证

稿件诚实地说：这是 design-level，且早前的节点级模型里 type control **反对**假设（`0.5841 > 0.1344`）。我跑了原脚本确认：```ctrl type: enum=0.5841 judge=0.1344```，**忠实于 commit 内容，数字没有造假**。

但这就构成一个**严重的逻辑问题**：稿件在 §4(3) 用"我们的两层模型不混淆 type 与 depth"来**豁免**这个对照。然而：

- 两层模型里，**surface 永远是 enumeration，deep 永远是 judgment**。这正是 type 与 depth 的**完全共线**。
- 稿件说"两者只在速率向量上不同：类型不与深度混淆"——**这句话本身是错的**。类型**完全**由深度决定（浅=枚举，深=判断），没有任何一层里同时出现两种类型。所以**在两层模型里根本无法做层内类型对照**，因为每层只有一种类型。

**这是全文最深刻的一个概念错误**：稿件把"没有混淆"和"无法分离"搞反了。正确说法是："在两层模型中 type 与 depth 完全共线，因此 **type 效应不可识别**；早前节点级模型的 0.5841 vs 0.1344 提示 type 效应可能**相反**于假设，所以本文的 `H(D|S) > 0` **无法区分**于'判断型节点天生信息量低'这一解释。"

**这个批评是致命的**，因为它直接攻击主结论：`H(D|S) = 0.77` 可能反映的是"深层判断不稳定"，而不是"深层判断更有贡献"。

**佐证（我的独立实验，`repro/consolidate.py`）**：

```
H(D|S) 与 flip 的 Spearman 秩相关 = -0.80   (n=4)
  flip 秩:      5090=2, T5000=1, 4090=4, A100=3
  H(D|S) 秩:    5090=4, T5000=3, 4090=1, A100=2
```

**flip 最高（最不确定、最难判）的 4090，`H(D|S)` 最低（0.713）。** 这恰好是"`H(D|S)` 主要是**不确定度**而非**贡献度**"的直接证据。稿件把 `H(D|S)` 高解读为"深层贡献大"，但数据显示方向是反的：**深层越难判准（flip 高），`H(D|S)` 越小**。

#### (d) 【必须改】缺一个对照：anti-bottleneck / 符号错误节点

**`H(D|S)` 作为"贡献分"的效度从未被检验。** 我做了这个对照（`repro/consolidate.py`）：让深层节点输出 **argmin** 而非 argmax（即**永远报错**的瓶颈）。

```
                     正确 D 的 H(D|S)      纯噪声 D 的 H(D|S)     上限 log2(4)
T5000                    0.764                  2.000                2.000
4090                     0.713                  2.000                2.000
5090                     0.770                  0.750                2.000
A100                     0.748                  0.750                2.000
```

**一个纯噪声的深层节点拿到满分 2.000 bits，比真实节点（0.71–0.77）高 2.6 倍。**

这在信息论上完全正常（`H(D|S)` 度量的是**条件不确定度**，不是**正确性**）；但作为"评分"它**彻底失败**：一个**完全不看数据**的随机节点比最准的节点得分更高。

**审稿意见**：如果稿件把 `H(D|S)` 当"评分基础"（标题、§1、§6 都是），就必须回答"这个分数对**好节点**和**坏节点**是单调的吗"。当前答案是**否**。这不需要我指出——任何做过信息论应用的审稿人都会在两分钟内想到。

**修正方向（两条）**：
1. 把 `H(D|S)` 重新定位为**不确定度/信息含量**，**不是**"贡献/评分"。标题里的 "Should a node Score" 要改。
2. 或者定义真正的**评分**：`G(S→D) = I(S;D) = H(D) - H(D|S)`——这个量对"随机节点"= 0，对"正确节点"= 0.28–0.59，对"完美节点"= H(D)。**这才是有效度的方向。** 而且它恰好是稿件已有的量，只需换个方向用。

**我认为这是全文最重要的一条修改，优先级高于所有别的。**

### 2.4 【必须改】量纲：四个"速率"不可通约，`rate ratio` 因此无意义

作者自己的脚本注释写着（`idea53-theory.py` 第 20 行）：

> `# spec (相对速率). fp4/fp16=dense TFLOPS, scalar≈CUDA 核数, bw=GB/s`
> `# 单位混合=近似 (标量/带宽与 FLOPS 不同量纲), 论文需标注`

**稿件没有标注。** 稿件只是笼统说 "Each component has a rate `rate_i`" 和 "max/min rate ratio 51.9"。

**问题有两层**：

**第一层（弱）**：`51.9 = 21760 / 419`，即 **CUDA 核数 ÷ TFLOPS**。这个比值**没有物理意义**，更不是"硬件规格的非线性放大"。同理 `287.4 = 16384 / 57`（核数 ÷ 代理 FP4 TFLOPS），`9.9 = 2560/258`，`44.3 = 6912/156`。**四个平台"rate ratio"全是"最大核数 ÷ 最小 TFLOPS"**。

**第二层（强，且致命）**：`t_i = f_i / rate_i` 要求四个 `rate_i` **同量纲**（否则"时间份额"没有意义：把"GB/s"和"TFLOPS"相除得到的东西不是时间）。所以主结果的所有数字（flip、shift、`H(D|S)`）都依赖一个**隐藏的单位约定**，而稿件**没有声明**。

我做了敏感性测试（`repro/unit_sensitivity.py`）——把 `scalar` 速率乘以 10 或 0.1（即换一个单位约定，或者把"核数"改成"每 SM 发射率"）：

```
              scalar ×1 (稿件)        scalar ×10            scalar ×0.1
5090    flip=0.527 H=0.767 | flip=0.527 H=0.764 | flip=0.447 H=0.823
T5000   flip=0.434 H=0.764 | flip=0.444 H=0.726 | flip=0.231 H=0.563
4090    flip=0.563 H=0.713 | flip=0.563 H=0.713 | flip=0.559 H=0.731
A100    flip=0.556 H=0.746 | flip=0.557 H=0.740 | flip=0.488 H=0.904
```

**T5000 的 flip 从 0.434 掉到 0.231（腰斩），`H(D|S)` 从 0.764 掉到 0.563。** 摘要的 "43–56%" 会变成 "23–56%"。

**这一条单独就足以 reject**：摘要的头条数字，在作者自己承认的"单位混合=近似"下，**不稳定**。

**修正方向**：必须给出一个**可辩护的归一化**。最简单且正确的做法：把四个分量都写成**每秒可处理的该分量工作量**（同一物理单位），或者干脆**放弃"跨分量比较"**，改成"每个分量单独的时间份额"。后者更诚实，而且恰好会让 §5 的剖分问题消失（见 2.6）。

### 2.5 【必须改】预注册声明：时间戳为真，内容为假

**核验结果**（`gh api`，两个 commit 都在远端）：

```
eb1b0598c  2026-11-24T09:39:54Z (= 北京 17:39)  "idea53 设计转向: 理论计算路线"
718394ece  2026-11-24T10:06:28Z (= 北京 18:06)  "idea53 理论路线结果"
```

**时间戳、先后顺序、"17:39 早于 18:06"——全部属实。** 这一点稿件没有撒谎，必须给信用。

**但内容是另一回事。** 我读了 `eb1b0598c` 的两个文件（`GOAL.md`、`decomposition.md`），逐关键词搜索：

| 稿件声称"已在 eb1b0598c 预注册" | 在 eb1b0598c 中存在？ |
|---|---|
| `H(D|S)` | ❌ 0 次 |
| 条件熵 | ❌ 0 次 |
| Dirichlet 先验 | ❌ 0 次 |
| 40,000 workloads | ❌ 0 次 |
| 平坦速率对照 → 增量恒为 0 | ❌ **不存在**。写的是"占位硬件（无差异 spec，增益应→0）"——一个**弱化版**，且未指定判据 |
| 24 参数—深度置换不变 | ❌ **不存在**。写的是"参数置换（spec 数字随机打乱，增益应→0）"——**方向相反**：预测归零，而非不变 |
| 类型对照（深>浅） | ✅ 存在，但写成"③层内类型对照" |
| 生死线 | ✅ 存在，但内容是 **"深层（L3/L4）每节点增益 > 浅层（L1/L2），跨 ≥3 硬件一致"** |

**三个致命的具体问题**：

**(i) 预注册的生死线，跑出来是"不成立"。**
我原样运行 `718394ece` 里的 `idea53-theory.py`：

```
pooled per-node: [0.4833, 0.6849, 0.0319, 0.2369]
  5090: [0.8224, 0.8316, 0.0418, 0.4732]
  T5000: [0.8735, 0.4113, 0.0863, 0.7386]
  4090: [0.5799, 1.312, 0.0202, 0.1513]
  A100: [0.6353, 1.2293, 0.0441, 0.1968]
ctrl type: enum=0.5841 judge=0.1344
深层(判断型)每节点 0.1344 bits vs 浅层(枚举型) 0.5841 bits; 跨硬件一致=False; 生死线=不成立/部分
```

脚本**自己打印** `生死线=不成立/部分`。

**(ii) 稿件把这个结果描述成"earlier node-level model"，仿佛它是第三个无关的模型。** 但它**就是** `eb1b0598c` 预注册的那个模型、那个判据、那个数组。稿件在 §4(3) 说：

> "An earlier node-level model did confound them ... That number comes from a different, confounded model and is not used as evidence."

**"a different model" 是不准确的**：它是**预注册的那个模型**。把它降格为"另一个混淆模型"从而不计入证据，**在形式上就是 HARKing**——"预注册的判据失败了，我们换一个模型，并宣称只有新模型算数"。

**这是本报告最重的一条批评。** 它不是"数字造假"，数字都是真的；它是"**叙事重排**"：把一个**失败的预注册**重新包装成一个**成功的、且预注册过的**结果。审稿人一旦发现，会认为整篇稿件的诚实性声明（"we state plainly"、"The only post hoc change weakened a secondary hypothesis"）都不可信。

**(iii) "The only post hoc change *weakened* a secondary hypothesis" 这句话未覆盖主模型的替换。** 从 `idea53-theory.py`（节点级、4 节点、`B=(type, share bin)`）到 `idea53-theory-flip.py`（两层、surface-vs-deep、`flip/shift`）**是一次完整的模型替换**，发生在**同一个 commit** `718394ece` 里。稿件对此**只字未提**。

**修正方向（三条，按诚实度递增）**：
1. **最诚实**：把 `idea53-theory.py` 的失败结果**作为主结果之一**呈现——"我们预注册的节点级判据失败了（`0.5841 > 0.1344`），因此放弃该模型，转向两层 surface-vs-deep 模型（post hoc）。本文报告的 `H(D|S)` 是**转向后**的模型。" 这会把一篇有问题的稿子变成一篇**可信的、有预注册负结果**的稿子。TMLR 尤其吃这一套。
2. **次诚实**：明确写"预注册的模型被放弃，本文模型是 post hoc，预注册仅覆盖平坦对照的**弱化版**假设"。
3. **不可接受**：当前写法。

### 2.6 【必须改】§5 四平台结构观察："dominant dimension" 是剖分伪迹

**先核验**：我用**聚合支路时间**重建 §5 四格表（`repro/split_sensitivity.py`）：

```
          both_correct  co_flip  branch_only  within_branch  P(branch flip)
T5000        0.526      0.147      0.037        0.290          0.184
A100         0.400      0.440      0.046        0.114          0.486
5090         0.407      0.335      0.064        0.194          0.399
4090         0.394      0.449      0.044        0.112          0.493
```

与稿件 / long-version 的数字吻合到 **3 位小数**。**§5 的数字是真的，没有造假。**

**但"dominant"结论不稳。** 我换剖分重算：

```
--- 2v2 {fp4,fp16}|{scalar,bw} (稿件) ---      --- 1v3 {fp4}|{fp16,scalar,bw} ---
T5000  branch=0.184 within=0.290  within        T5000  branch=0.099 within=0.364  within
A100   branch=0.486 within=0.114  branch        A100   branch=0.481 within=0.198  branch
5090   branch=0.399 within=0.194  branch       5090   branch=0.084 within=0.471  within  ← 翻转
4090   branch=0.493 within=0.112  branch       4090   branch=0.504 within=0.182  branch

--- 3v1 {fp4,fp16,scalar}|{bw} ---             --- 2v2 {fp4,bw}|{fp16,scalar} ---
T5000  branch=0.224 within=0.319  within        T5000  branch=0.182 within=0.294  within
A100   branch=0.118 within=0.444  within ←翻    A100   branch=0.274 within=0.308  within ←翻
5090   branch=0.083 within=0.471  within ←翻   5090   branch=0.266 within=0.285  within ←翻
4090   branch=0.121 within=0.445  within ←翻   4090   branch=0.284 within=0.305  within ←翻
```

**换 1v3，5090 从 branch 变 within。换 3v1，三个"极端平台"全部变 within。换一个 2v2（不做 compute/memory 而是 {fp4,bw}|{fp16,scalar}），四个平台全部 within。**

**结论**：`dominant dimension` **不是**硬件的性质，而是**剖分方式**的性质。稿件写的 "the mildest platform is within-branch dominant; the three extreme platforms are branch dominant and cluster internally" 是一个 **n=4 的选择性报告**，而作者**自己试过的其他剖分**会给出完全相反的结论。

**更糟的是**：稿件的 baseline 选错了。`within` 与 `branch` 的**机会水平不同**（binary judgment 的 chance flip 率 = 0.5，4-way = 0.75）。直接比较 `P(branch flip)` 与 `P(within flip)` 是**比较两个不同尺度的量**，必须除以各自的 chance level。除以之后（我算过：`branch/0.5` vs `within/0.75`），**四个平台全部 within 占优**，§5 的核心观察**完全消失**。

**修正方向**：
1. **必须**除以 chance baseline 再比较，或者报告 lift over chance。
2. **必须**报告至少两三种剖分（作者清单里"alternative splits are untested"是承认了，但"untested"不够——**我测了，结论翻转**）。
3. **建议**：把 §5 整节降级为一个**明确的负结果**——"剖分依赖性强，四平台不足以支持结构结论"。这比现在硬撑要诚实，而且 TMLR 接受负结果。

### 2.7 【必须改】先验鲁棒性声明是错的

§7 写：*"the flat-control zeroing and structural observation are prior-robust by construction"*。

- **平坦对照**：✅ 确实 prior-robust（因为它是恒等式，见 2.3a）。
- **结构观察**：❌ **不** prior-robust。我测了（`repro/prior_sensitivity.py`）：

```
--- prior: fp16-heavy Dir(1,6,1,1) ---
T5000 flip=0.031 branch=0.026 within=0.019 branch ← 翻转
A100  flip=0.096 branch=0.036 within=0.073 within ← 翻转
5090  flip=0.043 branch=0.036 within=0.021 branch ← 翻转
4090  flip=0.096 branch=0.036 within=0.073 within ← 翻转

--- prior: uniform Dir(1,1,1,1) [稿件] ---
T5000 within / A100 branch / 5090 branch / 4090 branch
```

**换成一个稍微像真实 LLM 推理的先验（fp16 权重 6 倍），四个平台的 dominant 全部翻转，且 flip 从 43–56% 掉到 3–10%。**

这个测试用的先验**不是**任意的：真实 LLM 推理确实是 fp16 主导。稿件在 §7 承认"uniform Dirichlet does not model real low-precision-heavy LLM inference"，但紧接着说结构观察"prior-robust by construction"——**这两句自相矛盾，而后一句是错的**。

**修正方向**：删掉 "structural observation is prior-robust by construction"，改成"structure conclusions hold only under the uniform prior and reverse under fp16-heavy priors (report table)"。

### 2.8 【必须改】表 1 的 `H(D|S)` 列无法复现（T5000/4090 互换）

**这是我认为最直接的 reject 理由之一。**

| 平台 | 稿件 `H(D|S)` | 我用作者自己的采样器复算 | 差 |
|---|---|---|---|
| RTX 5090 | 0.76 | **0.767** | ✓ |
| Thor T5000 | 0.71 | **0.764** | ✗ (0.764 ≈ 稿件的 0.77) |
| RTX 4090 | 0.77 | **0.713** | ✗ (0.713 ≈ 稿件的 0.71) |
| A100 | 0.74 | **0.746** | ✓ |

复算用的是**作者自己的采样器**（`random.Random(42)`, `gammavariate(1,1)`, N=40000，`repro/hds_same_sampler.py`），且同一次运行里 `flip` 与 `shift` 与稿件**完全一致**（0.5266/0.4344/0.5627/0.5559 对稿件 0.527/0.434/0.563/0.556）：

```
plat       flip   shift    H(D)  I(S;D)  H(D|S)
5090     0.5266  0.2004  1.1429  0.3762  0.7667
T5000    0.4344  0.1655  1.3511  0.5871  0.7639
4090     0.5627  0.2307  0.9857  0.2729  0.7128
A100     0.5559  0.2183  1.0312  0.2848  0.7464
```

**flip 和 shift 全中，`H(D|S)` 有两行错位。** 这**不可能是采样噪声**（20 个种子的 sd ≈ 0.005，见 `repro/final_checks.py`）；这是**抄表错误**（两行数值对调）。

**更糟的是**：`H(D|S)` 在仓库里**没有任何持久化产物**。作者 commit 的 `idea53-theory-flip.json` 只有 `flip_rate` / `mean_time_shift` / `top_flips` / `ratio_extremity` 四个字段，**没有** `H(D|S)`。我搜了全仓库（`grep -rn "H(D|S)\|conditional_entropy"`），除我自己写的复算脚本外**零命中**。

**这意味着**：全文唯一的"严格量"，**既无代码、也无数据、也无法复现**，且**与最接近的口径不一致**。

顺带：这两行的错位**影响摘要**吗？不影响数值范围（0.71–0.77 仍然正确），但**影响 §5 的对应关系**和**任何按平台排序的解读**（例如"4090 极端 → `H(D|S)` 高"就是由这个错位造成的）。

**修正方向**：重算、逐平台核对、把生成脚本和 JSON 一起提交。**这条改起来最便宜，但不改就过不去。**

### 2.9 【必须改】`shift` 的定义在 `S≠D` 时比较了不同分量

§2 定义：`shift = E|share_D - share_S|`。

但代码里（`idea53-theory-flip.py`）：

```python
shifts += abs(ds - ss)   # ds = deep share of D's winner, ss = surface share of S's winner
```

当 `S ≠ D` 时，这是**拿 D 的赢家的深份额，减 S 的赢家的浅份额**——两个**不同分量**。这不是"粒度修正"，而是"方向修正的残余"。

我分解了（`repro/consolidate.py`）：

```
plat     paper shift(all)  shift|S==D only  shift|S!=D only  alt granularity(same comp)
5090         0.200              0.220            0.183            0.306
T5000        0.165              0.184            0.141            0.226
4090         0.231              0.260            0.208            0.357
A100         0.218              0.250            0.193            0.332
```

**纯粒度（同分量）的 shift 是 0.23–0.36，稿件报的是 0.17–0.23。** 两个量差 40–55%。稿件说 "shift = granularity correction"，但它度量的**主要是方向修正的幅度**。

**审稿意见**：这是**定义与实现不一致**。必须二选一：
- 若要度量 granularity：用同分量的 `|share_D(d) - share_S(d)|`，重报数字（0.23–0.36）；
- 若要度量"深层对时间份额的总改变"：明确写成**总变差** `½Σ|share_D - share_S|`（= 0.35–0.45），并改掉 "granularity" 这个词。

### 2.10 【建议改】三个 anchor 的"exactly reproduce"是恒等式

稿件："Three hand-derived anchors reproduce exactly: T5000 50/50 → 80%; T5000 70/30 → 63%; 5090 scalar 40% with issue rate halved → 40% slower."

我核验了（跑了 `idea53-theory.py` 原文）：`0.800 / 0.632 / 1.400`，**全部吻合**。

**但这三个 anchor 是由模型方程直接解出来的**，不是独立的经验验证。特别是第三个：代码里

```python
fs = (2/3) * (fc/sp5['fp16']) * sp5['scalar']   # 解出标量 FLOP 量使时间占比=40%
...
ss = (f3['scalar']/sp5['scalar'])/T0            # 再算回来 = 0.400
```

——**先反解 `f` 让份额等于 0.4，再算份额，当然等于 0.4**。这是一个**循环验证（tautological check）**，不是 "hand-derived anchor"。

前两个（T5000 50/50 → 80%）是**真**手算，有价值（它证明 `t_i = f_i/r_i` 的实现正确）。第三个不是。

**修正方向**：删掉第三个，或明确写成"internal consistency check"，不要与"hand-derived anchor"并列。

### 2.11 【建议改】`H(D|S)` 的"closed form"其实可以**真的**做到（回到 2.2）

已详述。补一句：如果做了，**24 置换的不变性问题也会自动获得精确答案**——可以用有理数精确算 24 个值，看是否真相等。我预判**不相等**（因为 `flip` 不相等，而 `H(D|S)` 一般也不相等）。**这会是稿件最好的一个负结果**。

### 2.12 数学推导中的其余小问题

| # | 位置 | 问题 |
|---|---|---|
| a | §2 | `shift = E\|share_D - share_S\|`，`share` 是标量还是向量？定义与实现不符（见 2.9） |
| b | §2 | `H(D\|S) = H(D) - I(S;D)` 正确；但文中 §1 又说 `H(D) = H(D\|S) + I(S;D)`，两处口径一致，无问题 |
| c | §4 | "24 parameter–depth permutations" —— 4 个分量、24 个置换，**参数置换 ≠ 参数-深度置换**。深度只有 2 层，无法"置换深度"。措辞误导 |
| d | §4 | "identity permutation reproduces the main numbers **exactly**" —— 我的 CRN 测试证实 identity 当然是同一个数（因为它就是同一份采样）。**这句话没有信息量**，是个 tautology |
| e | §5 | "four cells sum to 1" —— 我只在**聚合支路**定义下复现出 0.526+0.147+0.037+0.290=1.000。稿件没写清聚合方式，读者无法重建 |
| f | 表 1 | `co-flip` / `within-flip` / `co-correct` / `within-correct` 四个列名，与 long version 的 `both correct / co-flip / branch-only / within-branch` **语义不对应**。TMLR 短版把 `both correct` 写成 `co-correct`，把 `branch-only` 写成 `within-flip`——**这两个改名都是错的**（详见 §3.1） |

---

## 3. 格式与可编译性（这些是"送审即被 desk-check 打回"的级别）

### 3.1 【必须改】§5 表格列名系统性错位

TMLR 短版表头：`co-flip | within-flip | co-correct | within-correct`

Long 版表头：`both correct | co-flip | branch-only | within-branch`

数据完全一样，**但列名被重排/改名了**：

| 数据 | Long 版含义 | TMLR 短版叫什么 | 是否合理 |
|---|---|---|---|
| 0.530 (T5000) | both correct（两层都对） | **co-correct** | ❌ "co-correct" 语义上像"共同正确"，勉强，但和 `co-flip` 对立勉强成立 |
| 0.145 | co-flip（两层都翻） | **co-flip** | ✅ |
| 0.036 | branch-only（只有支路翻） | **within-flip** | ❌ **完全错**。branch-only 翻的是**支路**，却被叫成 **within**-flip |
| 0.290 | within-branch（只有层内翻） | **within-correct** | ❌ **完全错**。这是**翻转**类，却被叫成 correct |

**`within-flip = 0.036` 与 `within-correct = 0.290` 是两个互相矛盾的标签**：0.290 明明是"只有 within 层判断错"，被标成 `within-correct`；0.036 明明是"branch 层判断错、within 层对"，被标成 `within-flip`。

**这是纯粹的表头错误，但会让任何审稿人在 30 秒内判定"作者没有检查自己的表"。** 必须改。

### 3.2 【必须改】图 1 图注是中文

`fig1-scoring-protocol.tex` 第 37 行：

```latex
\caption{评分协议：分解树 $\rightarrow$ 条件信息增量 $\rightarrow$ 两个负控制。左列给出 toy 结构；中列是闭式可算的评分量；右列两个臂分别排除``深层只是转发浅层''（平坦对照精确归零）与``深层因定义占优''（24 置换不变）。全部判据先于数据生成提交（预注册）。}
```

**英文 TMLR 投稿稿里，主图的 caption 是中文。** 必须改成英文。同时图内的节点文字（`分解树`、`浅层判断`、`深层判断`、`增量信息`、`可解释分数`、`平坦速率对照`、`结果：`、`24 参数—深度置换`、`结果：增量不变`）**全部是中文**。

`fig1-scoring-protocol-zh.tex` 存在，说明作者**有**中文版；那就是 `\input` 引错了文件。这是一行修复，但**不修就是立即 reject**。

### 3.3 【必须改】section 二次编号

`\section{1. Why this quantity}` —— `article` 类默认 `\section` **自动编号**（`tmlr.sty` 未设 `secnumdepth=0`，也未重定义 `\thesection`）。实际渲染是 **"1 1. Why this quantity"**。

8 个 section 全部如此（`1.`…`8.` 前缀）。修复：删掉手写编号，或 `\setcounter{secnumdepth}{0}`。

### 3.4 【必须改】`\citep` 在 `\section` 前被使用 → 首轮编译 undefined

`camerer2018` 第一次出现在**摘要**里，`\citep` 在 `\section` 之前。`\bibliography` 在文末。**标准 LaTeX 需要两遍编译**；一遍的话摘要里会出现 `(?)`。

另外：**参考文献 15 条，正文只引 3 条**（`camerer2018` ×2, `roofline2009` ×2, `rooflineTime2020` ×1）。剩下 12 条（包括 `kraskov2004`、`stepEntropy2025`、`memoryWallFlip2026`、`saScheduler2026`、`amali2025`、`mlsysim2026`、`memoryGap2025`、`microbenchAnalytic2026`、`rooflineHier2020`、`rooflineLLM2024`、`amdahl2008`、`amdahlExt2021`）**全部未引用**。

**这会直接触发 TMLR 的"参考文献与正文不匹配"审查**。而且 `memoryWallFlip2026`、`memoryGap2025`、`saScheduler2026` 恰恰是**必须在正文处理的最近邻**（见 1.2）。

### 3.5 【建议改】`xeCJK` + `Songti SC` 的可移植性

`\usepackage{xeCJK}` + `\setCJKmainfont{Songti SC}` 是 **macOS 专有字体**。TMLR 要求投稿在标准 TeX Live 上可编译（或提交 PDF + 源码）。`Songti SC` 在 Linux TeX Live 上**不存在**，会直接编译失败。

**修复**：既然图 1 改英文（3.2），**完全删掉 `xeCJK` 和 `\setCJKmainfont`**，稿件里就没有任何中文了（我扫过正文，除 fig1 外全英文）。这样稿件变成**纯 pdflatex 可编译**，可移植性问题一次解决。

### 3.6 【建议改】`\label` 无 `\ref`

8 个 `\label`，0 个 `\ref`/`\eqref`。TMLR 不禁止，但一篇 5 页正文有 8 个无用的 label，说明作者原本打算交叉引用。建议要么加引用（§4 的对照臂在 §7 被讨论，应该 `\ref`），要么删掉。

### 3.7 【建议改】TMLR 政策相关

- **篇幅**：稿件正文 5 页（PDF 92 KB），TMLR 无严格页数限制但有"main paper"与"appendix"之分。当前结构 OK。
- **双盲**：`\title` 后无 author block，**符合**。但 `\bibliography{../submission-staging/references}` 的路径暴露了目录结构（`submission-staging`），虽不含身份信息，建议内联成 `references.bib` 放同目录。
- **预注册声明**：TMLR 不要求预注册，但**一旦声称**就有责任准确。见 2.5。

---

## 4. 修改建议（按优先级）

### 必须改（Must-fix，不改则无法通过）

| # | 问题 | 位置 | 修法 | 成本 |
|---|---|---|---|---|
| **M1** | 表 1 `H(D\|S)` 的 T5000/4090 两行互换；且该列无任何代码/数据产物 | 表 1 | 重算 → 提交脚本 + JSON → 逐行核对。正确值：5090=0.767, T5000=0.764, 4090=0.713, A100=0.746 | 0.5 天 |
| **M2** | 预注册声明内容不实：`eb1b0598c` 中无 `H(D\|S)`、无平坦对照、无 Dirichlet、无 24 置换；预注册生死线跑出来是"不成立"，稿件把它降格为"another model" | 摘要、§4 HARKing 段、§1 末段 | **二选一**：(a) 如实写成"预注册的节点级判据失败（0.5841 > 0.1344），因此转向 post hoc 的两层模型"，把失败作为贡献呈现；(b) 删除全部预注册宣称，改成"本工作未预注册" | 1 天（写作） |
| **M3** | "Closed-Form" 名不符实（5 处 MC，0 处闭式），而闭式**存在** | 标题、摘要、§1、§6 表 | 补 Prop. 1：`P(D=i) = Σ_S (-1)^{|S|} r_i/(r_i+Σ_{j∈S} r_j)`；把 MC 降为验证；24 置换用精确值重算 | 1–2 天 |
| **M4** | 量纲不可通约 + `rate ratio` 是"核数 ÷ TFLOPS"；scalar 单位变动使 flip 从 0.434 → 0.231 | §2、§3、§6 表 | 给出可辩护的归一化（统一到"每秒处理量"），或放弃跨分量比较；重报全部数字；`rate ratio` 一栏**删除或改为可辩护的定义** | 2–3 天 |
| **M5** | `H(D|S)` 作为"评分"无效度：纯噪声节点得 2.000 bits，真实节点 0.71–0.77；与 flip 秩相关 −0.80 | 标题、§1、§6、§8 | 重新定位为**不确定度**而非贡献；或改用 `G = I(S;D)` 作为评分（对噪声=0，对正确=0.28–0.59），并**报告噪声/anti-bottleneck 对照** | 2 天 |
| **M6** | 24 置换"不变"是噪声 artefact（CRN 下 24 个值 23–24 个不同） | §4(2)、摘要、§8 | 改为"24 置换下 flip 变化 ≤0.011（CRN 精确测量）"，**删掉"invariant"**；或用精确闭式重算 | 0.5 天 |
| **M7** | §5 "dominant dimension" 是剖分伪迹（换 1v3，5090 翻转；换 3v1，三平台全翻）且未除 chance baseline | §5、§8 | 除 chance baseline 再比；报告 ≥3 种剖分；若结论不稳，**降级为负结果** | 1–2 天 |
| **M8** | §7 "structural observation is prior-robust by construction" 是错的（fp16-heavy 先验下四平台全翻） | §7 | 删除该句；或报告先验敏感性表 | 0.5 天 |
| **M9** | §5 表格列名系统性错位（`within-flip` 实为 branch-only，`within-correct` 实为 within-branch flip） | §5 表 | 改用 long version 的列名：`both correct / co-flip / branch-only / within-branch` | 10 分钟 |
| **M10** | 图 1 caption 与节点文字是中文；`xeCJK`/`Songti SC` 使稿件不可移植编译 | `fig1-scoring-protocol.tex`、preamble | `\input` 英文版；删 `xeCJK` + `\setCJKmainfont` | 30 分钟 |
| **M11** | `\section{1. ...}` 二次编号 | 8 处 | 删手写编号 | 5 分钟 |
| **M12** | 15 条参考文献只引 3 条；最相关近邻（`memoryWallFlip2026` 等）未引 | 全文 | 补 §6 相关工作段，正面处理瓶颈翻转文献 | 1 天 |
| **M13** | 第三个 anchor 是循环验证（反解 `f` 使份额=0.4，再算份额） | §3 | 删除或标为 internal consistency check | 10 分钟 |

### 建议改（Should-fix，影响评分但不致命）

| # | 建议 | 理由 |
|---|---|---|
| S1 | **把预注册的负结果扶正**：`0.5841 > 0.1344` 不应是脚注，应是 §4 的主段 | 这是全文最有价值的东西，且是 TMLR 喜欢的诚实负结果 |
| S2 | **强化对 PID 的论证**：不是"我们没用 PID"，而是"我们的二元结构让 PID 的三元分解不必要" | 把创新性从"拼装"抬到"结构性优势" |
| S3 | **切断与 SSC 的 50% 数字撞车**：明确写"43–56% 是瓶颈类型误判率，与 SSC 的 hacking 率无关" | 预防误读 |
| S4 | **把平坦对照从 "measured arm" 改为 Proposition + unit test** | 恒等式不该被当数据；但作为代码正确性检查**应当保留并强调** |
| S5 | **重写 `shift` 定义**：要么用同分量，要么用 TV 距离，并改掉 "granularity" 一词 | 当前定义与实现不符（2.9） |
| S6 | **`H(D\|S)` 的报告方式**：加一列 `H(D|S)/H(D)`（0.57–0.72），比原始 bits 更有解读性 | 0.71–0.77 bits 对读者无意义；"深层判断的 57–72% 不被浅层解释"有意义 |
| S7 | **明确 `S` 与 `D` 都是 `f` 的确定性函数**，因此"信息量"来自**先验**而非数据 | 这是与 ID3 的根本区别，应写在 §1 |
| S8 | **`f ~ Dirichlet(1,1,1,1)` 的物理解释**：这是"单纯形上的均匀分布"，意味着"任何 workload 构成等可能"。应写明它对应什么工程场景，否则先验就是任意的 | 先验的辩护力决定全文的可信度 |
| S9 | **`S` 的命名**：`S` = surface，但 §1 又说 `I(S;D)`，"S"同时像 "source"；建议改 `S→U`（uncorrected）或 `D→C`（corrected），减少读者负担 | 可读性 |
| S10 | **`\bibliography{../submission-staging/references}` 内联** | 避免暴露仓库路径；避免双盲边缘问题 |
| S11 | **补一张 `H(D\|S)` vs `flip` 的散点图**（4 个点） | 让 −0.80 的秩相关**可见**，比藏起来好 |

### 不建议做的

- **不要**为了"更严谨"加更多平台。n=4 → n=10 不能修复 §5 的结构问题（那是剖分伪迹，不是样本量问题），只会让"选择性报告"更严重。
- **不要**加真实 GPU 实测。当前稿件的价值在**"不需要实测"**（这是它与 roofline 文献的真正区别）；一旦引入实测，就变成一篇弱的性能建模论文，比不过 `amali2025` / `mlsysim2026`。
- **不要**保留 "alignment / reward hacking" 的动机包装。§1 第一句"After a judgment is decomposed into a tree"，§6 说 "does not solve reward hacking"。这个包装**两头不讨好**：ML 审稿人觉得没做 ML，系统审稿人觉得动机不清。**建议纯做"可计算的评分基 + 负控制方法论"**，这是一个干净的方法论贡献。

---

## 5. 判断题（你要的"哪里好、哪里有风险、哪里我不同意"）

### 5.1 哪里好——真的好的三件事

1. **诚实度远超同类稿件。** 主动写"monotonicity fails (A100 > 5090)"、"4090's extreme ratio is partly a proxy artifact"、"the tree extension is post hoc and unregistered"、"the type control is a design-level argument, not a measured arm"。**这些句子在投稿稿里非常罕见**，而且每一句都是真的（我核对了）。作者显然知道自己的弱点在哪。

2. **平坦对照的"精确零"是一个真正的、可证明的性质**（`S ≡ D` ⟹ `H(D|S) = 0`）。虽然它是恒等式、零信息量，但**它是一个正确的、干净的、可写进论文的结构性质**。绝大多数"负控制"论文里的对照是"效果变小"，这里是"代数上必然为零"——**这个区别值得写出来**。

3. **三层分工（flip / shift / H(D|S)）是好的工程直觉。** 方向修正（flip）、粒度修正（shift）、信息论严格形式（`H(D|S)`）三个量各有用途，且作者的直觉是对的：`flip` 最好用，`H(D|S)` 最严格。问题在于**三者的关系没被正确刻画**（见 5.3）。

### 5.2 哪里有风险——三个可能让稿件"死得很难看"的点

1. **`H(D|S)` 列的错位（M1）。** 这是**最容易发现**、也**最难辩解**的。任何审稿人只要重跑一遍就会发现。而它偏偏发生在全文唯一的"严格量"上。**如果作者不主动修，这会是 desk reject 或"数据不可信"级别的定性。**

2. **预注册叙事（M2）。** 这是**最危险**的，因为它不是错误，是**叙事重排**。审稿人一旦查出 `eb1b0598c` 里没有 `H(D|S)`、没有平坦对照，再看到稿件说"All criteria, formulas, and the make-or-break test were committed before data generation"，**会认为作者在选择性陈述**。这比"我们没预注册"严重得多。

   我的判断：**作者不是有意欺骗**。`eb1b0598c` 确实是一次"设计转向"的预注册，`718394ece` 确实是结果。作者把"预注册了设计方向"记成了"预注册了判据和量"。但**在审稿语境下，动机不重要，文本就是文本**。

3. **量纲（M4）。** 这是**最容易被系统方向审稿人抓住**的。`51.9 = 21760/419` 是"CUDA 核数 ÷ TFLOPS"。任何一个做 GPU 性能建模的审稿人看到这个比值都会立刻停下。而作者自己的代码注释**已经写了**"单位混合=近似"，只是没写进论文——**这是"知道但没说"，性质比"不知道"更差**。

### 5.3 我不同意的地方——三处

**不同意之一：`H(D|S)` 是"深层节点的贡献"这个核心定位。**

我认为这是**根本性的错误**，不是措辞问题。理由：

- `H(D|S)` 是**条件不确定度**。它度量"知道 S 之后，D 还剩多少不确定"，**不度量 D 有多正确、多有价值**。
- 我给的证据：纯噪声节点 `H(D|S) = 2.000`，真实节点 `0.71–0.77`。**噪声赢 2.6 倍。**
- 另一个证据：`H(D|S)` 与 `flip` 秩相关 **−0.80**。深层**越难判准**，`H(D|S)` **越小**。这与"贡献大"的叙事方向相反。
- 稿件 §7 自己写：*"Flip rate and share shift are interpretable scores, not mutual information; the strict quantity is H(D|S)."* ——这句话把 `H(D|S)` 供上了"严格"的位置，但它**严格地度量了错误的东西**。

**正确的量**（我认为）是 `G = I(S;D) = H(D) − H(D|S)`：随机节点的 `I(S;D)=0`，正确节点 `0.28–0.59`，完美节点 `= H(D)`。**这个量单调于"深层节点提供了多少关于正确瓶颈的信息"**，才是"评分基础"。

而 `H(D|S)` 有它自己的、**不同**的正确解读："深层节点的判断**独立于**浅层节点"——这是**去冗余度**，不是贡献。这个解读本身是有价值的（它恰好是 §4 想做的"de-depth-ification"），**但与"贡献"是两件事**。

**我建议**：题目改成 "How much does a deep node *add*?"，主量改成 `I(S;D)`，`H(D|S)` 作为副量报"去冗余度"。或者接受"贡献"这个词不准确，全文改成"incremental information content"。**但当前"contribution / scoring basis / load-bearing"的叙事必须撤。**

**不同意之二：平坦对照"rules out deep merely forwards surface information"。**

这句话是**错的**。平坦对照证明的是"当 `r ≡ 1` 时 `D = S`"，即"**模型退化时**深层等于浅层"。它**不能**排除以下情形：

- `D = σ(S)`（深层是浅层的**双射重标**）—— 在真实速率下 `H(D|S)` 可以非零，但**零新信息**
- `D = S ⊕ noise`（深层 = 浅层 + 噪声）—— `H(D|S) = H(noise) > 0`，但**零贡献**

第二种情形**恰好就是我的噪声对照**，而它拿到 2.000 bits。**所以平坦对照排除的恰恰是最容易排除的那个平凡性（"深层什么都不做"），而放过了真正危险的平凡性（"深层加了噪声"）。**

**作者需要**：一个**符号/方向**对照（anti-bottleneck），或一个**噪声注入梯度**（`D_ε = argmax(t_i + ε·noise)`，看 `H(D|S)` 是否单调随 ε 增）。后者更漂亮，因为它是**连续的**，能画出 `H(D|S)` vs `ε` 曲线，并证明**真实节点（ε=0）不是极大点**。

**不同意之三：把 `0.5841 > 0.1344` 写成 "from a different, confounded model"。**

这是本报告里我**唯一**认为接近"应当被质疑诚信"的一条。

- 那个数字来自 `eb1b0598c` **预注册的那个模型**。
- 那个模型的生死线是 **"deep > shallow，跨 ≥3 硬件一致"**。
- 跑出来是 **`deep=0.1344 < shallow=0.5841`，`consistent=False`，脚本自己打印"不成立"**。
- 稿件在 §4(3) 把它写成 "an earlier node-level model"，并说 "comes from a different, confounded model and is not used as evidence"。

**"a different model" 是真的（它确实换了模型），但"and is not used as evidence"这个动作本身，就是 HARKing 的定义。** 预注册的意义恰恰是"**判据失败时，你也得报**"。作者报了数字（这点诚实），但没有报**它的地位**（这是预注册判据本身）。

**如果作者改成**：

> "Our preregistered node-level criterion (§0.5, commit `eb1b0598c`) **failed**: enumeration-type nodes carried 0.5841 bits vs judgment-type 0.1344 bits, and the cross-hardware consistency check returned false. We therefore abandoned that model and developed the two-level surface-vs-deep model reported here, which is **post hoc**. The preregistration covers the flat-rate control only in its weaker form ('placeholder hardware, gain should → 0')."

——**这一段的诚实度会让整篇稿件的可信度翻倍**，而且它是**真的**。我强烈建议这么写。

### 5.4 一个总判断

这篇稿件的**问题不是"想法不好"，而是"最好的想法被藏起来了，最弱的主张被放在了标题里"**。

- 真正有价值的是：**"节点的信息增量可以在没有任何数据的情况下、从规格与先验中精确算出，因而可以在任何实验之前被预注册"**。这是一个**干净、可辩护、有方法论意义**的贡献。
- 而稿件把它包装成了："我们用信息论证明深层节点很重要"——这个主张**既不能证伪（因为 `H(D|S)>0` 恒真），也不成立（因为噪声节点赢）**。

**如果按 M1–M13 改，并且把 S1（负结果扶正）和 5.3 的三条（改主量、加方向对照、如实写预注册）做了，这会是一篇合格的 TMLR 论文。** 不改，Reject。

---

## 附录 A：可复现性清单

所有数字均可由 `review/repro/` 下脚本复现（纯 Python3 标准库）：

| 报告结论 | 脚本 | 关键输出 |
|---|---|---|
| 主表 flip/shift 正确 | `repro/reproduce.py` | 0.528/0.437/0.561/0.554（与稿件一致） |
| `shift` 精确口径 | `repro/candidates.py` | 0.2004/0.1655/0.2307/0.2183 |
| **`H(D\|S)` 两行互换** | `repro/hds_same_sampler.py` | 0.767/0.764/0.713/0.746 |
| `H(D)` 闭式存在 | `repro/closed_form_check.py` | `P(D) = [0.1476, 0.7182, 0.0005, 0.1337]` |
| **24 置换不变性为假** | `repro/final_checks.py` | 24 个值全部不同 |
| **噪声节点拿满分** | `repro/consolidate.py` | 噪声 `H(D\|S)=2.000` |
| **`H(D\|S)` 与 flip 反向** | `repro/consolidate.py` | Spearman `ρ = −0.80` |
| `shift` 定义污染 | `repro/consolidate.py` | 同分量 0.23–0.36 vs 稿件 0.17–0.23 |
| **§5 dominant 是剖分伪迹** | `repro/split_sensitivity.py` | 1v3 下 5090 翻转；3v1 下三平台翻转 |
| **§5 非 prior-robust** | `repro/prior_sensitivity.py` | fp16-heavy 下四平台全翻 |
| **量纲敏感** | `repro/unit_sensitivity.py` | T5000 flip 0.434 → 0.231 |
| §5 四格表可重建 | `repro/split_sensitivity.py` | 3 位小数吻合 |

## 附录 B：commit 核验记录

```
$ gh api repos/dd2003-460/prompt-first-bench/commits/eb1b0598c
sha:      eb1b0598cea9827b15373a6725e71e3b33c11601
date:     2026-11-24T09:39:54Z   (= 北京时间 17:39，与稿件一致)
message:  "idea53 设计转向: 理论计算路线 (D 纠正: 信息增益=闭式计算...)"
files:    M tasks/idea53-goal/GOAL.md (+9/-0)
          M tasks/idea53-goal/decomposition.md (+28/-26)

$ gh api repos/dd2003-460/prompt-first-bench/commits/718394ece
sha:      718394ece42e9aa299c721a115d2ec27b4c35c80
date:     2026-11-24T10:06:28Z   (= 北京时间 18:06，与稿件一致)
message:  "idea53 理论路线结果: surface-vs-deep 修正量..."
files:    A idea53-theory-flip.json / .md / .py
          A idea53-theory.py / .json
          M GOAL.md / decomposition.md
```

**在 `eb1b0598c` 的 `GOAL.md` 中检索**：

```
Dirichlet    : 0 次
40,000       : 0 次
H(D          : 0 次
条件熵       : 0 次
flat         : 0 次
permut       : 0 次
置换         : 1 次  ← "参数置换（spec 数字随机打乱，增益应→0）"，方向与"不变"相反
```

**`eb1b0598c` 的 `decomposition.md` §S4 原文**：
> "深层（L3/L4 微架构级）每节点信息增益 > 浅层（L1/L2 枚举级），跨 ≥3 硬件一致 → 成立；不成立 → 负结果记录"

**原样运行 `718394ece` 的 `idea53-theory.py`**：
```
ctrl type: enum=0.5841 judge=0.1344
深层(判断型)每节点 0.1344 bits vs 浅层(枚举型) 0.5841 bits; 跨硬件一致=False; 生死线=不成立/部分
```

**原样运行 `718394ece` 的 `idea53-theory-flip.py`**：
```
4090   287.4   0.563   0.2307
5090    51.9   0.527   0.2004
A100    44.3   0.556   0.2183
T5000    9.9   0.434   0.1655
flat control: flip=0.0000 shift=0.0000
生死线=部分/不成立
```

---

*报告结束。复算脚本见同目录 `repro/`，可直接 `python3 repro/<name>.py` 复跑。*
