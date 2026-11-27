# N86: 在13.0125GB可用KV显存下，若每token KV开销确为12KB（基于N20的GQA/MQA假设），则单序列最大上下文长度为 13.0125 * 102

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N39

## Claim

在13.0125GB可用KV显存下，若每token KV开销确为12KB（基于N20的GQA/MQA假设），则单序列最大上下文长度为 13.0125 * 1024^3 / (12 * 1024) ≈ 1,131,840 tokens。此数值远超max_model_len=262144，表明在NVFP4量化下，显存不再是限制单序列长度的瓶颈，瓶颈转移至计算延迟或KV Offload策略。

## Corrected Claim

在13.0125GB可用KV显存下，若每token KV开销确为12KB（基于N20的GQA/MQA假设），则单序列最大上下文长度为 13.0125 * 1024^3 / (12 * 1024) ≈ 1,131,840 tokens。此数值远超max_model_len=262144，表明在NVFP4量化下，显存不再是限制单序列长度的瓶颈，瓶颈转移至计算延迟或KV Offload策略。

## Evidence

先验知识/题面给定，逻辑校验通过：13.0125GB转换为字节后除以12KB/token，计算结果约为1,131,840 tokens，数值量级正确且逻辑自洽。
