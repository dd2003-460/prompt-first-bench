# N712: AWS p4d.24xlarge (8x H100 SXM) 2024年Q1-Q4 On-demand 价格稳定在 $32.77/hour，折算单卡小时成本为 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N292

## Claim

AWS p4d.24xlarge (8x H100 SXM) 2024年Q1-Q4 On-demand 价格稳定在 $32.77/hour，折算单卡小时成本为 $4.10/hour；该价格未包含数据传输费，且需扣除实例启动时间（约2-5分钟）对短任务有效利用率的影响（假设任务平均时长>10min，利用率修正系数≈0.95-1.0）。

## Corrected Claim

AWS p4d.24xlarge (8x A100 SXM) 2024年 On-demand 价格约为 $32.77/hour，折算单卡小时成本约为 $4.10/hour；该价格未包含数据传输费，且需考虑实例启动时间对短任务有效利用率的影响。

## Evidence

[质询]该陈述包含具体的经验性价格数据（$32.77/hour）和硬件配置细节（8x H100 SXM），属于经验事实。虽然 p4d.24xlarge 确实配备 8 张 A100 GPU（而非 H100，H100 通常对应 p5 系列实例），且 AWS 价格可能随时间或区域波动，但核心攻击点在于：缺乏外部来源支持具体数值，且硬件型号描述可能存在混淆（p4d 是 A100，p5 是 H100）。 | 经验事实，逻辑自洽但缺来源支持；且 p4d.24xlarge 通常搭载 A100 GPU 而非 H100，存在硬件型号描述错误的可能，但价格量级和计算逻辑（总价/8）在数学上自洽。

## Search Query

AWS p4d.24xlarge on-demand price 2024 H100 SXM per hour
