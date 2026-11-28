# N275: PagedAttention 的内部碎片率公式修正为：Fragmentation_Rate = (Sum(block_size - len_i mod bloc

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N87

## Claim

PagedAttention 的内部碎片率公式修正为：Fragmentation_Rate = (Sum(block_size - len_i mod block_size) for i in active_requests) / Sum(len_i)；在 block_size=16 且请求长度均匀分布的情况下，平均浪费空间为 block_size/2 = 8 tokens，因此理论最大碎片率为 8/len_avg，需结合实际科研任务中 prompt 长度的分布直方图（如 Log-normal 分布）计算期望碎片率。

## Corrected Claim

PagedAttention 的内部碎片率公式修正为：Fragmentation_Rate = (Sum(block_size - len_i mod block_size) for i in active_requests) / Sum(len_i)；在 block_size=16 且请求长度均匀分布的情况下，平均浪费空间为 block_size/2 = 8 tokens，因此理论最大碎片率为 8/len_avg，需结合实际科研任务中 prompt 长度的分布直方图（如 Log-normal 分布）计算期望碎片率。

## Evidence

先验知识/题面给定，逻辑校验通过：PagedAttention 的块分配机制导致每个活跃请求末尾存在未使用的空间，其大小在 [0, block_size) 区间内均匀分布时，期望浪费确为 block_size/2；碎片率定义为总浪费空间除以总 token 数，公式推导符合逻辑且量纲正确。

## Search Query

PagedAttention internal fragmentation rate block size average waste calculation
