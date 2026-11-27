# N143: vLLM 对 FP8 KV Cache 的支持状态：vLLM 自 v0.4.0 起支持 FP8 KV Cache (E4M3/E5M2)，但在 NVIDIA G

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N42

## Claim

vLLM 对 FP8 KV Cache 的支持状态：vLLM 自 v0.4.0 起支持 FP8 KV Cache (E4M3/E5M2)，但在 NVIDIA GPU 上默认回退到 BF16，除非显式启用 `--kv-cache-dtype fp8` 且硬件支持 FP8 Tensor Core (Ada/Hopper)。在 RTX 4090 上，FP8 KV Cache 存储可行，但计算 (Attention) 仍使用 BF16/FP16，仅节省显存，不加速计算。

## Corrected Claim

vLLM 支持 FP8 KV Cache (E4M3/E5M2)，通常需显式启用且依赖硬件支持（如 Ada/Hopper 架构）。在消费级 GPU（如 RTX 4090）上，FP8 KV Cache 主要节省显存，计算精度可能仍依赖 BF16/FP16 或特定内核支持，具体行为取决于 vLLM 版本及配置。

## Evidence

[质询]该陈述包含具体的版本号（v0.4.0）、默认行为（默认回退BF16）及硬件特定表现（RTX 4090上仅省显存不加速），属于经验事实。由于检索失败无外部来源支持，且vLLM版本迭代快，具体起始版本号和默认策略可能随版本变化，存在事实过时或细节偏差的风险。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

vLLM FP8 KV Cache support NVIDIA RTX 4090
