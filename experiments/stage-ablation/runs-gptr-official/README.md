# gptr baseline 状态：9/9 检索失败，不可用（2026-11-19）

## 结论
9 个 run（3 题 × 3 rep）全部输出 "No sources were retrieved" 声明，无实质研究内容。
不能作为 baseline 使用。

## 根因链（来源：/tmp/gptr-official-3q.log + 本机 curl 验证）
1. 8787 qwen3.8-27b 对 gptr 的 JSON schema 遵循不稳定
   → 日志反复 `handle_json_error` / `Failed to decode JSON from regex extraction`
   → subtopic 分解失败，fallback 到原 query
2. arxiv retriever 拿到超长中文全文 query（整题塞进 search_query）
   → export.arxiv.org 返回 HTTP 500/503（本机 curl 验证：https 超时，http 301→https）
3. gptr arxiv retriever 无兜底检索（s5 有 ego-direct 兜底，gptr 没有）
   → 检索空 → 模型输出失败声明

## 缓存检测
3 rep 的 sha256 都不同（nat: 7202/d501/3d5f, soc: 51c4/546a/89e5, gpu: f858/f27a/d3e4）
但内容全是失败声明，差异来自模型对"没检索到"的随机措辞，不是 3 个独立研究样本。

## 修复方向（任务书：cc-tasks/gptr-retriever-fix.md）
- 给 gptr 注入自定义 retriever，复用 s5 检索层（arxiv 短 query + ego-direct 兜底 + 缓存）
- 或 query 预处理：8787 提取 3-5 个英文检索关键词，替代中文全文
- 重跑 9 run（等 8787 空闲，避免和 langgraph 资源竞争）

## 当前主实验臂
s5/langgraph（有完整检索兜底），gptr 降级为"检索层不可用"对照臂，待修复后重跑。
