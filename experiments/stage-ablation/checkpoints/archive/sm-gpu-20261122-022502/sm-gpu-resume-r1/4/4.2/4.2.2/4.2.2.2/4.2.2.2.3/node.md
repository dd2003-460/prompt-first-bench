# N808: RTX 4090 单卡 BF16 算力为 82.6 TFLOPS，FP8 算力为 165.2 TFLOPS；Qwen3-27B 每 token 计算量约为 2 

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N251, N252, N253

## Claim

RTX 4090 单卡 BF16 算力为 82.6 TFLOPS，FP8 算力为 165.2 TFLOPS；Qwen3-27B 每 token 计算量约为 2 × 27B = 54 GFLOPS (仅权重读取主导的 Decode 阶段，实际 FLOPs 取决于稀疏性，此处取稠密上限)，单卡纯计算时间 T_compute = 54 GFLOPS / 165.2 TFLOPS ≈ 0.327 ms/token (FP8) 或 0.654 ms/token (BF16)。

## Corrected Claim

RTX 4090 单卡 BF16 算力为 82.6 TFLOPS，FP8 算力为 165.2 TFLOPS；Qwen3-27B 每 token 计算量约为 2 × 27B = 54 GFLOPS (仅权重读取主导的 Decode 阶段，实际 FLOPs 取决于稀疏性，此处取稠密上限)，单卡纯计算时间 T_compute = 54 GFLOPS / 165.2 TFLOPS ≈ 0.327 ms/token (FP8) 或 0.654 ms/token (BF16)。

## Evidence

先验知识/题面给定，逻辑校验通过：RTX 4090 FP8/BF16 算力数值符合官方规格（82.6/165.2 TFLOPS），27B 模型 Decode 阶段 FLOPs 估算（2×参数量）及时间计算（54/165200≈0.327ms, 54/82600≈0.654ms）在数学和物理量纲上均自洽。
