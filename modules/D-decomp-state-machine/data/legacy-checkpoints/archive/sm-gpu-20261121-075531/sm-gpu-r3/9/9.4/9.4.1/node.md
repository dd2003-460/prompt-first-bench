# N357: H100 80GB SXM 的 HBM3 内存带宽为 3350 GB/s，H100 80GB PCIe 的 HBM3 内存带宽为 2039 GB/s，带宽比值为

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N120

## Claim

H100 80GB SXM 的 HBM3 内存带宽为 3350 GB/s，H100 80GB PCIe 的 HBM3 内存带宽为 2039 GB/s，带宽比值为 1.643x；在 27B INT8 推理中，理论峰值 TPS 提升上限受限于此带宽比值，实际需修正计算单元效率差异。

## Corrected Claim

H100 80GB SXM 的 HBM3 内存带宽为 3350 GB/s，H100 80GB PCIe 的 HBM3 内存带宽为 2039 GB/s，带宽比值为 1.643x；在 27B INT8 推理中，理论峰值 TPS 提升上限受限于此带宽比值，实际需修正计算单元效率差异。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM (3.35 TB/s) 与 PCIe (2.04 TB/s) 带宽数值符合 NVIDIA 官方规格，比值 1.643 计算正确；INT8 推理在内存带宽受限场景下，理论峰值 TPS 提升上限确实受限于内存带宽比值，且需考虑计算单元效率差异的修正，逻辑自洽。

## Search Query

H100 SXM vs H100 PCIe memory bandwidth GB/s
