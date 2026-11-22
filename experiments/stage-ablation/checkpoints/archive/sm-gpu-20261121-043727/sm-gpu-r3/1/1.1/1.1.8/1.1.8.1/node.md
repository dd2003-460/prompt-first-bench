# N120: KV Cache 精度对显存占用的影响：N46 中假设 KV Cache 在 INT8 下减半（~4GB vs ~8GB），但需验证推理引擎（如 vLLM/Te

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N46

## Claim

KV Cache 精度对显存占用的影响：N46 中假设 KV Cache 在 INT8 下减半（~4GB vs ~8GB），但需验证推理引擎（如 vLLM/TensorRT-LLM）是否支持 KV Cache 量化。若仅权重量化而 KV Cache 保持 BF16，则 INT8 方案的总显存占用为 Weight(27GB) + KV_Cache(8GB) + Overhead(4GB) ≈ 39GB，而非 N46 估计的 35GB，这将改变最小显存阈值判断。

## Corrected Claim

KV Cache 精度对显存占用的影响：N46 中假设 KV Cache 在 INT8 下减半（~4GB vs ~8GB），但需验证推理引擎（如 vLLM/TensorRT-LLM）是否支持 KV Cache 量化。若仅权重量化而 KV Cache 保持 BF16，则 INT8 方案的总显存占用为 Weight(27GB) + KV_Cache(8GB) + Overhead(4GB) ≈ 39GB，而非 N46 估计的 35GB，这将改变最小显存阈值判断。

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算正确（27+8+4=39GB），且符合当前主流推理引擎（如vLLM/TensorRT-LLM）在早期或默认配置下KV Cache量化支持不如权重量化普及的工程事实，逻辑自洽。
