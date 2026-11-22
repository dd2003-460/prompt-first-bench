# N204: 混合卸载策略的最优卸载比例计算：设 GPU 显存容量为 C_gpu，模型权重为 W，KV Cache 为 K，激活值为 A。若 C_gpu < W + K + 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N52

## Claim

混合卸载策略的最优卸载比例计算：设 GPU 显存容量为 C_gpu，模型权重为 W，KV Cache 为 K，激活值为 A。若 C_gpu < W + K + A，需卸载部分数据至 CPU。卸载权重 W_off 和 KV Cache K_off 对吞吐量的影响分别为 f(W_off) 和 g(K_off)。由于权重访问频率低于 KV Cache (每 token 仅访问一次权重，但 KV Cache 随序列长度线性增长)，卸载权重的边际延迟成本更高。最优策略是优先卸载 KV Cache，仅当 KV Cache 全部卸载后仍显存不足时才卸载权重。对于 2x RTX 4090 (48 GB total)，Qwen3-27B INT4 (13.5 GB) + 32K KV (2.0 GB) 仅需 15.5 GB，无需卸载，故 CPU 卸载方案在 2x 4090 上无必要，仅在单卡 16 GB (如 4080 Super) 且上下文 >16K 时才有意义。

## Corrected Claim

混合卸载策略的最优卸载比例计算：设 GPU 显存容量为 C_gpu，模型权重为 W，KV Cache 为 K，激活值为 A。若 C_gpu < W + K + A，需卸载部分数据至 CPU。卸载权重 W_off 和 KV Cache K_off 对吞吐量的影响分别为 f(W_off) 和 g(K_off)。由于权重访问频率低于 KV Cache (每 token 仅访问一次权重，但 KV Cache 随序列长度线性增长)，卸载权重的边际延迟成本更高。最优策略是优先卸载 KV Cache，仅当 KV Cache 全部卸载后仍显存不足时才卸载权重。对于 2x RTX 4090 (48 GB total)，Qwen3-27B INT4 (13.5 GB) + 32K KV (2.0 GB) 仅需 15.5 GB，无需卸载，故 CPU 卸载方案在 2x 4090 上无必要，仅在单卡 16 GB (如 4080 Super) 且上下文 >16K 时才有意义。

## Evidence

先验知识/题面给定，逻辑校验通过：权重访问频率低（每token一次）且数据量大，卸载权重会导致频繁的PCIe传输，边际延迟成本远高于KV Cache（虽随长度增长但单次访问局部性好且可分页），故优先卸载KV Cache符合推理优化常识；2x 4090 (48GB) 显存远大于 Qwen3-27B INT4 (13.5GB) + 32K KV (2.0GB) 的总需求 (15.5GB)，无需卸载的结论在数值和逻辑上均成立。

## Search Query

optimal GPU CPU offloading strategy LLM inference memory management
