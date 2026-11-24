# N178: 人均日请求数 R_per_user 的低频保守估计：R_low = 20 次/人/天，对应总请求数 R_total_low = 5,000,000 × 20 =

- **status**: pending
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N51

## Claim

人均日请求数 R_per_user 的低频保守估计：R_low = 20 次/人/天，对应总请求数 R_total_low = 5,000,000 × 20 = 100,000,000 次/天，适用于轻度用户为主的场景

## Corrected Claim

人均日请求数 R_per_user 的低频保守估计：R_low = 20 次/人/天，对应总请求数 R_total_low = 5,000,000 × 20 = 100,000,000 次/天，适用于轻度用户为主的场景

## Evidence

父节点级核验未通过：不完备（子节点1关注内部构成分解（行为基准），子节点2关注外部约束验证（流量计算），两者角度不同且无逻辑矛盾，正交性良好。但完备性不足：父节点定义了R_low及其对应的总请求数，子节点仅验证了总请求数在特定Hit Rate下的流量约束，未覆盖R_low取值本身的合理性来源（如行业报告数据支撑）或R_total_low计算中用户基数（5,000,000）的假设验证，导致对父节点‘保守估计’这一核心属性的支撑不完整。）

## Search Query

average daily API requests per user social media platform
