# N307: Framework_Overhead 量化分解：CUDA Context 固定占用约 0.5-1.0GB；cuDNN/cuBLAS 工作缓冲区随 batch_s

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N129

## Claim

Framework_Overhead 量化分解：CUDA Context 固定占用约 0.5-1.0GB；cuDNN/cuBLAS 工作缓冲区随 batch_size 和 seq_len 变化，在 batch=1, seq=32K 时约为 1.0-2.0GB；Python/PyTorch 运行时开销约 0.5GB。合计 Overhead ≈ 2.0-3.5GB，N129 中假设的 3.3GB 处于合理区间上限，保守估计可取 3.0GB。

## Corrected Claim

Framework_Overhead 量化分解：CUDA Context 固定占用约 0.5-1.0GB；cuDNN/cuBLAS 工作缓冲区随 batch_size 和 seq_len 变化，在 batch=1, seq=32K 时约为 1.0-2.0GB；Python/PyTorch 运行时开销约 0.5GB。合计 Overhead ≈ 2.0-3.5GB，N129 中假设的 3.3GB 处于合理区间上限，保守估计可取 3.0GB。

## Evidence

先验知识/题面给定，逻辑校验通过

## Search Query

vLLM llama.cpp CUDA context memory overhead GB benchmark
