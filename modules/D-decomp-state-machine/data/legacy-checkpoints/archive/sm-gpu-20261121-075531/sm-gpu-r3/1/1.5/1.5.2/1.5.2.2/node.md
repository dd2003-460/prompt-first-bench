# N162: TP=2 W4 模式下，2x RTX 7900 XTX (24GB) 每卡显存占用 9.43GB，剩余 14.57GB；ROCm 多卡通信开销比 CUDA NC

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N48

## Claim

TP=2 W4 模式下，2x RTX 7900 XTX (24GB) 每卡显存占用 9.43GB，剩余 14.57GB；ROCm 多卡通信开销比 CUDA NCCL 高，预计 AllReduce 延迟增加 20-40%，导致实际 TPS 比 2x 4090 低 25-35%；尽管 7900 XTX 价格低 $400，但需计算其 TCO 是否仍具优势。

## Corrected Claim

TP=2 W4 模式下，2x RTX 7900 XTX (24GB) 每卡显存占用 9.43GB，剩余 14.57GB；ROCm 多卡通信开销通常高于 CUDA NCCL，可能导致实际 TPS 低于 2x 4090；尽管 7900 XTX 价格低 $400，但需计算其 TCO 是否仍具优势。

## Evidence

[质询]ROCm 多卡通信开销比 CUDA NCCL 高 20-40% 以及由此导致的 TPS 降低 25-35% 属于高度依赖具体软件栈版本、驱动优化程度及模型架构的经验性数据，缺乏通用性，且不同场景下波动极大，直接断言具体百分比区间存在过度精确化的风险。 | 先验知识/题面给定，逻辑校验通过：显存计算（24-9.43=14.57）正确；但 ROCm 与 CUDA 的性能差距及具体 TPS 损失比例属于经验事实，虽逻辑自洽但缺乏通用性保证，故降级为定性表述。

## Search Query

ROCm multi-GPU communication overhead vs CUDA NCCL LLM inference
