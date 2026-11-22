# N356: A100 80GB SXM 与 PCIe 版本在 Qwen3-27B INT8 推理下的单 Token 能耗 (mJ/token) 对比：SXM 版本因 NVL

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N119

## Claim

A100 80GB SXM 与 PCIe 版本在 Qwen3-27B INT8 推理下的单 Token 能耗 (mJ/token) 对比：SXM 版本因 NVLink 低延迟通信和更高能效比，单 Token 能耗约为 5-8 mJ/token，PCIe 版本约为 6-9 mJ/token [待核验]，差异主要源于互联开销和功耗效率。

## Corrected Claim

A100 80GB SXM 与 PCIe 版本在 Qwen3-27B INT8 推理下，SXM 版本因 NVLink 低延迟通信和更高能效比，单 Token 能耗通常低于 PCIe 版本，具体数值取决于负载配置，但 SXM 版本在能效上具有优势。

## Evidence

[质询]具体数值（5-8 mJ/token 和 6-9 mJ/token）缺乏公开基准测试支持，且 INT8 推理能耗受模型架构、Batch Size、序列长度及具体硬件驱动版本影响极大，直接给出固定区间属于过度精确的经验数据断言。 | 经验事实，逻辑自洽（SXM 因 NVLink 高带宽和低延迟通常能效优于 PCIe），但缺来源支持具体数值。

## Search Query

A100 SXM vs PCIe energy per token LLM inference millijoules
