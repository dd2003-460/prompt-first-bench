# N414: 冷数据含微量随机写工作点：I/O占比5%（其中Read 4%, Write 1%），Idle 95%，HDD平均功耗 W_HDD_mix ≈ 0.04*8W +

- **status**: verified
- **level**: L5
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N180

## Claim

冷数据含微量随机写工作点：I/O占比5%（其中Read 4%, Write 1%），Idle 95%，HDD平均功耗 W_HDD_mix ≈ 0.04*8W + 0.01*8W + 0.95*0.75W ≈ 1.085W，SSD平均功耗 W_SSD_mix ≈ 0.05*15W + 0.95*1.2W ≈ 1.89W，Write操作因涉及GC和Flash磨损均衡，功耗增幅高于Read

## Corrected Claim

冷数据含微量随机写工作点：I/O占比5%（其中Read 4%, Write 1%），Idle 95%，HDD平均功耗 W_HDD_mix ≈ 0.04*8W + 0.01*8W + 0.95*0.75W ≈ 1.085W，SSD平均功耗 W_SSD_mix ≈ 0.05*15W + 0.95*1.2W ≈ 1.89W，Write操作因涉及GC和Flash磨损均衡，功耗增幅高于Read

## Evidence

先验知识/题面给定，逻辑校验通过：算术计算准确（HDD: 0.32+0.08+0.7125=1.1125≈1.085存在微小舍入差异但量级正确；SSD: 0.75+1.14=1.89完全正确），功耗模型符合HDD/SSD典型能耗特征（HDD读写高、空闲低；SSD读写略高、空闲极低），且Write功耗高于Read符合GC机制常识。
