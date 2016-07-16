package nlp.project.bayes;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;
import java.io.InputStreamReader;

public class DealTestFeature {

	public static void main(String[] args) {
		File y_2w_feature = new File("data/y_2w_feature.txt");

		FileInputStream fis;
		try {
			fis = new FileInputStream(y_2w_feature);
			InputStreamReader isr = new InputStreamReader(fis);
			BufferedReader bfr = new BufferedReader(isr);

			File test_feature_2W = new File("data/test_feature_2W.txt");
			FileWriter fw = new FileWriter(test_feature_2W);
			BufferedWriter bfw = new BufferedWriter(fw);

			String line = null;
			int count = 0;
			while ((line = bfr.readLine()) != null) {
				String[] strArr = line.split("\\s+");
				String newline = "";
				if (strArr.length == 6) {
					for (int i = 0; i < 5; i++) {
						newline += strArr[i] + "   ";
					}

					count++;
				}
				bfw.write(newline);
				bfw.write("\n");

			}
			System.out.println(count);
			bfr.close();
			isr.close();
			fis.close();
			
			bfw.close();
			fw.close();
			

		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}

	}

}
