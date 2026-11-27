# N225: 在INT8权重+INT8 KV Cache配置下，总显存需求为32.35GB（权重27GB+KV 5.35GB），不含框架开销；若包含框架开销（约4GB），总需

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

在INT8权重+INT8 KV Cache配置下，总显存需求为32.35GB（权重27GB+KV 5.35GB），不含框架开销；若包含框架开销（约4GB），总需求为36.35GB。此配置下单卡RTX 4090 (24GB)仍不可行，但显存压力显著降低，可能允许更长的上下文或更大的Batch size。

## Corrected Claim

在INT8权重+INT8 KV Cache配置下，总显存需求为32.35GB（权重27GB+KV 5.35GB），不含框架开销；若包含框架开销（约4GB），总需求为36.35GB。此配置下单卡RTX 4090 (24GB)仍不可行，但显存压力显著降低，可能允许更长的上下文或更大的Batch size。

## Evidence

先验知识/题面给定，逻辑校验通过：27GB+5.35GB=32.35GB，32.35GB+4GB=36.35GB，数值计算自洽；24GB显存确实无法容纳32.35GB以上负载，结论合理。
