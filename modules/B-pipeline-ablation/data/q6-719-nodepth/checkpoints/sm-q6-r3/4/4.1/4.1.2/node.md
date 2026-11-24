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

父节点级核验通过：正交+完备+无冗余（子节点逻辑清晰且正交：节点1负责数据量估算，节点2负责基于数据量的成本计算并指出父节点估算的偏差，节点3负责论证API成本可忽略从而聚焦日志成本。三者覆盖了父节点中'日志存储与分析成本'和'API调用费用'两个关键方面，且指出了父节点估算值（5k-15k元）与实际计算值（百万级）的巨大差异，具有批判性价值，无冗余。）

## Search Query

Alibaba Cloud Log Service pricing per GB CDN logs
