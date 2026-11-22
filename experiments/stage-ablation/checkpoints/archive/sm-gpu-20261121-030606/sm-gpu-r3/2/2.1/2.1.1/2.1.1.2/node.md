# N216: 若将上下文长度从32K降至16K，KV Cache占用减半至1.99GB，INT8权重27GB + KV 1.99GB + 激活/开销2.5GB = 31.49

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N99

## Claim

若将上下文长度从32K降至16K，KV Cache占用减半至1.99GB，INT8权重27GB + KV 1.99GB + 激活/开销2.5GB = 31.49GB，仍超过RTX 4090 24GB显存，因此即使降低上下文至16K，INT8精度在单卡RTX 4090上仍不可行，必须使用W4/NVFP4精度（权重13.5GB）或更高显存硬件。

## Corrected Claim

若将上下文长度从32K降至16K，KV Cache占用减半至1.99GB，INT8权重27GB + KV 1.99GB + 激活/开销2.5GB = 31.49GB，仍超过RTX 4090 24GB显存，因此即使降低上下文至16K，INT8精度在单卡RTX 4090上仍不可行，必须使用W4/NVFP4精度（权重13.5GB）或更高显存硬件。

## Evidence

先验知识/题面给定，逻辑校验通过：KV Cache随上下文线性减半符合原理，INT8权重27GB+KV 1.99GB+开销2.5GB=31.49GB>24GB显存，数学推导自洽且符合硬件限制常识。
