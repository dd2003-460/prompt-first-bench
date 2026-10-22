# 02.5 交叉验证与矛盾

## 关键 claim 对照

| Claim | 独立来源/观察 | 交叉核验与边界 |
|---|---|---|
| 分解/规划可能有收益 | arXiv:2405.16510 报约40% vs 2.92%；arXiv:2503.09572 报长程任务高成绩；ACONIC arXiv:2510.07772 报 SATBench +8.8pp Claude、+15.0pp LLaMA | 三项互相独立论文给出正向线索，但系统/任务/模型/基线各异，均不能识别裸 prompt vs 同模型同环境的纯分解效应。摘要数字未全文复核，置信度中低。来源：https://arxiv.org/abs/2405.16510 ; https://arxiv.org/abs/2503.09572 ; https://arxiv.org/abs/2510.07772 |
| 分解/agentic planning 不保证提升 | arXiv:2603.06064 搜索摘要报告 agentic 20% vs direct 50%；与上列结果表面相反 | 这是任务/条件依赖的反例，具体样本与 treatment 尚未逐文核验；不能断言总体反效果。与正向论文并不构成同一实验矛盾，反而限制普遍化。https://arxiv.org/abs/2603.06064 |
| 开源框架含计划/拆解机制 | LangChain 官方 Plan-and-Execute；AutoGen 官方 task decomposition 文档 | 两者验证可实现架构类别，不支持成功率因果结论。AutoGen 当前 repo 存档状态，机制说明仍可作为历史事实。https://www.langchain.com/blog/planning-agents ; https://github.com/microsoft/autogen |

## 交叉核验边界
- 任务书要求“arena 多模型对战各答一遍”。本运行环境没有调度其他模型/代理的调用工具；未声称完成多模型投票或独立 LLM 复核。用多个公开论文作来源交叉，不等价于多模型评审。
- `ralph` 与 `ego-browser` 未安装；网页 LLM 回执缺失。搜索工具只作线索，重要数字应在正式实验/复核中打开论文全文核表。
- 关键来源来自不同研究团队/不同基准，属于来源独立，但具体论文质量、审稿状态及测量可比性不等。没有把数量当作效果合并。
- Q2/Q3 的组件因果边际均无直接证据，保留为空缺。

阶段判定：PASS（不确定性已保留，行动阶段可据此设计实验）；按通用规则自检，非外部 Reviewer 回执。