#!/bin/bash
git pull
# 脚本参数配置（按需修改）
PID_FILE="pid"       # PID存储路径
LOG_FILE="log"       # 日志文件路径
CMD="uvicorn app:app --host 0.0.0.0 --port 18080"    # 需要执行的命令
VENV_PATH=".venv/bin/activate"
# 终止旧进程函数
kill_old_process() {
    if [[ -f $PID_FILE ]]; then
        local old_pid=$(cat $PID_FILE)
        if ps -p $old_pid > /dev/null 2>&1; then
            echo "[$(date)] 终止旧进程 PID: $old_pid" | tee -a $LOG_FILE
            kill -SIGTERM $old_pid && sleep 2
            if ps -p $old_pid > /dev/null 2>&1; then
                kill -SIGKILL $old_pid
                echo "[$(date)] 强制终止 PID: $old_pid" | tee -a $LOG_FILE
            fi
        fi
        rm -f $PID_FILE
    fi
}

# 启动新进程
start_new_process() {
    source $VENV_PATH 
    nohup $CMD >> $LOG_FILE 2>&1 &
    echo $! > $PID_FILE
    echo "[$(date)] 启动新进程 PID: $(cat $PID_FILE)" | tee -a $LOG_FILE
}

# 主流程
kill_old_process
start_new_process
