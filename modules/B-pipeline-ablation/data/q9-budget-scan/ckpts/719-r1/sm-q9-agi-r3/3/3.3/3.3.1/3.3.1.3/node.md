# N194: MTP 加速比的实际测量：在 V100 上运行 100 次 1024-token 生成任务，对比开启与关闭 MTPx4 的总耗时，计算实际 Speedup，预期

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N55

## Claim

MTP 加速比的实际测量：在 V100 上运行 100 次 1024-token 生成任务，对比开启与关闭 MTPx4 的总耗时，计算实际 Speedup，预期 Speedup = 1.3 ± 0.1，若 < 1.2 则禁用 MTP 以减少开销。

## Corrected Claim

在 V100 上运行 1024-token 生成任务，对比开启与关闭 MTP 的总耗时，实测加速比通常在 1.5 倍左右（参考来源 [2]），若加速比低于 1.2 则建议禁用 MTP 以减少开销。

## Evidence

[质询]陈述中提到的 'MTPx4' 及具体的 'Speedup = 1.3 ± 0.1' 阈值缺乏来源直接支持。来源 [2] 提到的是 '1.5 倍' 加速，来源 [3] 显示不同配置下速度差异较大（如 50 vs 30 t/s，约 1.67 倍），且来源 [1] 主要讨论 Prefill 阶段而非 Decode 阶段的 MTP 加速比。此外，'MTPx4' 这一具体参数组合在提供的来源中未出现，可能是特定实验设定或笔误，导致该具体数值断言无法被现有证据完全证实。 | 来源 [2] 和 [3] 证实了 MTP 在 V100 上能带来显著加速（1.5x 左右），逻辑上支持 MTP 有效且加速比大于 1.2 的判断，但具体数值 '1.3 ± 0.1' 和 'MTPx4' 配置未被直接引用，属于经验事实且缺乏精确来源支持，故降级。

## Search Query

Qwen3.8-27B MTP speedup benchmark V100

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_31458015/article/details/162136299&rut=68e2b14b6dfe84f4bba6a31824bb7ccdcb896190d478360f174dff3bad94534d', 'type': 'ddg', 'title': 'V100跑Qwen3.6实测：MTP预填充并行化大幅提升首token速度'}
- {'url': 'https://blog.csdn.net/shen12138/article/details/160983251&rut=1e98159434119a499f370393b591059814e421c2da307d1da2670a379624a096', 'type': 'ddg', 'title': '使用 llama.cpp + MTP 分支实现 1.5 倍 Token 输出加速实战指南'}
- {'url': 'https://www.bilibili.com/en/video/BV1ZvLr6WE8h/&rut=e391f6689fa4a0d8838215b8d4d88544b3a0fadeec125995f589065323d007a2', 'type': 'ddg', 'title': 'MTP 加速哪家强？1Cat-vLLM 1.0.0 对比 llama.cpp 输出速度实测'}
