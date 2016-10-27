package com.mengfly.encode_decode;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.Security;

import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.digest.DigestUtils;
import org.bouncycastle.crypto.Digest;
import org.bouncycastle.crypto.digests.MD4Digest;
import org.bouncycastle.crypto.digests.MD5Digest;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class DMTest {
	
	private static String src = "I'm Learning MD";

	/**
	 * jdk实现MD5加密
	 */
	public static void jdkMD5() {
		try {
			MessageDigest md = MessageDigest.getInstance("MD5");
			byte[] md5Bytes = md.digest(src.getBytes());//通过digest进行加密
			//需要将byte数组转换成16进制
			System.out.println("JDK Md5:"+ Hex.encodeHexString(md5Bytes));
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * jdk实现MD2加密
	 */
	public static void jdkMD2() {
		try {
			MessageDigest md = MessageDigest.getInstance("MD2");
			byte[] md5Bytes = md.digest(src.getBytes());//通过digest进行加密
			//需要将byte数组转换成16进制
			System.out.println("JDK Md2:"+ Hex.encodeHexString(md5Bytes));
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}
		
	}
	
	/**
	 * bc实现MD4加密
	 */
	public static void bcMD4() {
		Digest digest = new MD4Digest();
		digest.update(src.getBytes(), 0, src.getBytes().length);
		byte[] md4Bytes = new byte[digest.getDigestSize()];
		digest.doFinal(md4Bytes, 0);
		//将bytes数组转换为16进制
		System.out.println("bcMD4:" + org.bouncycastle.util.encoders.Hex.toHexString(md4Bytes));
	}
	
	/**
	 * bc实现MD5加密
	 */
	public static void bcMD5() {
		Digest digest = new MD5Digest();
		digest.update(src.getBytes(), 0, src.getBytes().length);
		byte[] md5Bytes = new byte[digest.getDigestSize()];
		digest.doFinal(md5Bytes, 0);
		//将bytes数组转换为16进制
		System.out.println("bcMD5:" + org.bouncycastle.util.encoders.Hex.toHexString(md5Bytes));
	}
	
	/**
	 * 利用JDK提供的addProvider方法为JDK提供MD4算法
	 * 为JDK动态添加bc的Provider
	 */
	public static void bcMD4FromProvider() {
		Security.addProvider(new BouncyCastleProvider());//添加Provider，来支持算法
		try {
			MessageDigest md = MessageDigest.getInstance("MD4");//这时候就可以使用MD4了
			byte[] md4Bytes = md.digest(src.getBytes());//通过digest进行加密
			//需要将byte数组转换成16进制
			System.out.println("bc Md4:"+ org.bouncycastle.util.encoders.Hex.toHexString(md4Bytes));
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * cc实现MD5加密
	 * cc其实还是利用了JDK来实现的加密，只是简化了操作，因此它也没有提供MD4的加密算法
	 */
	public static void ccMD5() {
		byte[] md5Bytes = DigestUtils.getMd5Digest().digest(src.getBytes());
		System.out.println("cc MD5:" + Hex.encodeHexString(md5Bytes));
	}
	
	
	
	public static void main(String[] args) {
		jdkMD5();
		jdkMD2();
		bcMD4();
		bcMD5();
		bcMD4FromProvider();
		ccMD5();
	}

}
