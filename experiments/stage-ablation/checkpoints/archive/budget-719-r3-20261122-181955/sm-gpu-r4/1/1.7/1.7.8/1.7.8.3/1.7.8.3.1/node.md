# N684: INT4 (AWQ/GPTQ) 量化中，Scale 和 Zero-point 的存储粒度通常为每 128 元素一个 FP16 Scale (2 bytes) 和

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N244

## Claim

INT4 (AWQ/GPTQ) 量化中，Scale 和 Zero-point 的存储粒度通常为每 128 元素一个 FP16 Scale (2 bytes) 和 FP16 Zero-point (2 bytes)，合计 4 bytes/128 elements；额外开销为 (27.16e9 / 128) * 4 bytes = 0.85 GB；总权重占用为 13.58 (INT4 主体) + 0.85 = 14.43 GB，而非 N244 估算的 13.87 GB（N244 假设了更紧凑的存储或不同的粒度）。

## Corrected Claim

INT4 (AWQ/GPTQ) 量化中，Scale 和 Zero-point 的存储粒度通常为每 128 元素一个 FP16 Scale (2 bytes) 和 FP16 Zero-point (2 bytes)，合计 4 bytes/128 elements；额外开销为 (27.16e9 / 128) * 4 bytes = 0.85 GB；总权重占用为 13.58 (INT4 主体) + 0.85 = 14.43 GB，而非 N244 估算的 13.87 GB（N244 假设了更紧凑的存储或不同的粒度）。

## Evidence

先验知识/题面给定，逻辑校验通过：AWQ/GPTQ 标准实现中 Scale/Zero-point 通常以 FP16 存储且粒度为 128 元素，计算 (27.16e9 / 128) * 4 bytes ≈ 0.85 GB 及总权重 14.43 GB 的推导在数学和工程惯例上均自洽。
