# S10 Rubric v2 — 硬指标化修订（2026-11-07）

## 动机（为什么改）

Round 1 异族 judge 的 κ 诊断显示：M1/M2（硬维度）κ=1.0，M4/M5/M6（软维度）κ≤0.04。
根因不是 judge 不认真，而是**软维度的评分标准本身有歧义**——"什么算好的 gap coverage"没有可操作的判据，两个 judge 只能靠语感，语感必然不同步。

成璐指令：**软指标转化为硬指标 + 没要求的就不用管**。

转化原则：一个维度是"硬的"当且仅当它的判据可以写成**计数/匹配规则**，judge 不需要做主观质量判断。如果判据里出现"好的""充分的""高质量的"这类词，它就是软的，必须继续拆到能数为止。

## 修订后的维度表

| Dim | 旧定义（软） | 新定义（硬） | 计分方法 | judge 需要主观判断吗 |
|-----|-------------|-------------|---------|-------------------|
| M1 | Specificity: specific verifiable facts? | **数值断言命中率**：输出中每个带数字的断言（价格/参数/百分比），与 gold tree 对应叶子值比对，±10% 容差内算命中 | matched / total_numeric_claims | ❌ 纯比对 |
| M2 | Completeness: covers major sub-questions? | **gold 主干节点覆盖率**：gold tree 的 depth≤2 节点（主干），输出中语义覆盖的比例 | covered_trunk_nodes / total_trunk_nodes | ⚠️ 半硬（"语义覆盖"仍需判断，但对象集合固定） |
| M3 | Fabrication control: properly hedged? | **无源具体断言率**：输出中"具体数值+无来源标注"的断言占比。hedge 词（可能/大概/约）不计为来源。 | 1 - (unsourced_specifics / total_specifics) | ❌ 纯计数 |
| M4 | Gap coverage: identifies what it couldn't determine? | **显式缺口声明计数**：输出中符合以下任一模式的句子数：① "无法验证/查不到/未披露/黑盒" + 具体对象名；② "[待核验]" 标记；③ "conf ≤ X" + 原因说明。**只数指认了具体对象的，泛化 hedge 不算。** | min(count / 3, 1.0)（≥3 个即满分） | ❌ 模式匹配 |
| M5 | Source quality: relevant, authoritative? | **删除**（并入 M3）。理由：截断传输下 source 信息不完整，且"权威"是软判断。来源有无已由 M3 的 unsourced_specifics 捕获。 | — | — |
| M6 | URL validity: real working URLs? | **URL 存活率**（不变，本来就是硬的）：sources 列表中抽样 3 条 HEAD 请求，200 = alive | alive / sampled | ❌ 纯程序 |

### 总分公式（v2）

```
total = 0.35·M1 + 0.25·M2 + 0.25·M3 + 0.15·M4
```

M5 删除、M6 降权后并入 M3（无源断言率已隐含"你引用的东西存不存在"的问题）。
权重逻辑：M1（说对了吗）最重，M2（说全了吗）次之，M3（有没有瞎编）再次，M4（知不知道自己不知道）最轻——因为 M4 是元能力，重要但不是研究质量的第一性。

## 给 Judge 的新指令模板

```
你是研究质量评审。对以下模型输出按 4 个维度打分，每个维度的判据是【计数规则】，不需要你做质量判断。

M1 数值命中率：找出输出中所有带具体数字的断言（价格、参数、百分比、容量等）。
对照 gold 值逐条比对，±10% 容差内算命中。
score = 命中数 / 总断言数。没有数字断言则 score = null（不计入总分）。

M2 主干覆盖率：gold tree 的 depth≤2 节点共 N 个（已列出）。
判断输出是否覆盖了每个节点的主题（关键词匹配即可，不要求措辞相同）。
score = 覆盖数 / N。

M3 无源断言率：找出输出中所有"具体数值断言"。
检查每条是否有来源标注（URL、"据X论文"、"官方文档"、"conf X"）。
hedge 词（可能/大概/约/通常）不算来源。
score = 1 - 无源数 / 总数。没有数值断言则 score = 1.0。

M4 显式缺口声明：数输出中符合以下模式的句子：
(a) "无法验证/查不到/未披露/黑盒/不存在公开信息" + 紧跟具体对象名
(b) "[待核验]" 标记
(c) "conf ≤ 0.X" + 原因说明
泛化的不确定性表达（"可能在某范围""取决于..."）不算。
score = min(句数 / 3, 1.0)。

输出 JSON: {"M1": x.xx|null, "M2": x.xx, "M3": x.xx, "M4": x.xx,
            "m1_detail": "matched/total", "m3_detail": "sourced/total",
            "m4_sentences": [...]}
```

## 预期效果

- **κ 应该从 0.40 → 0.8+**：M1/M3/M4 变成计数题后，两个 judge 的差异只剩 M2 的"语义覆盖"判断（占权重 25%），整体一致性大幅提升。
- **A 臂的分数会变化**：自判时 A 臂 M3=1.0（因为短输出+hedge 多），v2 下 M3 按"无源具体断言率"算——A 臂如果有无源数字照样被扣分，虚假完整性不再得利。
- **论文表述更干净**：所有维度都有可复现的计分规则，reviewer 没法质疑"你的 M4 是怎么打出来的"。

## 迁移成本

- `score_s10.py` 需改：M3 逻辑重写（hedge_count → unsourced_specifics 计数）、M4 逻辑重写（judge LLM → 正则模式匹配）、删 M5、M6 降权。
- 异族 battle prompt 需重写为上面的新模板。
- 历史分数（self-judge round 1 + hetero round 1）不可直接对比——口径变了。标注为 rubric-v1 存档。