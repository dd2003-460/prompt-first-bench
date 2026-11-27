# N69: 核实 RTX 4090 在 LLM 推理（非训练）场景下的实际 MFU 范围：查阅 LLM 推理引擎（如 vLLM, llama.cpp）在 RTX 4090 

- **status**: degraded
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N24

## Claim

核实 RTX 4090 在 LLM 推理（非训练）场景下的实际 MFU 范围：查阅 LLM 推理引擎（如 vLLM, llama.cpp）在 RTX 4090 上运行 7B-70B 模型的公开基准测试，区分 Prefill 阶段（计算受限，MFU 较高）和 Decode 阶段（内存受限，MFU 极低，通常 <10%）的 MFU 差异，修正 N24 中笼统的 30%-45% 说法

## Corrected Claim

RTX 4090 在 LLM 推理中，Prefill 阶段计算受限，MFU 相对较高；Decode 阶段内存受限，MFU 通常极低（<10%）。具体 MFU 数值需结合特定模型和引擎实测，笼统的 30%-45% 说法不准确，应区分阶段。

## Evidence

[质询]参考来源主要提供吞吐量（tok/s）和延迟数据，未直接提供 MFU（Model FLOPs Utilization）的具体数值或 Prefill/Decode 阶段的 MFU 细分数据，无法直接验证 30%-45% 或 <10% 的具体数值范围。 | 来源 [1] 和 [2] 提供了 RTX 4090 在 llama.cpp 下的推理性能基准，证实了硬件和场景的相关性，但缺乏 MFU 的直接测量数据；逻辑上 Decode 阶段受内存带宽限制导致 MFU 极低是公认事实，但具体数值缺乏直接来源支持。

## Search Query

RTX 4090 LLM inference MFU Model FLOPs Utilization prefill decode benchmark vLLM

## Retrieval Sources

- {'url': 'https://www.hardware-corner.net/rtx-4090-llm-benchmarks/&rut=fe39484b784d4af85908d80fcab7d1891e165690c272438abe2338bc4a5b542b', 'type': 'ddg', 'title': 'RTX 4090 LLM Benchmarks: Performance Across 4K - 131K Context Sizes'}
- {'url': 'https://www.hardware-corner.net/gpu-llm-benchmarks/rtx-4090/&rut=e8ec9e218e0cf87476196b4f5439a93d7912a7ceb2e8b014deb792476d04ece7', 'type': 'ddg', 'title': 'RTX 4090 Local LLM Benchmarks, Context Scaling & Supported Models 2026 ...'}
- {'url': 'https://modelfit.io/gpu/rtx-4090/&rut=5c143e9bb23f1db7c636bfbd4819acf90f4ee18257296097ac62927f484c13e4', 'type': 'ddg', 'title': 'RTX 4090 24GB Local LLM (2026): Runs 32B at est. 39 tok/s'}
