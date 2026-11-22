# N29: 性价比核心指标定义：Cost_Per_Token = (Hardware_Cost + Electricity_Cost_Per_Hour * Deployme

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

性价比核心指标定义：Cost_Per_Token = (Hardware_Cost + Electricity_Cost_Per_Hour * Deployment_Hours) / Total_Tokens_Generated。在本地工作站长期部署场景下，若假设24/7运行，电力成本占比显著；若为按需推理，则硬件折旧成本占比更高。建议采用 'Effective_Tokens_Per_Dollar' = (Throughput_tokens_per_sec * 3600 * 8760 * Utilization_Factor) / Hardware_Cost 作为静态指标，其中Utilization_Factor需根据业务负载设定（保守取0.3-0.5）。

## Corrected Claim

性价比核心指标定义：Cost_Per_Token = (Hardware_Cost + Electricity_Cost_Per_Hour * Deployment_Hours) / Total_Tokens_Generated。在本地工作站长期部署场景下，若假设24/7运行，电力成本占比显著；若为按需推理，则硬件折旧成本占比更高。建议采用 'Effective_Tokens_Per_Dollar' = (Throughput_tokens_per_sec * 3600 * 8760 * Utilization_Factor) / Hardware_Cost 作为静态指标，其中Utilization_Factor需根据业务负载设定（保守取0.3-0.5）。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点2与子节点4存在严重逻辑重叠和矛盾。子节点2定义了基于时间的直线折旧（年折旧$426.67），而子节点4定义了基于产出的摊销公式（Amortized_Hardware_Cost），两者对Hardware_Cost的归一化方式不同（时间 vs 产出），且子节点4的计算示例直接使用了子节点2的折旧数值，导致概念混淆。此外，子节点1和2均涉及硬件成本的具体数值计算，存在部分冗余。）
