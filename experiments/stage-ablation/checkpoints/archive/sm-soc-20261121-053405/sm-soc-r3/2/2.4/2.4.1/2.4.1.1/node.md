# N136: 成交周期 $T_{cycle}$ 的测量噪声 $\sigma_{T}$：定义为平台日志中“上架时间”到“成交时间”差值的标准差。由于人工操作延迟、时区差异及数据

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: stochastic
- **rework_count**: 0
- **parent_ids**: N44

## Claim

成交周期 $T_{cycle}$ 的测量噪声 $\sigma_{T}$：定义为平台日志中“上架时间”到“成交时间”差值的标准差。由于人工操作延迟、时区差异及数据同步问题，$\sigma_{T}$ 通常包含系统误差。假设 $\sigma_{T} \approx 0.15 \times \mu_{T}$（即变异系数 15%），若平均成交周期 $\mu_{T} = 10$ 天，则 $\sigma_{T} \approx 1.5$ 天。

## Corrected Claim

成交周期 $T_{cycle}$ 的测量噪声 $\sigma_{T}$：定义为平台日志中“上架时间”到“成交时间”差值的标准差。由于人工操作延迟、时区差异及数据同步问题，$\sigma_{T}$ 通常包含系统误差。假设 $\sigma_{T} \approx 0.15 \times \mu_{T}$（即变异系数 15%），若平均成交周期 $\mu_{T} = 10$ 天，则 $\sigma_{T} \approx 1.5$ 天。

## Evidence

先验知识/题面给定，逻辑校验通过
