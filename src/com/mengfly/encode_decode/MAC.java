package com.mengfly.encode_decode;

import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;

import javax.crypto.Mac;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.binary.Hex;
import org.bouncycastle.crypto.digests.MD5Digest;
import org.bouncycastle.crypto.macs.HMac;
import org.bouncycastle.crypto.params.KeyParameter;

public class MAC {
	
	
	public static final String src = "I'm Learning HMAC";//消息
	
	public static final String miyao = "pyl";//消息密钥
	
	/**
	 * jdk实现Hmac算法
	 */
	public static void jdkHmacMD5() {
		try {
//			KeyGenerator generator = KeyGenerator.getInstance("HmacMD5");//初始化KeyGrnerator
//			SecretKey generateKey = generator.generateKey();//产生密钥
//			byte[] key = generateKey.getEncoded();//获得密钥
			
			byte[] key = null;
			try {
				key = Hex.decodeHex(new char[]{'a','a','a','a','a','a','a','a','a','a'});
			} catch (DecoderException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			//还原密钥：
			SecretKey restoreSecreKt = new SecretKeySpec(key, "HmacMD5");
			Mac mac = Mac.getInstance(restoreSecreKt.getAlgorithm());
			//初始化mac
			mac.init(restoreSecreKt);
			byte[] hmacMD5Bytes = mac.doFinal(src.getBytes());//执行摘要			
			System.out.println("jdkHmacMd5Str:" + Hex.encodeHexString(hmacMD5Bytes));
			
		} catch (NoSuchAlgorithmException | InvalidKeyException e) {
			e.printStackTrace();	
		}
	}
	
	/**
	 * bc实现HMacMD5加密
	 */
	public static void bcHmacMD5() {
		HMac hmac = new HMac(new MD5Digest());
		hmac.init(new KeyParameter(org.bouncycastle.util.encoders.Hex.decode("aaaaaaaaaa")));
		hmac.update(src.getBytes(), 0, src.getBytes().length);
		
		byte[] hmacBytes = new byte[hmac.getMacSize()];
		hmac.doFinal(hmacBytes, 0);
		System.out.println("bcHmacMD4Str:" + org.bouncycastle.util.encoders.Hex.toHexString(hmacBytes));
		
	}
	
	
	
	public static void main(String[] args) {
		jdkHmacMD5();
		bcHmacMD5();
	}

}
