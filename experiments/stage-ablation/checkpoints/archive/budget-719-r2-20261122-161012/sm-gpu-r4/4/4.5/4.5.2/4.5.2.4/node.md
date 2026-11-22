# N237: A100/H100 的 Batch Size 扩展受限于 Prefill 阶段 FLOPS 而非显存，当 Batch > 10 时，Prefill 延迟线性增长

- **status**: pending
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

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 817)

## Search Query

A100 H100 batch size prefill latency Qwen3 27B

## Retrieval Sources

- {'url': 'https://zhuanlan.zhihu.com/p/2092271469376161383&rut=6cd248b8994c28c1b2b8713bdbc1d4ce39ea8ab81e018739b19bb8f075cea33f', 'type': 'ddg', 'title': '2026年A100、H800、H20、4090 GPU榜单：大模型Token推理性能、显存、带宽与架构评测'}
