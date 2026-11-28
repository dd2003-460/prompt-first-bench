# N70: 工作点B（混合架构）的成本构成公式为 Cost_B = Cost_Local_80% + Cost_Cloud_20%，其中 Cost_Local_80% 为本

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19, N20, N21

## Claim

工作点B（混合架构）的成本构成公式为 Cost_B = Cost_Local_80% + Cost_Cloud_20%，其中 Cost_Local_80% 为本地处理 80% 任务的能耗成本（基于 N31 公式乘以 0.8），Cost_Cloud_20% 为云端 API 处理 20% 复杂推理任务的费用，需根据所选云端模型（如 GPT-4o）的 token 单价和输入输出长度估算

## Corrected Claim

工作点B（混合架构）的成本构成公式为 Cost_B = Cost_Local_80% + Cost_Cloud_20%，其中 Cost_Local_80% 为本地处理 80% 任务的能耗成本（基于 N31 公式乘以 0.8），Cost_Cloud_20% 为云端 API 处理 20% 复杂推理任务的费用，需根据所选云端模型（如 GPT-4o）的 token 单价和输入输出长度估算

## Evidence

父节点级核验通过：正交+完备+无冗余（三个子节点分别对应显式成本中的本地部分、云端部分以及父节点未明确列出但属于完整成本构成的隐性部分。三者定义域互斥（Local vs Cloud vs Hidden），逻辑上无重叠或矛盾。虽然第三个子节点涉及的内容在父节点公式中未直接出现，但在学术分解中补充‘隐性成本’以完善‘成本构成’是合理且必要的，因此视为覆盖完备。各节点均为独立的成本维度，不构成同一参数的不同取值，无冗余。）
