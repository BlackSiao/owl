#!/bin/bash

# 第一个脚本参数设定城市
city=$1
curl wttr.in/${city}?lang=zh

