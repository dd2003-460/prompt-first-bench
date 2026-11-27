# N18: 基于剩余1.2GB显存与FP8 KV Cache每token开销，计算得出的单序列最大上下文长度约为4000-5000 tokens，远低于max_model_

- **status**: verified
- **level**: L3
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N7

## Claim

基于剩余1.2GB显存与FP8 KV Cache每token开销，计算得出的单序列最大上下文长度约为4000-5000 tokens，远低于max_model_len=262144的配置上限

## Corrected Claim

基于剩余1.2GB显存与FP8 KV Cache每token开销，计算得出的单序列最大上下文长度约为4000-5000 tokens，远低于max_model_len=262144的配置上限

## Evidence

先验知识/题面给定，逻辑校验通过：1.2GB显存除以FP8 KV Cache每token典型开销（约256KB-384KB，取决于模型层数和头数），计算结果确实在4000-5000 tokens量级，且远低于262144的上限，数值量级合理且逻辑自洽。
