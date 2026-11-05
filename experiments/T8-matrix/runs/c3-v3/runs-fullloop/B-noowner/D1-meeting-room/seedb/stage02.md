我将开始执行阶段 02。首先按流程要求运行 `ralph prompt-first web-llm` 命令，围绕阶段 01 的空缺条件进行核验，并将真实回执写入工件。

<tool_call>
<function=Bash>
<parameter=command>
which ralph && ralph --version 2>&1 | head -5; echo "---EXIT: $?"
</parameter>
<parameter=description>
Check if ralph executable is installed
</parameter>
</function>
</tool_call>