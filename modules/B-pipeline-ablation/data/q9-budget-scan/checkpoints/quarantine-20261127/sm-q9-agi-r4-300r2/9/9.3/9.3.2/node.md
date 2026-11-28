# N217: 并行化序列化收益边界：由于Python GIL限制，多线程并行序列化JSON对象的加速比S_parallel上限为1.0（即无加速）；若要突破此瓶颈需使用C++

- **status**: verified
- **level**: L4
- **source**: knowledge
- **edge_type**: cartesian
- **rework_count**: 0
- **parent_ids**: N84

## Claim

并行化序列化收益边界：由于Python GIL限制，多线程并行序列化JSON对象的加速比S_parallel上限为1.0（即无加速）；若要突破此瓶颈需使用C++扩展库（如ujson或orjson），其单线程速度为std json的5-10倍（~0.05-0.1ms/次），此时100步循环总开销降至5-10ms，进一步验证了原始结论中'可忽略不计'的稳健性。

## Corrected Claim

并行化序列化收益边界：由于Python GIL限制，多线程并行序列化JSON对象的加速比S_parallel上限为1.0（即无加速）；若要突破此瓶颈需使用C++扩展库（如ujson或orjson），其单线程速度为std json的5-10倍（~0.05-0.1ms/次），此时100步循环总开销降至5-10ms，进一步验证了原始结论中'可忽略不计'的稳健性。

## Evidence

先验知识/题面给定，逻辑校验通过：Python GIL确实限制了CPU密集型任务（如JSON序列化）的多线程加速比至约1.0；ujson/orjson作为C扩展库，其性能通常比标准库json快5-10倍，量级估算合理。
