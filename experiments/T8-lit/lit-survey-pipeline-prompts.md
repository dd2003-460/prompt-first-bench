# T8 Part B: Pipeline Prompt 文献调研

> origin: ai · arena agent mode · 2026-11-02 UTC  
> 来源数: 7（不同研究团队；均为开放论文/预印本，无付费墙）  
> 覆盖: arXiv / NeurIPS / ICLR（含一篇 2026 年预印本）

## 方法与范围

检索日期 2026-11-02；关键词：`LLM agents pipeline ablation planning reflection remove stage empirical study agent workflow`、`self correction large language models cannot self correct reasoning without external feedback`、`Self Refine iterative refinement rounds performance diminishing returns`、`Reflexion language agents verbal reinforcement learning ablation`、`LLM as judge position verbosity self preference bias`、`CRITIC tool interactive critiquing`。筛选：优先原始论文、会议全文和可检查表格，纳入阶段/反馈消融或明确对照；排除只提供框架功能、无效果对照的介绍；2023–2026 补充经典研究与较新直接证据。搜索不是穷尽式系统综述，未对 AutoGen、CrewAI、LangGraph 宣称全面覆盖。

conf 是对**该条表述在限定条件下成立的主观信心**，不是统计置信度或效应概率。百分比差异均用百分点（pp）；论文单项结果非其他团队复现。交叉验证指不同团队对相近机制的证据相互印证，不代表数值或 pfb 结果已被独立复现。没有读取仓库其他文件；L1、pfb、M8 和 C3 仅按任务描述理解，不假定其具体实现。

## Q1: Multi-stage pipeline 各阶段贡献度

- **有阶段消融，但不是干净的“只删除第 N 步 system prompt”。** PIVOT 的旅行任务阶段消融报告相对完整系统的平均下降：Verify 13.3、Plan 11.4、Evolve 10.8、Inspect 4.2；这支持阶段效应不均，但移除的是功能阶段，涉及流程及信息，不可解释为纯 prompt 文字效应。该 2026 预印本结果及度量口径见表 2；不能移植其数值到 pfb。来源：https://arxiv.org/html/2605.11225v1 。conf=0.88。
- **独立机制交叉验证：阶段依赖与非加性。** Reflexion 在 HumanEval Rust 最难 50 题的表 3 中：基础 0.60，保留测试但去反思 0.60，保留反思但去测试 0.52，完整 0.68（pass@1）。反思的删除效应依赖测试是否存在，且相对于完整系统去掉测试的差为 16 pp、去掉反思为 8 pp；不是每个 prompt 可独立分配固定份额。PIVOT 与 Reflexion 支持不均/交互的方向，但任务、指标和干预不同，非同一数值重复实验。来源：https://arxiv.org/html/2303.11366 、https://arxiv.org/html/2605.11225v1 。conf=0.93。
- **直接证据缺口。** 在本次检索中未找到针对 AutoGen/CrewAI/LangGraph 对全部阶段逐个仅清空 system prompt、保留调用与上下文，再比较最终真实性的系统实验；也未找到 pfb 七段的直接证据。阶段、提示、工具、轮次消融是不同干预，不能混称。来源（对照案例）：https://arxiv.org/html/2303.11366 、https://arxiv.org/html/2605.11225v1 。conf=0.85（仅限本次检索）。

## Q2: Critic/Reviewer prompt 有效性边界

- **有效的候选条件：可定位、可执行的反馈和能检验错误的信号。** Self-Refine 表 2 在代码优化上，定制反馈 27.5、通用反馈 26.0、无反馈 24.8；CRITIC 使用搜索/代码执行等外部工具，并报告无工具自评在其 QA 对照中效果很小或低于初始输出。两项独立研究支持反馈信息质量重要，但不能推断任意外部工具或任意 reviewer 必然有效。来源：https://arxiv.org/pdf/2303.17651 、https://arxiv.org/pdf/2305.11738 。conf=0.90。
- **表演性风险：看似认真审查却未净修正事实，甚至破坏正确答案。** Huang 等在无外部反馈的推理任务中发现自我修正常不改善甚至降级；Reflexion 无测试的反思条件 0.52 低于基础 0.60，提供独立的相近风险证据。两者不证明所有无工具反馈均无效：Self-Refine 在部分生成任务获益。来源：https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf 、https://arxiv.org/html/2303.11366 、https://arxiv.org/pdf/2303.17651 。conf=0.93。
- **任务/错误类型比“简单或复杂”标签更具体。** Self-Refine 的 GPT-4 数学推理 92.9→93.1（+0.2 pp），代码优化 27.3→36.0（+8.7 pp）；Huang 等亦在推理上报告无外部反馈的限制。不能据此断言复杂任务必然受益、简单任务必然无效；错误可检测性、基线和反馈信号均可能影响结果。来源：https://arxiv.org/pdf/2303.17651 、https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf 。conf=0.91。
- **评审偏差可伪造收益。** Zheng 等记录位置、冗长和自增强偏差；Wataoka 等在所测模型中发现 GPT-4 自偏好，并提出文本熟悉度/困惑度解释（相关性，不是已确证因果）。因此对换比较顺序、记录长度，并用独立事实核验/盲人工抽检校准；不同模型评审也不自动无偏。来源：https://arxiv.org/pdf/2306.05685 、https://arxiv.org/pdf/2410.21819 。conf=0.91。

## Q3: Staged revision vs one-shot

- **存在收益但基线不同会混淆。** Self-Refine 比单次生成在若干任务上提高，但 GSM8K GPT-4 仅 +0.2 pp；Huang 等发现改进初始提示、排除 oracle 反馈后，纯内部修正在其推理设置可退化。交叉看：不能把“多轮”当作无条件优势，更不能把 preference 提升等同真实性提升。来源：https://arxiv.org/pdf/2303.17651 、https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf 。conf=0.94。
- **具体边际曲线例子，不是通用规律。** Self-Refine 附录 N 代码优化表：Direct 9.7%，带反馈第 1 轮 15.3%（+5.6 pp），第 2 轮 15.6%（相对第 1 轮 +0.3 pp），指标为优化成功比例，非 M8；表中无反馈第 1/2 轮为 10.1/10.4%。这是单一设置的边际递减示例，未验证其差异显著性；不能推广为所有任务第 2 轮只增 0.3 pp。来源：https://arxiv.org/pdf/2303.17651 。conf=0.93。
- **Reflexion 不等于简单单轮 revision。** 它使用反馈、记忆和跨尝试反思；Rust 表 3 中完整 0.68 对去反思 0.60 的差为 +8 pp，条件是保留测试生成。其 HumanEval Python 91.0 对 GPT-4 基线 80.1 的跨系统对比不应当归因于单一反思 prompt 或一次 revision。来源：https://arxiv.org/html/2303.11366 。conf=0.94。

## Q4: L1→pipeline 映射合理性论证

- **结论：可迁移为待测方向，不可直接迁移为效应大小、排序或贡献百分比。** L1 在完整组件集合背景下测到的删除效应，换成 pfb 后任务分布、上游输入、下游容错、信息和资源预算都可能改变；PIVOT 阶段不均及 Reflexion 测试×反思交互支持此警告。来源：https://arxiv.org/html/2605.11225v1 、https://arxiv.org/html/2303.11366 。conf=0.92。
- **形式化：** 对目标任务分布 D、完整配置 1，定义阶段 i 的完整背景删除效应 Δᵢ(D)=E_D[M8(1)−M8(1−i)]；这是局部、依赖其他阶段都开启的对比，不是唯一的归因份额。若两阶段有交互，ΣΔᵢ 可以不等于整体效应，不能把虚构的 planning 60%、execution 10% 当已证事实。来源（交互示例）：https://arxiv.org/html/2303.11366 。conf=0.94。
- **对简单 decomp 与复杂 pfb：** 如果 critic 在前者近零，不能推出后者近零；更丰富的证据、不同错误结构或阶段依赖可能改变方向，反之亦然。Self-Refine 的跨任务差异和 CRITIC 工具条件支持异质性，但没有直接估计 decomp→pfb 的预测准确度。来源：https://arxiv.org/pdf/2303.17651 、https://arxiv.org/pdf/2305.11738 。conf=0.90。
- **局限：** 文献的编程 pass@1、QA F1、任务偏好和旅行约束通过率均非 M8 核验真实性率；模型版本、工具、提示和样本不同。这里未测 L1 与 pfb，不能声称观察到了本仓库效应。来源：https://arxiv.org/html/2303.11366 、https://arxiv.org/pdf/2305.11738 、https://arxiv.org/html/2605.11225v1 。conf=0.97。

## 对 T8 Part C 实验设计的启示

- **预注册假设而非定论：** H1 七段删除效应不等；H2 critic 的效果随可靠外部证据可用性改变；H3 第二次 revision 的边际收益可能小于第一次，但也可能为负。反驳“所有 prompt 均等/自评必增益/边际必递减”的普遍断言；均需本地数据验证。来源：https://arxiv.org/html/2605.11225v1 、https://arxiv.org/html/2303.11366 、https://arxiv.org/pdf/2303.17651 、https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf 。conf=0.91。
- **C3 paired runs：** 对同一任务、相同输入与模型版本配对完整与 7 个单段消融，随机化运行顺序，多随机种子/重复；预先固定数据快照、解码和工具设置，保留完整轨迹、失败与缺失结果。分别定义两种干预：①只替换目标 prompt 为中性占位、保留调用/上下文接口；②跳过阶段并明确旁路输入。两者估计不同效应；工具和后续阶段尽可能保持一致，并记录实际差异。来源：https://arxiv.org/html/2303.11366 、https://arxiv.org/html/2605.11225v1 。conf=0.88。
- **指标和不确定性：** 预先冻结 M8 的核验单位、分母与无可核验声明/失败处理；对同一任务计算配对差，并按任务聚类 bootstrap 的 95% 区间，报告每臂绝对值、配对差、样本量及缺失率。七项比较预定主要对比或做 Holm 校正；若区间跨零，不应直接认定无效，需结合预注册最小有意义效应与样本量/功效。来源（测量偏差背景）：https://arxiv.org/pdf/2306.05685 、https://arxiv.org/pdf/2410.21819 。conf=0.88。
- **分层与控制：** 预先按任务难度、错误类型和证据可用性分层；小样本交互作为探索性分析。critic 做 2×2（critic 有/无 × 外部证据有/无），固定其他阶段；revision 测 0/1/2 轮，并加同等调用/令牌预算的重采样或强化 one-shot 对照，记录 tokens、耗时、正确→错误和错误→正确转移。外部核验与生成过程隔离，盲化条件；若用 LLM 比较则双向交换顺序、记录长度及人工校准。来源：https://arxiv.org/html/2303.11366 、https://arxiv.org/pdf/2303.17651 、https://arxiv.org/pdf/2306.05685 。conf=0.91。

## 来源清单

| # | 标题 | 类型 | URL | 关键发现一句话 |
|---|---|---|---|---|
| 1 | Shinn et al., Reflexion (2023) | NeurIPS 论文 | https://arxiv.org/html/2303.11366 | 测试与反思在 Rust 消融中互补。 |
| 2 | Madaan et al., Self-Refine (2023) | NeurIPS 论文 | https://arxiv.org/pdf/2303.17651 | 反馈与迭代结果依任务而异。 |
| 3 | Huang et al., Large Language Models Cannot Self-Correct Reasoning Yet (2024) | ICLR 论文 | https://proceedings.iclr.cc/paper_files/paper/2024/file/8b4add8b0aa8749d80a34ca5d941c355-Paper-Conference.pdf | 无外部信号的推理自纠可能退化。 |
| 4 | Gou et al., CRITIC (2024) | ICLR 论文 | https://arxiv.org/pdf/2305.11738 | 工具交互能为纠错提供反馈。 |
| 5 | Zheng et al., Judging LLM-as-a-Judge (2023) | NeurIPS 论文 | https://arxiv.org/pdf/2306.05685 | LLM 评审存在位置、长度等偏差。 |
| 6 | Wataoka et al., Self-Preference Bias in LLM-as-a-Judge (2024) | NeurIPS workshop 论文 | https://arxiv.org/pdf/2410.21819 | 部分模型表现自偏好，与熟悉度相关。 |
| 7 | PIVOT: Bridging Planning and Execution in LLM Agents via Trajectory Refinement (2026) | arXiv 预印本 | https://arxiv.org/html/2605.11225v1 | 旅行任务中的阶段消融影响不均。 |
