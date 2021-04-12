import numpy as np
import matplotlib.pyplot as plt

def draw(values):
    plt.rcParams['font.sans-serif'] = 'SimHei'

    plt.rcParams['axes.unicode_minus'] = False
 

    plt.style.use('seaborn-colorblind')
 
    feature = ['红色','绿色','黄色','白色','蓝色']
 
    # 设置每个数据点的显示位置，在雷达图上用角度表示
    angles=np.linspace(0, 2*np.pi,len(values), endpoint=False)
    
    # 拼接数据首尾，使图形中线条封闭
    values=np.concatenate((values,[values[0]]))
    angles=np.concatenate((angles,[angles[0]]))
   
    # 绘图
    fig=plt.figure()
    # 设置为极坐标格式
    ax = fig.add_subplot(111, polar=True)
    # 绘制折线图
    ax.plot(angles, values, 'o-', linewidth=2)
    # 填充颜色
    ax.fill(angles, values, alpha=0.25)
 
    # 设置图标上的角度划分刻度，为每个数据点处添加标签
    ax.set_thetagrids(angles * 180/np.pi, feature)
 
    # 设置雷达图的范围
    ax.set_ylim(0,5)
    # 添加标题
    plt.title('5种色系倾向')
    # 添加网格线
    ax.grid(True)
 
    plt.show()
