# N383: A100 80GB (SXM/PCIe) 在 24/7 连续 LLM 推理负载下的稳态平均功耗实测值（瓦特），需澄清原 400W 假设是否混淆了 H100 数据

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N135

## Claim

A100 80GB (SXM/PCIe) 在 24/7 连续 LLM 推理负载下的稳态平均功耗实测值（瓦特），需澄清原 400W 假设是否混淆了 H100 数据，A100 的实际 TDP 为 250W(PCIe)/300W(SXM)，稳态功耗通常接近但略低于 TDP，需获取具体实测均值。

## Corrected Claim

A100 80GB 的 TDP 规格为 250W (PCIe) 和 300W (SXM)。在 24/7 连续 LLM 推理负载下，其稳态平均功耗通常接近但略低于 TDP，具体数值取决于实际负载强度，需参考特定场景下的实测数据。

## Evidence

[质询]该陈述包含具体的硬件规格参数（A100 TDP 250W/300W），属于经验事实。虽然这些数值在业界是公认的标准值，但当前检索无可用来源，无法通过外部证据直接验证其准确性，且‘稳态平均功耗’的具体实测值因负载而异，原陈述中‘需获取具体实测均值’表明该数据尚未确定，存在不确定性。 | 经验事实，逻辑自洽但缺来源支持。A100 的 TDP 规格（PCIe 250W, SXM 300W）符合 NVIDIA 官方公开规格，逻辑上稳态功耗接近 TDP 是合理的，但因无外部来源直接支持具体实测均值，且属于硬件规格类经验事实，依据规则降级。

## Search Query

A100 80GB average power consumption sustained LLM inference watts TDP
