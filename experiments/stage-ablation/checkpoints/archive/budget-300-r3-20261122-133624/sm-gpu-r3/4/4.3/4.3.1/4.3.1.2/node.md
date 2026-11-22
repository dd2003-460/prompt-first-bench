# N313: SGLang 0.4.0+ 版本对 Qwen3-27B 的官方支持状态：已支持 Qwen3 架构，吞吐量与 vLLM 0.6.4+ 相当（差异 < 5%），但支

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N102

## Claim

SGLang 0.4.0+ 版本对 Qwen3-27B 的官方支持状态：已支持 Qwen3 架构，吞吐量与 vLLM 0.6.4+ 相当（差异 < 5%），但支持更灵活的上下文长度配置（最大 128K tokens），适合长上下文场景；若使用 SGLang 0.3.x 或更早版本，需回退至 llama.cpp，导致吞吐量下降 20-25%（基于 N102 的吞吐量下降估算），且不支持 RadixAttention 的 KV Cache 复用，显存占用增加 15-20%（基于 RadixAttention 的显存节省估算）

## Corrected Claim

SGLang 0.4.0+ 版本支持 Qwen3 架构，通常具备更灵活的上下文长度配置（如支持长上下文场景），性能表现与 vLLM 相当；若使用 SGLang 0.3.x 或更早版本，可能因缺乏对 Qwen3 架构的原生优化或 RadixAttention 支持，导致吞吐量下降及显存占用增加，具体幅度需根据实际部署环境测试确定。

## Evidence

[质询]该陈述包含大量具体的经验性数值（如吞吐量差异<5%、显存增加15-20%、最大上下文128K等），这些属于特定软件版本在特定硬件/配置下的性能基准数据，无法从第一性原理推导，且缺乏来源支持，存在数值不准确或口径混淆的风险。 | 经验事实，逻辑自洽但缺来源支持（本轮检索无可用来源）

## Search Query

SGLang 0.4.0 Qwen3-27B support RadixAttention benchmark vs vLLM
