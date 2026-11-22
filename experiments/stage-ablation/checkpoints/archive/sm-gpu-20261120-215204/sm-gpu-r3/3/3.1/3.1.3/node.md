# N84: 若坚持单卡 RTX 4090 且 32K 上下文，唯一可行精度组合为 W4A16 权重 + FP8/INT4 KV Cache + FlashAttention

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N18

## Claim

若坚持单卡 RTX 4090 且 32K 上下文，唯一可行精度组合为 W4A16 权重 + FP8/INT4 KV Cache + FlashAttention-2，此时显存占用约为 17GB (权重) + 10GB (FP8 KV) + 2GB (开销) = 29GB，仍超出 24GB，故结论为：单卡 RTX 4090 无法在 32K 上下文下运行 Qwen3-27B，N18 的‘极致性价比’前提在 32K 约束下不成立，需修正为 16K 上下文或双卡方案。

## Corrected Claim

单卡 RTX 4090 在 32K 上下文下运行 Qwen3-27B 面临极高的显存压力，标准 W4A16 + FP8 KV Cache 配置通常超出 24GB 显存限制；若需稳定运行，建议降低上下文至 16K 或采用双卡方案，或通过更激进的量化（如 W3A16）及框架优化尝试极限运行。

## Evidence

[质询]数值估算存在显著不确定性：1. Qwen3-27B 的 W4A16 权重显存占用并非固定 17GB，取决于量化算法（如 GPTQ/AWQ）及校准数据，通常在 14-16GB 之间；2. FP8 KV Cache 在 32K 上下文下的占用量高度依赖模型架构参数（层数、头数、头维度），10GB 的估算可能偏高或偏低，且未考虑 FlashAttention-2 对 KV Cache 实际驻留显存的优化效果（FA2 主要优化计算而非存储，但某些实现可能结合 PagedAttention 等机制影响峰值显存）；3. '2GB 开销' 过于简化，实际推理框架（如 vLLM/TensorRT-LLM）的激活值、临时缓冲区开销可能更高。 | 先验知识/题面给定，逻辑校验通过。虽然具体显存数值（17GB+10GB+2GB=29GB）是基于典型工程经验的估算，且不同量化方案和框架实现可能导致实际占用在 24GB 边缘波动（例如若权重优化至 15GB 且 KV Cache 优化至 8GB，则可能勉强运行），但结论方向（单卡 4090 在 32K 上下文下运行 27B 模型极具挑战且通常不可行或需极致优化）符合当前硬件与模型规模的基本物理限制。由于缺乏具体来源支持精确数值，且存在通过激进量化或框架优化使其勉强运行的可能性，故降级为定性表述。

## Search Query

RTX 4090 24GB limit 32k context LLM inference feasibility
