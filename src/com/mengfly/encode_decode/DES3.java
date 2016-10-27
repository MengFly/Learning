package com.mengfly.encode_decode;

import java.security.Key;
import java.security.Security;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.DESedeKeySpec;

import org.apache.commons.codec.binary.Hex;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class DES3 {

	private static String src = "I'm Learing 3DES";

	/**
	 * jdk实现3DES加密解密
	 */
	public static void jdk3DES() {
		try {
			// 生成密钥
			KeyGenerator keyGenerator = KeyGenerator.getInstance("DESede");// 获取DES的密钥
			keyGenerator.init(168);// 设定keySize
			SecretKey secretKey = keyGenerator.generateKey();
			byte[] byteKey = secretKey.getEncoded();

			DESedeKeySpec desKeySpec = new DESedeKeySpec(byteKey);
			SecretKeyFactory factory = SecretKeyFactory.getInstance("DESede");
			Key convertSecretKey = factory.generateSecret(desKeySpec);

			// 加密
			Cipher cipher = Cipher.getInstance("DESede/ECB/PKCS5Padding");// 设置工作方式和填充方式
			cipher.init(Cipher.ENCRYPT_MODE, convertSecretKey);// 加密模式
			byte[] jdkDESBytes = cipher.doFinal(src.getBytes());
			System.out.println("jdkEncode3DESStr:" + Hex.encodeHexString(jdkDESBytes));

			// 揭秘操作
			cipher.init(Cipher.DECRYPT_MODE, convertSecretKey);// 解密模式
			byte[] decodeJdkDESBytes = cipher.doFinal(jdkDESBytes);
			System.out.println("jdkDecode3DESStr:" + new String(decodeJdkDESBytes));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	/**
	 * bc实现的3DES加密和解密
	 */
	private static void bc3DES() {
		Security.addProvider(new BouncyCastleProvider());// 添加Provider
		try {
			// 生成密钥
			KeyGenerator keyGenerator = KeyGenerator.getInstance("DESede", "BC");// 获取DES的密钥,指定使用BC的
			keyGenerator.init(168);// 设定keySize
			SecretKey secretKey = keyGenerator.generateKey();
			byte[] byteKey = secretKey.getEncoded();

			DESedeKeySpec desKeySpec = new DESedeKeySpec(byteKey);
			SecretKeyFactory factory = SecretKeyFactory.getInstance("DESede");
			Key convertSecretKey = factory.generateSecret(desKeySpec);

			// 加密
			Cipher cipher = Cipher.getInstance("DESede/ECB/PKCS5Padding");// 设置工作方式和填充方式
			cipher.init(Cipher.ENCRYPT_MODE, convertSecretKey);// 加密模式
			byte[] bcDESBytes = cipher.doFinal(src.getBytes());
			System.out.println("bcEncode3DESStr:" + Hex.encodeHexString(bcDESBytes));

			// 揭秘操作
			cipher.init(Cipher.DECRYPT_MODE, convertSecretKey);// 解密模式
			byte[] decodeBcDESBytes = cipher.doFinal(bcDESBytes);
			System.out.println("bcDecode3DESStr:" + new String(decodeBcDESBytes));
		} catch (Exception e) {
			e.printStackTrace();
		}

	}

	public static void main(String[] args) {
		jdk3DES();
		bc3DES();
	}
}
