# N133: 显存带宽瓶颈修正：实际吞吐量公式需除以权重精度字节数，即 Throughput = Bandwidth / (Weight_Size_GB * Precisio

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N22

## Claim

显存带宽瓶颈修正：实际吞吐量公式需除以权重精度字节数，即 Throughput = Bandwidth / (Weight_Size_GB * Precision_Bytes + Activation_GB + KV_Cache_GB)，因为带宽是字节/秒，而权重大小通常以参数量计，必须统一单位

## Corrected Claim

显存带宽瓶颈修正：实际吞吐量公式需除以权重精度字节数，即 Throughput = Bandwidth / (Weight_Size_GB * Precision_Bytes + Activation_GB + KV_Cache_GB)，因为带宽是字节/秒，而权重大小通常以参数量计，必须统一单位

## Evidence

先验知识/题面给定，逻辑校验通过
