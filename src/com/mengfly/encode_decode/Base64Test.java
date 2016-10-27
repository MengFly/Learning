package com.mengfly.encode_decode;

import java.io.IOException;

import org.apache.commons.codec.binary.Base64;

import sun.misc.BASE64Decoder;
import sun.misc.BASE64Encoder;

public class Base64Test {

	private static String src = "I'm learning Base64";

	/**
	 * 通过jdk实现base64加密
	 * import sun.misc.BASE64Decoder;
	 */
	public static void jdkBase64() {
		// 进行编码
		BASE64Encoder encoder = new BASE64Encoder();
		String encodeStr = encoder.encode(src.getBytes());
		System.out.println("encodeStr:" + encodeStr);
		// 进行解码
		String decodeStr = null;
		BASE64Decoder decoder = new BASE64Decoder();
		try {
			decodeStr = new String(decoder.decodeBuffer(encodeStr));
		} catch (IOException e) {
			e.printStackTrace();
		}
		System.out.println("decodeStr:" + decodeStr);

	}
	
	/**
	 * 使用CommonsCodec进行加密和解密
	 * import org.apache.commons.codec.binary.Base64;
	 */
	public static void commonsCodecBase64() {
		//进行加密
		byte[] encodeBytes = Base64.encodeBase64(src.getBytes());
		System.out.println("encodeStr:" + new String(encodeBytes));
		
		byte[] decodeBytes = Base64.decodeBase64(encodeBytes);
		System.out.println("decodeStr:" + new String(decodeBytes));
		
	}
	
	/**
	 * 使用bouncyCastleBase64进行加密和解密
	 */
	public static void bouncyCastleBase64() {
		byte[] encodeBytes = org.bouncycastle.util.encoders.Base64.encode(src.getBytes());
		System.out.println("encodeStr:" + new String(encodeBytes));
		
		byte[] decodeBytes = org.bouncycastle.util.encoders.Base64.decode(encodeBytes);
		System.out.println("decodeStr:" + new String(decodeBytes));
	}


	public static void main(String[] args) {
		jdkBase64();
		commonsCodecBase64();
		bouncyCastleBase64();

	}

}
