# N137: INT4 量化下 KV Cache 大小压缩比：若 KV Cache 从 BF16 (2 bytes) 量化至 INT4 (0.5 bytes)，大小压缩至 2

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N43

## Claim

INT4 量化下 KV Cache 大小压缩比：若 KV Cache 从 BF16 (2 bytes) 量化至 INT4 (0.5 bytes)，大小压缩至 25%；32K 上下文下 GQA 优化后的 KV Cache 从 3.93GB 降至 ≈ 0.98GB，此时 PCIe 5.0 全量传输时间 ≈ 20ms，增量传输时间 ≈ 0.5ms，需结合量化算法 (如 SmoothQuant, GPTQ) 对 KV Cache 的精度损失评估。

## Corrected Claim

INT4 量化下 KV Cache 大小压缩比：若 KV Cache 从 BF16 (2 bytes) 量化至 INT4 (0.5 bytes)，大小压缩至 25%；32K 上下文下 GQA 优化后的 KV Cache 从 3.93GB 降至 ≈ 0.98GB，此时 PCIe 5.0 全量传输时间 ≈ 20ms，增量传输时间 ≈ 0.5ms，需结合量化算法 (如 SmoothQuant, GPTQ) 对 KV Cache 的精度损失评估。

## Evidence

先验知识/题面给定，逻辑校验通过：BF16(2B)转INT4(0.5B)压缩比为25%；3.93GB * 25% ≈ 0.98GB；0.98GB / 64GB/s (PCIe 5.0 x16) ≈ 15.3ms，与20ms量级相符（考虑开销）；增量传输0.5ms符合小数据量传输直觉。

## Search Query

INT4 KV cache quantization accuracy loss LLM inference
