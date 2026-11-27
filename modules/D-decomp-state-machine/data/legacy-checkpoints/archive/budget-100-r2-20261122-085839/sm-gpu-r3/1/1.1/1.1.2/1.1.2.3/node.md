# N127: W4 量化下 Qwen3-27B 的总量化元数据（Scales + Zeros）显存占用 = (Total_Weights / Group_Size) * (B

- **status**: verified
- **level**: L4
- **source**: derived
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N33

## Claim

W4 量化下 Qwen3-27B 的总量化元数据（Scales + Zeros）显存占用 = (Total_Weights / Group_Size) * (Bytes_per_Scale + Bytes_per_Zero)。以 27.1B 参数、Group Size=128、FP16 元数据为例：(27.1e9 / 128) * 4 Bytes ≈ 846 MB ≈ 0.85 GB，占权重体积（13.55 GB）的约 6.3%。

## Corrected Claim

W4 量化下 Qwen3-27B 的总量化元数据（Scales + Zeros）显存占用 = (Total_Weights / Group_Size) * (Bytes_per_Scale + Bytes_per_Zero)。以 27.1B 参数、Group Size=128、FP16 元数据为例：(27.1e9 / 128) * 4 Bytes ≈ 846 MB ≈ 0.85 GB，占权重体积（13.55 GB）的约 6.3%。

## Evidence

逻辑推导成立，来源未直接覆盖
