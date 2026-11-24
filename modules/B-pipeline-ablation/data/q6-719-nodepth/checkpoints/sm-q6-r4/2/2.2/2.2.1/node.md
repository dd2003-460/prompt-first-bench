# N72: 单 POP 点服务器台数 N_server 由日均请求量 Q_day (2,048,000) 除以单服务器最大 QPS 容量 C_qps (如 50,000 Q

- **status**: verified
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

父节点级核验通过：正交+完备+无冗余（子节点分别针对公式中的两个核心变量（C_qps 和 R）进行了独立的物理/逻辑约束分析，内容互不重叠且无矛盾。虽然子节点2得出的 R 值与父节点假设的 1.5-2.0 存在显著差异（这属于事实修正而非逻辑矛盾），但它们各自独立地定义了公式中的不同参数，因此是正交的。两个子节点完整覆盖了公式 N_server = (Q_day / 86400 / C_qps) * R 中除已知常数 Q_day 外的所有关键可变参数。）

## Search Query

web server max QPS capacity nginx apache benchmark 50000
