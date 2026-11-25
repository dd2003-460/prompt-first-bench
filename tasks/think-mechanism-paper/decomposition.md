# decomposition · think-mechanism-paper（2026-11-25）

## 分解树

```
think-mechanism-paper
├── T1 起草英文 LaTeX（subagent）
│   ├── 核心: 理解=压缩-解压往返无损不动点 D∘C=id
│   ├── 4 侧面: 预言力/微扰/适配度/主项锚定
│   ├── 2 推导: 基的选择(多分辨率基) + 两阶段压缩(选域→精化)
│   ├── 5 个可注入操作模板 T1-T5（含触发条件）
│   └── 7/7 推导一致性检验（标注=内部一致性，非外部验证）
├── T2 引用核验（Lead, terminal, arXiv API https）
├── T3 arena review 派发+回执（Lead, ego-browser）
├── T4 修订+重编译（subagent）
└── T5 时间戳锁+投稿（Lead, 等 D"投"）
```

## 正交性核对
- T1 产出=稿件（tex+md），T2 产出=引用回执 JSON，T3 产出=arena 报告归档，T4 产出=修订稿，T5 产出=分支+hash。互不重叠 ✓
- T2 依赖 T1（引用列表出自稿件）；T3 依赖 T1+T2（review 前引用必须干净，防 arena 打"编造引用"）；T4 依赖 T3 ✓ 串行合理

## 空缺清单
- [ ] 论文标题待定（起草时 sub 给 3 候选，Lead 定）
- [ ] 语料引用：D 的 claude.ai 会话是私人语料，论文里只能引用"匿名化后的结构特征"，不能贴原文 → 起草约束
- [ ] 撞车风险预判：conceptual framework 类论文 novelty 弱，arena Q1 大概率要求收窄 → 预收窄=操作协议(5 模板)+可检验预言，不 claim 机制发现
- [ ] 7/7 检验的 7 条假设列表在源文件 §检验节，起草时逐条保留原话对照

## 任务表

| # | 任务 | 执行 | 验收（一行） | 状态 |
|---|---|---|---|---|
| T1 | 起草英文 LaTeX | subagent | `draft/paper.tex` 编译 0 error + 8-15 页 + 数字映射表 `draft/number-trace.md` | **DONE**（r1 死于 27b 输出上限；r2 sa-0-b2c986a9 增量写入协议成功：paper.tex 476 行 + paper.pdf 8pp 0 err + number-trace 24 映射 + titles.md；Lead 独立复验：重编译 0 err/8pp/无 undefined/红线词 0/7-7 全限定/AI-use 在 §395） |
| T2 | 引用核验 | Lead | `receipts/citations-verify-*.json` 100% 有 URL | **DONE**（6 条实查：Newman 2005/Kaspschak 2020/Koh&Liang 2017/Daubechies 1988/Skalse 2022/Gallego 2025；抓到 1 条记忆伪造风险 Everitt 1811.07861=硬件仿真论文，已换真实文献；占位 cite 清零，最终重编译 0 err/0 undefined，commit e7c901ddc） |
| T3 | arena review | Lead | `arena-review-report-raw-*.md` 归档 + 抽验 ≥3 条 ID | **DONE**（回执核验：任务书 sha256 原样带回 ✓；paper blob sha1 cf4f5335 本地复算一致 ✓ 证明读了全文；Q1 六条 arXiv ID 抽验 6/6 真实且日期吻合 ✓。报告：`arena-review-report-raw-20261126.md` + `receipts/arena-review-receipt-verify-20261126.json`。判决：需修改后投 conf 0.7，top-3 修改=①Def1 非平凡性约束+全文 ≈id ②derivations 降级 ③worked example+最小 pilot；另 Q3c 两处越界表述、Q1 Chaitin 2006 必引、Q5b LLM 套壳观感） |
| T4a | 文本修订 | subagent | 修订稿编译 0 err + arena 修改①②④⑤⑥ 落地 + 红线词仍 0 | 待派发 |
| T4b | 最小 pilot | subagent | 5 prompt×27b before/after 结果表 + 机械审计分（checklist 出自模板本身） | **DONE**（round-2 正式，commit c704a6637：10/10 ok，A 3/5 vs B 5/5，raw 原始返回字节级一致，截断+窗口位置声明在位；Lead verify_t4b.py ALL PASS。round-1 被 00:47 Lead checkout 误伤丢盘，保留在 thinkmech-review df624a6bd 历史。sub 收尾撞 27b 重复循环报 failed，实际全交付） |
| T4c | pilot 填入论文 | → 并入 T4a M7 | pilot 分数表+解读+局限声明进 Protocol 节末 | 并入 T4a（T4b 数据在盘上后 T4a 直接填，省一轮派发） |
| T5 | 时间戳锁 | Lead | 孤儿分支 + SHA256SUMS 远程验证 200 | 等 D"投" |

## 关键源文件（sub 必读）
- `projects/AI-计算科学/D1-persona-align/memory/d-thinking-mechanism-first-principles-20261124.md`（核心框架，准则在上推论在下）
- `projects/AI-计算科学/D1-persona-align/memory/general-thinking-template-20261124.md`（5 模板 + 标杆语料路径）
- 标杆语料（只读结构特征，不贴原文）：`/Users/a1-6/WorkBuddy/AI对话抓取归档/data/ai_chats/corpus/claude/` 下 3 个 .md
- 模板参照（可靠写法先例）：`pfb/tasks/idea53-goal/`（audit-final / minimal-zero-cost-publication-decision / arena-review-receipt）

## claim 边界（起草硬约束）
1. 定位 = descriptive formalization + actionable protocol（描述性形式化 + 可注入操作协议）
2. 禁止 claim：人类/AI 思考机制的发现、认知科学结论、"这是思考的本质"
3. 允许 claim：该框架对 D 语料 7/7 内部一致（标注 internal consistency, not external validation）；5 模板可作为 agent prompt 注入（操作性声明，不 claim 有效性，有效性=pfb T2 实验待做）
4. 最近邻定位（起草时引用，T2 核验）：compression-as-understanding 类（Zipf/power law in cognition）、perturbation theory in ML、multiresolution analysis、active learning of specifications
