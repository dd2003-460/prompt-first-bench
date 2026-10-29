# origin: ai
# T8-可解释性研究 · 前沿文献调研（r51）
> 来源：arena agent mode 会话 `01a18567-c0e6-7f59-bb78-0fce9c18bd41`（2026-10-29）。
> 本文件为**基于调研汇报的结构化重建版**；307 行全文以 arena 会话 clone 内 `research/interpretability/literature-survey.md` 为准（待回 arena 取原文回填）。
> 纯文献调研，未跑实验、未改代码。

## 核心判定：我们的方法 vs 方向 2 成熟 interpretability 方法

**一句话："半重复"——重复的恰好是最站不住的那一半。**

1. **不是新问题**。context/component attribution 已有成熟问法与输出形态（PromptAnatomy、TokenSHAP、LAP、ContextCite 等），我们只是把打分函数换成了更弱的 `1−cos`。
2. **确有 gap，但是工程 gap 不是方法优势**：对"6–7 段流程 prompt 做组件级贡献归因"确实没有开箱工具（PromptAnatomy 目标是鲁棒性、TokenSHAP 是 token 级）。**缺工具，不缺原理。** conf 中。
3. **最接近的先例是 LAP（EMNLP 2025）**：hidden-space 距离确实与最坏情况性能下降相关——**但前提是语义等价改写**。我们的操作是删除语义内容，前提被破坏，`1−cos` 里混进了"被删内容的语义量"。candidate-freeze 最长 → 偏离度 0.454 很可能主要是**长度效应**（机制上确定存在，数据未验证）。
4. **另一个硬伤**：原始 5120 维向量上的 cos 受各向异性 + rogue dims 支配；owner-tag 0.428 vs evidence-url 0.421 差 0.007，**不能承载排序**。

### 该用什么替代（按推荐序）
| 方案 | 说明 | conf |
|---|---|---|
| ① 输出空间 logprob drop | 首选，直接测删除后目标 token 概率变化，是因果信号 | 低（llama.cpp 侧 logprobs 未实测） |
| ② ContextCite 式随机消融 + 稀疏线性代理 | 统计上更稳的归因 | 中 |
| ③ activation patching / causal tracing | **不推荐**：粒度不匹配、要改 llama.cpp 源码 | — |
| ④ 保留 `1−cos` | 只作"候选提出"，不作排序依据 | 中 |

## 给 C3 实验设计的 5 条修正（均含文献依据 + 改法 + 验收判据）

- **R1 · C1 加三道地板**：sham 偏离地板；`Spearman(偏离度, 删除token数)` > 0.7 则 top-k 作废（防长度效应）；z-score 后重算 + 多 seed CI（CI 重叠视为并列）。**"双证据链独立收敛"表述应删除。**
- **R2 · 重写 M8**：现行"未执行=权重 0"让该条目从分子分母同时消失＝把遗漏当不存在。改成预注册"核验机会集" + **M8-cover / M8-truth 联合判读**。（与我 r50 修正 4 一致，文献佐证。）
- **R3 · 分析单元改为 (题, 条目)**：配对差值 + 任务块聚类 SE，n 由 MDE 反推（当前 n=4 **确定性 underpowered**），Holm 校正。（与 r50 修正 2 一致并强化。）
- **R4 · 3 个单删 → 2³ 全因子 8 组测交互**：sham 改为 token-matched「连贯但任务无关」文本。
- **R5 · judge 校准前置为门禁**：换位双判 + Conflict Rate、家族隔离、CALM 扰动 Robustness Rate、κ≥0.6、长度相关检查。

## 低 conf / 未找到（完整登记见 arena 全文 §7）
- "prompt 组件消融现成工具"：**未找到**（不敢断言不存在，仅本轮渠道未覆盖中文/工业界实践）→ conf 中
- ContextCite 打败 semantic-similarity 基线：二手转述，未读原文表 → conf 低
- llama.cpp 是否暴露可用 logprobs：**未实测** → 替代方案①可行性存疑
- r47 数值是否主要由长度/rogue dims 驱动：机制确定、数据未验证
- 2026 年预印本（2607.07504 等）：仅引其设计模式，不引数值 → conf 低

## 一句话总结
**C3 不必推翻，但 R1/R2/R3 不做，跑出来的任何"显著"在文献标准下都站不住。**

## 下一步（待成璐确认方向）
1. 回 arena 取 307 行 survey 原文回填本文件
2. 实测 llama.cpp `/embedding` 或 chat 端点能否出 logprob（决定替代方案①可行性）
3. 按 R1-R5 重写 C3 方案 v3
4. 再派 arena 对抗核验 v3 → 通过后 ninfer :8000 直跑 paired runs