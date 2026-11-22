# N138: 在W8A8量化中，若采用Per-Channel量化粒度，Scale/Zeropoint显存开销 = num_output_channels * 2 bytes 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N40

## Claim

在W8A8量化中，若采用Per-Channel量化粒度，Scale/Zeropoint显存开销 = num_output_channels * 2 bytes * num_linear_layers；对于Qwen3-27B (约60个线性层，hidden_dim=4096)，开销约为 60 * 4096 * 2 * 2 ≈ 0.98 MB，远低于权重显存，可忽略不计；若采用Per-Tensor粒度，开销进一步降至 KB 级。

## Corrected Claim

在W8A8量化中，若采用Per-Channel量化粒度，Scale/Zeropoint显存开销 = num_output_channels * 2 bytes * num_linear_layers；对于Qwen3-27B (约60个线性层，hidden_dim=4096)，开销约为 60 * 4096 * 2 * 2 ≈ 0.98 MB，远低于权重显存，可忽略不计；若采用Per-Tensor粒度，开销进一步降至 KB 级。

## Evidence

先验知识/题面给定，逻辑校验通过：Per-Channel量化每个输出通道需存储scale和zero_point（通常各1字节或2字节，此处按2字节计算），总开销为层数*通道数*2*2，计算结果0.98MB量级正确，且远低于权重显存，结论合理。

## Search Query

W8A8 quantization scale zero point memory overhead per-channel
