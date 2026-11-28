# N106: 定义 MTP×4 投机解码的加速比公式：Speedup = T_standard / T_speculative，其中 T_standard 为无投机解码的单步

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N29

## Claim

定义 MTP×4 投机解码的加速比公式：Speedup = T_standard / T_speculative，其中 T_standard 为无投机解码的单步生成时间，T_speculative 为含草稿生成、验证及回滚的总时间

## Corrected Claim

定义 MTP×4 投机解码的加速比公式：Speedup = T_standard / T_speculative，其中 T_standard 为无投机解码的单步生成时间，T_speculative 为含草稿生成、验证及回滚的总时间

## Evidence

父节点级核验未通过：不完备（子节点之间存在概念重叠和逻辑包含关系。前两个子节点（高/低接受率工作点）是第三个子节点（临界点模型）的具体实例或结果，而非独立的正交维度。此外，父节点定义的是通用公式 Speedup = T_standard / T_speculative，但子节点未涵盖公式中 T_standard 和 T_speculative 的具体构成分解（如 T_standard 的基准定义，T_speculative 中草稿生成、验证、回滚各部分的数学表达），仅给出了特定场景下的数值结果，导致对‘公式本身’的覆盖不完整。）

## Search Query

speculative decoding speedup formula definition
