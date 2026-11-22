# N80: RTX 4090 (Ada Lovelace) 运行 Qwen3-27B 时，W4A8/W4A16 精度下的实际推理吞吐量（Tokens/s）与 BF16 精度

- **status**: pending
- **level**: L3
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N17

## Claim

RTX 4090 (Ada Lovelace) 运行 Qwen3-27B 时，W4A8/W4A16 精度下的实际推理吞吐量（Tokens/s）与 BF16 精度的比值，需考虑反量化计算开销抵消部分带宽优势，预期比值为 1.8-2.2 倍，需检索具体 benchmark 数据。

## Corrected Claim

RTX 4090 运行 Qwen3-27B 时，W4A8/W4A16 精度下的实际推理吞吐量通常高于 BF16，具体加速比取决于反量化实现效率与硬件带宽瓶颈，理论预期在 1.8-2.2 倍左右，但需具体 benchmark 数据验证。

## Evidence

父节点级核验失败（LLM 错误）：Unterminated string starting at: line 10 column 5 (char 815)

## Search Query

RTX 4090 Qwen3-27B 4bit quantization inference throughput benchmark

## Retrieval Sources

- {'url': 'https://dashen-tech.com/ai-tech/qwen38-27b-deployment-guide/&rut=aaf906668f1b8fafbac7f3c6d54d6c9103a71d8c17508fb461dc08b547b4e001', 'type': 'ddg', 'title': 'Qwen3.8 27B 本地部署：RTX 4090 单卡运行+6方案对比（2026） | Dashen-Tech'}
- {'url': 'https://www.kongchang.com/articles/4090pao-qwen3-27b-q4liang-hua-128kshang-xia-wen-shi-zhan&rut=c4c8e00bb1aa4d820272234f47c72446c82ff68ed221fd28543c531bbbb41d78', 'type': 'ddg', 'title': '4090跑Qwen3 27B实测：Q4量化+128K上下文显存计算与调优指南 - 控场AI'}
- {'url': 'https://blog.csdn.net/student_upupgpu/article/details/164257079&rut=c53139faf81f9df353e743b651d3fc0c3c3ed7fbc773e39014030640ee59a892', 'type': 'ddg', 'title': 'RTX 4090 24GB 能跑 Qwen3.8-27B 吗？单卡显存计算与云端部署指南'}
