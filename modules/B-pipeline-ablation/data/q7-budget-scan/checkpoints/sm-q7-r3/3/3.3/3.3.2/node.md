# N66: 工作点B（HDD+SSD分层，最优性价比）：SSD层缓存命中率 η=90% 时，有效扫描吞吐 T_eff = η×T_ssd + (1-η)×T_hdd；若 η

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N19

## Claim

工作点B（HDD+SSD分层，最优性价比）：SSD层缓存命中率 η=90% 时，有效扫描吞吐 T_eff = η×T_ssd + (1-η)×T_hdd；若 η=90%，T_scan ≈ 10TB/3GB/s + 90TB/250MB/s ≈ 6.4h，超过SLA(2h)，隐性成本 C_wait = (6.4-2)h × ¥5000/h × 2/day

## Corrected Claim

工作点B（HDD+SSD分层，最优性价比）：SSD层缓存命中率 η=90% 时，有效扫描吞吐 T_eff = η×T_ssd + (1-η)×T_hdd；若 η=90%，T_scan ≈ 10TB/3GB/s + 90TB/250MB/s ≈ 6.4h，超过SLA(2h)，隐性成本 C_wait = (6.4-2)h × ¥5000/h × 2/day

## Evidence

父节点级核验未通过：非正交（子节点1和子节点2在容量计算上存在逻辑矛盾与重叠。子节点1声称SSD需容纳全部100TB温数据（V_ssd=111TB），而子节点2声称HDD需容纳剩余400TB冷数据及SSD溢出（隐含SSD仅缓存部分或数据分布不同）。若SSD已容纳全部100TB温数据，则不存在‘SSD溢出部分’给HDD，且总容量分配逻辑（100+400=500）与‘分层缓存’概念冲突（通常分层意味着SSD只存热点，而非全量温数据）。此外，父节点强调‘缓存命中率’，暗示数据不在SSD中全量驻留，但子节点1的计算假设全量驻留，导致内部逻辑不一致。）
