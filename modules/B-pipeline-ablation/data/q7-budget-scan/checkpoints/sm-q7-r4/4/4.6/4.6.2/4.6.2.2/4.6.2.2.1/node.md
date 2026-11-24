# N501: SSD写缓存层带宽需求计算：为满足4小时内重建400TB数据，所需持续写入带宽 B_req = 400TB / 4h ≈ 27.8 GB/s。鉴于单块7.68T

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N219

## Claim

SSD写缓存层带宽需求计算：为满足4小时内重建400TB数据，所需持续写入带宽 B_req = 400TB / 4h ≈ 27.8 GB/s。鉴于单块7.68TB NVMe SSD受GC限制实际持续写带宽约为1.5-2.0 GB/s（修正N219中>3GB/s的乐观估计，参考N68），所需SSD数量 N_ssd_bw = ceil(27.8 / 1.5) ≈ 19块。

## Corrected Claim

SSD写缓存层带宽需求计算：为满足4小时内重建400TB数据，所需持续写入带宽 B_req = 400TB / 4h ≈ 27.8 GB/s。鉴于单块7.68TB NVMe SSD受GC限制实际持续写带宽约为1.5-2.0 GB/s（修正N219中>3GB/s的乐观估计，参考N68），所需SSD数量 N_ssd_bw = ceil(27.8 / 1.5) ≈ 19块。

## Evidence

先验知识/题面给定，逻辑校验通过：400TB/4h=27.8GB/s，27.8/1.5≈18.53，向上取整为19，计算无误且符合NVMe SSD持续写带宽的工程常识。

## Search Query

NVMe SSD sustained write bandwidth garbage collection overhead GB/s
