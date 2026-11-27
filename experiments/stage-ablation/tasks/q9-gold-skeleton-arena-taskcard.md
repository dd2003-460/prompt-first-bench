# origin: ai · 2026-11-23 21:40 · D2 gold 骨架 arena 任务卡（待 D 确认 Q9 题面 v1 后派发）

> 状态: 已派发（2026-11-26 20:30，D 批准 APPROVALS#2，题面 v1 已冻结 @ 8a9c45bfa）。
> 派发通道: arena agent mode（ego-browser），SOP 见 .claude/skills/arena-outsource/SKILL.md。
> 拆法: 按 SOP 3a，拆 2 个 subagent（主调研 + 交叉验证），并行。

## 任务卡 A（主调研）

```
[任务] 为"research-AGI 预算控制"题面建 gold 骨架：完整覆盖 5 项贡献因子
（模型能力轴/预算轴/检索质量轴/记忆轴/自我认识闭环）的分解树，
回答"在 150 节点预算内，性价比最高、最快且可靠地让 AI 获得自我认识能力
（gap 标记→补全→post_acc 闭环）的路径分解是什么"。

[背景]
- 题面（已冻结 v1, D 2026-11-26 批准）: 本分支 experiments/stage-ablation/tasks/q9-agi-question-v0.md
  的「## 题面 v1」段（150 节点 / 5 因子清单 / 排序键 post_acc 三项已确认）
- 硬件: 4× V100-SXM2-16GB (cc 7.0, TP=4), Qwen3-27B NVFP4 vLLM,
  不改权重只用 prompt+外部工具, 预算 150 研究节点（定值）
- 排序键: 单位预算闭环成功率 = gap 标记→补全→补全后 verified/(verified+contradicted) 占比
  (metacog_axis post_acc; unverifiable/ambiguous 不进分母, 同 q9-agi-question-v0.md L44 口径)
- 记忆轴机制锚点（防调研发散）: pfb/research/q9-memory-axis-design-20261124.md
  题面"记忆轴（跨 session 状态保持）"有具体机制先例——DreamCoder/LILO 的
  跨 run claim 库（verified claim 抽取→相似度注入→省重新发现节点）。
  该文档给了 3 组件结构 + 2 臂第一实验设计 + P1 实测连接（rep 间 claim
  重叠仅 4.7% = 库机制直接攻击的浪费）。arena 调研记忆轴时以此为锚点，
  不是结论——gap 判断（开放 research 域无先例 conf 0.6）需 arena 独立核验。
- 参考格式: pfb/bench/rubric-v3/ablation/gold-tree.md（frozen ed552c4, 38 判定点格式）
- 三条硬规则（题面歧义审计结论, gold 必须遵守）:
  ① 每个参数定值或显式声明"模型自选且 gold 按模型选的值重算"
  ② 每个因子必须在题面可见（骨架结构/数值不泄露给被测模型）
  ③ 定稿后冻结, 改动需 D 确认

[约束] 中文; 每条结论标 conf(0-1); 给来源 URL; 不确定标"未验证";
  调研顺序: GitHub 开源实现 → arXiv/见刊 → 交叉验证 → 自己推

[交付] markdown 分解树: 根节点(排序键) → 5 因子分支 → 每因子 3-6 子节点,
  每节点一行: [因子] claim | 测量口径 | 来源 URL | conf
  另附: 因子间依赖/交互 1 张表（哪些因子互相耦合, 如预算轴×检索质量轴）

[长度] ≤50 行核心 + 附录
[落盘约束] 文件不存在=任务未完成
```

## 任务卡 B（交叉验证）

```
[任务] 独立回答任务卡 A 的同一问题（5 因子分解树），用于交叉验证门禁。
  不读任务卡 A 的交付物，独立调研后给同格式输出。
[背景] 同任务卡 A（题面/硬件/排序键/三条硬规则）
[约束] 同任务卡 A
[交付] 同任务卡 A 格式
[长度] ≤50 行
[落盘约束] 文件不存在=任务未完成
```

## 派发后

- 两卡交付 → Lead 对比矛盾点 → 交叉验证回执（≥2 successful_provider_ids）
- gold 骨架落 pfb/bench/rubric-v3/ablation/gold-Q9.md（格式同 gold-Q6.md）
- rubric 判定点 × 层级（D3）随 gold 一起出
- metacog_axis 在 Q9 上跑通（替换 TCO 题的测量对象）= ⑤ 子项完成判据

## 派发记录（Lead 追加）

- 卡 A：2026-11-26 20:30 派发（会话 01a217e1-361f-722e-a89e-50aa4f218b5c），20:53 完成；push 被沙箱无凭据阻断，patch 经 CAS API 拉回落盘 @ b47817a2d（2026-11-27）。
- 卡 B：2026-11-26 未派发（arena 搜索"任务卡 B"/"独立回答" 无匹配会话）；2026-11-27 16:05 重派（会话 `01a21c04-f223-7b8b-bb8a-9a191b6b1291`，HEAD `d92374e61`）。**等待中**：完成后 CAS API 拉 patch → `git am` 回收；核验 = 指纹 `c298969d...` 复算 + 29 叶对照 + 与 A 的分歧清单。

## 卡 B 派发说明（2026-11-27 重派用，agent 读本节）

[仓库] dd2003-460/prompt-first-bench，分支 thinkmech-review（HEAD 见派发 prompt 声明）。
[任务] 执行上文「任务卡 B（交叉验证）」：独立回答任务卡 A 的同一问题（5 因子分解树）。
  独立性要求（硬）：不读 experiments/stage-ablation/tasks/q9-gold-skeleton-A.md（卡 A 交付物，
  本分支上存在——禁止读取，读了即独立性失效）；背景/约束/交付格式以任务卡 A 段为准。
[交付] ① 文件 experiments/stage-ablation/tasks/q9-gold-skeleton-B.md（格式同任务卡 A 交付要求）
  ② git add + commit（作者 arena-agent <arena-agent@local>，subject 含 "Q9 D2: gold 骨架 B"）
  ③ 生成 git format-patch -1 > 0001-Q9-D2-gold-B-arena.patch 存 workspace 根目录
  （push 若无凭据被阻断属预期：不要重试 push、不要索要 token——patch 落盘即完成，Lead 拉回）
[回执] 对话末尾原样带回以下指纹 + commit sha + patch 文件名 + 交付文件行数：
  REPO=https://github.com/dd2003-460/prompt-first-bench BRANCH=thinkmech-review
  TASKCARD_SHA256=c298969d55a4778812407429051d029bf91ef05de2556ca5d30eb435a04f6669
  （自洽规则：本任务卡全文中所有含 "TASKCARD_SHA256=" 的行整行剔除后，剩余全文 sha256）
[核验纪律] 同任务卡 A：arXiv ID 逐个 abs 页核验、凭记忆 ID 被证伪要记录、
  论文自报数字标 [待交叉验证]、无法核验标「未验证」。
