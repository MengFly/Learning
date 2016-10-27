package com.mengfly.encode_decode;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.Security;

import org.apache.commons.codec.binary.Hex;
import org.apache.commons.codec.digest.DigestUtils;
import org.bouncycastle.crypto.Digest;
import org.bouncycastle.crypto.digests.SHA1Digest;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class SHA {

	public static final String src = "I'm Learning SHA";

	/**
	 * JDK 实现SHA1加密 例如：利用JDK实现SHA-384进行加密就是
	 * MessageDigest.getInstance("SHA-384");
	 */
	public static void jdkSHA1() {
		try {
			MessageDigest digest = MessageDigest.getInstance("SHA");
			digest.update(src.getBytes());
			byte[] sha1Bytes = digest.digest();
			String sha1Str = Hex.encodeHexString(sha1Bytes);
			System.out.println("JDKSHA1Str:" + sha1Str);
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}
	}

	/**
	 * 利用bc实现SHA1加密 例如：实现SHA-512加密就是new SHA512Digest();
	 */
	public static void bcSHA1() {
		Digest digest = new SHA1Digest();
		digest.update(src.getBytes(), 0, src.getBytes().length);
		byte[] sha1Bytes = new byte[digest.getDigestSize()];
		digest.doFinal(sha1Bytes, 0);
		System.out.println("bcSHA1Str:" + org.bouncycastle.util.encoders.Hex.toHexString(sha1Bytes));
	}

	/**
	 * 因为jdk没有提供SHA224的实现因此我们可以 通过addProvider为JDK添加SHA224的实现
	 */
	public static void jdkSHA224FromBC() {
		Security.addProvider(new BouncyCastleProvider());
		try {
			MessageDigest digest = MessageDigest.getInstance("SHA-224");
			byte[] sha224Bytes = digest.digest(src.getBytes());
			String sha224Str = Hex.encodeHexString(sha224Bytes);
			System.out.println("jdkSHA224FromBCStr:" + sha224Str);
		} catch (NoSuchAlgorithmException e) {
			e.printStackTrace();
		}
	}
	
	/**
	 * 利用cc进行sha1加密
	 */
	public static void ccSHA1() {
		System.out.println("ccSHA1Str:" + DigestUtils.sha1Hex(src.getBytes()));
		System.out.println("ccSHA1Str:" + DigestUtils.sha1Hex(src));
	}

	public static void main(String[] args) {
		jdkSHA1();
		bcSHA1();
		jdkSHA224FromBC();
		ccSHA1();
	}

}
