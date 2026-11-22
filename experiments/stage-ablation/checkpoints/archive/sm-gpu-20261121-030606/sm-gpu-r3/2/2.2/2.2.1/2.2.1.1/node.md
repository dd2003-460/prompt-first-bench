# N223: RTX 5090 在 INT8 精度下的可行性修正：权重占用 27GB (27B*1B) + KV Cache 5.2GB + 激活 1.3GB + Overh

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N102

## Claim

RTX 5090 在 INT8 精度下的可行性修正：权重占用 27GB (27B*1B) + KV Cache 5.2GB + 激活 1.3GB + Overhead 3GB = 36.5GB > 32GB，仍不可行；若采用 W4 精度 (13.5GB)，总占用 = 13.5 + 5.2 + 1.3 + 3 = 23GB < 32GB，可行且余量 28%。

## Corrected Claim

RTX 5090 在 INT8 精度下的可行性修正：权重占用 27GB (27B*1B) + KV Cache 5.2GB + 激活 1.3GB + Overhead 3GB = 36.5GB > 32GB，仍不可行；若采用 W4 精度 (13.5GB)，总占用 = 13.5 + 5.2 + 1.3 + 3 = 23GB < 32GB，可行且余量 28%。

## Evidence

先验知识/题面给定，逻辑校验通过：算术运算正确（27+5.2+1.3+3=36.5>32；13.5+5.2+1.3+3=23<32），余量计算合理（(32-23)/32≈28%），符合显存占用估算逻辑。
