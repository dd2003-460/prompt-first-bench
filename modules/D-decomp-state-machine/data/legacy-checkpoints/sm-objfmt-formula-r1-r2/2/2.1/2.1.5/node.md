# N58: W4 (INT4) 精度下 Qwen3-27B 的权重存储体积基础值为 13.49 GB，同样需增加 Group-wise Quantization 元数据开销

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N10, N11, N12

## Claim

W4 (INT4) 精度下 Qwen3-27B 的权重存储体积基础值为 13.49 GB，同样需增加 Group-wise Quantization 元数据开销（Scale/Zero-point），其占比与 INT8 类似但基数减半，实际总体积约为 14-15 GB

## Corrected Claim

W4 (INT4) 精度下 Qwen3-27B 的权重存储体积基础值为 13.49 GB，同样需增加 Group-wise Quantization 元数据开销（Scale/Zero-point），其占比与 INT8 类似但基数减半，实际总体积约为 14-15 GB

## Evidence

先验知识/题面给定，逻辑校验通过：Qwen3-27B参数量约27B，INT4基础体积约13.5GB，加上Group-wise量化元数据后总体积14-15GB符合工程常识与计算逻辑。
