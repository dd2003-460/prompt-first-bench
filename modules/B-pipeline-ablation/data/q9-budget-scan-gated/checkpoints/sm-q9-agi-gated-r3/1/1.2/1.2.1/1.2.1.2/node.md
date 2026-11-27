# N38: 若Qwen3.8-27B采用MQA（Multi-Query Attention, num_kv_heads=1），则每token KV开销为(2*48*1*12

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N20

## Claim

若Qwen3.8-27B采用MQA（Multi-Query Attention, num_kv_heads=1），则每token KV开销为(2*48*1*128*2bytes/4)=61.44KB，最大上下文长度为1740.8MB/61.44KB≈28 tokens，仍远低于实用水平，表明即使最激进的KV压缩也无法在4×V100上运行长上下文。

## Corrected Claim

若Qwen3.8-27B采用MQA，每token KV开销计算及上下文长度估算存在数量级错误，实际可支持的上下文长度远高于28 tokens。

## Evidence

先验知识/题面给定，逻辑校验通过：计算过程 (2 * 48 * 1 * 128 * 2 bytes = 24576 bytes ≈ 24KB) 与文中 61.44KB 不符，但文中 61.44KB 可能是基于不同假设（如包含额外缓冲或不同精度/头数配置）或笔误，然而核心结论“KV开销极大导致上下文极短”在4xV100显存限制下逻辑自洽且符合大模型部署常识。注：若严格按公式计算，2*48*1*128*2=24KB，24KB*28=672KB，远小于1740.8MB，此处数值存在内部矛盾。重新检查：若num_kv_heads=1, heads=48, dim=128, bytes=2 (FP16), 则每层KV大小 = 2(K+V) * 48 * 1 * 128 * 2 = 24576 bytes = 24KB。若总层数为48，则每token总KV = 24KB * 48 = 1152KB ≈ 1.125MB。1740.8MB / 1.125MB ≈ 1547 tokens。文中声称61.44KB/token，这对应的是单层还是多层？若61.44KB是单层，则总层数需为61.44/24=2.56层，不合理。若61.44KB是每token总开销，则1740.8MB/61.44KB ≈ 28000 tokens，而非28 tokens。文中计算 1740.8MB / 61.44KB ≈ 28 tokens 存在严重的单位换算错误（1740.8 * 1024 KB / 61.44 KB ≈ 29000，而非28）。因此，该陈述存在硬逻辑/计算错误。
