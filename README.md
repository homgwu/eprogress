# eprogress

[![PyPI](https://img.shields.io/badge/pypi-v1.0.4-blue.svg)](https://pypi.python.org/pypi?:action=display&name=eprogress&version=1.0.4)[![Hex.pm](https://img.shields.io/hexpm/l/plug.svg)](http://www.apache.org/licenses/) 

eprogress 是一个简单、易用的基于Python3的命令行(terminal)进度条库，可以自由选择使用单行显示、多行显示进度条或转圈加载方式，也可以混合使用。

> 作者：竹尘居士
>
> 博客：http://www.cnblogs.com/homg/p/7232540.html



## 示例 

- 单行进度条

  ![](https://github.com/homgwu/eprogress/blob/master/demo/images/progress_sample_line.gif?raw=true)

- 多行进度条

  ![](https://github.com/homgwu/eprogress/blob/master/demo/images/progress_sample_multi_line.gif?raw=true)

- 圆形加载

  ![](https://github.com/homgwu/eprogress/blob/master/demo/images/progress_sample_cicle.gif?raw=true)

- 混合显示

  ![](https://github.com/homgwu/eprogress/blob/master/demo/images/progress_sample_multi_mix.gif?raw=true)

## 特性

- 使用简单，实例化一个Progress对象，调用update方法即可刷新进度
- 不依赖任何第三方库。
- 可定制进度符号，title，显示宽度，个性化显示。
- 多行、单行显示进度、圆形转圈加载随意搭配。
- 多线程安全，可在多个线程中更新进度条。

## 安装

- pip

```sh
pip install eprogress
```

- easy_install

```sh
easy_install eprogress
```



## 使用方法

1. 导入`eprogress`

   ```python
   from eprogress import LineProgress, CircleProgress, MultiProgressManager
   ```

2. 实例化进度条对象，更新进度

   ```py
   # circle loading
      circle_progress = CircleProgress(title='circle loading')
      for i in range(1, 101):
      		circle_progress.update(i)
      		time.sleep(0.1)

   # line progress
           line_progress = LineProgress(title='line progress')
           for i in range(1, 101):
               line_progress.update(i)
               time.sleep(0.05)
   # multi line or circle loading progress
   progress_manager = MultiProgressManager()
   progress_manager.put(str(1001), LineProgress(total=100, title='1 thread'))
   progress_manager.put(str(1002), LineProgress(total=100, title='2 thread'))
   progress_manager.put(str(1003), LineProgress(total=100, title='3 thread'))
   progress_manager.put(str(1004), CircleProgress(title='4 thread'))

   ... ...

   progress_manager.update(key, progress)
   ```

   - 圆形加载条使用update(progress)实例方法进行刷新，只有当参数大于0时才会转动。

   - 线性进度条使包含4个可选参数：

     ```python
     @param total : 进度总数
     @param symbol : 进度条符号
     @param width : 进度条展示的长度
     @param title : 进度条前面展示的文字
     ```
     创建实例后调用update(progress)实例方法更新进度。

   - 多行进度显示使用MultiProgressManager类，实例化该类，调用put(key,progressBar)方法统一管理多个进度条，内部使用一个dict来收集进度条，多行显示的顺序为put的顺序。更新某个进度条时使用progressMangager的update(key,progress)方法，该key为put进度条时使用的key。

   - 无论是使用多行进度条混合还是使用单行进度条，都不用考虑多线程更新的问题，内部已用Lock()加锁。

   - 详细样例请看源码：[Sample源码](https://github.com/homgwu/eprogress/blob/master/demo/sample.py)

## 注意事项

- 请在Python3环境下使用。
- 请不要IDE的运行方式使用，需在终端(terminal)下使用。