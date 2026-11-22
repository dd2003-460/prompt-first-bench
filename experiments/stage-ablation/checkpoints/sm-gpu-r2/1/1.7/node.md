# N13: 量化精度选择对显存占用的线性影响系数：不同精度下的 bytes/weight 值（BF16=2, FP8=1, INT8=1, NVFP4=0.5, W4=0.

- **status**: pending
- **level**: L2
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N1, N2, N3

## Claim

量化精度选择对显存占用的线性影响系数：不同精度下的 bytes/weight 值（BF16=2, FP8=1, INT8=1, NVFP4=0.5, W4=0.5），以及由此推导的显存节省比例

## Corrected Claim

量化精度选择对显存占用的线性影响系数：不同精度下的 bytes/weight 值（BF16=2, FP8=1, INT8=1, NVFP4=0.5, W4=0.5），以及由此推导的显存节省比例

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了 FP8 和 W4 两种精度，未涵盖父节点中提到的 NVFP4、INT8 等所有关键精度；且两个子节点本质上是同一计算逻辑（显存=参数量*精度字节数）在不同参数下的实例，属于冗余的枚举而非正交的概念分解。）

## Search Query

quantization precision bytes per weight BF16 FP8 INT8 NVFP4 W4
