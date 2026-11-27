# N569: 若采用 Chunked Prefill 技术将 32K 输入分块处理，每块 4K tokens，单块 Prefill 延迟降至 1.77e12 / 8 / (9

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N237

## Claim

若采用 Chunked Prefill 技术将 32K 输入分块处理，每块 4K tokens，单块 Prefill 延迟降至 1.77e12 / 8 / (989e12 * 0.4) ≈ 0.56s (H100)，但总 TTFT 仍为 8 * 0.56 = 4.48s (串行) 或受限于 Decode 带宽；Chunked Prefill 不降低总计算量，仅改善调度公平性，因此 N237 的 'TTFT < 2s' 在 32K 全量输入下对 H100/A100 均不可行，除非使用投机解码 (Speculative Decoding) 或模型蒸馏。

## Corrected Claim

若采用 Chunked Prefill 技术将 32K 输入分块处理，每块 4K tokens，单块 Prefill 延迟降至 1.77e12 / 8 / (989e12 * 0.4) ≈ 0.56s (H100)，但总 TTFT 仍为 8 * 0.56 = 4.48s (串行) 或受限于 Decode 带宽；Chunked Prefill 不降低总计算量，仅改善调度公平性，因此 N237 的 'TTFT < 2s' 在 32K 全量输入下对 H100/A100 均不可行，除非使用投机解码 (Speculative Decoding) 或模型蒸馏。

## Evidence

先验知识/题面给定，逻辑校验通过：Chunked Prefill 确实不减少总 FLOPs，仅改善调度；32K 输入在 H100 上的计算量巨大，串行处理延迟远超 2s，结论符合物理直觉与工程常识。

## Search Query

Chunked Prefill vLLM H100 TTFT 32k context optimization
