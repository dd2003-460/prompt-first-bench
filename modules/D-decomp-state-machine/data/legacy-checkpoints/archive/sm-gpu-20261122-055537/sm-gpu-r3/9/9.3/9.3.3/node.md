# N359: 注意力计算效率 (Compute Efficiency) 受 block_size 影响：较小的 block_size (16) 意味着更频繁的内存访问边界检查

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N113

## Claim

注意力计算效率 (Compute Efficiency) 受 block_size 影响：较小的 block_size (16) 意味着更频繁的内存访问边界检查和非连续内存访问模式，导致 GPU 内存合并访问 (Memory Coalescing) 效率降低；在 RTX 4090 上，block_size=16 相比 block_size=64 在 Decode 阶段的 Attention 内核执行时间预计增加 5-15% [待核验]，主要源于指令开销而非带宽瓶颈。

## Corrected Claim

注意力计算效率受 block_size 影响：较小的 block_size (16) 意味着更频繁的内存访问边界检查和非连续内存访问模式，导致 GPU 内存合并访问效率降低；在 RTX 4090 上，block_size=16 相比 block_size=64 在 Decode 阶段的 Attention 内核执行时间预计会有所增加（具体幅度取决于实现细节，通常为数个百分点至两位数），主要源于指令开销及缓存效率降低。

## Evidence

[质询]具体数值区间（5-15%）缺乏通用基准测试支持，且高度依赖于具体的序列长度、头数及硬件微架构优化，属于特定实验条件下的经验数据而非普适物理定律；此外，'主要源于指令开销而非带宽瓶颈'的归因在 block_size=16 这种小批量场景下可能过于绝对，因为非连续访问导致的缓存未命中（Cache Miss）往往也会显著增加有效带宽压力，二者通常耦合存在。 | 先验知识/题面给定，逻辑校验通过：小 block_size 确实导致更频繁的边界检查和更差的内存合并访问，从而降低 GPU 效率，定性逻辑自洽；但具体百分比为经验估计，无来源直接支持，故降级。

## Search Query

vLLM paged attention block size impact on throughput
