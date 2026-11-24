# N72: 单 POP 点服务器台数 N_server 由日均请求量 Q_day (2,048,000) 除以单服务器最大 QPS 容量 C_qps (如 50,000 Q

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N13

## Claim

单 POP 点服务器台数 N_server 由日均请求量 Q_day (2,048,000) 除以单服务器最大 QPS 容量 C_qps (如 50,000 QPS) 得出，并需乘以冗余系数 R (通常 1.5-2.0) 以应对峰值负载，即 N_server = (Q_day / 86400 / C_qps) * R。

## Corrected Claim

单 POP 点服务器台数 N_server 由日均请求量 Q_day (2,048,000) 除以单服务器最大 QPS 容量 C_qps (如 50,000 QPS) 得出，并需乘以冗余系数 R (通常 1.5-2.0) 以应对峰值负载，即 N_server = (Q_day / 86400 / C_qps) * R。

## Evidence

父节点级核验未通过：不完备（子节点分别针对公式中的两个核心变量 C_qps 和 R 进行独立解释，二者互不重叠且无逻辑矛盾，正交性良好。然而，父节点公式中明确包含的日均请求量 Q_day (2,048,000) 这一关键输入参数在子节点中完全缺失，未对其来源、计算方式或合理性进行拆解，导致分解不完备。此外，子节点2指出 R 的典型值（5.0-7.1）与父节点假设（1.5-2.0）存在显著差异，虽然这属于对父节点假设的修正/细化，但在严格的结构分解中，父节点作为‘定义’，子节点应解释其组成部分，若子节点直接否定父节点的前提，通常意味着父节点本身有误或需要重构，但这主要影响一致性而非正交性或冗余性。主要问题在于 Q_day 的缺失。）

## Search Query

web server max QPS capacity nginx apache benchmark 50000
