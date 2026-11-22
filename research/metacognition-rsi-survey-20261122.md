# 元能力 / 自我认知 / 递归自我改进 文献调研（2026-11-22）

> origin: ai · 2026-11-22 · 触发：D 质疑"scaling law 和 bitter lesson 到底指什么" + "模型能否实现自我认知/自主规划" + "信息充分=AGI 命题是否可靠"
> 方法：local-first（pfb/research 无覆盖，competitor-survey 是 deep research agent 不相关）→ arXiv API 滚雪球两轮（元认知/自我认知/校准/RSI）→ 关键 4 篇拉全文摘要核实。
> 置信度：arXiv ID/摘要来自 arxiv.org 官方页（来源①，本轮工具输出）。论文自报数字未独立复现，标 [待交叉验证]。

## §1 核心发现（按 D 的三个问题组织）

### 问题 A：模型能否实现"自我认知/自主规划"？scaling 能不能涌现出来？

**结论：模型有部分自我认知（事实层），但缺完整的元认知（监控+控制）。scaling 能涌现前者，没有证据能涌现后者。**

**A1. 事实层自我认知：存在，且随 scaling 出现**
- **Factual Self-Awareness** — arXiv:2505.21399（2025-05-27, Tamoyan et al.）
  - 证据：LLM 在 residual stream 里有**线性特征**编码"这次事实回忆对不对"（internal compass），在生成时点就存在，不是生成后检查。
  - scaling：跨模型规模实验显示 self-awareness **训练早期快速出现、中间层峰值**。
  - 含义：模型"知道自己这次可能答错"的信号**在权重里**，可被 logprob 探针读出。
  - 与 D 已有洞察对齐：logprob 探针做优先级排序（不做触发）——这篇给了它存在性的证据。

**A2. 完整元认知（监控+控制）：默认缺失**
- **Metacognitive Myopia** — arXiv:2408.05568（2024-08-10）
  - 核心论点：LLM 缺元认知的**两个组件**——monitoring（监控）和 control（控制）。
  - 缺这两样导致 5 类症状：无效 token 整合、冗余信息易感、忽略基础率、基于频率的决策规则、嵌套数据的高阶统计推断失当。
  - 含义：**"知道自己不知道"（monitoring）+ "主动去补"（control）这一整环，模型默认没有。** 这正是 harness 填的缺口。
  - 关键：这篇把元认知定义为 monitoring+control 两组件，不是单一"自知"。模型有 A1 的 factual signal（监控的一半），但缺 control（主动行动去补缺口）。

**A3. 自我认知是否"涌现"：涌现的是事实层，不是元认知控制**
- 搜 "emergence AND metacognition AND LLM" 命中的涌现论文（2511.00926 AI Self-Awareness Index、2411.18530 自我认同数学框架）都是**事实层/自我定位**，不是"监控+控制"的完整元认知循环。
- 没有一篇证明"scaling 到某个规模，监控+控制的完整元认知循环会自发涌现"。
- **这是 D 怀疑的对的地方**：scaling law 测的是固定任务 loss 下降，bitter lesson 测的是有奖励信号任务的搜索+学习。元认知（监控+控制）**没有 loss 可以优化**（"知道自己不知道"没有 ground truth），所以不在 scaling law 的承诺范围内。

### 问题 B：递归自我改进（RSI）的边界——harness 自我改进会不会退化？

**结论：RSI 真实存在但"有界"（bounded by designer），且有一个具体的失败模式：贪心 gate 把噪声当进步。**

**B1. RSI 是有界的（designer 设的边界）**
- **Bounded Recursive Self-Improvement** — arXiv:1312.6764（2013-12-24, Nivel/Thórisson/Schmidhuber et al.）
  - 核心：机器通过建模自身+环境，在**设计者设的边界内**实现递归自我改进。
  - 原则：autocatalysis（自催化）、endogeny（内生性）、reflectivity（反思性）。
  - 含义：自我改进不是无限的，被 harness/设计者边界约束。**我们这套 harness 就是那个"边界"。**

**B2. harness 自我改进的具体失败模式（直接警告我们）**
- **Trustworthy RSI with Statistical Guarantees (TRUST)** — arXiv:2611.10787（2026-11-07, Gao et al.）
  - **直接对应我们**："refining their own harnesses **without retraining** their underlying LLMs"——和我们的"prompt+hook 不改权重"完全同构。
  - **核心警告**：greedy gate（只看验证分数更高就接受更新）**会把观察到的增益误判为真实进步，导致性能退化**。
  - 数字 [待交叉验证]：greedy gate 接受劣化更新的比率 45.59% → TRUST 统计 gate 降到 2.78%。
  - 用的模型：DeepSeek-V4-Flash 和 **Qwen-3.8-Flash**（和我们 27b 同族）。
  - **对我们的直接含义**：pfb bench 分数就是那个"验证分数"。如果我用它贪心地接受 harness 改动（"分数涨了所以这个改动好"），45% 的概率是在接受噪声。需要统计 gate（多次重跑 + 显著性检验），不能单次分数涨就接受。

**B3. RSI 的近期方向（2026 密集）**
- SwarmRSI（2610.20431）：科学 agent swarm 的 RSI。
- COEVO（2609.33398）：context 和参数共同进化做 RSI。
- SciMARS（2611.12552）：多 agent harness 的闭环递归任务局部适应。
- 趋势：RSI 从理论进实践，但**全部强调"gate/统计保证/边界"**，没有一篇是"无界自我改进"。

### 问题 C："信息充分 = 决定是否成功的唯一条件 = AGI" 这个命题可靠吗？有人说过吗？

**结论：命题本身不可靠（三个漏洞），但它的"精化版"可靠，且接近三个已有思想。没有人精确说过原命题。**

**C1. 原命题的三个漏洞**
1. **循环定义**："信息充分"本身需要知道答案才能判定。"信息是否充分"的判定依赖"答案是什么"，所以"信息充分"不能独立定义。
2. **混淆信息与计算**：即使信息充分，模型还需要**推理/计算**出答案。信息充分 + 推理能力不足 = 仍然失败。所以不是"信息充分"一个条件，是"信息充分 + 推理能力"两个。
3. **真正的瓶颈是元认知，不是信息**：模型失败通常不是因为"缺信息"，而是因为"不知道自己缺信息"（metacognitive myopia，A2）。所以真正的 AGI 条件不是"信息充分"，是"模型能判断自己的信息是否充分 + 主动补 + 推理到答案"。

**C2. 精化版（可靠）**
> **AGI = 模型能监控自己的信息缺口（monitoring）+ 主动获取缺失信息（control）+ 推理到答案（reasoning）**
> 即完整的元认知循环。

这个精化版：
- 可操作化（我们的 bench 测的正是这个循环的质量：coverage/压缩/Pareto）。
- 对齐 A1+A2：模型有 monitoring 的一半（factual signal），缺 control（主动补）和完整的 monitoring（知道自己不知道什么）。
- 对齐 B1：harness 就是外部提供 monitoring+control 的"边界"，模型内部化这个循环的点 = AGI。

**C3. 接近的已有思想（没有人精确说过原命题，但有三条相邻线）**
1. **Solomonoff induction**（Solomonoff 1964-1978）：给定环境的完整描述，最优归纳推理。这是"信息充分→最优决策"的理论极限，但是理论构造，不是操作化 AGI 定义。
2. **World model = AGI**（LeCun JEPA 2022, Ha & Schmidhuber world models 2018）：AGI = 完整的世界模型。接近"信息充分"但框架是"world model"不是"信息充分"。
3. **Metacognitive loop**（A2 的 monitoring+control）：把 AGI 定义为"能监控+控制自己的认知"。这是精化版 C2 的直接来源。

**C4. 判断**
- 原命题"信息充分=唯一条件=AGI"：**不可靠**（循环定义 + 混淆信息/计算 + 漏掉元认知瓶颈）。
- 精化版"元认知循环=AGI"：**可靠**（可操作化、对齐文献、我们的 bench 直接测它）。
- 没有人精确说过原命题；精化版是三条相邻线的交集，是我们自己的综合。

## §2 对我们框架设计的直接含义

1. **logprob 探针有存在性证据**（A1, 2505.21399）：模型内部有 factual self-awareness signal，可被读出。D 的"logprob 做优先级不做触发"有文献支撑。
2. **harness 填的是 monitoring+control 缺口**（A2, 2408.05568）：SM 的 checkpoint/分解/验证/预算 = 外部提供元认知循环。
3. **harness 自我改进必须用统计 gate，不能贪心**（B2, 2611.10787）：pfb bench 分数不能单次涨就接受改动，需要多次重跑+显著性。这是新发现的设计约束。
4. **RSI 有界**（B1, 1312.6764）：harness 自我改进被设计者边界约束，不是无限。
5. **AGI 的操作性定义 = 元认知循环**（C2）：我们的 bench 测"离元认知循环完全内部化还差多少"（SM 增益 = 缺口）。

## §3 待办
- [ ] 2611.10787 TRUST 的 45.59%→2.78% 数字交叉验证（ego-browser 问 ≥2 LLM：是否有独立复现/质疑）
- [ ] 2505.21399 的"linear feature in residual stream"是否被独立复现（这是 interpretability 声明，单源）
- [ ] 把"统计 gate"约束写进 harness 自我改进 SOP（pfb bench 分数不能贪心接受）
- [ ] 精化版 AGI 定义（元认知循环）落进 D1-persona-align 的目标函数索引
