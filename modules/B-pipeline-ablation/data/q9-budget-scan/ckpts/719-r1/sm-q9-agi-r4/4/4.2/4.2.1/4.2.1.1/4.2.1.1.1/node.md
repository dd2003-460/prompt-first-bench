# N588: Wikidata SPARQL 查询中，'高频三元组'的定义需量化为：在 Wikipedia 语料库（约 6000 万篇文章）中，Subject-Predica

- **status**: degraded
- **level**: L5
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N210

## Claim

Wikidata SPARQL 查询中，'高频三元组'的定义需量化为：在 Wikipedia 语料库（约 6000 万篇文章）中，Subject-Predicate-Object 三元组的共现频率 F_spo > 100 次；该阈值可通过预构建的倒排索引快速过滤，预计保留的三元组数量约为 Wikidata 总三元组（约 1.5 亿）的 5%-10%。

## Corrected Claim

在基于 Wikipedia 语料库的 Wikidata SPARQL 优化场景中，'高频三元组'通常定义为共现频率超过特定阈值（如 100 次）的 SPO 组合，具体阈值及保留比例（如 5%-10%）需根据实际语料库统计分布确定，非固定标准。

## Evidence

[质询]该陈述包含具体的经验性阈值（F_spo > 100）和预测比例（5%-10%），这些并非 Wikidata 或 SPARQL 的标准定义，而是特定研究或工程实践中的假设参数，缺乏通用标准支持，且具体数值高度依赖于语料库版本和过滤策略，极易出错。 | 参考来源 [1] 为军事飞机事故列表，与 Wikidata 数据查询完全无关，无可用外部证据；该陈述属于经验事实（具体参数值），逻辑上虽自洽（高频过滤通常保留少量数据），但缺乏来源直接支持，故降级。

## Search Query

Wikidata triple frequency threshold Wikipedia corpus co-occurrence

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/List_of_accidents_and_incidents_involving_military_aircraft_%281950%E2%80%931954%29', 'type': 'wikipedia', 'title': 'List of accidents and incidents involving military aircraft (1950–1954)'}
