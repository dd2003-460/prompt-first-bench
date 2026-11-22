# N352: 首字延迟（Time to First Token, TTFT）是LLM交互中决定‘即时感’的核心指标，其感知阈值与总生成延迟不同；100ms阈值通常应用于TTF

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N122

## Claim

首字延迟（Time to First Token, TTFT）是LLM交互中决定‘即时感’的核心指标，其感知阈值与总生成延迟不同；100ms阈值通常应用于TTFT而非每1K tokens的生成速率（Time Per Output Token, TPOT），需区分两者在UX研究中的不同定义

## Corrected Claim

首字延迟（Time to First Token, TTFT）是LLM交互中决定‘即时感’的核心指标，其感知阈值与总生成延迟不同；100ms阈值通常应用于TTFT而非每1K tokens的生成速率（Time Per Output Token, TPOT），需区分两者在UX研究中的不同定义

## Evidence

先验知识/题面给定，逻辑校验通过：TTFT与TPOT定义区分明确，100ms作为TTFT感知阈值符合UX研究常识，无逻辑矛盾。
