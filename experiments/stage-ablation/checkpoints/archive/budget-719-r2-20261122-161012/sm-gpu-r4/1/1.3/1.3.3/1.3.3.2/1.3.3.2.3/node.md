# N377: 安装 2 张 3.5 槽 GPU 在 Fractal Torrent 中的物理冲突检查项：第二张卡尾部与机箱前部 3 个 140mm 风扇位的最小净空距离需 ≥

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N157, N158, N159

## Claim

安装 2 张 3.5 槽 GPU 在 Fractal Torrent 中的物理冲突检查项：第二张卡尾部与机箱前部 3 个 140mm 风扇位的最小净空距离需 ≥ 5mm，若净空 < 5mm，则需移除前部风扇位 1 和 2，导致机箱总进风量减少约 40%（基于单风扇 80 CFM 估算）。

## Corrected Claim

安装 2 张 3.5 槽 GPU 在 Fractal Torrent 中的物理冲突检查项：第二张卡尾部与机箱前部 3 个 140mm 风扇位的最小净空距离需 ≥ 5mm（具体取决于GPU长度），若净空不足，需移除前部风扇位 1 和 2，导致机箱总进风量减少约 66.7%（基于单风扇 80 CFM 估算，2/3 风扇移除）。

## Evidence

[质询]数值量级与逻辑推导存在严重矛盾：移除2个风扇位（共160 CFM）相对于3个风扇位（共240 CFM）的总进风量，减少比例应为 160/240 ≈ 66.7%，而非陈述中的40%。此外，'5mm净空'作为硬性阈值缺乏通用标准支持，属于特定场景下的经验值，且未提供具体GPU型号，无法验证该物理冲突的普遍性。 | 经验事实，逻辑自洽但缺来源支持；且内部数值计算（40% vs 66.7%）存在明显逻辑错误，无法通过第一性原理推导得出该特定百分比，故降级。

## Search Query

Fractal Design Torrent 3.5 slot GPU clearance front fans conflict
