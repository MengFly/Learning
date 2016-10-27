package com.mengfly.encode_decode;

import java.security.Key;
import java.security.SecureRandom;

import javax.crypto.Cipher;
import javax.crypto.SecretKeyFactory;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.PBEParameterSpec;

import org.apache.commons.codec.binary.Hex;

public class PBE {
	
	private static String src = "I'm Learing PBE";

	public static void jdkPBE() {
		try {
			// 初始化盐
			SecureRandom random = new SecureRandom();
			byte[] salt = random.generateSeed(8);

			// 口令与密钥
			String password = "imooc";
			PBEKeySpec pbeKeySpec = new PBEKeySpec(password.toCharArray());
			SecretKeyFactory factory = SecretKeyFactory.getInstance("PBEWITHMD5andDES");
			Key key = factory.generateSecret(pbeKeySpec);
			
			//加密
			PBEParameterSpec pbeParameterSpec = new PBEParameterSpec(salt, 100);//需要迭代的次数
			Cipher cipher = Cipher.getInstance("PBEWITHMD5andDES");
			cipher.init(Cipher.ENCRYPT_MODE, key, pbeParameterSpec);
			byte[] jdkPBEBytes = cipher.doFinal(src.getBytes());
			System.out.println("jdkEncodePBEStr" + Hex.encodeHexString(jdkPBEBytes));
			
			
			//解密
			cipher.init(Cipher.DECRYPT_MODE, key, pbeParameterSpec);
			byte[] jdkDecodePBEBytes = cipher.doFinal(jdkPBEBytes);			
			System.out.println("jdkDecodePBEStr:" + new String(jdkDecodePBEBytes));
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		jdkPBE();
	}
}
