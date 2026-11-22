# N14: 模型权重显存占用计算：Weight_Size = Params × Bytes_per_param。BF16: 27B × 2 bytes = 54 GB; F

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N2

## Claim

模型权重显存占用计算：Weight_Size = Params × Bytes_per_param。BF16: 27B × 2 bytes = 54 GB; FP8: 27B × 1 byte = 27 GB; INT8: 27B × 1 byte = 27 GB; NVFP4: 27B × 0.5 bytes = 13.5 GB; W4 (INT4): 27B × 0.5 bytes = 13.5 GB。

## Corrected Claim

模型权重显存占用计算：Weight_Size = Params × Bytes_per_param。BF16: 27B × 2 bytes = 54 GB; FP8: 27B × 1 byte = 27 GB; INT8: 27B × 1 byte = 27 GB; NVFP4: 27B × 0.5 bytes = 13.5 GB; W4 (INT4): 27B × 0.5 bytes = 13.5 GB。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了 INT8 和 NVFP4 两种精度的额外开销细节，未覆盖父节点中提到的 BF16、FP8、W4 等其他精度情况，导致信息不完备。此外，INT8 和 NVFP4 的额外开销描述逻辑相似（均为量化参数+缩放因子开销），存在结构上的冗余，可抽象为通用量化开销模型。）
