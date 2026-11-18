# 任务：LangGraph pfb 状态机验证

## 环境
- 工作目录：/Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
- Python：/Library/Developer/CommandLineTools/usr/bin/python3（3.9，langgraph + SqliteSaver）
- 模型：qwen3.8-27b @ http://127.0.0.1:8787/v1

## 执行命令
```bash
cd /Users/a1-6/Desktop/workspace/pfb/experiments/stage-ablation
rm -f /tmp/langgraph-pfb-full-*.sqlite*
/Library/Developer/CommandLineTools/usr/bin/python3 -u langgraph-pfb-full.py nat --max-nodes 12 --max-depth 2
/Library/Developer/CommandLineTools/usr/bin/python3 -u langgraph-pfb-full.py gpu --max-nodes 12 --max-depth 2
```

## 验收
- 两题各跑完（日志末尾有 `[LG:stop]` 或 `FINAL` 标记）
- 输出含 S_α 值 + verified 比例
- checkpoint sqlite 文件存在

## 注意
- 如果 arXiv API 502，等 30s 重试（脚本内置 retry）
- 单 run 预计 15-40 分钟
