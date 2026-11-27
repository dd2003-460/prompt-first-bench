# N357: H100 PCIe 显存带宽 2039 GB/s 的构成验证：HBM3 5120-bit 位宽 × 3.0 Gbps 等效频率 / 8 = 1920 GB/s 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N128

## Claim

H100 PCIe 显存带宽 2039 GB/s 的构成验证：HBM3 5120-bit 位宽 × 3.0 Gbps 等效频率 / 8 = 1920 GB/s 理论峰值，标称 2039 GB/s 可能包含 ECC 校验开销或厂商测试条件差异，该数值为硬件固定参数，HBM3 架构下带宽密度显著高于 GDDR6。

## Corrected Claim

H100 PCIe 显存带宽标称为 2039 GB/s，这是基于 HBM3 5120-bit 位宽和约 3.2 Gbps 等效频率（或厂商特定测试条件）得出的硬件固定参数，HBM3 架构下带宽密度显著高于 GDDR6。

## Evidence

[质询]数值计算存在明显错误：5120-bit 位宽 × 3.0 Gbps / 8 应等于 1920 GB/s，而非陈述中声称的 2039 GB/s；且 H100 PCIe 实际标称带宽通常为 2039 GB/s 是基于 HBM3 的特定频率（约 3.2 Gbps 或更高）或包含其他架构特性，单纯用 3.0 Gbps 无法推导出 2039 GB/s，存在内部逻辑矛盾。 | 逻辑校验失败：5120 * 3.0 / 8 = 1920，与 2039 不符；且 H100 PCIe 的 2039 GB/s 是已知硬件规格，但推导过程数值错误。
