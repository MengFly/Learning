package com.mengfly.tools;

public class Tools {
	
	public static  void printA(Object[] arr) {
		StringBuilder printSb = new StringBuilder("[");
		for(Object item : arr) {
			printSb.append(item.toString());
			printSb.append(",");
		}
		printSb.append("]", printSb.length()-1, printSb.length());
	}

	public static void printA(int[] a) {
		StringBuilder printSb = new StringBuilder("[");
		for(int item : a) {
			printSb.append(item);
			printSb.append(",");
		}
		printSb.append("]");
		System.out.println(printSb.toString());
	}

}
