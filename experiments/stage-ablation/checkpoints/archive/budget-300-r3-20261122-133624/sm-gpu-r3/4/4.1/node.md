# N29: 多卡推理的张量并行（TP）通信开销占比 = (2 × 模型参数量 × 激活值大小 × 层数 × 步数) / (总推理时间)，在 PCIe 5.0 (64 GB/

- **status**: pending
- **level**: L2
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N4

## Claim

多卡推理的张量并行（TP）通信开销占比 = (2 × 模型参数量 × 激活值大小 × 层数 × 步数) / (总推理时间)，在 PCIe 5.0 (64 GB/s) 下，27B 模型 TP=2 的通信延迟约为 12-15ms/step，占端到端延迟的 5-10% [待核验：需实测或引用 vLLM 基准]，远高于 NVLink (900 GB/s) 的 <1ms 开销。

## Corrected Claim

多卡推理的张量并行（TP）通信开销主要取决于激活值大小和互联带宽。在 PCIe 5.0 (64 GB/s) 下，27B 模型 TP=2 的通信延迟显著高于 NVLink (900 GB/s)，具体数值（如 12-15ms/step）需根据实际 Batch Size 和序列长度实测确定，通常占端到端延迟的 5-10% 以上。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 9 column 5 (char 818)

## Search Query

PCIe 5.0 vs NVLink bandwidth tensor parallelism overhead LLM inference latency

## Retrieval Sources

- {'url': 'https://blog.csdn.net/qq_46207024/article/details/157467340&rut=b16e89f91b9776705e272dbd96807dd7e429233728e414c1f768d233e4ffff5a', 'type': 'ddg', 'title': '多卡并行策略：Tensor Parallelism（TP）在昇腾上的通信机制'}
- {'url': 'https://blog.csdn.net/iymei4986533030/article/details/161917736&rut=206e80a10b6af48921c01098f62beca1d681f6bba4bf71fa356a54d18d63b962', 'type': 'ddg', 'title': 'AI 推理性能调优：Tensor Parallelism 与 Pipeline Parallelism 的通信优化_tp'}
- {'url': 'https://ascendai.csdn.net/69797faea16c6648a98596b7.html&rut=01b4b2ea06632597d235131a486c31f78e6c882ae9c1803cb0992f045af81eb4', 'type': 'ddg', 'title': '多卡并行策略：Tensor Parallelism（TP）在昇腾上的通信机制'}
