# N244: 工作点B（平衡/标准）：NVFP4量化，Group Size=64。Scale Factor开销为1 byte/64 params = 0.0156 bytes

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N94

## Claim

工作点B（平衡/标准）：NVFP4量化，Group Size=64。Scale Factor开销为1 byte/64 params = 0.0156 bytes/param。总权重显存 = 27e9 * (0.5 + 0.0156) ≈ 13.92 GB。相比N94基准13.69GB，增加0.23GB，精度略降，显存增加可控，适合大多数场景。

## Corrected Claim

工作点B（平衡/标准）：NVFP4量化，Group Size=64。Scale Factor开销为1 byte/64 params = 0.0156 bytes/param。总权重显存 = 27e9 * (0.5 + 0.0156) ≈ 13.92 GB。相比N94基准13.69GB，增加0.23GB，精度略降，显存增加可控，适合大多数场景。

## Evidence

先验知识/题面给定，逻辑校验通过：NVFP4为4-bit格式（0.5 bytes/param），Group Size=64且Scale Factor通常为8-bit（1 byte），开销计算 1/64=0.0156 bytes/param 正确；总显存 27e9 * 0.5156 ≈ 13.92 GB 计算无误；与基准对比逻辑自洽。
