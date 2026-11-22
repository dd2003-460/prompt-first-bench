# N161: 修正N19/N12矛盾：Qwen3-27B在INT8精度下权重占用应为13.5GB（27B参数×1字节），N19中'INT8为27GB'为错误，INT8与FP8

- **status**: verified
- **level**: L3
- **source**: search
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N79

## Claim

修正N19/N12矛盾：Qwen3-27B在INT8精度下权重占用应为13.5GB（27B参数×1字节），N19中'INT8为27GB'为错误，INT8与FP8在位宽上均为8-bit，权重占用相同，均为13.5GB

## Corrected Claim

Qwen3-27B在INT8精度下权重占用应为27GB（27B参数×1字节），INT4精度下权重占用约为13.5GB。

## Evidence

逻辑推导成立：27B参数×1字节/参数=27GB（注意：此处需仔细检查计算，27 * 1 = 27，而非13.5。等等，27B是270亿参数。27,000,000,000 * 1 byte = 27,000,000,000 bytes = 27 GB。陈述中说'27B参数×1字节'应为13.5GB，这在数学上是错误的。27 * 1 = 27。除非它指的是27B是27 * 10^9，而13.5GB是27 * 0.5？不对。INT8是1字节。27B * 1B = 27GB。陈述声称是13.5GB，这是计算错误。但是，让我们再看一眼。27B通常指27 Billion。27 * 10^9 * 1 byte = 27 GB。如果陈述说INT8是13.5GB，那它可能混淆了FP16(2 bytes) -> 54GB, INT8(1 byte) -> 27GB, INT4(0.5 byte) -> 13.5GB。所以陈述中的数值13.5GB对应的是INT4，而不是INT8。因此，陈述中'INT8...权重占用应为13.5GB'是事实错误。

## Search Query

Qwen3-27B INT8 weight size GB

## Retrieval Sources

- {'url': 'https://www.toutiao.com/article/7633052620612977167/&rut=4afdd7bcd56c88ffb2140c8952498cd5c3fb1f5d4e10a21551b80ce996d3e88f', 'type': 'ddg', 'title': 'Qwen3.6-27B量化大反转!FP8竟不如INT8，选模型必避的坑'}
