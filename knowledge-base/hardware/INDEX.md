# 硬件知识库 INDEX

> origin: ai · 2026-11-19 · 服务 S5 管线 gpu 题（不再需要 webllm 查规格）
> 共 17 卡 / 19 版本（+6 卡 staging 待入，见文末——T53b 62 run 跑完前不入 corpus，保 run 同质性）
> 数据源：hw-survey-flashnext 报告 + gold-tree 候选扩展 + MFU 调研 + D1-gpu-research-2026/GPU-SPECS.md + NVIDIA 官网 + en.wikipedia.org 规格表
> 缺的字段标 null = [待核验]，不凭记忆补

| 卡 | 厂商 | 架构 | 版本数 | 文件 |
|---|---|---|---|---|
| RTX 3090 | NVIDIA | Ampere | 1 | rtx-3090.json |
| RTX 5070 Ti | NVIDIA | Blackwell | 1 | rtx-5070-ti.json |
| RTX 5090 | NVIDIA | Blackwell | 1 | rtx-5090.json |
| RX 9700 | AMD | RDNA4 | 1 | rx-9700.json |
| V100 SXM2 | NVIDIA | Volta | 1 | v100-sxm2.json |
| A100 | NVIDIA | Ampere | 2 | a100.json |
| H100 | NVIDIA | Hopper | 1 | h100.json |
| L40S | NVIDIA | Ada Lovelace | 1 | l40s.json |
| TPU v5p | Google | TPU | 1 | tpu-v5p.json |
| TPU v5e | Google | TPU | 1 | tpu-v5e.json |
| Groq LPU | Groq | SRAM | 1 | groq-lpu.json |
| Cerebras WSE-3 | Cerebras | SRAM | 1 | cerebras-wse-3.json |
| SambaNova RDU | SambaNova | SRAM+HBM2e | 1 | sambanova-rdu.json |
| Mac Studio M5 Ultra | Apple | Apple Silicon | 2 | mac-studio-m5-ultra.json |
| Mac Studio M5 Max | Apple | Apple Silicon | 1 | mac-studio-m5-max.json |
| DGX Spark GB10 | NVIDIA | Grace Blackwell | 1 | dgx-spark-gb10.json |
| Intel Arc Pro B70 | Intel | Battlemage | 1 | intel-arc-pro-b70.json |

## 字段说明

- `mem_gb`: 显存/内存容量 (GB)
- `mem_bw_tbps`: 显存/内存带宽 (TB/s)，null = [待核验]
- `flops_fp16_tflops`: FP16 峰值算力 (TFLOPs)，null = [待核验]
- `flops_int8_tops`: INT8 峰值算力 (TOPS)，null = [待核验]
- `tdp_w`: 热设计功耗 (W)，null = [待核验]
- `price_usd`: 价格 (USD)，字符串（含区间/多地区），null = [待核验]
- `source`: 数据出处（文件路径 + 章节）
- `conf`: 置信度 (0-1)
- `notes`: 备注（实测数据/限制/矛盾）

## 数据源

1. `experiments/stage-ablation/runs/hw-survey-flashnext/report.md` — 10 平台量化对比表（内存/带宽/decode t/s/价格/功耗）
2. `experiments/stage-ablation/runs/hw-survey-flashnext/loop-artifacts/stages/02-information-research/research.md` — 9 条检索记录（R9700 价格/radiance 成熟度/M5 Ultra 实测/RunPod 价格）
3. `bench/rubric-v3/ablation/gold-tree.md` — 候选硬件扩展（V100/TPU/Groq/Cerebras/SambaNova 的 FLOPs/带宽/显存）
4. `tasks/gpu-gold-tree-completion/research/mfu-microarch-decomposition.md` — NCU 指标名表 + A100/H100 HBM 带宽

## Staging（2026-11-20 扩 6 卡，T53b 62 run 跑完后 mv 进本目录）

> 为什么 staging：本地检索是每次 query 实时 grep corpus 目录，正在跑的 SM 会立刻吃到新文件
> → gpu 臂内早期/晚期 run 不对称，污染 formula/text Δ。数据已查证落盘，只等批次结束。
> 入目录时同步：表头 17→23 卡 + 表格补 6 行 + 验证 grep 命中（注意 top-8 截断问题，见下）。

| 卡 | 文件 (hardware-staging/) | 来源 | conf |
|---|---|---|---|
| RTX 4090 | rtx-4090.json | GPU-SPECS.md (②) + NVIDIA 官网 (①) | 0.85 |
| MI300X | mi300x.json | GPU-SPECS.md (②) | 0.8 |
| Mac Studio M3 Ultra | mac-studio-m3-ultra.json | GPU-SPECS.md (②) | 0.75 |
| T4 | t4.json | en.wikipedia.org NVIDIA_Tesla 规格表 (①) | 0.8 |
| L4 | l4.json | en.wikipedia.org NVIDIA_Tesla 规格表 (①) | 0.8 |
| MI250X | mi250x.json | 无可靠源，带宽/算力 null [待核验] | 0.4 |

**已知机制缺陷（入目录前必须修，否则扩了也捞不到）**：`_local_corpus_search` 用
`grep -rilE` 按目录序取前 8 文件，无相关性排序。通用词（TDP/HBM2e/RTX）命中所有卡文件，
目标卡被挤到 top-8 外。实测 6 类 query 只 4 类命中新卡。修法候选：grep 后按"query 词在
文件内出现次数"重排（最小改动，一条规则覆盖，不加新依赖）。