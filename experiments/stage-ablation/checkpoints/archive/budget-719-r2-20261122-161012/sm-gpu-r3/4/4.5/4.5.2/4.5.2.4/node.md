# N237: A100/H100 的 Batch Size 扩展受限于 Prefill 阶段 FLOPS 而非显存，当 Batch > 10 时，Prefill 延迟线性增长

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N109

## Claim

A100/H100 的 Batch Size 扩展受限于 Prefill 阶段 FLOPS 而非显存，当 Batch > 10 时，Prefill 延迟线性增长，可能突破 TTFT < 2s 阈值，需实测验证。

## Corrected Claim

A100/H100 的 Batch Size 扩展主要受限于 Prefill 阶段的 FLOPS 算力而非显存带宽；随着 Batch Size 增加，Prefill 延迟通常呈线性增长，可能突破 TTFT 阈值，具体临界点需根据模型规模和硬件配置实测验证。

## Evidence

[质询]该陈述包含具体的经验阈值（Batch > 10）和具体的性能指标（TTFT < 2s），这些数值高度依赖于模型规模、序列长度、硬件配置及具体推理框架，并非普适的物理或数学定律，属于经验事实。参考来源仅定性指出 H100 在 Prefill 阶段算力更强，未提供 Batch Size 与延迟的具体线性关系或阈值数据，无法直接支持该具体数值结论。 | 逻辑上 Prefill 阶段计算密集，受 FLOPS 限制且延迟随 Batch 线性增长符合直觉；但具体阈值（Batch>10, TTFT<2s）为经验参数，来源 [1] 仅间接支持 H100 Prefill 算力优势，未覆盖具体数值，依据经验事实排除条款降级。

## Search Query

A100 H100 batch size prefill latency Qwen3 27B

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2092271469376161383&rut=6cd248b8994c28c1b2b8713bdbc1d4ce39ea8ab81e018739b19bb8f075cea33f', 'type': 'ddg', 'title': '2026年A100、H800、H20、4090 GPU榜单：大模型Token推理性能、显存、带宽与架构评测'}
