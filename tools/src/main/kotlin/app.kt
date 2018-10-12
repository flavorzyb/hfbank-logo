package com.zhuyanbin

import java.io.File

var index = 100
fun main(args: Array<String>) {
    val file = File(Config.imagePath)
    val  fileTreeWalk = file.walk()
    fileTreeWalk.filter { it.isFile }
            .filter {
                val ext = it.extension.toLowerCase()
                ext == "png" || ext == "jpg" || ext == "jpeg"
            }
            .forEach { renameImage(it) }
}

fun renameImage(file: File) {
    val fileName = file.name
    val ext = file.extension.toLowerCase()
    if (!fileName.startsWith("0")) {
        index ++
        val name = getFileName(index, ext)
        file.renameTo(File(file.parent + File.separator + name))
    }
}

fun getFileName(index: Int, extName: String): String {
    var result = index.toString() + "." + extName

    if (index < 1000) {
        result = "0$result"
    }

    return result
}