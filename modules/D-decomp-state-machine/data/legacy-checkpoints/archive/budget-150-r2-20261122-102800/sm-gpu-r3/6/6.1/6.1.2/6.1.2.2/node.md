# N338: RX 7900 XTX 在 W4 量化 (GPTQ/AWQ) 下的推理性能对比：RX 7900 XTX 的 INT8 吞吐约为 395 TOPS，W4 量化通常

- **status**: degraded
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N134

## Claim

RX 7900 XTX 在 W4 量化 (GPTQ/AWQ) 下的推理性能对比：RX 7900 XTX 的 INT8 吞吐约为 395 TOPS，W4 量化通常通过 INT8 或混合精度实现。相比 RTX 4090 (W4 吞吐约 69.2 tokens/s @ N155 数据)，RX 7900 XTX 的 W4 吞吐预计约为 RTX 4090 的 60-70% (基于 INT8 算力比 395/330 ≈ 1.2x 但带宽和软件栈劣势抵消)。具体数值需实测，预估为 40-50 tokens/s。

## Corrected Claim

RX 7900 XTX 的 INT8 算力约为 120-130 TOPS（非 395 TOPS）。在 W4 量化下，由于显存带宽（1936 GB/s vs 1008 GB/s）优势，RX 7900 XTX 的推理吞吐通常高于 RTX 4090，具体数值需实测，预估可能在 60-80 tokens/s 范围（取决于模型大小），而非低于 RTX 4090。

## Evidence

[质询]数值量级与逻辑推导存在严重矛盾：1. 395 TOPS 的 INT8 算力对于 RX 7900 XTX 而言量级错误（实际约为 120-130 TOPS，395 TOPS 更接近 RTX 4090 的 FP16 或更高精度算力，或混淆了稀疏/密集算力）；2. 基于错误的算力比（395/330 ≈ 1.2x）推导出 RX 7900 XTX 性能优于 RTX 4090 的假设，与最终结论（60-70% 性能）自相矛盾；3. 40-50 tokens/s 的预估对于 RX 7900 XTX 在 W4 量化下的大模型推理而言可能偏低或偏高，取决于具体模型大小，但缺乏实测数据支持。 | 先验知识/题面给定，逻辑校验未通过：算力数值量级错误导致推导逻辑断裂，且无外部来源支持具体吞吐数值。
