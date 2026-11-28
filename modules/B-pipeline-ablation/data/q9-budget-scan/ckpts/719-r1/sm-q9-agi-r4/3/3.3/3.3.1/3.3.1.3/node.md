# N194: MTP 加速比的实际测量：在 V100 上运行 100 次 1024-token 生成任务，对比开启与关闭 MTPx4 的总耗时，计算实际 Speedup，预期

- **status**: pending
- **level**: L4
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N55

## Claim

MTP 加速比的实际测量：在 V100 上运行 100 次 1024-token 生成任务，对比开启与关闭 MTPx4 的总耗时，计算实际 Speedup，预期 Speedup = 1.3 ± 0.1，若 < 1.2 则禁用 MTP 以减少开销。

## Corrected Claim

在 V100 上运行 1024-token 生成任务，对比开启与关闭 MTP 的总耗时，实测加速比通常在 1.5 倍左右（参考来源 [2]），若加速比低于 1.2 则建议禁用 MTP 以减少开销。

## Evidence

父节点级核验未通过：不完备, 有冗余（子节点本质上是同一实验在不同假设条件（接受率/负载）下的三个采样点，属于参数化变体而非独立正交维度；且未覆盖父节点中'运行100次统计'及'<1.2禁用'的具体执行逻辑。）

## Search Query

Qwen3.8-27B MTP speedup benchmark V100

## Retrieval Sources

- {'url': 'https://blog.csdn.net/weixin_31458015/article/details/162136299&rut=68e2b14b6dfe84f4bba6a31824bb7ccdcb896190d478360f174dff3bad94534d', 'type': 'ddg', 'title': 'V100跑Qwen3.6实测：MTP预填充并行化大幅提升首token速度'}
- {'url': 'https://blog.csdn.net/shen12138/article/details/160983251&rut=1e98159434119a499f370393b591059814e421c2da307d1da2670a379624a096', 'type': 'ddg', 'title': '使用 llama.cpp + MTP 分支实现 1.5 倍 Token 输出加速实战指南'}
- {'url': 'https://www.bilibili.com/en/video/BV1ZvLr6WE8h/&rut=e391f6689fa4a0d8838215b8d4d88544b3a0fadeec125995f589065323d007a2', 'type': 'ddg', 'title': 'MTP 加速哪家强？1Cat-vLLM 1.0.0 对比 llama.cpp 输出速度实测'}
