# N375: Fractal Design Torrent 机箱内安装 2 张 3.5 槽 GPU 时，第二张卡（非 CPU 直连位）的风量衰减系数为 0.80-0.85（即

- **status**: degraded
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N157, N158, N159

## Claim

Fractal Design Torrent 机箱内安装 2 张 3.5 槽 GPU 时，第二张卡（非 CPU 直连位）的风量衰减系数为 0.80-0.85（即减少 15-20%），该系数直接用于修正第二张卡的稳态核心温度预测值。

## Corrected Claim

在 Fractal Design Torrent 机箱内安装 2 张 3.5 槽 GPU 时，第二张卡的风量衰减系数通常在 0.80-0.85 之间（即减少 15-20%），该系数可作为修正第二张卡稳态核心温度预测值的参考基准，但需根据具体风扇配置和GPU散热需求进行调整。

## Evidence

[质询]该衰减系数（0.80-0.85）为特定机箱、特定GPU尺寸及特定风扇配置下的经验测量值，并非普适物理常数；不同GPU厚度、风扇转速及机箱风道设计会导致该系数显著波动，直接作为固定系数用于预测缺乏普适性依据。 | 经验事实，逻辑自洽但缺来源支持（检索无可用来源，且该数值属于特定硬件组合的经验参数，无法从第一性原理严格推导，故降级）。

## Search Query

Fractal Design Torrent dual 3-slot GPU airflow reduction percentage
