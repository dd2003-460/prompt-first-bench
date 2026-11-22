# N85: 信号传递博弈的均衡条件：在 Spence 模型框架下，高挂价 P_high 作为质量信号 Q_high 的可信性取决于分离均衡条件：P_high - C(Q_h

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

信号传递博弈的均衡条件：在 Spence 模型框架下，高挂价 P_high 作为质量信号 Q_high 的可信性取决于分离均衡条件：P_high - C(Q_high) >= P_low - C(Q_low) + Cost_of_Misrepresentation。量化 Cost_of_Misrepresentation (被买家识破低质高价的损失) 需大于 10% 的商品价值，才能维持 15-25% 的溢价均衡。

## Corrected Claim

在 Spence 模型框架下，高挂价作为质量信号的可信性取决于分离均衡条件：高质卖家维持高价的收益需大于其模仿低质卖家策略的收益加上被识破的成本。具体的溢价比例和成本阈值取决于市场结构和成本函数，并非固定的 10% 或 15-25%。

## Evidence

父节点级核验未通过：不完备（子节点在逻辑维度上保持了较好的正交性（分别对应不等式右侧成本项、左侧收益项差值、以及买家信念更新机制），且无冗余。但在完备性上存在明显缺失：父节点明确提出了‘维持 15-25% 溢价均衡’的具体量化目标，但子节点仅分别分析了不等式两边和买家阈值，缺乏将这三者整合以验证‘15-25%溢价’这一具体数值范围是否满足分离均衡条件的最终综合验证节点。此外，Spence模型通常要求低质卖家模仿高质卖价的成本高于其收益（即 Spence 条件：C_high - C_low < P_high - P_low < C_high - C_low + ... 等变体），子节点2仅关注高质卖家自身收益，未明确涵盖低质卖家不模仿的激励相容约束（Incentive Compatibility for Low Type），这是分离均衡成立的核心条件之一。）

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2084289064304485189&rut=3fe2a84b3d73f03247ec23647769fd32489c4b523b83a89119418ccac7dcf51f', 'type': 'ddg', 'title': '高级微观经济学——Spence教育信号模型（博弈论） - 知乎'}
