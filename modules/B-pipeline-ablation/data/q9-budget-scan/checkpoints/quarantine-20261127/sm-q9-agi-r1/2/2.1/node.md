# N12: Agent拓扑中的状态转移图定义：状态集合S={Hypothesis_Gen, Experiment_Design, Tool_Exec, Data_Analy

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

Agent拓扑中的状态转移图定义：状态集合S={Hypothesis_Gen, Experiment_Design, Tool_Exec, Data_Analysis, Conclusion_Draw, Knowledge_Update}，转移概率矩阵P(S_i -> S_j)由Prompt中的状态机规则定义；需量化每个状态的平均停留时间（token数）和失败重试率（Retry_Rate），以评估闭环完成一次完整科研循环的预期总Token消耗。

## Corrected Claim

Agent拓扑中的状态转移图定义：状态集合S={Hypothesis_Gen, Experiment_Design, Tool_Exec, Data_Analysis, Conclusion_Draw, Knowledge_Update}，转移概率矩阵P(S_i -> S_j)由Prompt中的状态机规则定义；需量化每个状态的平均停留时间（token数）和失败重试率（Retry_Rate），以评估闭环完成一次完整科研循环的预期总Token消耗。

## Evidence

先验知识/题面给定，逻辑校验通过
