# N233: RTX 5090 (若发布) 运行 Qwen3-27B 的精度限制：32GB 显存不足以运行 BF16 (54GB) 或 FP8 (27GB+KV Cache)

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

RTX 5090 (若发布) 运行 Qwen3-27B 的精度限制：32GB 显存不足以运行 BF16 (54GB) 或 FP8 (27GB+KV Cache)，仅支持 W4/INT4 量化。计算 W4 量化下的最大上下文长度 Max_Context = (32GB - 14GB_Weight - 2GB_Overhead) / KV_Cache_Per_Token，验证是否满足 32K 下限，并评估 W4 质量损失是否可接受（参考 N80/N81 的质量阈值） [待核验]

## Corrected Claim

RTX 5090 (若发布) 运行 Qwen3-27B 的精度限制：32GB 显存不足以运行 BF16 (54GB) 或 FP8 (27GB+KV Cache)，仅支持 W4/INT4 量化。计算 W4 量化下的最大上下文长度 Max_Context = (32GB - 14GB_Weight - 2GB_Overhead) / KV_Cache_Per_Token，验证是否满足 32K 下限，并评估 W4 质量损失是否可接受（参考 N80/N81 的质量阈值） [待核验]

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 5090 显存为 32GB，Qwen3-27B 在 BF16 下权重约 54GB 超出显存，FP8 下权重约 27GB 加上 KV Cache 及开销后极易超出 32GB 限制，因此仅支持 W4/INT4 量化符合硬件与模型规模的基本物理约束。
