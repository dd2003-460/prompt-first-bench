# N84: Qwen3-27B TP=2时，每层AllReduce通信量 = 2 * Hidden_Size * Batch_Size * Bytes_per_elemen

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N24

## Claim

Qwen3-27B TP=2时，每层AllReduce通信量 = 2 * Hidden_Size * Batch_Size * Bytes_per_element。假设Hidden=4096, Batch=1, BF16: 2 * 4096 * 1 * 2 = 16 KB/层。48层总通信量 = 48 * 16 KB = 768 KB/step

## Corrected Claim

Qwen3-27B TP=2时，每层AllReduce通信量 = 2 * Hidden_Size * Batch_Size * Bytes_per_element。假设Hidden=4096, Batch=1, BF16: 2 * 4096 * 1 * 2 = 16 KB/层。48层总通信量 = 48 * 16 KB = 768 KB/step

## Evidence

先验知识/题面给定，逻辑校验通过：TP=2时AllReduce通信量公式为2*H*B*Bytes，数值计算48*2*4096*1*2=786432 Bytes=768 KB，量纲与数值均正确。
