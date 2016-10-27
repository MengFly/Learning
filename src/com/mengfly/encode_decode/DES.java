package com.mengfly.encode_decode;

import java.security.Key;
import java.security.Security;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESKeySpec;

import org.apache.commons.codec.binary.Hex;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

/**
 * DES算法简单用法
 * @author mengfei
 *
 */
public class DES {
	
	private static final String src = "I'm Learing DES";
	
	public static void jdkDES() {
		try {
			//生成密钥
			KeyGenerator keyGenerator = KeyGenerator.getInstance("DES");//获取DES的密钥
			keyGenerator.init(56);//设定keySize
			SecretKey secretKey = keyGenerator.generateKey();
			byte[] byteKey = secretKey.getEncoded();
			
			DESKeySpec desKeySpec = new DESKeySpec(byteKey);
			SecretKeyFactory factory = SecretKeyFactory.getInstance("DES");
			Key convertSecretKey = factory.generateSecret(desKeySpec);
			
			//加密
			Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");//设置工作方式和填充方式
			cipher.init(Cipher.ENCRYPT_MODE, convertSecretKey);//加密模式
			byte[] jdkDESBytes = cipher.doFinal(src.getBytes());
			System.out.println("jdkEncodeDESStr:" + Hex.encodeHexString(jdkDESBytes));
			
			//揭秘操作
			cipher.init(Cipher.DECRYPT_MODE, convertSecretKey);//解密模式
			byte[] decodeJdkDESBytes = cipher.doFinal(jdkDESBytes);
			System.out.println("jdkDecodeDESStr:" + new String(decodeJdkDESBytes));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	
	/**
	 * 两种方式：
	 * 1、通过添加Provider
	 * 2、通过调用BC的API
	 */
	public static void bcDES() {
		Security.addProvider(new BouncyCastleProvider());//添加Provider
		
		try {
			//生成密钥
			KeyGenerator keyGenerator = KeyGenerator.getInstance("DES","BC");//获取DES的密钥,指定使用BC的
			keyGenerator.init(56);//设定keySize
			SecretKey secretKey = keyGenerator.generateKey();
			byte[] byteKey = secretKey.getEncoded();
			
			DESKeySpec desKeySpec = new DESKeySpec(byteKey);
			SecretKeyFactory factory = SecretKeyFactory.getInstance("DES");
			Key convertSecretKey = factory.generateSecret(desKeySpec);
			
			//加密
			Cipher cipher = Cipher.getInstance("DES/ECB/PKCS5Padding");//设置工作方式和填充方式
			cipher.init(Cipher.ENCRYPT_MODE, convertSecretKey);//加密模式
			byte[] bcDESBytes = cipher.doFinal(src.getBytes());
			System.out.println("bcEncodeDESStr:" + Hex.encodeHexString(bcDESBytes));
			
			//揭秘操作
			cipher.init(Cipher.DECRYPT_MODE, convertSecretKey);//解密模式
			byte[] decodeBcDESBytes = cipher.doFinal(bcDESBytes);
			System.out.println("bcDecodeDESStr:" + new String(decodeBcDESBytes));
		} catch (Exception e) {
			e.printStackTrace();
		}
		
	}
	
	
	
	public static void main(String[] args) {
		jdkDES();
		bcDES();
	}

}
