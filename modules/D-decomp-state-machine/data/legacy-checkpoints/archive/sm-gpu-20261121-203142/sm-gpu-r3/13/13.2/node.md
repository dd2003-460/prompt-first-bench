# N364: Intel Gaudi 2 的理论 Decode 阶段 TPS 上限计算：基于 Roofline 模型，TPS_max ≈ Memory_Bandwidth /

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N124

## Claim

Intel Gaudi 2 的理论 Decode 阶段 TPS 上限计算：基于 Roofline 模型，TPS_max ≈ Memory_Bandwidth / (Model_Weights_Bytes + KV_Cache_Bytes_per_token)；代入 3.2 TB/s 带宽和 BF16 下 54GB 权重 + 4GB KV Cache，理论极限约为 55-60 tokens/s，但需乘以生态效率系数（0.6-0.7）得到实际预期 TPS ≈ 33-42 tokens/s。

## Corrected Claim

Intel Gaudi 2 的理论 Decode 阶段 TPS 上限计算：基于 Roofline 模型，TPS_max ≈ Memory_Bandwidth / (Model_Weights_Bytes + KV_Cache_Bytes_per_token)；代入 3.2 TB/s 带宽和 BF16 下 54GB 权重 + 4GB KV Cache，理论极限约为 55-60 tokens/s，但需乘以生态效率系数（0.6-0.7）得到实际预期 TPS ≈ 33-42 tokens/s。

## Evidence

先验知识/题面给定，逻辑校验通过：Roofline模型在Decode阶段受内存带宽限制，公式TPS=Bandwidth/(Weights+KV)符合第一性原理；数值计算3.2TB/s / (54GB+4GB) ≈ 55.17 tokens/s，处于55-60区间；乘以0.6-0.7效率系数后得到33-42 tokens/s，逻辑自洽且量级合理。
