package com.mengfly.encode_decode;

import java.security.Key;

import javax.crypto.Cipher;
import javax.crypto.KeyGenerator;
import javax.crypto.SecretKey;
import javax.crypto.spec.SecretKeySpec;

import org.apache.commons.codec.binary.Hex;

public class AES {

	private static String src = "I'm Learning AES";
	
	
	public static void jdkAES() {
		
		try {
			//生成Key
			KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
			keyGenerator.init(128);//设置keySize
//			keyGenerator.init(new SecureRandom());//生成默认的长度
			SecretKey secretKey = keyGenerator.generateKey();
			byte[] keyBytes = secretKey.getEncoded();//生成Key的内容,这里就要求进行加密和解密的keyBytes内容一定要一致，否则就解密不了
			//Key的转换
			Key key = new SecretKeySpec(keyBytes, "AES");
			
			//加密
			Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");//设置加解密模式（加解密模式，工作模式，填充方式）
			cipher.init(Cipher.ENCRYPT_MODE, key);
			byte[] jdkAESBytes = cipher.doFinal(src.getBytes());//得到加密后的结果
			System.out.println("jdkEncodeAESStr:" + Hex.encodeHexString(jdkAESBytes));
			
			//进行解密
			cipher.init(Cipher.DECRYPT_MODE, key);
			byte[] jdkDecodeAESBytes = cipher.doFinal(jdkAESBytes);
			System.out.println("jdkDecodeAESStr:" + new String(jdkDecodeAESBytes));
			
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public static void main(String[] args) {
		jdkAES();
	}
	
}
