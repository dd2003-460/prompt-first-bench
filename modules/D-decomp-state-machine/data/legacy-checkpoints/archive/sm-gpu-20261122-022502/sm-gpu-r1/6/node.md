# N28: 候选硬件筛选边界：排除显存带宽 < 500GB/s 的GPU（如L4, T4）用于交互式32K上下文推理，因KV Cache加载延迟导致TTFT > 5s；排除

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: (root)

## Claim

候选硬件筛选边界：排除显存带宽 < 500GB/s 的GPU（如L4, T4）用于交互式32K上下文推理，因KV Cache加载延迟导致TTFT > 5s；排除内存带宽 < 100GB/s 的统一内存方案（如M1/M2非Ultra系列），因吞吐量低于 5 tokens/s

## Corrected Claim

候选硬件筛选边界：排除显存带宽 < 500GB/s 的GPU（如L4, T4）用于交互式32K上下文推理，因KV Cache加载延迟导致TTFT > 5s；排除内存带宽 < 100GB/s 的统一内存方案（如M1/M2非Ultra系列），因吞吐量低于 5 tokens/s

## Evidence

检索失败: no sources from any channel (all 5 failed)
