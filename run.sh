#!/bin/bash
git pull
PID_FILE="pid"       
LOG_FILE="log"      
CMD="uv run uvicorn app:app --host 0.0.0.0 --port 18080"

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

start_new_process() {
    nohup $CMD >> $LOG_FILE 2>&1 &
    echo $! > $PID_FILE
    echo "[$(date)] 启动新进程 PID: $(cat $PID_FILE)" | tee -a $LOG_FILE
}

kill_old_process
start_new_process
