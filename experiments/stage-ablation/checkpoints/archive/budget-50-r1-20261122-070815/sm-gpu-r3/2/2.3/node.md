# N14: INT8 精度下 Qwen3-27B 的质量损失通常略高于 FP8，需评估是否可接受，显存占用为 BF16 的一半

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N2

## Claim

INT8 精度下 Qwen3-27B 的质量损失通常略高于 FP8，需评估是否可接受，显存占用为 BF16 的一半

## Corrected Claim

INT8 精度下 Qwen3-27B 的显存占用为 BF16 的一半；其质量损失与 FP8 相比需根据具体任务评估，部分场景下 FP8 可能表现更优或相当。

## Evidence

[质询]来源[1]标题及摘要暗示在特定场景下FP8可能不如INT8（即INT8质量损失可能更小或相当），这与陈述中“INT8质量损失通常略高于FP8”的普遍性结论存在潜在冲突或至少表明该结论并非绝对，且来源主要讨论的是Qwen3.6-27B而非Qwen3-27B，存在版本混淆风险。 | 显存占用为BF16的一半符合INT8与BF16位宽对比的第一性原理（8bit vs 16bit）；但关于质量损失的具体比较，来源[1]标题暗示FP8在某些情况下表现不佳，未直接支持“INT8损失通常高于FP8”这一通用结论，且来源针对的是Qwen3.6-27B，属于间接且可能矛盾的证据，故降级。

## Search Query

Qwen3-27B INT8 quantization quality loss benchmark

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7633052620612977167/&rut=6570a6542b1d5f72eb607f31dbdb4326634d49905bfe3516b0982e43a7654057', 'type': 'ddg', 'title': 'Qwen3.6-27B量化大反转!FP8竟不如INT8，选模型必避的坑'}
