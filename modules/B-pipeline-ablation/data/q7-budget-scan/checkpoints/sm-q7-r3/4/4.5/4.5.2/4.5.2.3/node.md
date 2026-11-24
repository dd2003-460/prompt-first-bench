# N272: 应用层一致性检查时间 T_check 不仅包含固定的 4h 基础检查，还需加上数据完整性校验时间 T_hash = Data_Size / Hash_Throu

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N87

## Claim

应用层一致性检查时间 T_check 不仅包含固定的 4h 基础检查，还需加上数据完整性校验时间 T_hash = Data_Size / Hash_Throughput；假设 500TB 数据哈希校验吞吐为 500 MB/s，T_hash = 500,000,000 MB / 500 MB/s = 1,000,000 秒 ≈ 278 小时；因此 T_check_realistic = 4h + 278h = 282h，原假设 4h 严重低估了大规模数据的一致性验证成本。

## Corrected Claim

应用层一致性检查时间 T_check 不仅包含固定的 4h 基础检查，还需加上数据完整性校验时间 T_hash = Data_Size / Hash_Throughput；假设 500TB 数据哈希校验吞吐为 500 MB/s，T_hash = 500,000,000 MB / 500 MB/s = 1,000,000 秒 ≈ 278 小时；因此 T_check_realistic = 4h + 278h = 282h，原假设 4h 严重低估了大规模数据的一致性验证成本。

## Evidence

先验知识/题面给定，逻辑校验通过：单位换算正确（500TB=500,000,000MB），除法运算正确（500,000,000/500=1,000,000s），时间转换正确（1,000,000s≈277.78h≈278h），加法正确（4+278=282h）。
