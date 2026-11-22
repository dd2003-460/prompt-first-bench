# N135: A100 80GB PCIe 版本在 FP8 推理模式下的实际功耗：其 TDP 为 300W (SXM) 或 250W (PCIe)，需确认 24/7 推理负载

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N39

## Claim

A100 80GB PCIe 版本在 FP8 推理模式下的实际功耗：其 TDP 为 300W (SXM) 或 250W (PCIe)，需确认 24/7 推理负载下的实际平均功耗是否显著低于 TDP 上限，以修正 OpEx 计算中的 400W 假设（原计算可能高估了 A100 功耗或混淆了 H100 数据）。

## Corrected Claim

A100 80GB PCIe 版本标称 TDP 约为 250W，SXM 版本约为 300W。在 FP8 推理模式下，实际平均功耗通常低于 TDP 上限，但具体数值需依据实际负载监控数据确认，原 400W 假设可能高估了功耗。

## Evidence

[质询]该陈述包含具体的硬件规格数值（A100 TDP 300W/250W）及功耗行为假设，属于经验事实。由于检索失败，无法通过外部来源直接验证这些具体数值及'实际平均功耗显著低于TDP'的结论，存在数据混淆或量级偏差的风险。 | 经验事实，逻辑自洽但缺来源支持。A100 TDP 数值符合公开常识，但具体推理负载下的平均功耗需实测数据支持，当前无可用外部证据。

## Search Query

NVIDIA A100 80GB PCIe actual power consumption inference load watts
