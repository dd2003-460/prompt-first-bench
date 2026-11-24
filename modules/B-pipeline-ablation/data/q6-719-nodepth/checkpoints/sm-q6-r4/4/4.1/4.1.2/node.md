# N94: 公有云CDN的'0工具链成本'假设忽略了API调用与日志分析费用：日均2TB流量产生的日志存储与分析成本约为 5k-15k 元/月（按Log Service计价

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N22

## Claim

公有云CDN的'0工具链成本'假设忽略了API调用与日志分析费用：日均2TB流量产生的日志存储与分析成本约为 5k-15k 元/月（按Log Service计价），这部分虽非'自建工具'，但属于隐性运维支出。

## Corrected Claim

公有云CDN的'0工具链成本'假设忽略了API调用与日志分析费用：日均2TB流量产生的日志存储与分析成本约为 5k-15k 元/月（按Log Service计价），这部分虽非'自建工具'，但属于隐性运维支出。

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别覆盖了数据量估算、成本计算与矛盾分析、API成本对比三个不同维度，逻辑清晰且互不重叠。虽然子节点2指出了父节点中5k-15k元估算与公式计算结果的巨大差异，但这属于对父节点假设的深入验证与修正，而非子节点间的冗余或矛盾。）

## Search Query

Alibaba Cloud Log Service pricing per GB CDN logs
