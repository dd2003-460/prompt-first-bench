# N12: 基础设施成本C_infra的摊销模型：C_infra = (N_nodes × C_node_capex / L_life) + (N_nodes × C_no

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N2

## Claim

基础设施成本C_infra的摊销模型：C_infra = (N_nodes × C_node_capex / L_life) + (N_nodes × C_node_opex_monthly / 12)，N_nodes为节点数，C_node_capex为单节点资本支出，L_life为折旧年限（通常5年）

## Corrected Claim

基础设施成本C_infra的摊销模型：C_infra = (N_nodes × C_node_capex / L_life) + (N_nodes × C_node_opex_monthly / 12)，N_nodes为节点数，C_node_capex为单节点资本支出，L_life为折旧年限（通常5年）

## Evidence

父节点级核验未通过：非正交, 不完备, 有冗余（1. 正交性不足：子节点2（混合架构）同时包含了自建（子节点1的变体）和公有云（子节点3的变体），与子节点1和3在架构维度上存在重叠，并非完全独立的互斥分类。2. 完备性缺失：父节点公式明确包含运营支出项 (N_nodes × C_node_opex_monthly / 12)，但所有子节点均只计算了资本支出（Capex）的摊销，完全忽略了Opex部分，导致模型应用不完整。3. 冗余性高：子节点1和2本质上是同一类“自建/混合自建”策略在不同节点数（N=10 vs N=5）下的参数化实例，可以合并为一个参数化工作点，而非两个独立的定性节点。）

## Search Query

CDN edge node capex depreciation 5 year straight line
