package nlp.project.bayes;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {

	public static File trainFeature = new File(
			"data/8w_cut_train.txt_feature.txt");
	public static File test = new File("data/test_feature_2W.txt");
	public static int trainNum = 80000;// 训练集信息个数

	public static double pc0, pc1;// 统计训练样本中分类为0的概率 p(0|c)和分类为1的概率p(1|c)

	public static void calPc01() {
		
		if (trainFeature.exists()) {

			try {
				FileInputStream fis = new FileInputStream(trainFeature);
				InputStreamReader isr = new InputStreamReader(fis);
				BufferedReader bfr = new BufferedReader(isr);

				String line = null;
				int i = 0;
				pc0 = 0;
				pc1 = 0;
				while ((line = bfr.readLine()) != null) {
					String[] lineArr = line.split("\\s+");
					if (lineArr[5].equals("yes")) {
						pc1++;
					} else {
						pc0++;
					}
				}
				System.out.println("pc0:" + pc0 + ",\tpc1:" + pc1);

				pc0 = (double) pc0 / 80000;
				pc1 = (double) pc1 / 80000;
				System.out.println("pc0:" + pc0 + ",\tpc1:" + pc1);
				bfr.close();
				isr.close();
				fis.close();
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			System.out.println("Training text file load fail!");
		}

	}

	// 训练集上计算p(Ai|c)
	public static double calPai(int Ai, int i, int c) {
		int countI = 0, allCount = 0;
		String classrify = "";
		if (c == 0) {
			classrify = "no";
		} else if (c == 1) {
			classrify = "yes";
		}

		if (trainFeature.exists()) {

			try {
				FileInputStream fis = new FileInputStream(trainFeature);
				InputStreamReader isr = new InputStreamReader(fis);
				BufferedReader bfr = new BufferedReader(isr);

				String line = null;

				while ((line = bfr.readLine()) != null) {
					String[] lineArr = line.split("\\s+");
					if (lineArr[5].equals(classrify)) {
						allCount++;
					}

					if (lineArr[5].equals(classrify)
							&& (Integer.parseInt(lineArr[i]) == Ai)) {
						countI++;
					}
				}

				// System.out.println("allcount:"+allCount);
				bfr.close();
				isr.close();
				fis.close();
			} catch (FileNotFoundException e) {
				e.printStackTrace();
			} catch (IOException e) {
				e.printStackTrace();
			}
		} else {
			System.out.println("Training text file load fail!");
		}

		return countI / (double) allCount;
	}

	public static void main(String[] args) {
		calPc01();
		if (test.exists()) {
			try {
				FileInputStream fis = new FileInputStream(test);
				InputStreamReader isr = new InputStreamReader(fis);
				BufferedReader bfr = new BufferedReader(isr);
				
				File bayes_2w_feature=new File("data/bayes_2w_feature.txt");
				FileWriter fw=new FileWriter(bayes_2w_feature);
				BufferedWriter bfw = new BufferedWriter(fw);
				
				

				String line = null;
				int i=0;
				double testPc0=1,testPc1=1;
				while((line=bfr.readLine())!=null){
					String[] lineArr = line.split("\\s+");
					testPc0=pc0;
					testPc1=pc1;
					//System.out.println(testPc0+":"+testPc1);
					for (int j = 0; j < 5; j++) {
						testPc0*=calPai(Integer.parseInt(lineArr[0]), j, 0);
						testPc1*=calPai(Integer.parseInt(lineArr[1]), j, 1);
					}
					if (testPc0>testPc1) {
						System.out.println("no");
						line+=" no";
						bfw.write(line);
						bfw.write("\n");
					}else{
						System.out.println("yes");
						line+=" yes";
						bfw.write(line);
						bfw.write("\n");
					}
					
				}
				bfw.close();
				fw.close();
				
				bfr.close();
				isr.close();
				fis.close();
			} catch (Exception e) {
				e.printStackTrace();
			}

			
		} else {
			System.out.println("Testing text file load fail!");
		}
		
		
		

	}
}
