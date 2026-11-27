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

父节点级核验未通过：不完备, 有冗余（子节点仅覆盖了FP8和W4两种情况，遗漏了父节点明确列出的INT8和NVFP4精度，导致不完备。此外，两个子节点结构高度相似（均为：精度->字节数->文件大小->节省比例），本质上属于同一逻辑模板在不同参数下的实例，存在结构性冗余，应合并为通用公式或参数表。）

## Search Query

quantization precision bytes per weight BF16 FP8 INT8 NVFP4 W4
