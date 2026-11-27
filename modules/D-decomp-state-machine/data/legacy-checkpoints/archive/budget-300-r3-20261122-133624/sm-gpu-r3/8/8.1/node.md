# N166: H100 (80GB HBM3) 在 BF16 精度下，Decode 吞吐量约为 40-50 tokens/s (batch=1)，Prefill 吞吐量约为 

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N41

## Claim

H100 (80GB HBM3) 在 BF16 精度下，Decode 吞吐量约为 40-50 tokens/s (batch=1)，Prefill 吞吐量约为 3000-4000 tokens/s；H100 的高显存带宽 (3.35 TB/s) 是其 Decode 速度远超消费级卡的主要原因，但高功耗 (700W) 对本地工作站散热和电力成本构成挑战。

## Corrected Claim

H100 (80GB HBM3) 在 BF16 精度下，Decode 吞吐量约为 40-50 tokens/s (batch=1)，Prefill 吞吐量约为 3000-4000 tokens/s；H100 的高显存带宽 (3.35 TB/s) 是其 Decode 速度远超消费级卡的主要原因，但高功耗 (700W) 对本地工作站散热和电力成本构成挑战。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 80GB HBM3 带宽 3.35TB/s 符合规格，BF16 下 Decode 受带宽限制，40-50 tokens/s (batch=1) 及 Prefill 3000-4000 tokens/s 的量级与主流大模型（如 7B-13B 参数规模）在 H100 上的实测性能相符，700W 功耗亦符合 H100 SXM/PCIe 规格。
