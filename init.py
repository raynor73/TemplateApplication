#!/usr/bin/env python3

import sys
import shutil
import os
from pathlib import Path

def updateAppIdInFile(filePath, placeholderAppId, appId):
	file = open(filePath, "r", encoding="utf-8")
	fileContent = file.read()
	file.close()

	fileContent = fileContent.replace(placeholderAppId, appId)

	filePathOld = filePath + ".old"
	shutil.move(filePath, filePathOld)

	file = open(filePath, "w", encoding="utf-8")
	file.write(fileContent)
	file.close()

	os.remove(filePathOld)

def processAppModule(androidTestRootPath, testRootPath, rootPath, placeholderAppId, appId):
	shutil.move(
		androidTestRootPath + placeholderAppId.replace(".", "/"),
		androidTestRootPath + appId.replace(".", "/")
	)
	shutil.move(
		testRootPath + placeholderAppId.replace(".", "/"),
		testRootPath + appId.replace(".", "/")
	)
	shutil.move(
		rootPath + placeholderAppId.replace(".", "/"),
		rootPath + appId.replace(".", "/")
	)

	appAndroidTestKtFiles = list(Path(androidTestRootPath).rglob("*.kt"))
	for filePath in appAndroidTestKtFiles:
		updateAppIdInFile(str(filePath), placeholderAppId, appId)

	appTestKtFiles = list(Path(testRootPath).rglob("*.kt"))
	for filePath in appTestKtFiles:
		updateAppIdInFile(str(filePath), placeholderAppId, appId)

	appKtFiles = list(Path(rootPath).rglob("*.kt"))
	for filePath in appKtFiles:
		updateAppIdInFile(str(filePath), placeholderAppId, appId)

	updateAppIdInFile("./app/build.gradle", placeholderAppId, appId)

if (len(sys.argv) <= 1):
	print("Usage:", sys.argv[0], "APPLICATION_ID")
	exit()

appAndroidTestRootPath = "./app/src/androidTest/java/"
appTestRootPath = "./app/src/test/java/"
appRootPath = "./app/src/main/java/"
placeholderAppId = "ilapin.template"
applicationId = sys.argv[1]

processAppModule(
	appAndroidTestRootPath, appTestRootPath, appRootPath, placeholderAppId, applicationId
)

processAppModule(
	"./core/src/androidTest/java/",
	"./core/src/test/java/",
	"./core/src/main/java/",
	"ilapin.template.core",
	applicationId + ".core"
)
