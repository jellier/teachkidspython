# 第二课 Python会画画-画一个金灿灿的五角星

Hi,大家好，我是葫芦妈妈。上节课我们学习了画简单的几何图形，但都是黑白线条的，有点无聊。   

这节课我们要进一步学习turtle的绘图功能，画一个金灿灿的五角星，就像这样       
<div align="center">
<img src="pic/p-3-1.png" width="202" height="196" />
</div>

回忆一下上节课的代码，要先做准备工作，将turtle模块导入到程序中，然后将绘图工具交给变量t。

<table>
<tr>
<td>第一步，画图准备：</td>
<td>
<img src="pic/p-3-5.png" width="222" height="140" />
</td>
</tr>
</table>

如何画一个五角星呢？我们观察可以发现，五角星是由5个等腰三角形围在一起组成的，只要从其中的一个点开始，沿着每个三角形的外围依次描边，就能将五角星的轮廓勾勒出来。   
<div align="center">
<img src="pic/star.gif" width="233" height="228" />
</div>