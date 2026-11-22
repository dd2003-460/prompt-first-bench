# N421: H100 SXM 在 BF16 精度下，Prefill 阶段（计算密集）的理论峰值算力为 989 TFLOPS (FP16/BF16 无稀疏)。对于 27B 模

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N166

## Claim

H100 SXM 在 BF16 精度下，Prefill 阶段（计算密集）的理论峰值算力为 989 TFLOPS (FP16/BF16 无稀疏)。对于 27B 模型，Prefill 单 token 计算量约为 54 GFLOPS，理论最大 Prefill 吞吐量为 989,000 GFLOPS / 54 GFLOPS/token ≈ 18,314 tokens/s。实际受限于内存带宽和调度开销，实测 Prefill 吞吐量通常在 3000-5000 tokens/s 之间，N166 的 3000-4000 tokens/s 处于保守区间。

## Corrected Claim

H100 SXM 在 BF16 精度下，Prefill 阶段（计算密集）的理论峰值算力为 989 TFLOPS (FP16/BF16 无稀疏)。对于 27B 模型，Prefill 单 token 计算量约为 54 GFLOPS，理论最大 Prefill 吞吐量为 989,000 GFLOPS / 54 GFLOPS/token ≈ 18,314 tokens/s。实际受限于内存带宽和调度开销，实测 Prefill 吞吐量通常在 3000-5000 tokens/s 之间，N166 的 3000-4000 tokens/s 处于保守区间。

## Evidence

先验知识/题面给定，逻辑校验通过：H100 SXM BF16 峰值算力 989 TFLOPS 符合 NVIDIA 官方规格；27B 模型 Prefill 单 token 计算量约 2*27G=54 GFLOPS 符合线性层计算量估算逻辑；理论吞吐 989000/54≈18314 tokens/s 计算正确；实际吞吐受限于内存带宽和调度，3000-5000 tokens/s 处于合理工程经验区间。

## Search Query

H100 BF16 prefill throughput tokens per second 27B model
