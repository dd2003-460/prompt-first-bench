# N96: 全自建策略月度带宽成本 C_bw_self_total = 10 * C_bw_per_pop，其中 C_bw_per_pop 为单POP带宽租赁成本（假设 ¥

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N24

## Claim

全自建策略月度带宽成本 C_bw_self_total = 10 * C_bw_per_pop，其中 C_bw_per_pop 为单POP带宽租赁成本（假设 ¥15,000/月，覆盖160GB/天出网），计算得 10 * 15,000 = ¥150,000/月。

## Corrected Claim

全自建策略月度带宽成本 C_bw_self_total = 10 * C_bw_per_pop，其中 C_bw_per_pop 为单POP带宽租赁成本（假设 ¥15,000/月，覆盖160GB/天出网），计算得 10 * 15,000 = ¥150,000/月。

## Evidence

父节点级核验未通过：非正交, 有冗余（子节点3（实际租赁成本）与子节点1、2存在逻辑冲突和冗余。父节点定义的成本模型是基于固定假设（¥15,000/POP），而子节点3通过计算得出的实际成本（¥2300-4600）与父节点假设严重不符，导致分解结果自相矛盾。此外，子节点1和2是计算子节点3的中间步骤，若父节点旨在解释‘全自建策略成本’，则子节点应统一采用同一套成本逻辑，而非并列展示‘假设值’和‘推导值’。）
