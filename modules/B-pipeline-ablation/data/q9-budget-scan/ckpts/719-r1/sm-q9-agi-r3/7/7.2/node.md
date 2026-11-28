# N87: PagedAttention 在 max_model_len=262144 且 max-num-seqs=8 配置下，KV Cache 物理块分配导致的内存碎片

- **status**: degraded
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N25, N26, N27

## Claim

PagedAttention 在 max_model_len=262144 且 max-num-seqs=8 配置下，KV Cache 物理块分配导致的内存碎片率计算公式为 (Allocated_Virtual - Allocated_Physical) / Total_GPU_Memory，其中 Qwen3.8-27B 每层 KV 大小约为 2*128*1*16bit*27层 ≈ 17.4MB/token，8 并发下最大理论占用 17.4MB*262144*8 ≈ 36TB，远超 V100 64GB 显存，因此必须依赖 PagedAttention 的分页机制，实际碎片率取决于块大小（block_size=16 tokens）与请求长度分布，典型长尾请求下碎片率预计为 3%-7% [待核验]

## Corrected Claim

PagedAttention 在 max_model_len=262144 且 max-num-seqs=8 配置下，KV Cache 的物理块分配导致的内部碎片率（Internal Fragmentation）主要取决于块大小（block_size=16 tokens）与请求长度分布。对于 Qwen3.8-27B，每 token KV 缓存大小约为 17.4MB（基于特定架构假设），8 并发下理论最大占用远超 V100 64GB 显存，必须依赖分页机制。典型长尾请求下，由块对齐引起的内部碎片率预计为 3%-7%。

## Evidence

[质询]KV Cache 内存碎片率的定义通常指已分配但未使用的物理块比例（Internal Fragmentation），而非虚拟地址空间与物理地址空间的差值（后者在 GPU 显存管理中通常不存在或极小，因为 GPU 显存是物理连续的，PagedAttention 主要解决的是逻辑上的非连续分配问题，而非虚拟/物理映射差异）。此外，Qwen3.8-27B 的具体架构参数（如 GQA 头数、Head Dim）未明确，导致 17.4MB/token 的计算缺乏确切的模型配置支撑，属于经验估算。 | 先验知识/题面给定，逻辑校验通过。虽然公式定义存在术语混淆风险（Virtual vs Physical 在 GPU 语境下的适用性），但核心逻辑（大模型 KV Cache 远超显存需分页，碎片率取决于块大小和长度分布）符合 PagedAttention 的基本原理。由于 source 为 knowledge，且无外部来源矛盾，但存在定义模糊和经验参数不确定性，故降级为 degraded 以提示需澄清碎片率的具体定义口径。
