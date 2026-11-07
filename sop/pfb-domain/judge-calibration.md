# Judge 校准与评分规范

> origin: ai · 2026-11-07 · pfb 领域 SOP
> 为什么需要这份文件：pfb 的核心产出是"prompt A 比 prompt B 好 X 分"这个结论。如果 judge 本身不可靠，所有数字都是噪音。这份文件定义"什么样的 judge 结果可以对外说"，以及怎么操作 battle 通道拿到异族分数。

## 核心规则

**自判不对外。** 本地 27b（vLLM @127.0.0.1:8787）的评分只用于：
- 方向判断（哪个臂大概更好）
- 快速迭代（改 prompt 后看趋势）
- 调试（确认 pipeline 没跑崩）

任何要写进论文、发 arXiv、或对外宣称的数字，必须满足：
- ≥2 个不同模型家族的独立评分
- Fleiss' κ ≥ 0.6（judge 间一致性）
- M3 fabrication 维度单独锚定（round 1 发现这是分歧最大的维度）

## M1-M6 维度含义

| 维度 | 名称 | 测什么 | 注意 |
|------|------|--------|------|
| M1 | 事实准确率 | 输出中的具体数值/事实是否正确 | 需要 gold tree 对照 |
| M2 | 结构完整性 | 答案是否覆盖了问题的各个子方面 | 跟 M4 有重叠但侧重不同 |
| M3 | 不确定性标注 | 模型是否诚实标注了"我不确定" | **高分≠好**——短输出+大量hedge会得高分但内容空 |
| M4 | 缺口覆盖 | 对 gold tree 中叶子节点的覆盖程度 | **最大区分度来源**（S10 中 A vs B/C/D/E 差 0.5） |
| M5 | 诚实度 | 有没有编造不存在的事实/引用 | 需要 URL/数字 spot-check |
| M6 | URL 存活 | 引用的链接是否可访问 | 机械反馈臂常为 0（模型根本不引用） |

**为什么 M4 最重要**：它直接测量"模型有没有真正去查资料并用到"。M1 高但 M4 低 = 模型凭记忆答对了表面问题但没深挖。M4 高但 M1 低 = 模型查了但查错了。两个一起看才有信息量。

## 异族 Judge：Battle 通道操作

### 为什么用 battle 而不是直接调 API
lmarena.ai battle mode 给你两个匿名模型独立回答同一问题，投票后揭晓模型名。这天然解决了"上下文隔离"（两个模型互不可见）和"模型归因"（知道谁说了什么）。而且免费。

### 操作步骤

1. **准备盲打材料**：把评分任务书（含 rubric + 待评 run 文本）整理成一份 prompt。关键：去掉所有能暗示"正确答案"的信息，否则 judge 会偏向看起来像标准答案的输出。

2. **ego-browser 打开 lmarena.ai**（已登录 xyifeng81）：
   ```bash
   ego-browser open "https://lmarena.ai/chat"
   ```

3. **新建 chat，发送盲打材料**。两个匿名模型各自独立作答。

4. **投票**（选 A 好 / B 好 / 平局均可）。投票后页面揭晓双方真实模型名。
   - ⚠️ 不投票 = 白跑。不知道谁是谁，分数没法归因。
   - 自动化：发送/投票按钮用 ego-browser JS 事件派发；若触发失败，降级半手动（我准备材料，成璐点两下）。

5. **记录**：模型名 + 完整回答文本 → 落盘 `bench/rubric-v3/scorers/<date>-battle-<id>.json`
   ```json
   {
     "kind": "ralph_web_llm_cross_check",
     "channel": "lmarena-battle",
     "date": "2026-11-07",
     "models": ["model-a-name", "model-b-name"],
     "responses": [
       {"model": "model-a-name", "text": "完整回答原文（不是摘要）"},
       {"model": "model-b-name", "text": "完整回答原文"}
     ],
     "successful_provider_ids": ["model-a-name", "model-b-name"],
     "observed_at": "2026-11-07T14:30:00+08:00"
   }
   ```

6. **每轮新会话**（不污染上下文）。N 轮得 N×2 个模型家族的独立分数。

7. **收齐 ≥3 个不同家族后算 Fleiss'κ**。消费 `assert-kappa-receipt.py` schema。

### 要点
- 存原始回答全文，不是摘要——后续复算要用原文
- 同一份材料发多次 = 多个独立样本，但同一模型家族只取一次（防重复计数）
- 核对揭晓的模型名与记录一致；回答文本 sha256 入库

## Judge 校准 Round 1 结果（2026-11-07）

- 通道：lmarena battle（mistral-large-4-high + gemini-3.8-flash）
- κ = 0.70 → **PASS**（≥0.6 阈值）
- M3 fabrication 是分歧最大维度 → 需要单独锚定 rubric（[待做]）
- 校准材料：packet v2 三 run 评分任务书

## Conf Cap 规则

- 本地 27b 自判：conf cap = 0.7（不能声称比这更确定）
- 异族 judge：conf cap = 0.9（多源交叉验证后可以提高）
- 为什么 cap 存在：judge 也是 LLM，它的"信心"不等于"正确性"。cap 是承认这个局限性的方式。

## 常见错误

1. **用 Perplexity 单通道当异族 judge**：Perplexity 是单一服务，不算"不同家族"。cross_judge.py 用的就是 Perplexity，只能当参考不能当门禁。
2. **κ 没过就冻结数字**：κ < 0.6 说明 judge 之间意见不一致，此时算出的分数没有统计意义。
3. **M3 高分当好消息报**：M3 测的是"标不确定"的行为，不是"内容质量"。一个全是"我不确定"的输出 M3=1.0 但 M4=0.1。