# Judge v1.0：严格且不变的评测标准

> origin: ai · 2026-11-22 · 触发：D 指令"这次必须确定严格和不变的 judge 方式然后再开始具体规划和实验"
> 原则：全部不依赖 LLM 主观判断，same input → same output，可复现。

## 设计原则

1. **机械性**：每个指标都是确定性计算，不依赖 LLM 评分
2. **不变性**：阈值和权重在实验开始前冻结，实验过程中不调整
3. **可复现**：same input + same code → same output（vLLM 并发非确定性只影响模型输出，不影响 judge）
4. **覆盖性**：三层 judge 覆盖"对不对"（数值）、"全不全"（结构）、"准不准"（gold 匹配）

## 三层 Judge

### L-机械（数值正确性）

**覆盖**：有公式的节点（K7 数据：29/122 节点有公式，19 个 sympy 可解析）

**方法**：
1. 从模型输出节点中提取公式（sympy 解析）
2. 与 gold formula 对比（sympy.simplify(diff) == 0）
3. 数值匹配：模型输出数值 vs gold 数值，容差 10%（|model - gold| / |gold| < 0.10）

**指标**：
- `formula_correct`：bool，公式是否正确
- `numeric_correct`：bool，数值是否在容差内
- `mechanical_score`：(formula_correct + numeric_correct) / 2，有公式的节点取均值

**局限**：只覆盖有公式的节点（~24%），无公式的节点不参与此层评分。

### L-结构（树完整性）

**覆盖**：全部节点

**方法**：
1. 去重：相同文本的节点只计一次（精确匹配）
2. 计算去重后的树深度（max depth）
3. 计算去重后的节点总数
4. 计算分支因子（平均每个非叶节点的子节点数）
5. 与 gold tree 对比（gold：37 节点，depth 5）

**指标**：
- `depth`：去重后最大深度（0-1 归一化：depth / gold_depth）
- `node_count`：去重后节点总数
- `branching_factor`：平均分支因子
- `structure_score`：0.5 * (depth / gold_depth) + 0.5 * (min(node_count, gold_node_count) / gold_node_count)

**局限**：结构指标是"完整性"代理，不直接衡量"正确性"。一个结构完整但数值错误的树会得高分。

### L-覆盖（gold 匹配度）

**覆盖**：全部节点

**方法**：
1. 模型输出节点文本 → bge-m3 embedding（dim 1024, MPS）
2. gold tree 36 个 unit → bge-m3 embedding
3. 计算每个模型节点与每个 gold unit 的 cosine similarity
4. 匹配规则：cosine ≥ 0.80 → 匹配（一个 gold unit 最多被 3 个模型节点匹配，MAGNET_LIMIT=3）
5. 覆盖率 = 匹配的 gold unit 数 / 总 gold unit 数

**指标**：
- `coverage`：匹配的 gold unit 比例（0-1）
- `magnet_count`：超过 MAGNET_LIMIT 的 gold unit 数（诊断用）
- `coverage_score`：coverage（直接使用）

**阈值**：cosine ≥ 0.80 [待标定]——用 gold tree 的 36 个 unit 做 ROC 曲线标定（正例：同一 unit 的不同表述；负例：不同 unit）。当前 0.65 太松（confirmed precision 不够），0.80 是初始值。

**局限**：embedding 匹配是"语义相似度"，不是"正确性"。两个语义相近但数值错误的节点会被误判为匹配。这是 L-机械层要补的。

## 综合评分

`total_score = 0.4 * mechanical_score + 0.3 * structure_score + 0.3 * coverage_score`

权重 [待标定]——初始值 0.4/0.3/0.3，理由：数值正确性最重要（0.4），结构和覆盖同等重要（各 0.3）。后续用消融实验（去掉某层看分数变化）验证权重合理性。

## 可复现性保证

- 所有指标都是确定性计算（sympy、cosine、去重）
- 不依赖 LLM 评分（无 LLM judge）
- 阈值和权重在实验开始前冻结（本文件）
- vLLM 并发非确定性只影响模型输出（节点文本），不影响 judge 计算
- 同一模型输出 + 同一 judge 代码 → 同一分数（100% 可复现）

## 与旧 judge 的对比

| 维度 | 旧 judge（LLM judge） | 新 judge v1.0 |
|---|---|---|
| 数值正确性 | LLM 主观判断 | sympy 机械验证 |
| 结构完整性 | LLM 主观判断 | 去重后深度/节点数/分支因子 |
| gold 匹配 | embedding 0.65 阈值 | embedding 0.80 阈值 + MAGNET_LIMIT |
| 可复现性 | 低（LLM 有随机性） | 高（确定性计算） |
| 覆盖 | 全部节点 | 机械层只覆盖有公式节点（~24%） |

## 深层节点信息增益：文献定位（2026-11-22 arXiv 检索 3 轮，来源①）

D 的 idea："深层推理节点对瓶颈计算的信息增益可以用粗略模型计算"。检索结果：

| 论文 | 做了什么 | 与我们的关系 |
|---|---|---|
| **arXiv:2411.11984**（2024-11）Understanding CoT in LLMs through Information Theory | 信息论形式化 CoT，**量化每个推理步的信息增益**，识别贡献步 | 理论基础，**线性链**版本 |
| arXiv:2608.21883（2026-08）VIG | 视觉信息增益当 GRPO 奖励做 CoT 压缩 | 信息增益当优化信号的先例 |
| arXiv:2511.15886（2025-11）What Really Counts? | CoT 的 step/token 级 attribution（多语言） | attribution 方法可借鉴 |

**定位**：线性 step-level 信息增益已有工作（2411.11984 直接对应）；**树结构分支节点的条件信息增益没找到**（3 轮检索无命中，conf 0.6，检索有盲区）。→ **引用 + 推广，不是独立创新点**。Workshop 里放 discussion（理论 + 代理指标），full paper 再展开。风险：ICLR 2027 在审 4 篇 RSI 论文可能已做树级版本，读论文时重点核对。

## 待标定项

1. **cosine 阈值 0.80**：用 gold tree 36 unit 做 ROC 曲线标定
2. **权重 0.4/0.3/0.3**：用消融实验验证
3. **数值容差 10%**：用 gold tree 的数值分布标定（gold 数值的自然变异范围）

## 实验设计（基于 judge v1.0）

**补重复实验**：
- K7 的 5 个预算点（50/100/150/300/719），3→8-12 重复
- 用 checkpoint 前缀缓存节省成本（L1/L2 checkpoint 共享前缀）
- 每个 run 用 judge v1.0 评分
- 统计：效应大小、置信区间、p 值（配对 t 检验或 Wilcoxon 符号秩检验）

**统计功效**：
- SM vs 裸臂：gpu +0.105，如果标准差 ~0.05，每组需要 ~8-12 重复
- 预算扫描：5 个预算点，每个需要 ~8-12 重复
- 总计：~50-75 runs（当前 15 runs，需要 3-5 倍）
