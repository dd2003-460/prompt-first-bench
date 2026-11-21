# origin: ai
# 任务书：T-PR-16 对抗核验 + 滚雪球（约束组合×深树评测 novelty + 时间尺度 TCO 分解）
# 派发目标：arena 会话 01a1ca66-5358-7039-bcfa-b2fbf65a5a27（prompt-first-bench）
# 派发日期：2026-11-21

[任务] 两件事：(A) 对抗核验 pfb 的 novelty 声明；(B) 滚雪球调研"时间尺度分解 TCO × LLM 自主分解"是否有先例。

[背景]
pfb（prompt-first-bench）在做一个私有小规模 bench：3 题 × 2 臂（SM 状态机管线 vs 裸跑）× 10 轮，
用 gold 分解树（gpu 题 37 节点/深度 5/17 叶子）+ 38 判定点 rubric 打两个分：
coverage（对 gold 叶子的关键词命中）和 depth（每判定点 3-6 个深度档位，LLM judge 打 0-1 连续分）。
当前 novelty 声明（conf 0.8，本地调研结论）：
  "约束组合（正交/完备/依赖/压缩）× 深树 × 过程评测的交叉点是 2026 新兴空白；
   各子分支已分别验证约束（ICML 2026 OHD 2602.01969）、依赖（GPRM 2611.20755 开放问题）、
   完备性（Knossos 2610.04721）的独立价值，但无人组合进一个深树评测。"
本地已有调研（勿重复，作为你的起点）：
  modules/B-pipeline-ablation/research/process-depth-eval-survey-20261121.md（30+ 篇，三轮滚雪球）
  modules/B-pipeline-ablation/research/budget-sensitivity-goal-spec-survey-20261121.md（预算 tradeoff 空白区确认）

[A 对抗核验] 攻击上面 novelty 声明，找反例：
  A1. 有没有 2024-2026 论文同时用了 ≥2 个约束（正交/完备/依赖/压缩）+ 树结构 + 过程/深度判分？
      重点查 OpenReview（ICML/NeurIPS/ICLR 2025-2026）、ACL Anthology、arXiv。
      已知近邻：RPTS 2511.06899（树+逐节点 faithfulness）、OHD 2602.01969（正交分解+EM/judge）、
      SPRING 2609.34660（约束追踪+过程监督）、AgentAudit 2602.09341（推理树审计）。
      问：这些里有没有哪个其实已经"组合"了，我们的"无人组合"声明是否站不住？
  A2. "depth 作为一等指标 + 多档连续分（非二元）"有没有先例？ResearchRubrics 2511.07685 的
      logical nesting 轴是怎么操作化打分的（二元还是连续）？
  A3. 量级质疑：3 棵 gold 树 vs RPTS 390 棵，"差 2 量级"这个说法在评审眼里是否致命？
      有没有小规模（<50 实例）但被顶会接收的树结构评测先例？
  交付：每条给 verdict（站得住/站不住/部分站得住）+ 反例论文（arXiv ID + venue + 一句话证据）+ conf。

[B 滚雪球] 时间尺度分解 × TCO × LLM：
  B1. 有没有论文把 TCO/成本分解沿**时间轴**递归拆（瞬时成本 vs 长期成本 vs 价格波动/市场周期）？
      领域不限（HPC/云经济学/金融/供应链）。关键词方向：TCO + time horizon / price volatility /
      market cycle / depreciation curve / commodity cycle + GPU。
  B2. 有没有让 LLM **自主**产出带时间尺度的成本分解树（不是人建 gold 树让 LLM 填）？
  B3. GPU 价格波动/市场周期作为 TCO 决策变量，有没有量化研究（如"占空比假设差一倍结论翻转"
      这类敏感性分析在硬件采购决策里的先例）？
  交付：每条列论文（arXiv ID/venue + 一句话证据 + conf），没找到就明确说"未找到"并给检索记录。

[约束] 中文回答；每条结论标 conf(0-1)；给来源 URL；不确定标"未验证"；
  检索用 arXiv API / OpenReview API / ACL Anthology，不用付费渠道。
[交付] markdown：§A 对抗核验（3 条 verdict 表）+ §B 滚雪球（3 条结果表）+ §C 检索记录（可复现 query 列表）
[长度] ≤60 行核心 + 附录
[落盘约束] 文件不存在=任务未完成。交付物写到仓库 tasks/T-PR-16-result.md（你 checkout 的分支）。
[回执] 完成后回执必须含 repo URL + branch + commit_sha + 本任务书 sha256（防读旧版）。
