# N85: L40S 48GB 运行 Qwen3-27B INT8 权重 + BF16 KV Cache (32K) 时，显存占用为 27GB (权重) + 40GB (K

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N19

## Claim

L40S 48GB 运行 Qwen3-27B INT8 权重 + BF16 KV Cache (32K) 时，显存占用为 27GB (权重) + 40GB (KV) = 67GB，超出 48GB 显存，故 INT8 权重方案在 32K 上下文下不可行，必须使用 FP8 权重或 KV Cache 量化。

## Corrected Claim

L40S 48GB 运行 Qwen3-27B INT8 权重 + BF16 KV Cache (32K) 时，仅权重与 KV Cache 的显存占用估算约为 67GB，已超出 48GB 显存限制，因此该配置在 32K 上下文下大概率不可行，需采用 FP8 权重或 KV Cache 量化等优化手段。

## Evidence

[质询]KV Cache 的 40GB 估算缺乏具体模型架构参数（如层数、头数、头维度）支持，且未考虑激活值显存（Activation Memory）和 CUDA 上下文开销，导致总显存估算可能偏高或偏低，结论的鲁棒性存疑。 | 先验知识/题面给定，逻辑校验通过：INT8 权重 27GB 合理（27B * 1 byte），但 KV Cache 40GB 为经验估算值，缺乏架构细节支撑，且未计入激活值开销，故降级为定性表述。

## Search Query

NVIDIA L40S 48GB Qwen3 27B 32k context memory requirements
