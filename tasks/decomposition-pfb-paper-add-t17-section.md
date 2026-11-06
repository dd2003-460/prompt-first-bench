
## Stage 01: 五字段

### 1. 本地背景扫描

| # | 查什么 | 证据 |
|---|--------|------|
| B1 | §5.3 当前结构 | "The Arena Channel" 316w, char 33518-35417 |
| B2 | LoCoMo in refs? | YES (grep "Mao"/"LoCoMo" → True) |
| B3 | 当前字数 | 7197w (≤7200, 余量仅 3w) |
| B4 | Ref entries | 45 (numbered) |

### 2. 调研对象全集

**候选插入位置**:
- A: §5.3 末尾新增 "#### Memory Benchmark Validation" 子节 ✓ (选: 逻辑连贯, arena→local memory 是自然扩展)
- B: §5.4 Limitations 中提及 ✗ (不够突出, T17 是正面结果不是 limitation)
- C: 新 §5.6 ✗ (论文结构已定, 加新 section 影响大)

**排除项**: cross-conversation 数据 (conv1/2/3) — 未跑, 不能写入; 只能写 conv4 单点结果并标注 "preliminary"

### 3. 正交维度拆解

- **内容维度** (T17 数据 + 方法论关联): 加什么 ✓
- **字数维度** (trim 哪些段落腾空间): 减什么 ✓
- **引用维度** (in-text ↔ refs 一致): 对什么 ✓
- 完备性: 加+减+对 = 完整修改 ✓

### 4. 量化定义

- **插入增量**: Δwords = new_§5.3_words − 316 (目标 ≤250w 子节)
- **Trim 需求**: trim_needed = max(0, 7197 + Δwords − 7200)
- **最终约束**: wc -w ≤ 7200
- **一致性**: grep 所有 "(Author, Year)" → 每条在 References 有 entry

### 5. 任务书

本地执行 (写作任务, 不需 arena):
1. 写 T17 子节 (~200-250w): 数据表 + 方法论关联 + "preliminary" caveat
2. 插入 §5.3 末尾 (arena paragraph 之后)
3. wc -w → 若 >7200 则 trim §2.2/§2.4/§4.1 冗余句
4. grep 验证 in-text ↔ refs
5. commit + push

**失败降级**: 字数压不下来 → T17 子节压缩到 150w (只保留核心数据表+一句方法论关联)

### 6. 验收标准

| # | 指标 | 阈值 | 检查方法 |
|---|------|------|----------|
| A1 | T17 子节存在且 ≥150w | yes | grep "Memory Benchmark" + wc |
| A2 | 总字数 ≤7200w | yes | wc -w paper-draft.md |
| A3 | LoCoMo 引用存在 | yes | grep "Mao" references |
| A4 | 无缺失 refs | 0 missing | grep all citations vs refs |
| A5 | Push 成功 | yes | git push exit 0 |
