I'll start by examining the environment to understand what's available before executing the stage 02 workflow.

<tool_call>
<function=Bash>
<parameter=command>
which ralph; echo "---ralph exit: $?---"; which ego-browser; echo "---ego-browser exit: $?---"; echo "=== pwd ==="; pwd; echo "=== ls -la ==="; ls -la
</parameter>
<parameter=description>
Check for ralph and ego-browser executables and list working directory
</parameter>
</function>
</tool_call>