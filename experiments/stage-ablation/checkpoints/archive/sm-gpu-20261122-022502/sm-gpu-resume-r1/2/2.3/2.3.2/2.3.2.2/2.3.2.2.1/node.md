# N620: 二手 H100 在 FP8 推理下的实际有效算力保留率约为 98%-100%，主要受限于 ECC 错误率导致的静默数据损坏风险而非硬件老化，需通过定期 CRC 

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N191, N192, N193

## Claim

二手 H100 在 FP8 推理下的实际有效算力保留率约为 98%-100%，主要受限于 ECC 错误率导致的静默数据损坏风险而非硬件老化，需通过定期 CRC 校验（每 24h 一次，耗时 <5min）确认无错误后方可维持全速运行。

## Corrected Claim

二手 H100 在 FP8 推理下的实际有效算力保留率通常较高，主要风险在于 ECC 错误导致的静默数据损坏，建议通过定期校验确认硬件健康状态以维持稳定运行。

## Evidence

[质询]该陈述包含具体的工程经验参数（如'98%-100%保留率'、'每24h一次CRC校验'、'耗时<5min'），这些属于特定硬件在特定运维策略下的经验事实，无法从第一性原理严格推导，且缺乏来源支持其具体数值和运维标准的准确性。 | 经验事实，逻辑自洽但缺来源支持

## Search Query

H100 FP8 inference performance degradation ECC error rate secondary market reliability
