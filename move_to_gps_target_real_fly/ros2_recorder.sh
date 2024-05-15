#!/bin/bash

#请这样使用：
# chmod +x record_filtered_topics.sh
# ./record_filtered_topics.sh my_bag

# 检查是否有足够的参数传入
if [ $# -eq 0 ]; then
    echo "Usage: $0 <output_directory>"
    exit 1
fi

output_directory=$1
exclude_topics="(/rosout /parameter_events /_hidden_topics)"

# 获取所有主题
all_topics=$(ros2 topic list)

# 过滤主题
topics_to_record=""
for topic in $all_topics; do
    if [[ ! $exclude_topics =~ $topic ]]; then
        topics_to_record+=" $topic"
    fi
done

# 记录过滤后的主题
ros2 bag record -o $output_directory $topics_to_record
