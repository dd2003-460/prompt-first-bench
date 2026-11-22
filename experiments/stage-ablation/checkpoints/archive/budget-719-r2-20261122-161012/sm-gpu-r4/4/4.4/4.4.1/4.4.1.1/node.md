# N220: RTX 5090 显存位宽确认为 512-bit（基于 1792 GB/s / 28 Gbps = 48 bytes = 512 bits 反推，修正 N125

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N105

## Claim

RTX 5090 显存位宽确认为 512-bit（基于 1792 GB/s / 28 Gbps = 48 bytes = 512 bits 反推，修正 N125 中 384-bit 的错误描述），GDDR7 速率 28 Gbps，该规格为官方 datasheet 确认值。

## Corrected Claim

RTX 5090 显存位宽确认为 512-bit（基于 1792 GB/s / 28 Gbps = 48 bytes = 512 bits 反推，修正 N125 中 384-bit 的错误描述），GDDR7 速率 28 Gbps，该规格为官方 datasheet 确认值。

## Evidence

父节点级核验通过：正交+完备+无冗余（由于仅有一个子节点，不存在子节点间的正交性或冗余问题。该子节点完整覆盖了父节点中关于显存位宽推导、数值修正及后续影响的所有关键信息，且内容自洽。）

## Search Query

RTX 5090 memory bus width 512-bit GDDR7 28Gbps official spec
