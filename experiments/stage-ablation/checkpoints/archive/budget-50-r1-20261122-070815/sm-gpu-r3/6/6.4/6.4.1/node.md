# N369: INT4 权重显存占用 13.5 GB 的推导：27B 参数 * 0.5 bytes/param = 13.5 GB，此值假设所有参数均为 INT4 量化，未考

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N130

## Claim

INT4 权重显存占用 13.5 GB 的推导：27B 参数 * 0.5 bytes/param = 13.5 GB，此值假设所有参数均为 INT4 量化，未考虑 LayerNorm/Embedding 等保持 BF16 的部分（通常增加 0.5-1.0 GB）

## Corrected Claim

INT4 权重显存占用 13.5 GB 的推导：27B 参数 * 0.5 bytes/param = 13.5 GB，此值假设所有参数均为 INT4 量化，未考虑 LayerNorm/Embedding 等保持 BF16 的部分（通常增加 0.5-1.0 GB）

## Evidence

先验知识/题面给定，逻辑校验通过：27B参数 * 0.5 bytes/param = 13.5 GB 计算正确，且关于未量化部分（LayerNorm/Embedding）增加 0.5-1.0 GB 的估计符合工程常识（27B模型中非量化参数占比小，BF16下约0.5-1GB合理）。
