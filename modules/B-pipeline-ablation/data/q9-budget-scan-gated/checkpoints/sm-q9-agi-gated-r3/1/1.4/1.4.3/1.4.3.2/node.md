# N52: 修正 N27 忽略的 KV Cache 显存竞争效应：当上下文长度 n > 4096 tokens 时，FP8 KV Cache 占用显存 E_kv = n *

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N27, N28, N29

## Claim

修正 N27 忽略的 KV Cache 显存竞争效应：当上下文长度 n > 4096 tokens 时，FP8 KV Cache 占用显存 E_kv = n * 12KB，挤占 draft model 可用的激活内存，导致 draft model 计算出现 OOM 或需启用 offload，此时接受率 α 的下降不再仅由注意力稀释引起，而是受限于硬件资源约束，需引入显存可用性系数 β(n) = min(1, E_avail / E_kv)。

## Corrected Claim

修正 N27 忽略的 KV Cache 显存竞争效应：当上下文长度 n 较大时，KV Cache 占用显存 E_kv 随 n 线性增长（具体系数取决于模型架构），挤占 draft model 可用的激活内存，可能导致 OOM 或需启用 offload。此时接受率 α 的下降受限于硬件资源约束，需引入显存可用性系数 β(n) 来反映资源瓶颈。

## Evidence

[质询]公式 E_kv = n * 12KB 缺乏具体的模型架构参数（如层数、头数、头维度）作为前提，属于特定配置下的经验估算而非通用物理定律；此外，'n > 4096' 这一阈值具有高度硬件依赖性，并非普适真理。 | 先验知识/题面给定，逻辑校验通过：KV Cache 显存占用确实随上下文长度线性增长并会与激活内存竞争，导致 OOM 或 Offload，进而影响推理稳定性；但具体数值 12KB/token 和阈值 4096 为经验参数，在无外部来源支持且非第一性原理严格推导的情况下，依据经验事实排除条款降级。
