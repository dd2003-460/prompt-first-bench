# T-arena-autoresearch-20261117

> origin: ai（由 Hermes 生成，D 2026-11-17 触发）
> 目标仓库：https://github.com/dd2003-460/prompt-first-bench.git
> 目标分支：main（HEAD 1f474e69）
> 交付分支：arena/f65a5a27-prompt-first-bench（commit 后 push）
> 会话：arena.ai/agent/01a1ca66-5358-7039-bcfa-b2fbf65a5a27（taskSpace: tpr15-dispatch，绑定 pfb/main）
> 本任务只涉及 pfb 仓库，不涉及其他仓库。

## 背景

D 需要调研开源免费的 autoresearch 系统（AI 自主跑实验→提修改方案→应用优化的循环系统），要求：
1. 开源、免费
2. 稳定跑实验
3. 能提出修改方案
4. 能应用优化
5. 包含 Arena（LMArena）相关系统
6. 性能对比 + 优劣势分析

已初步调研（competitor-survey.md §6.7）：
- Arbor（Decentralised-AI/Arbor）：hypothesis tree + backpropagate + held-out margin + LiteLLM
- hugoferreira/autoresearch：falsifiable hypotheses + strict-mode firewall
- karpathy/autoresearch：单文件 + 固定预算 + eval 冻结

本任务要求 arena 做更深入的调研，补充：
1. 更多开源 autoresearch 系统（至少 5 个）
2. LMArena 相关的 autoresearch 系统（如果有）
3. 每个系统的性能数据（benchmark 分数、实验效率）
4. 优劣势对比表
5. 跟 pfb 的对比（pfb 是分解树+rework 机制的 deep research bench）

## 调研问题

### Q1：开源 autoresearch 系统全景

列出所有开源、免费、能自主跑实验→提修改方案→应用优化的 AI 系统（至少 5 个），每个系统给出：
- 名称 + GitHub URL + stars
- 核心机制（一句话）
- 实验循环（怎么跑实验、怎么提修改、怎么应用优化）
- 模型支持（支持哪些 LLM，是否支持本地模型）
- 隔离机制（实验怎么隔离，main 分支怎么保护）
- 验证机制（怎么验证改进是真实的，防过拟合）
- 性能数据（benchmark 分数、实验效率、成本）
- 优劣势（至少 3 个优势 + 3 个劣势）

已知系统（需补充细节）：
- Arbor（github.com/Decentralised-AI/Arbor）
- hugoferreira/autoresearch（github.com/hugoferreira/autoresearch）
- karpathy/autoresearch（github.com/karpathy/autoresearch）

需补充的系统（至少 2 个）：
- 其他开源 autoresearch 系统（搜索 GitHub "autoresearch" / "AI scientist" / "autonomous research agent"）

### Q2：LMArena 相关的 autoresearch 系统

LMArena（lmarena.ai）是否有相关的 autoresearch 系统？如果有：
- 系统名称 + URL
- 核心机制
- 跟 pfb 的关系（pfb 用 arena 做外包调研）
- 性能数据
- 优劣势

如果 LMArena 没有专门的 autoresearch 系统，说明原因，并列出 LMArena 生态中跟 autoresearch 最接近的系统。

### Q3：性能对比

所有调研到的系统，做一个性能对比表：
- 系统名称
- 适用场景（ML 训练 / 通用优化 / deep research / 其他）
- 模型支持（本地模型 / API / 混合）
- 实验效率（每小时实验数 / 每夜实验数）
- 成本（免费 / 付费 / 混合）
- 隔离机制（git worktree / 容器 / 无）
- 验证机制（held-out / bootstrap CI / 无）
- 防过拟合（有 / 无）
- 可复现性（源码公开 / 部分公开 / 不公开）
- 社区活跃度（stars / issues / 最近 commit）

### Q4：跟 pfb 的对比

pfb 的核心机制：
- 分解树（153 节点、6 顶层维度、cartesian/quotient 边）
- rework 机制（发现缺口→重新分解→再验证）
- judge 打分（同族自判，conf 上限 0.7）
- 本地模型（27b @ vLLM 127.0.0.1:8787）

对比维度：
- 假设管理（树 / 列表 / 无）
- 实验隔离（git worktree / 状态机内部 / 无）
- 验证机制（held-out / bootstrap CI / judge / 无）
- 教训传播（backpropagate / lesson layer / rework events / 无）
- 模型支持（任意 / 本地 / API）
- 可复现性（源码公开 / 部分公开 / 不公开）
- 适用场景（通用优化 / 现有系统优化 / deep research bench）

## 交付物

1. `experiments/stage-ablation/autoresearch-survey.md` — 完整调研报告
   - §1 开源 autoresearch 系统全景（至少 5 个系统，每个 300 字以上）
   - §2 LMArena 相关的 autoresearch 系统
   - §3 性能对比表
   - §4 跟 pfb 的对比
   - §5 结论 + 推荐（哪个系统最适合 pfb 的场景）

2. `experiments/stage-ablation/autoresearch-search-log.json` — 检索日志
   - 每条记录：query / source / result_count / top_results / observed_at
   - 至少 5 条独立检索

3. `experiments/stage-ablation/web-llm/autoresearch-crosscheck.json` — 网页 LLM 交叉验证回执
   - 至少 2 个独立 LLM 服务（Perplexity / DeepSeek / GLM 任选 2）
   - 每个服务：provider_id / response / observed_at
   - 矛盾点记录

## 验收标准

- [ ] 至少 5 个开源 autoresearch 系统（含 Arbor / hugoferreira / karpathy + 至少 2 个新发现）
- [ ] 每个系统有 GitHub URL + stars + 核心机制 + 性能数据 + 优劣势
- [ ] LMArena 相关的 autoresearch 系统已调研（有或无都说明）
- [ ] 性能对比表完整（至少 8 个维度）
- [ ] 跟 pfb 的对比完整（至少 7 个维度）
- [ ] 网页 LLM 交叉验证 ≥2 个独立服务
- [ ] 检索日志 ≥5 条独立检索
- [ ] 所有数字带出处（GitHub / arXiv / 官网）
- [ ] 落盘到 pfb 仓库 main 分支 + push 到 arena/f65a5a27-prompt-first-bench

## 约束

- 只用免费渠道（GitHub / arXiv / 官网 / 网页 LLM）
- 不调用付费 API
- 不修改 pfb 的核心代码（只加调研文档）
- 所有数字带出处，查不到标 [待核验]
- 交叉验证：关键结论 ≥2 个独立 LLM 服务

## 回执指纹

完成后回执须含：
- repo URL: https://github.com/dd2003-460/prompt-first-bench.git
- branch: arena/f65a5a27-prompt-first-bench
- commit_sha: <commit hash>
- 交付物文件列表 + 每个文件的行数
- 性能对比表的行数
- 网页 LLM 交叉验证的 provider_ids
