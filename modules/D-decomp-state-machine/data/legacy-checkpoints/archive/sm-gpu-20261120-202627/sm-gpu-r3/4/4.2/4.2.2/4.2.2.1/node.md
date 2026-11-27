# N334: RTX 4090 在 Qwen3-27B (INT8/FP8) Decode 阶段 (Batch=1, 32K context) 的实测平均功耗 P_avg 约

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N105

## Claim

RTX 4090 在 Qwen3-27B (INT8/FP8) Decode 阶段 (Batch=1, 32K context) 的实测平均功耗 P_avg 约为 380-420W，对应功耗占比系数 α_avg ≈ 0.84-0.93 (基于 TDP=450W)，高于预估计的 70%，主要受限于 GDDR6X 显存高负载带宽需求。

## Corrected Claim

RTX 4090 在 Qwen3-27B (INT8/FP8) Decode 阶段 (Batch=1, 32K context) 的功耗预计接近其 TDP (450W)，主要受限于 GDDR6X 显存高负载带宽需求，具体实测值需依据特定测试环境确定。

## Evidence

[质询]该陈述包含具体的实测功耗数值（380-420W）和特定场景下的性能系数，属于经验事实。在缺乏任何参考来源支持的情况下，无法验证其数值的准确性，且不同测试环境（如驱动版本、散热条件、具体模型量化实现）可能导致显著差异。 | 经验事实，逻辑自洽但缺来源支持。RTX 4090 TDP为450W，380-420W对应84%-93%负载，符合高带宽显存访问（Decode阶段）导致功耗接近TDP的物理直觉，但具体数值无外部证据佐证。

## Search Query

RTX 4090 LLM inference power consumption watts decode phase benchmark
