# Q4 · 数据处理架构（t17-generalization 域）

> 题面来源：`projects/decomp/bench/runs/t17-generalization/task-rag-vs-longctx.txt` 的任务段（原样）
> gold 锚点：`projects/decomp/bench/gold-rag-vs-longctx/tree.md`（26 节点 gold 树，根标量 ¢/1k_correct）

## 题面

我们有一个企业知识库问答系统，文档总量大概 50 万页，用户问题需要引用文档内容回答且不能编造。我在纠结三种架构：纯 RAG（切块嵌入检索）、纯长上下文（直接塞进 128K 模型）、或者混合方案。
请帮我拆解：决定「每千次正确回答的成本」的所有因素都有哪些，并判断哪种架构最划算。

## gold 要点（判分用，不进 prompt）

- 根标量：¢/1k_correct（每千次正确回答成本），正确 = 引用准确 + 无编造
- 结构指纹：候选=数据管道架构，叶子=信息流属性（召回/定位衰减/token 结构）
- 成本侧分裂：建设成本 vs 边际成本两类
- SHARED 参数：doc_scale（三路径耦合）；约束=文档规模划掉纯长 ctx
- 主导黑盒：检索召回 × 定位衰减（镜像双黑盒）