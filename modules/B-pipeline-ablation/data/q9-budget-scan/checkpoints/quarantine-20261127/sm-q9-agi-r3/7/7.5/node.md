# N117: 知识图谱更新器模块的故障率 F_module5 定义为：F_module5 = (Corrupted_Entries / Total_Updates)，其中 C

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N30

## Claim

知识图谱更新器模块的故障率 F_module5 定义为：F_module5 = (Corrupted_Entries / Total_Updates)，其中 Corrupted_Entry 指向量数据库中嵌入向量与文本内容不匹配或索引损坏，需定期运行一致性检查脚本，比对随机抽样条目的嵌入余弦相似度与预期阈值，设定阈值 F_module5 <= 5% 作为达标条件。

## Corrected Claim

知识图谱更新器模块的故障率 F_module5 定义为：F_module5 = (Corrupted_Entries / Total_Updates)，其中 Corrupted_Entry 指向量数据库中嵌入向量与文本内容不匹配或索引损坏，需定期运行一致性检查脚本，比对随机抽样条目的嵌入余弦相似度与预期阈值，设定阈值 F_module5 <= 5% 作为达标条件。

## Evidence

先验知识/题面给定，逻辑校验通过
