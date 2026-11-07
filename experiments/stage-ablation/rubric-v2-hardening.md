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
| M5 | Source quality: relevant, authoritative? | **调研行为计数**（硬指标化）：① sources 字段非空；② 可解析 URL ≥3 条；③ 独立域名 ≥2 个（防刷源）。"权威"判断去掉——pfb 测的是"会不会调研"不是"引用品味"。 | min(①·0.3 + ②·0.4 + ③·0.3, 1.0) | ❌ 纯计数/程序 |
| M6 | URL validity: real working URLs? | **URL 存活率**（不变，本来就是硬的）：sources 列表中抽样 3 条 HEAD 请求，200 = alive | alive / sampled | ❌ 纯程序 |

### 总分公式（v2）

```
total = 0.30·M1 + 0.20·M2 + 0.20·M3 + 0.10·M4 + 0.10·M5 + 0.10·M6
```

权重逻辑：M1（说对了吗）最重，M2/M3（说全了吗/有没有瞎编）并列次之，M4/M5/M6（元能力/调研行为/引用真实性）各占 10%。
M5 回归的理由：pfb 的核心假设是"给模型调研工具能提升研究质量"——如果不评"它到底去没去查"，这个假设就测不到。M5 现在只数行为（查没查、查了几个独立源），不判断品味（引得好不好）。

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

M5 调研行为：检查 sources 字段和输出文本中的引用。
① sources 列表非空？(0/1)
② 可解析的完整 URL（http/https + 域名 + 路径）≥3 条？(0/1)
③ 这些 URL 来自 ≥2 个不同域名？(0/1)
score = 0.3·① + 0.4·② + 0.3·③。
注意：只数"有没有去查"，不判断来源权威与否。

M6 URL 存活：从 sources 中抽样 3 条 URL（不足 3 条则全取），
逐条做 HTTP HEAD 请求，状态码 200-399 = alive。
score = alive / sampled。无 URL 则 score = 0。

输出 JSON: {"M1": x.xx|null, "M2": x.xx, "M3": x.xx, "M4": x.xx, "M5": x.xx, "M6": x.xx,
            "m1_detail": "matched/total", "m3_detail": "sourced/total",
            "m4_sentences": [...], "m5_detail": "urls=N domains=M"}
```

## Sub 工具配置（实验设计层）

pfb 实验给被测 sub 的工具集 = **所有调研工具 − 抄答案通道**：

| 给 | 不给（抄答案） |
|---|---|
| ego-browser（登录态网页浏览） | gold tree 文件（bench/rubric-v3/ablation/gold-Q*.md） |
| arXiv API（论文检索） | 历史 run 输出（experiments/stage-ablation/s*-runs/） |
| web_fetch（纯 HTML 页提取） | 竞品调研笔记（competitor-survey.md） |
| terminal（跑代码验证数字） | 本 rubric 文件本身 |
| read_file / search_files（读工作区公开资料） | arena 任务书中的"关键叶子值示例"段 |
| multi-search-engine（必应/百度） | |

实现方式：sub 的 workspace 里 symlink 所有公开资料，但 gold/answer 类文件不放入其可见路径。
prompt 中明确告知："你可以使用浏览器、搜索引擎、arXiv API 等工具自由调研。你的 sources 字段必须列出实际访问过的来源。"

## 预期效果

- **κ 应该从 0.40 → 0.8+**：M1/M3/M4 变成计数题后，两个 judge 的差异只剩 M2 的"语义覆盖"判断（占权重 25%），整体一致性大幅提升。
- **A 臂的分数会变化**：自判时 A 臂 M3=1.0（因为短输出+hedge 多），v2 下 M3 按"无源具体断言率"算——A 臂如果有无源数字照样被扣分，虚假完整性不再得利。
- **论文表述更干净**：所有维度都有可复现的计分规则，reviewer 没法质疑"你的 M4 是怎么打出来的"。

## 迁移成本

- `score_s10.py` 需改：M3 逻辑重写（hedge_count → unsourced_specifics 计数）、M4 逻辑重写（judge LLM → 正则模式匹配）、M5 回归（sources 字段解析 + 域名去重计数）。
- 异族 battle prompt 需重写为上面的新模板。
- 历史分数（self-judge round 1 + hetero round 1）不可直接对比——口径变了。标注为 rubric-v1 存档。
- **S10 旧 run 的 M5/M6 = 0 是工具缺失导致的**（当时 sub 没有 ego-browser/搜索工具，自然没 sources）。v2 实验需要**带工具重跑**才有意义——这本身就是一个消融维度：S10-noTools vs S10-withTools。