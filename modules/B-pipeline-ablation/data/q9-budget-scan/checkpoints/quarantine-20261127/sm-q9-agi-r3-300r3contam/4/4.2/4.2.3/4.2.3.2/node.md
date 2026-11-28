# N166: N57中KV Cache分页碎片化的量化模型：vLLM使用PagedAttention时，N个并发序列的KV Cache页分配会导致内存碎片率Fragmenta

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N57

## Claim

N57中KV Cache分页碎片化的量化模型：vLLM使用PagedAttention时，N个并发序列的KV Cache页分配会导致内存碎片率Fragmentation(N)随N增加而上升，需建立Fragmentation(N) = γ * log(N)模型，γ为碎片化系数，进而推导有效KV Cache容量减少导致的Prefill阶段延迟增加ΔT_prefill(N)。

## Corrected Claim

vLLM 使用 PagedAttention 时，KV Cache 采用分页存储以消除外部内存碎片，但仍存在内部碎片（页内未用空间）和元数据开销。随着并发序列 N 增加，总 KV Cache 占用线性增长，可能导致 GPU 显存压力增大，从而限制最大并发数或触发 Swap/Preemption，间接影响系统吞吐量和尾延迟，但并非直接通过‘碎片率随 N 对数增长’导致 Prefill 延迟增加。

## Evidence

[质询]该陈述将‘内存碎片率’与‘有效容量减少’及‘延迟增加’强行关联，并指定了具体的对数增长模型 Fragmentation(N) = γ * log(N)。然而，PagedAttention 的核心设计初衷正是通过分页机制消除传统连续内存分配带来的外部碎片问题，其剩余开销主要源于内部碎片（页内未用空间）和元数据管理，而非随并发数 N 呈对数增长的‘碎片率’。此外，Prefill 阶段的延迟主要取决于计算密集度（FLOPs）和带宽，KV Cache 容量的‘碎片化’并不直接导致 Prefill 延迟增加（Prefill 通常一次性写入，不涉及随机读取或频繁换页），该因果链条在逻辑上存在混淆，且指定的对数模型缺乏通用理论支撑，属于未经证实的经验假设。 | 先验知识/题面给定，逻辑校验发现因果链条存疑：PagedAttention 旨在解决外部碎片，Prefill 延迟主要受计算量影响而非 KV Cache 碎片率，且指定的对数模型缺乏普遍适用性，故降级。
