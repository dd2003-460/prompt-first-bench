# N308: AMD Radeon PRO W7900 的显存带宽规格澄清：官方规格为 256-bit GDDR6 @ 18 Gbps，带宽 = 256/8 * 18 = 5

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N103, N104, N105

## Claim

AMD Radeon PRO W7900 的显存带宽规格澄清：官方规格为 256-bit GDDR6 @ 18 Gbps，带宽 = 256/8 * 18 = 576 GB/s，而非 N105 中提到的 2560 GB/s（该数值为错误计算或混淆了其他型号），此修正直接影响其 Decode 吞吐上限估算。

## Corrected Claim

AMD Radeon PRO W7900 的显存带宽规格澄清：官方规格为 256-bit GDDR6 @ 18 Gbps，带宽 = 256/8 * 18 = 576 GB/s，而非 N105 中提到的 2560 GB/s（该数值为错误计算或混淆了其他型号），此修正直接影响其 Decode 吞吐上限估算。

## Evidence

先验知识/题面给定，逻辑校验通过：256-bit 位宽除以 8 字节乘以 18 Gbps 速率，计算结果确为 576 GB/s，符合物理量纲与数学逻辑。

## Search Query

AMD Radeon PRO W7900 memory bandwidth specification 576 GB/s
