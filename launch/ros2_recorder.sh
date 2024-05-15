#!/bin/bash

#请这样使用：
# chmod +x ros2_recorder.sh
# bash ros2_recorder.sh (my_bag)
# ros2 bag play my_bag

#!/bin/bash
# 获取当前日期和时间，日期格式为 YYYY-MM-DD，时间格式为 HHMMSS
today=$(date +%Y-%m-%d)
current_time=$(date +%H.%M.%S)

# 检查是否有足够的参数传入
if [ $# -eq 0 ]; then
    # 如果没有提供输出目录，则使用默认目录
    output_directory=~/ros2_recorder/$today/$current_time
    echo "No output directory specified. Using default directory: $output_directory"
else
    output_directory=$1
fi

exclude_topics="(/rosout /parameter_events /_hidden_topics)"


# 循环直到发现非默认节点的主题
found_topics=0
while [ $found_topics -eq 0 ]; do
    # 获取所有主题
    all_topics=$(ros2 topic list)
    
    # 过滤主题
    topics_to_record=""
    for topic in $all_topics; do
        if [[ ! $exclude_topics =~ $topic ]]; then
            topics_to_record+=" $topic"
            found_topics=1
        fi
    done

    # 如果没有发现非默认节点的主题，等待一段时间后再次检查
    if [ $found_topics -eq 0 ]; then
        echo "No non-default topics found. Waiting..."
        sleep 1  # 等待1秒
    fi
done

echo "Recording topics: $topics_to_record"
# 记录过滤后的主题
ros2 bag record -o $output_directory $topics_to_record
