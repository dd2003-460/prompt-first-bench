# subagent-injection-protocol — subagent 派发注入协议

**origin: ai** · 2026-11-16 · D指令："每次主模型说了啥就叫 subagent 看" + "只看某一段话最好"
配套：pfb-autonomy-v3 机制层；与 arena 任务书同一哲学——给问题，不给背景小说。

## 为什么只传片段
整段对话全灌有两个坏处：token 烧得快（subagent 预算有限）+ 噪声大（历史闲聊稀释当前指令）。
正确做法：只传最小必要片段。固定部分（persona/验收标准）传一次，动态部分（D 最新质疑原文 + 待核断言）派发前由 Lead 截取。

## 派发公式

```
dispatch_subagent(task):
  context =
    PERSONA_BLOCK        # ≤300字，绑定动作不绑空话
  + GOAL_ACCEPTANCE      # 验收标准原文
  + LAST_USER_CHALLENGE  # D 上一轮质疑的原文段落（Lead 截取）
  + SPECIFIC_CLAIM       # 要它证明/反驳的那一条断言
  → 要求输出: 结论 + 证据路径 + 置信度，不许只给观点
```

## PERSONA_BLOCK 初稿（条件触发式，≤300字）

你是独立核验者，不是助手。遇到以下情况必须停下质疑：
- 数字无出处（没有文件路径/运行记录）
- 单一来源、无交叉验证的结论
- 与已有 checkpoint/日志矛盾的表述
- 任务描述与实际数据不一致（如任务说 77 条，数据里是 80 条）
输出格式（必须）：
1. 结论（一句话，带置信度 0-1）
2. 证据（文件路径 + 字段名/行号）
3. 未能验证的部分（明说"未验证"，不猜）
禁止：无证据给观点；用"大概/可能"填充缺失数据。

## 截取规则
1. 只传最小必要片段：goal 验收标准 + D 最新质疑原文 + 待核的具体断言
2. 背景 ≤10 行，逐行问"删掉这行 subagent 还能独立回答吗？能→删"
3. 不传整段对话历史
4. subagent 无网络（AGENTS.md 硬规则）：需要在线信息由 Lead 代查写文件，subagent 读文件

## 实例 #1（2026-11-16 · soc pending 77 分类）
- GOAL_ACCEPTANCE：soc 臂 gate 要求 cov ≥ 0.898；当前 174/283=0.615；本地估算现实上限 230/283≈0.813
- SPECIFIC_CLAIM：「pending 77 中约 46 个是 knowledge/given 类可翻 verified」——证明或反驳这个数字
- 数据文件：experiments/stage-ablation/checkpoints/sm-soc-r1.json
- 交付物：experiments/stage-ablation/loop-artifacts/stages/arena-outsource/soc-pending77-subagent.md
- 交叉验证：与 core team 独立分类（soc-gap-team-20261116.md）对比，记录分歧点