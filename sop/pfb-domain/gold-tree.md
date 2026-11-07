# Gold Tree 构建规范

> origin: ai · 2026-11-07 · pfb 领域 SOP
> 为什么需要这份文件：gold tree 是评分的"标准答案"。它的质量直接决定 M4（缺口覆盖）和 M1（事实准确率）的可信度。gold 建错了，模型答对了反而被扣分——比不评分更糟。

## 什么是 Gold Tree

一棵树，节点是概念/子问题，叶子是**具体可验证的事实值**（数字、名称、公式）。

```
Q7: 存储分层架构成本优化
├── F1: 热/温/冷数据定义
│   ├── [leaf] 热数据: 访问频率 > X 次/天
│   └── [leaf] 冷数据: > 90 天未访问
├── F2: 各层介质与定价
│   ├── [leaf] HDD: $28/TB (Seagate 2026)
│   ├── [leaf] OSS 标准: ¥0.12/GB·月 (阿里云)
│   └── [leaf] SSD: $0.105/GB·月 (AWS gp3)
├── F3: 冗余与开销
│   ├── [leaf] EC 8+3 冗余因子 = 1.375
│   ├── [leaf] 元数据开销 ≈ 1.05×
│   └── [leaf] 保留水位 = 1.25×
└── F4: 迁移策略
    ├── [leaf] 生命周期规则触发条件
    └── [leaf] 恢复时间目标 (RTO)
```

**为什么叶子必须是具体值**："HDD 比较便宜"不是叶子——没法判对错。"$28/TB"是叶子——可以 grep 模型输出里有没有这个数字。M4 的 Jaccard 计算依赖叶子值的精确匹配。

## 构建流程

1. **调研**（先查后拆原则）：
   - arXiv 搜相关论文（方法/理论）
   - 厂商官网查具体数值（定价/规格）
   - ≥3 个独立源交叉验证关键数值
   - 记录来源 URL + 访问日期

2. **分解**：按正交子方面拆节点（不是按"重要性"排）
   - 正交性检查：两个节点的答案会不会重叠？会 → 合并或重新切分
   - 完整性检查：把所有叶子拼回去，能不能回答原始问题？漏了 → 补节点

3. **写 gold**：markdown 格式，每个 leaf 带来源标注
   ```markdown
   ## F2: 各层介质与定价
   - HDD 裸盘: **$28/TB** (Seagate Exos X 20TB, 2026 Q3 报价) [source: seagate.com/specs]
   - OSS 标准存储: **¥0.12/GB·月** (阿里云华东1) [source: aliyun.com/product/oss/pricing]
   ```

4. **验证**：
   - 叶子数 ≥ 15（太少 → 区分度不够，所有臂都能全覆盖）
   - 至少 5 个叶子是"非直觉值"（不是随便搜一下就能找到的常识）
   - 跟已有 Q1-Q5 gold 正交（不测同一个知识点）

## 当前 Gold 清单

| 文件 | 题 | 节点数 | 叶子数 | 状态 |
|------|---|--------|--------|------|
| `bench/rubric-v3/ablation/gold-Q1.md` | LLM 评估 | [待核验] | [待核验] | ✅ |
| `bench/rubric-v3/ablation/gold-Q2.md` | RAG | [待核验] | [待核验] | ✅ |
| `bench/rubric-v3/ablation/gold-Q3.md` | 事实性 | [待核验] | [待核验] | ✅ |
| `bench/rubric-v3/ablation/gold-Q4.md` | 对齐 | [待核验] | [待核验] | ✅ |
| `bench/rubric-v3/ablation/gold-Q5.md` | 多模态 | [待核验] | [待核验] | ✅ |
| `bench/rubric-v3/ablation/gold-Q6.md` | CDN/边缘 | 41 | 15 | ✅ (D-face) |
| `bench/rubric-v3/ablation/gold-Q7.md` | 存储分层 | 44 | 16 | ✅ (D-face) |
| Q8-Q10 | B1 新题 | — | — | 🔄 任务卡已写，gold 未建 |

## B1 新题模板

每道新题需要：
1. **question file**：`bench/questions/Q<N>-<topic>.txt`（问题描述 + 已知条件 + 要求）
2. **gold tree**：`bench/rubric-v3/ablation/gold-Q<N>.md`（按上面流程建）
3. **QUESTIONS 注册**：`ablation_harness.py` 的 QUESTIONS dict 加条目
4. **ARXIV_QUERIES**：`research_hook.py` 加搜索词
5. **KNOWN_SITES**（如适用）：验证过的商业站点 URL

**正交性检查**：新题的核心知识点不能跟 Q1-Q7 重叠。Q8（LLM benchmark 设计）、Q9（多模态架构 CLIP/SAM/GPT-4V）、Q10（RLHF pipeline）已确认正交。

## Jaccard 覆盖率计算

```python
def jaccard_coverage(output_text, gold_leaves):
    """
    gold_leaves: list of (value_string, context_keywords)
    对每个 leaf: output 中是否包含 value_string 或其等价表述
    coverage = hits / total_leaves
    """
```

**注意**：
- 数值匹配允许 ±1% 容差（$28 vs $28.00 算命中）
- 单位必须一致（$28/TB ≠ $28/GB）
- "约 1.375" 和 "1.375" 都算命中
- 纯关键词出现不算（必须出现在正确上下文中）——这是 judge_m4() 的工作

## 常见错误

1. **叶子太抽象**："需要考虑成本"不是叶子。"$28/TB"才是。
2. **来源单一**：一个数值只有一个 source → 如果那个 source 错了，gold 就错了。关键值 ≥2 源。
3. **时效性**：定价会变。gold 里标注访问日期，超过 6 个月重新验证。
4. **跟 prompt 耦合**：gold 不应该"恰好"匹配某个 prompt 的输出结构。它是独立于任何臂的标准答案。