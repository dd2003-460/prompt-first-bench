# N18: 引用准确性率：生成的参考文献需通过DOI解析与摘要匹配验证，准确性率需>95%才能达到可发表标准（预期幻觉引用率约3-5%，需通过外部API验证）

- **status**: degraded
- **level**: L2
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 1
- **parent_ids**: N3

## Claim

引用准确性率：生成的参考文献需通过DOI解析与摘要匹配验证，准确性率需>95%才能达到可发表标准（预期幻觉引用率约3-5%，需通过外部API验证）

## Corrected Claim

生成的参考文献需通过DOI解析与摘要匹配验证以消除幻觉引用（来源[1]指出虚构引用是LLM常见问题），具体可发表标准的准确性率阈值（如>95%）取决于特定期刊或项目的要求，并非通用固定值。

## Evidence

[质询]陈述中关于“准确性率需>95%”以及“预期幻觉引用率约3-5%”的具体数值阈值缺乏通用标准支持，属于特定项目或论文的经验性设定，而非行业公认的第一性原理或普遍事实。 | 来源[1]确认了LLM存在虚构引用（fabricated citations）及检测挑战，间接支持了需要验证的必要性，但未提供具体的95%阈值或3-5%幻觉率数据；作为经验事实，逻辑自洽但缺来源直接支持具体数值。

## Search Query

LLM citation hallucination rate DOI verification accuracy benchmark 2026

## Retrieval Sources

- {'url': 'https://en.wikipedia.org/wiki/Hallucination_%28artificial_intelligence%29', 'type': 'wikipedia', 'title': 'Hallucination (artificial intelligence)'}
- {'url': 'https://en.wikipedia.org/wiki/Large_language_model', 'type': 'wikipedia', 'title': 'Large language model'}
- {'url': 'https://en.wikipedia.org/wiki/Sycophancy_%28artificial_intelligence%29', 'type': 'wikipedia', 'title': 'Sycophancy (artificial intelligence)'}
