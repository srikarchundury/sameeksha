/*
 * Word count workload for BigDataBench
 */
package cn.ac.ict.bigdatabench

import org.apache.spark.SparkContext
import org.apache.spark.SparkContext._
import org.apache.spark.sql._
import org.apache.spark.SparkConf

object WordCount {

  def main(args: Array[String]): Unit = {
    if (args.length < 3) {
      System.err.println("Usage: spark-submit samikshabench.jar <on/off> <benchmark> <input_file> [<slices>]")
      System.err.println("arg1: Tungsten ; values: on,off")
      System.err.println("arg2: Benchmark ; values: sum,join,wordcount,basicwordcount")
      System.err.println("arg3: Input File")
      System.exit(1)
    }

    var splits = 1

    val conf = new SparkConf().setAppName("BigDataBench WordCount")    

    val sc = new SparkContext(conf)
    if(args(0)=="on") {
    	conf.set("spark.sql.codegen.wholeStage","true")
    }
    else {
        conf.set("spark.sql.codegen.wholeStage","false")
    }

    val sqlContext= new org.apache.spark.sql.SQLContext(sc)
    import sqlContext.implicits._

    if(args(1)=="wordcount") {
        val linesDF = sc.textFile(args(2)).toDF("line")
        val wordsDF = linesDF.explode("line","word")((line: String) => line.split(" "))
        val wordCountDF = wordsDF.groupBy("word").count()
    	wordCountDF.show()
    }

    if(args(1)=="basicwordcount") {
        val filename = args(2)
        //val save_file = args(1)

        val lines = sc.textFile(filename, splits)
        val words = lines.flatMap(line => line.split(" "))
        val words_map = words.map(word => (word, 1))
        val result = words_map.reduceByKey(_ + _)
        println(result.collect.mkString("\n"))
        //result.saveAsTextFile(save_file)
        //println("Result has been saved to: " + save_file)
    }

    else {
    	var df = sqlContext.read.format("csv").load(args(2))
        if(args(1)=="sum") {
    		df.selectExpr("sum(_c0)").show()
    	}
    	if(args(1)=="join") {
		df.join(sc.range(0,1000L,1).toDF( ), "_c0").count()
    	}
    }
    

  }

}
