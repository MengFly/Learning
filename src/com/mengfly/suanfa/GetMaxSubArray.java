package com.mengfly.suanfa;

import com.mengfly.tools.Tools;

/**
 * 找到一个数组的最大子数组
 * 这个问题可以这样考虑：
 * 最大子数组无非有三种情况：
 * 1、最大子数组在这个数组中心点左半部分
 * 2、最大子数组在这个数组中心点右半部份
 * 3、最大子数组经过这个数组的中心点
 * 因此求解只需要比较这三种情况下面的最大子数组那个是最大的就求解出了数组的最大子数组
 * 而求解作伴部分的最大子数组和求解右半部份的最大子数组的求解和求解一个数组的最大子数组是同一类问题
 * 这就相当于把元问题分解为了两个和元问题相同的子问题和一个类似的子问题
 * 只需要将求解经过中心点的最大子数组就可以通过递归求解出一个数组的最大子数组
 * @author mengfei
 *
 */
public class GetMaxSubArray {

	/**
	 * 这个类是标志着最大子数组的类。
	 * @author mengfei
	 *
	 */
	static class Point {

		int maxSubArrayLeft;// 最大子数组左侧在初始数组中的位置
		int maxSubArrayRight;// 最大子数组右侧在初始数组右边的位置
		int sum;// 最大子数组所有元素的和

		//构造方法
		public Point(int maxSubArrayLeft, int maxSubArrayRight, int sum) {
			this.maxSubArrayLeft = maxSubArrayLeft;
			this.maxSubArrayRight = maxSubArrayRight;
			this.sum = sum;
		}

		//重写toString方法，便于调试
		@Override
		public String toString() {
			return "left:" + maxSubArrayLeft + "\n" + "right:" + maxSubArrayRight + "\n" + "sum:" + sum;
		}
	}

	/**
	 * 找出经过中心点的最大子数组
	 * 
	 * @param array
	 *            要查找的数组
	 * @param low
	 *            要查找的数组的左边位置
	 * @param mid
	 *            要查找的数组的中心位置
	 * @param high
	 *            要查找的数组的右边位置
	 * @return 返回一个标志最大子数组的Point
	 */
	private static Point findMaxCrossSubArray(int[] array, int low, int mid, int high) {
		// 获取最大子数组的左边位置
		int sum = 0;
		int maxLeft = mid;
		int leftSum = array[mid];
		//从右向左对元素依次相加，如果相加结果比之前相加的结果大，说明之前的位置还不是最大子数组的位置，记录位置
		for (int i = mid; i >= low; i--) {
			sum += array[i];
			if (sum > leftSum) {
				// 如果求和的值大于当前求和的最大值，就记录当前的位置
				leftSum = sum;
				maxLeft = i;
			}
		}

		// 获取最大子数组的右边位置
		sum = 0;// 对sum进行清零。进行右边的求和
		int maxRight = mid + 1;
		int rightSum = array[mid + 1];
		//从左向右对元素依次相加，如果相加结果比之前相加的结果大，说明之前的位置还不是最大子数组的位置，记录位置
		for (int i = mid + 1; i <= high; i++) {
			sum += array[i];
			if (sum > rightSum) {
				// 如果求和的值大于当前求和的最大值，就记录当前的位置
				rightSum = sum;
				maxRight = i;
			}
		}
		//返回经过中心点的最大子数组的表示类
		return new Point(maxLeft, maxRight, leftSum + rightSum);
	}

	/**
	 * 找到数组的最大子数组
	 * 
	 * @param array
	 *            要进行查找的数组
	 * @param low
	 *            要进行查找的左边位置
	 * @param high
	 *            要进行查找的右边位置
	 * @return 返回标志最大子数组的位置的Point类
	 */
	private static Point findMaxImumSubArray(int[] array, int low, int high) {
		if (high == low) {// 如果元素只有一个就直接返回
			return new Point(low, high, array[low]);
		} else {
			int mid = (int) ((low + high) / 2);// 获取中心点，向下取整
			// 递归获取左边数组的最大子数组
			Point leftMaxSubArrayPoint = findMaxImumSubArray(array, low, mid);
			// 递归获取右边数组的最大子数组
			Point rightMaxSubArrayPoint = findMaxImumSubArray(array, mid + 1, high);
			// 获取通过中心点的最大子数组
			Point crossMaxSubArrayPoint = findMaxCrossSubArray(array, low, mid, high);
			// System.out.println(crossMaxSubArrayPoint);
			// 对这三个子数组进行比较，那个大那个就是这个数组的最大子数组
			if (leftMaxSubArrayPoint.sum > rightMaxSubArrayPoint.sum
					&& leftMaxSubArrayPoint.sum > crossMaxSubArrayPoint.sum) {
				return leftMaxSubArrayPoint;
			} else if (rightMaxSubArrayPoint.sum > leftMaxSubArrayPoint.sum
					&& rightMaxSubArrayPoint.sum > crossMaxSubArrayPoint.sum) {
				return rightMaxSubArrayPoint;
			} else {
				return crossMaxSubArrayPoint;
			}
		}
	}

	/**
	 * 查找指定数组的最大子数组
	 * 
	 * @param array
	 *            要进行查找的数组
	 * @return 查找到的最大子数组
	 */
	public static int[] findMaxSubArray(int[] array) {
		return findMaxSubArray(array, 0, array.length - 1);
	}

	/**
	 * 查找指定数组的指定位置的最大子数组
	 * 
	 * @param array
	 *            要查找的子数组
	 * @param left
	 *            要进行查找的片段的左边位置
	 * @param right
	 *            要进行查找的片段的右边位置
	 * @return 最大子数组
	 */
	public static int[] findMaxSubArray(int[] array, int left, int right) {
		Point maxSubArrayPoint = findMaxImumSubArray(array, left, right);
		// System.out.println(maxSubArrayPoint);
		int[] subMaxArray = new int[maxSubArrayPoint.maxSubArrayRight - maxSubArrayPoint.maxSubArrayLeft + 1];
		for (int i = maxSubArrayPoint.maxSubArrayLeft, j = 0; i <= maxSubArrayPoint.maxSubArrayRight; i++, j++) {
			subMaxArray[j] = array[i];
		}
		return subMaxArray;
	}

	public static void main(String[] args) {
		int[] a = { 4, -1, 8, -2, -5, 7 };
		int[] max = findMaxSubArray(a, 0, a.length - 1);
		Tools.printA(max);
		
		int[] a2 = {8, 7, -9, 2, -7, 6, -5, 10};
		int[] max2 = findMaxSubArray(a2);
		Tools.printA(max2);
	}
}
