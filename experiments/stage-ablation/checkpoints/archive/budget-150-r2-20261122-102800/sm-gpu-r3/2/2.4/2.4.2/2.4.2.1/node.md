# N231: CUDA OOM 风险阈值量化：当剩余显存 < 5% 时，CUDA 内存分配器碎片化导致 OOM 概率从 <1% 上升至 >30%；具体而言，24 GB 卡运行

- **status**: degraded
- **level**: L4
- **source**: search
- **edge_type**: quotient
- **rework_count**: 1
- **parent_ids**: N84

## Claim

CUDA OOM 风险阈值量化：当剩余显存 < 5% 时，CUDA 内存分配器碎片化导致 OOM 概率从 <1% 上升至 >30%；具体而言，24 GB 卡运行 W4 (19.28 GB 需求) 余量 4.72 GB (24%)，OOM 风险 <1%；48 GB 卡运行 INT8 (33.86 GB 需求) 余量 14.14 GB (39%)，OOM 风险 <0.1%；64 GB 卡运行 BF16 (63.0 GB 需求) 余量 1.0 GB (1.6%)，OOM 风险 >50%，不可行。

## Corrected Claim

CUDA OOM风险与剩余显存比例及碎片化程度正相关。24 GB卡运行W4（余量24%）风险较低；48 GB卡运行INT8（余量39%）风险极低；64 GB卡运行BF16（余量1.6%）因余量过少且易受碎片化影响，OOM风险极高，通常不可行。

## Evidence

[质询]该陈述包含具体的经验性统计数值（如OOM概率从<1%升至>30%、>50%等），这些并非CUDA内存分配器的第一性原理或数学公理，而是依赖于具体硬件、驱动版本、分配策略及工作负载的经验数据。在无外部来源支持的情况下，无法验证这些具体概率阈值的准确性，属于典型的经验事实。 | 经验事实，逻辑自洽但缺来源支持。数值计算（如24-19.28=4.72）正确，但OOM概率的具体量化缺乏来源佐证，且不同场景下碎片化影响差异巨大，具体百分比不可靠。

## Search Query

CUDA OOM probability threshold remaining VRAM percentage memory fragmentation
