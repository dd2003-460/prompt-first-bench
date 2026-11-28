# N25: FP8 KV Cache 将显存占用降低至 FP16 的 50% 左右，使得 max_model_len=262144 在 4×16GB 显存下的理论最大并发序

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N4

## Claim

FP8 KV Cache 将显存占用降低至 FP16 的 50% 左右，使得 max_model_len=262144 在 4×16GB 显存下的理论最大并发序列数 (max-num-seqs) 上限为 16-24 条，受限于剩余显存空间约 12GB/卡 [待核验]

## Corrected Claim

FP8 KV Cache 将显存占用降低至 FP16 的 50% 左右，从而显著提升了 max_model_len=262144 在 4×16GB 显存下的理论最大并发序列数上限，具体数值取决于模型规模及系统开销。

## Evidence

[质询]该陈述包含具体的经验性参数（如'剩余显存约12GB/卡'、'并发数16-24'），这些数值高度依赖于具体的模型架构（参数量、层数、头数）、硬件配置及vLLM版本，并非通用物理定律或数学恒等式，无法从第一性原理严格推导得出。 | FP8相比FP16显存减半的逻辑正确，但具体并发数上限和剩余显存数值属于特定场景下的经验估算，缺乏来源支持且无法通过纯逻辑推导验证其精确性。

## Search Query

vLLM fp8 kv cache memory usage calculation max num seqs long context
