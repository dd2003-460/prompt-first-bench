# N215: 修正2x RTX 4090吞吐量估算：基于单卡实测22 tokens/s (N149)及PCIe多卡通信开销（通常导致效率降至1.2-1.5x而非2x），2x 

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: quotient
- **rework_count**: 0
- **parent_ids**: N70

## Claim

修正2x RTX 4090吞吐量估算：基于单卡实测22 tokens/s (N149)及PCIe多卡通信开销（通常导致效率降至1.2-1.5x而非2x），2x RTX 4090在INT8下的实际吞吐量应修正为26-33 tokens/s，而非N70假设的30-40 tokens/s；此修正将降低其性价比分子。

## Corrected Claim

修正2x RTX 4090吞吐量估算：基于单卡实测22 tokens/s (N149)及PCIe多卡通信开销（通常导致效率降至1.2-1.5x而非2x），2x RTX 4090在INT8下的实际吞吐量应修正为26-33 tokens/s，而非N70假设的30-40 tokens/s；此修正将降低其性价比分子。

## Evidence

先验知识/题面给定，逻辑校验通过：22 tokens/s 乘以 1.2-1.5 倍效率系数得出 26.4-33 tokens/s，计算准确且符合多卡通信开销的工程常识。

## Search Query

RTX 4090 dual GPU vLLM inference throughput overhead PCIe
