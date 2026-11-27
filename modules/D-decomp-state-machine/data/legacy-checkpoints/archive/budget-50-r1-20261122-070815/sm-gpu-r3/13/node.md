# N151: Apple M2 Ultra 统一内存架构在 LLM 推理中的有效带宽利用率，实测数据表明其 800 GB/s 标称带宽在实际 LLM Decode 阶段通常只

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

Apple M2 Ultra 统一内存架构在 LLM 推理中的有效带宽利用率，实测数据表明其 800 GB/s 标称带宽在实际 LLM Decode 阶段通常只能达到 50-60% (约 400-480 GB/s)，导致实际 tokens/s 远低于理论计算值 (59 tokens/s)，需修正为实测值以准确对比 GPU 方案。

## Corrected Claim

Apple M2 Ultra 统一内存架构在 LLM 推理中的有效带宽利用率，实测数据表明其 800 GB/s 标称带宽在实际 LLM Decode 阶段通常只能达到 50-60% (约 400-480 GB/s)，导致实际 tokens/s 远低于理论计算值 (59 tokens/s)，需修正为实测值以准确对比 GPU 方案。

## Evidence

检索失败: no sources from any channel (all 5 failed)
