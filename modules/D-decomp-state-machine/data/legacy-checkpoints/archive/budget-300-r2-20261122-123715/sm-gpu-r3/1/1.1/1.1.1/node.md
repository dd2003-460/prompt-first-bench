# N28: RTX 4090 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache) + 2GB

- **status**: pending
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N5

## Claim

RTX 4090 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache) + 2GB(激活/框架) ≈ 20GB，小于 24GB 物理显存，无需 Offload，可完整驻留 GPU

## Corrected Claim

RTX 4090 单卡在 W4 量化下运行 Qwen3-27B 32K 上下文的显存占用为 13.5GB(权重) + 4.5GB(KV Cache) + 2GB(激活/框架) ≈ 20GB，小于 24GB 物理显存，无需 Offload，可完整驻留 GPU

## Evidence

父节点级核验未通过：非正交, 不完备（1. 正交性/一致性错误：子节点4存在严重的逻辑矛盾，FP8量化下权重本身已占用约27GB（27B参数 * 1Byte），加上KV Cache和激活，总显存远超33.5GB，且仅降低KV Cache无法解决权重超出的问题，结论错误。2. 完备性/范围错误：父节点仅描述W4量化下的显存占用及驻留情况，但子节点2、3、4、5引入了吞吐量计算、FP8量化对比、W8量化等父节点未涵盖的新维度，导致子节点集合超出了父节点的语义范围，不符合分解原则。）
