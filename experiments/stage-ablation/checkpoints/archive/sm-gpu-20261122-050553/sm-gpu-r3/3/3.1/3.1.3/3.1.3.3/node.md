# N203: 若采用 Per-tensor 量化（无 Block-wise scale factor），FP8 权重严格为 1 byte/param，总占用 27.0 GB；

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N65

## Claim

若采用 Per-tensor 量化（无 Block-wise scale factor），FP8 权重严格为 1 byte/param，总占用 27.0 GB；但 Per-tensor 量化在 LLM 中易导致精度损失，vLLM 默认推荐 Block-wise，因此实际部署应按 27.84 GB 估算显存需求。

## Corrected Claim

若采用 Per-tensor 量化（无 Block-wise scale factor），FP8 权重严格为 1 byte/param，总占用 27.0 GB；但 Per-tensor 量化在 LLM 中易导致精度损失，vLLM 默认推荐 Block-wise，因此实际部署应按 27.84 GB 估算显存需求。

## Evidence

先验知识/题面给定，逻辑校验通过：FP8为8位浮点，Per-tensor量化下每参数1字节，27B参数对应27.0GB；Block-wise因额外存储scale factor导致显存略增（27.84GB），且vLLM等主流框架确实推荐Block-wise以平衡精度与显存，逻辑自洽且符合工程常识。
