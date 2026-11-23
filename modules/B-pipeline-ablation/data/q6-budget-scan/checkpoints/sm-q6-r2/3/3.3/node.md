# N28: 回源率模型：R_origin = 1 - H_cache，其中H_cache为缓存命中率，回源率直接影响回源带宽成本和源站负载，典型值为5-20%

- **status**: verified
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N3

## Claim

回源率模型：R_origin = 1 - H_cache，其中H_cache为缓存命中率，回源率直接影响回源带宽成本和源站负载，典型值为5-20%

## Corrected Claim

回源率模型：R_origin = 1 - H_cache，其中H_cache为缓存命中率，回源率直接影响回源带宽成本和源站负载，典型值为5-20%

## Evidence

父节点级核验通过：正交+完备+无冗余（子节点分别从‘带宽成本’、‘源站计算成本’和‘核心变量（命中率）的推导’三个维度展开，逻辑清晰且互不重叠。父节点强调R_origin影响‘带宽成本’和‘源站负载’，子节点1和2分别对应这两点，子节点3补充了如何计算决定R_origin的H_cache，覆盖了公式中所有关键变量及其经济影响，无冗余。）
