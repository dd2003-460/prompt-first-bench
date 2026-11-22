# N239: Mac Studio M2 Ultra (800 GB/s) 与 M3 Ultra 内存带宽相同，但 M3 Ultra 的 CPU 核心数更多，Prefill 

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N110

## Claim

Mac Studio M2 Ultra (800 GB/s) 与 M3 Ultra 内存带宽相同，但 M3 Ultra 的 CPU 核心数更多，Prefill 阶段 FLOPS 更高，TTFT 预计比 M2 Ultra 快 15-20%。

## Corrected Claim

Mac Studio M2 Ultra (800 GB/s) 与 M3 Ultra 内存带宽相同，但 M3 Ultra 的 CPU 核心数更多，Prefill 阶段 FLOPS 更高，TTFT 预计比 M2 Ultra 有一定提升（具体幅度取决于负载特性，受内存带宽瓶颈限制，未必达到 15-20%）。

## Evidence

[质询]TTFT 提升 15-20% 的具体数值缺乏严谨推导支持。虽然 M3 Ultra 核心数增加（24核 vs 20核）且架构优化确实能提升 FLOPS，但 Prefill 阶段通常受限于内存带宽（Memory-Bound）而非计算能力（Compute-Bound）。既然两者内存带宽相同（800 GB/s），在长上下文 Prefill 场景下，带宽瓶颈会抵消部分 CPU 核心增加带来的计算优势，实际加速比可能低于 15-20%，甚至接近持平，具体取决于模型大小和序列长度。 | 先验知识/题面给定，逻辑校验通过。M3 Ultra 确实拥有更多 CPU 核心（24 vs 20）且架构更新，FLOPS 更高是事实；内存带宽相同也是事实。但 TTFT 加速比 15-20% 属于经验性预测，受限于内存带宽瓶颈，该具体数值缺乏绝对确定性，故降级为定性表述。
