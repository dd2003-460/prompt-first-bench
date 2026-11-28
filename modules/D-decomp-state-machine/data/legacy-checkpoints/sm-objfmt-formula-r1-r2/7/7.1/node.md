# N104: RTX 5090 的显存规格确认为 32GB GDDR7，其有效带宽需考虑 GDDR7 的 PAM3 调制特性及驱动优化，理论峰值带宽 1792 GB/s 是厂

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N40

## Claim

RTX 5090 的显存规格确认为 32GB GDDR7，其有效带宽需考虑 GDDR7 的 PAM3 调制特性及驱动优化，理论峰值带宽 1792 GB/s 是厂商标称值，实际在 LLM 推理负载下的有效带宽利用率通常为 70-85%

## Corrected Claim

RTX 5090 的显存规格为 32GB GDDR7，理论峰值带宽约为 1792 GB/s。实际在 LLM 推理负载下的有效带宽利用率受多种因素影响，通常低于理论峰值，具体数值需根据实际测试确定。

## Evidence

[质询]具体数值（32GB、1792 GB/s）及利用率范围（70-85%）属于经验事实，缺乏来源支持，且不同负载下利用率波动较大，固定区间可能不准确。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

RTX 5090 GDDR7 bandwidth efficiency LLM inference actual throughput vs theoretical
