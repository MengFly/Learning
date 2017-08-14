/*
Navicat MySQL Data Transfer

Source Server         : test
Source Server Version : 50713
Source Host           : localhost:3306
Source Database       : imooc

Target Server Type    : MYSQL
Target Server Version : 50713
File Encoding         : 65001

Date: 2017-01-16 17:03:34
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for account
-- ----------------------------
DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `acctid` int(11) DEFAULT NULL COMMENT '账户Id',
  `money` int(11) DEFAULT NULL COMMENT '余额'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of account
-- ----------------------------
INSERT INTO `account` VALUES ('11', '300');
INSERT INTO `account` VALUES ('12', '10');
