# N224: 修正N10与N16矛盾：在INT8权重+FP16 KV Cache配置下，总显存需求为37.7GB（权重27GB+KV 10.7GB），不含框架开销；若包含vL

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N75

## Claim

修正N10与N16矛盾：在INT8权重+FP16 KV Cache配置下，总显存需求为37.7GB（权重27GB+KV 10.7GB），不含框架开销；若包含vLLM/CUDA框架开销（约4GB），总需求为41.7GB。此配置下单卡RTX 4090 (24GB)不可行，需双卡或A100 40GB。

## Corrected Claim

修正N10与N16矛盾：在INT8权重+FP16 KV Cache配置下，总显存需求为37.7GB（权重27GB+KV 10.7GB），不含框架开销；若包含vLLM/CUDA框架开销（约4GB），总需求为41.7GB。此配置下单卡RTX 4090 (24GB)不可行，需双卡或A100 40GB。

## Evidence

先验知识/题面给定，逻辑校验通过：INT8权重(27GB)与FP16 KV Cache(10.7GB)相加得37.7GB，加上约4GB框架开销得41.7GB，数值量级与算术逻辑自洽，且符合RTX 4090显存限制的工程常识。
