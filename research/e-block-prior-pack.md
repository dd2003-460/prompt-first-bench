# E 块先验包 — 目标函数设计 + 方差感知（成璐 2026-11-12 指令）

> origin: ai · 传话太监代写 · 最高优先级
> 用途：你写/校准目标函数前必须过一遍这个包。不是"参考"，是**约束**——你的参数选择必须能对着这里的锚点说"我为什么选这个值而不是那个"。

## 1. 坑清单（具体到我们的场景，不是泛泛的 Goodhart）

| # | 坑 | 我们代码里的位置 | 后果 | 已有缓解 | 还缺什么 |
|---|-----|-----------------|------|---------|---------|
| P1 | contribution 单点估计（temp=0, n=1）→ 方差盲区 | classify_edge line 255/274 | 高不确定性分支被误剪（看起来贡献低其实只是采样噪声） | classify_edge_var 已写但默认 contrib_samples=1 → **退化为现状** | 启用多采样 + 标定 n 和 λ |
| P2 | objective 自估公式无 grounding | Decision 19 的 Final_Score 只打印不驱动 | 模型写个好看但区分度为零的公式，所有 edge 得分趋同 → 排序失效 | EA3 gold 题反向校验（设计有，没跑） | 跑 ≥3 道已知优劣的题验证公式区分度 |
| P3 | 停止判据只看 gain 均值 | J_stop: gain < ε 连续 M 轮 | 方差大时提前停 = 探索不足，树浅了 | stop_std_max=0.15 已定义 | 接进主循环（目前只定义没调用） |
| P4 | judge 本身是 LLM → self-play 噪声 | drb_race_judge.py 用 qwen2.5-7b | 分数波动 ±3-5 分，n=10 时可能吞掉真实差异 | B-face 异族 judge 设计（未跑） | 至少 2 个 judge 交叉 + 报告区间不报点值 |
| P5 | 阈值拍脑袋（gain_threshold=0.5, contribution_threshold=0.1） | s5_state_machine.py line 105/118 | 没有数据支撑 → 换题面就失效 | 无 | 用 S8M n=30 数据回标：看实际 gain 分布定合理切点 |
| P6 | arxiv-only retriever → 金融/社会/娱乐题搜不到东西 | gptr_drb10_run.py RETRIEVER="arxiv" | 6/10 DRB 题只出 300-600 字空壳 | 无 | 换 Bing/DDG-lite 或标注为"retriever 受限下界" |

## 2. 对标锚点（你的参数得有参照系）

### DRB Leaderboard 分布（GPT-5.5 judge, 2026-11-10, 来源① research/drb-leaderboard-gpt55.csv）

| 档位 | 分数范围 | 代表 | 含义 |
|------|---------|------|------|
| SOTA harness | 54-57 | cellcog-max 56.72, beane-harness 56.14 | 定制 agentic pipeline，输出公开方法闭源 |
| 大厂产品 | 43-50 | OpenAI Deep Research 47.84, Perplexity 43.05 | 通用 deep research 产品 |
| 弱基线 | <42 | grok-deeper-search 41.22 | 基本不可用 |

**对我们的含义**：如果 GPT-Researcher + Qwen3-27B 管线在 DRB n=10 上拿到 >50，说明框架+本地模型组合已经超越 OpenAI 产品；>56 则超越所有已发表 SOTA。但前提是 retriever 不能是 arxiv-only（见 P6）。

### 我们自己的基线（S8M n=30, rubric v2, 来源② runs/s8-report.md）

| 臂 | 分数 | 含义 |
|----|------|------|
| S0 (no hook) | 0.5558 | 裸模型 |
| S1 (+search) | 0.5746 | 加搜索几乎没提升（Δ+0.019） |
| S5 (+hierarchy+verify) | 0.7907 | 层级分解+核验 → 大跳 |

**对 gain_threshold 的启示**：S1→S5 的 Δ=0.216 是"有效结构改进"的量级。如果 decompose 一轮的 marginal gain 连 0.05 都到不了，大概率是在做无效展开。0.5 作为 threshold 可能太高（会过早停），建议先用 S8M 数据的 gain 分布做 empirical CDF 再定。

### CellCog-max 报告特征（来源① HF Space raw_data, 100 articles 已下载检查）

- ~60k chars/article, 106 citations
- MECE 框架方法论（Mutually Exclusive Collectively Exhaustive）
- 结构：Executive Summary → Methodology → 多维度分析 → 结论
- 无模型名、无架构、无工具链披露（闭源 harness）

**对"好答案"标准的具象化**：我们的状态机产出如果要对标这个水平，verify 阶段应该检查：(a) 每个 claim 是否有 ≥1 个可溯源引用 (b) 维度覆盖是否 MECE（gap_check 已经在做）(c) 最终合成是否有 executive summary 级别的凝练。

## 3. 方法论锚（社科/决策科学视角，不是纯 ML reward hacking）

### 3.1 Multi-Attribute Utility Theory (MAUT)

目标函数 = 多个维度的加权组合。关键问题：**权重怎么定？**

- AHP (Analytic Hierarchy Process): 两两比较维度重要性 → 一致性检验 (CR < 0.1) → 导出权重向量
- 对我们的映射：RACE 四维度 (Comprehensiveness / Insight / Instruction Following / Readability) 的权重不应该等权，应该按"deep research 场景下哪个维度最区分好坏答案"来定
- **操作建议**：用 DRB leaderboard 的 18 个 entry 做回归——overall_score ~ w1*comp + w2*insight + w3*IF + w4*read，拟合出的 w 就是经验权重

### 3.2 Variance-Aware Decision Making

经典框架（Raiffa 1960, decision under uncertainty）：
- 期望效用 = E[U] - λ·Var(U)^β （β∈[0,1] 控制风险厌恶程度）
- 对我们的映射：剪枝判据 `mean(contribution) + λ·std(contribution) < θ` 就是这个结构的特例（β=1）
- **λ 的标定**：不是拍 1.0，而是看"误剪率 vs 保留冗余率"的 trade-off curve。用 drb-2 那 51 个 degraded 节点做 retrospective：如果当时有方差信息，哪些会被正确保留？

### 3.3 Construct Validity（构念效度）

你的指标真的测你想测的东西吗？
- "contribution" 想测的是"这个子维度对最终答案的信息增量"
- 但 LLM 单次调用给的 0-1 分数可能测的是"这个子维度听起来多重要"（表面相关 ≠ 因果贡献）
- **检验方法**：ablation——把某个子维度从树里删掉，看最终答案质量掉多少。掉得多 = 真贡献高。这是 ground truth，LLM 打分只是 proxy。
- 成本：每道题 ×N 个 ablation run，贵但只在 calibrate 阶段做一次

### 3.4 Goal Setting 的社科 SOP（Locke & Latham 目标设定理论）

- 目标要 specific（不是"提高质量"而是"comprehensiveness ≥ 55"）
- 要有 commitment（模型自估的 objective 如果没有后续 verify 回路 = 没有 commitment = 无效目标）
- 难度适中（太容易 = 没挑战，太难 = 放弃）→ 对应我们的 gain_threshold 不能设得太高
- **对我们的直接启示**：E1（objective 进决策回路）的本质就是给模型一个有 commitment 的目标——不是"估个公式打印出来"，而是"每轮 decompose 后对照公式算当前得分，低于阈值就继续拆"

## 4. 给你的具体行动建议（不是选项，是推荐路径）

按产投比排序：

1. **先修 P6（retriever）**：DRB10 那 6 道短题重跑用 Bing retriever。不做这步，后面所有分数都是 garbage in garbage out。成本：改一行配置 + 重跑 20min。
2. **P5 回标阈值**：从 S8M n=30 的 per-round gain 数据画分布图，定 empirical 90th percentile 作为新 gain_threshold。成本：一段 pandas。
3. **P1 启用多采样**：contrib_samples=5, temperature=0.3, λ=1.0 先跑一版看 std 分布，再调。成本：GPU rerun 时间 ×5（但只跑 classify_edge 步骤，不是全树）。
4. **P2 gold 题校验**：拿 3 道已知答案质量的题（比如 DRB reference article 当 gold），跑我们的 objective 公式看排序是否正确。成本：3 次 LLM 调用。
5. **P3 接 stop_std_max 进主循环**：一行改动。

做完 1+2+5 就能重新跑 GPU 题看效果（EA1 验收）。3+4 是下一轮的事。

## 5. 成璐原话（最高优先级指令）

> "之前r7有跑复现我记得，那这种原生涌现感觉，很适合跑idea，可以调研"
> "主线还是优化但是我已经没头绪了目标函数看起来确实可以激活但是我们几乎是拍脑袋随机赶着ai"
> "所以让他自己写目标函数，优化啥的怎么样了，他可以准确度量信息并且考虑var这种问题吗"

翻译成人话：你要的不是"加个 variance 参数"，是**整个目标函数从装饰品变成真正的控制器**。上面 5 条是路径，但核心问题是 E1（objective 进回路）——如果公式不进 classify_edge 和 stop 的决策逻辑，其他都是锦上添花。