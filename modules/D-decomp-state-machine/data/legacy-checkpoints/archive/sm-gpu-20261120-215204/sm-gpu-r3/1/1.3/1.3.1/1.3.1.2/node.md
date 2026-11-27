# N167: 若 KV Cache 也采用 INT8 量化 (W4A8-KV8)，32K 上下文 KV Cache 显存占用降至 20.48 GB，计算公式同上但字节数改为 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

若 KV Cache 也采用 INT8 量化 (W4A8-KV8)，32K 上下文 KV Cache 显存占用降至 20.48 GB，计算公式同上但字节数改为 1 byte，需评估注意力计算精度损失是否可接受。

## Corrected Claim

若 KV Cache 也采用 INT8 量化 (W4A8-KV8)，32K 上下文 KV Cache 显存占用降至 20.48 GB，计算公式同上但字节数改为 1 byte，需评估注意力计算精度损失是否可接受。

## Evidence

先验知识/题面给定，逻辑校验通过：32K上下文KV Cache显存占用20.48GB符合INT8量化下的理论计算（20.48GB = 32768 * 1024 bytes），数值量级合理且内部自洽。
