package com.mengfly.suanfa;

import com.mengfly.tools.Tools;

/**
 * 插入排序 依次从数组里面取出数值，依次和前面已经排好序的数值进行比较。 如果前面的数值比这个值大的话就向后移，知道前面的数不大于这个值为止。
 * 最后将这个值插入正确位置 其中i为当前正在比较的数值所在的初始位置 j为当前要和这个数值比较的数值的数所在的位置
 */
public class InsertSort {

	/**
	 * 这是升序的代码
	 */
	public void sort(int[] sortArray) {
		for (int i = 1; i < sortArray.length; i++) {
			int key = sortArray[i];// 取出当前要和前面的值比较的值
			int j = i - 1;// 获取第一个要比较的值的位置，为当前值的前一个位置
			while (j >= 0 && sortArray[j] > key) {
				// 如果比较的值比当前的值大的话，就把这个值向后移动
				sortArray[j + 1] = sortArray[j];
				j --;// 将位置向前移动，继续比较
			}
			// 此时的j的位置所在的元素比当前的值要小，最后将当前值插入到不比他大的值的后面
			sortArray[j + 1] = key;
			// 这样就完成了一个元素的插入
		}
	}

	public static void main(String[] args) {
		int[] a = { 1, 3, 4, 5, 6, 9, 8, 7, 0, 2 };
		new InsertSort().sort(a);
		Tools.printA(a);
	}

}
