# N883: INT4 权重 + BF16 KV Cache 场景下的显存占用：Memory_Weights_INT4 ≈ 14.34 GB (含校准开销，见 N278)。M

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N276, N277, N278

## Claim

INT4 权重 + BF16 KV Cache 场景下的显存占用：Memory_Weights_INT4 ≈ 14.34 GB (含校准开销，见 N278)。Memory_KV_BF16 = 2.01 GB。Memory_Activations ≈ 0.54 GB (假设 batch=1, 32K context, 激活值检查点启用)。Memory_Overhead ≈ 1.0 GB (CUDA 上下文、临时缓冲区等)。Total = 14.34 + 2.01 + 0.54 + 1.0 = 17.89 GB < 24 GB。结论：BF16 KV Cache 在单卡 4090 上可行，N32 中关于溢出的假设错误。

## Corrected Claim

INT4 权重 + BF16 KV Cache 场景下的显存占用：Memory_Weights_INT4 ≈ 14.34 GB (含校准开销，见 N278)。Memory_KV_BF16 = 2.01 GB。Memory_Activations ≈ 0.54 GB (假设 batch=1, 32K context, 激活值检查点启用)。Memory_Overhead ≈ 1.0 GB (CUDA 上下文、临时缓冲区等)。Total = 14.34 + 2.01 + 0.54 + 1.0 = 17.89 GB < 24 GB。结论：BF16 KV Cache 在单卡 4090 上可行，N32 中关于溢出的假设错误。

## Evidence

先验知识/题面给定，逻辑校验通过：各项显存占用数值量级合理（INT4权重14.34GB、BF16 KV Cache 2.01GB、激活值0.54GB、开销1.0GB），总和17.89GB小于24GB，结论自洽。
